"""Welt des Roboter-Parcours und das Nachspielen einer Befehlsfolge.

Eine Welt ist ein Raster aus Zeichen:
  #  Wand            .  frei
  Z  Ziel            K  Kristall
  >  ^  <  v         Start mit Blickrichtung (Osten, Norden, Westen, Süden)
Außerhalb des Rasters ist Wand. y wächst nach unten.

Die Sandbox meldet nur, welche Befehle das Programm in welcher Zeile
gegeben hat. Was daraus folgt (Weg, Absturz, Ziel, Kristalle), rechnet
`nachspielen` hier im Backend; so zählt allein, was die Befehle bewirken.
"""

from typing import Literal

from pydantic import BaseModel, Field, model_validator

Befehl = Literal["gehe", "links", "rechts", "nimm"]
# Osten, Norden, Westen, Süden
RICHTUNGEN = ((1, 0), (0, -1), (-1, 0), (0, 1))
START_ZEICHEN = ">^<v"
ERLAUBT = set("#.ZK") | set(START_ZEICHEN)


class Welt(BaseModel):
    karte: list[str] = Field(min_length=1)

    @model_validator(mode="before")
    @classmethod
    def _aus_text(cls, daten):
        # in Level-Dateien steht die Karte als Textblock
        if isinstance(daten, str):
            return {"karte": [z.strip() for z in daten.strip().splitlines()]}
        return daten

    @model_validator(mode="after")
    def _stimmig(self) -> "Welt":
        breite = len(self.karte[0])
        if any(len(zeile) != breite for zeile in self.karte):
            raise ValueError("alle Zeilen der Karte gleich lang")
        zeichen = "".join(self.karte)
        if set(zeichen) - ERLAUBT:
            raise ValueError(f"unbekannte Zeichen {sorted(set(zeichen) - ERLAUBT)}")
        if sum(zeichen.count(s) for s in START_ZEICHEN) != 1 or zeichen.count("Z") != 1:
            raise ValueError("genau ein Start und ein Ziel")
        return self

    @property
    def breite(self) -> int:
        return len(self.karte[0])

    @property
    def hoehe(self) -> int:
        return len(self.karte)

    def finde(self, gesucht: str) -> list[tuple[int, int]]:
        return [(x, y) for y, zeile in enumerate(self.karte) for x, z in enumerate(zeile) if z in gesucht]

    def start(self) -> tuple[int, int, int]:
        x, y = self.finde(START_ZEICHEN)[0]
        return x, y, START_ZEICHEN.index(self.karte[y][x])

    def frei(self, x: int, y: int) -> bool:
        return 0 <= x < self.breite and 0 <= y < self.hoehe and self.karte[y][x] != "#"


class Aktion(BaseModel):
    befehl: Befehl
    zeile: int = 0


class RoboterSchritt(BaseModel):
    """Ein Befehl und die Lage danach."""

    befehl: Befehl
    zeile: int
    x: int
    y: int
    richtung: int


class RoboterLauf(BaseModel):
    """Der nachgespielte Lauf in einer Welt."""

    schritte: list[RoboterSchritt]
    am_ziel: bool
    kristalle_offen: int
    fehler: str | None = None
    geschafft: bool


def nachspielen(welt: Welt, aktionen: list[Aktion], programmfehler: str | None = None) -> RoboterLauf:
    x, y, richtung = welt.start()
    kristalle = set(welt.finde("K"))
    (ziel,) = welt.finde("Z")
    schritte: list[RoboterSchritt] = []
    fehler = None
    for nr, a in enumerate(aktionen, start=1):
        if a.befehl == "gehe":
            dx, dy = RICHTUNGEN[richtung]
            if not welt.frei(x + dx, y + dy):
                fehler = f"Schritt {nr}, Zeile {a.zeile}: gegen die Wand gelaufen"
                break
            x, y = x + dx, y + dy
        elif a.befehl == "links":
            richtung = (richtung + 1) % 4
        elif a.befehl == "rechts":
            richtung = (richtung + 3) % 4
        elif a.befehl == "nimm":
            if (x, y) not in kristalle:
                fehler = f"Schritt {nr}, Zeile {a.zeile}: hier liegt kein Kristall"
                break
            kristalle.discard((x, y))
        schritte.append(RoboterSchritt(befehl=a.befehl, zeile=a.zeile, x=x, y=y, richtung=richtung))
    fehler = fehler or programmfehler
    am_ziel = (x, y) == ziel
    return RoboterLauf(
        schritte=schritte,
        am_ziel=am_ziel,
        kristalle_offen=len(kristalle),
        fehler=fehler,
        geschafft=fehler is None and am_ziel and not kristalle,
    )
