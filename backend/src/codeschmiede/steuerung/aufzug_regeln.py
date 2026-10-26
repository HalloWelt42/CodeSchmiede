"""Regeln der Aufzugsteuerung: kleine Prüfungen auf einer nachgespielten Fahrt.

Eine Regel steht mit ihren Werten in der Level-Datei, etwa `{art: bedient, hoechstens: 60}`. Sie liest die Ereignisse
der Welt (Fahrten, Ankünfte, Türen, Wenden, Verstöße), das Protokoll je Sekunde und die Bilanz der Fahrgäste und
liefert Befunde mit der Stelle.
"""

from dataclasses import dataclass
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field

from .aufzug_welt import TEMPO
from .teilschritte import Befund

BEFUNDE_JE_REGEL = 3
ETAGE = ["EG", *[str(e) for e in range(1, 20)]]


def etage(e: int) -> str:
    return "im EG" if e == 0 else f"in Etage {e}"


@dataclass
class AufzugLauf:
    """Ein nachgespielter Ablauf, wie die Regeln ihn lesen."""

    name: str
    sichtbar: bool
    dauer: int
    etagen: int
    ereignisse: list[dict]
    protokoll: list[list]
    fahrgaeste: list[dict]
    feuer_ab: int | None
    fehler: str | None = None

    def von(self, aufzug: str) -> list[dict]:
        return [e for e in self.ereignisse if e["aufzug"] == aufzug]

    def aufzuege(self) -> list[str]:
        return sorted({e["aufzug"] for e in self.ereignisse})

    def vor_feuer(self, t: float) -> bool:
        return self.feuer_ab is None or t < self.feuer_ab


def _verstoesse(lauf: AufzugLauf, gruende: tuple[str, ...]) -> list[Befund]:
    return [Befund(e["t"], f"Aufzug {e['aufzug']} {etage(e['etage'])}: {e['text']}")
            for e in lauf.ereignisse if e["art"] == "verstoss" and e["grund"] in gruende][:BEFUNDE_JE_REGEL]


class TuerSicher(BaseModel):
    """Nie fahren mit offener Tür, nie über das Haus hinaus."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["tuer_sicher"]

    def pruefe(self, lauf: AufzugLauf) -> list[Befund]:
        return _verstoesse(lauf, ("offen_fahren", "haus"))


class KeinEinklemmen(BaseModel):
    """Die Tür geht nie zu, solange jemand in der Tür steht."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["kein_einklemmen"]

    def pruefe(self, lauf: AufzugLauf) -> list[Befund]:
        return _verstoesse(lauf, ("einklemmen",))


class Ueberlast(BaseModel):
    """Die Tür geht nie zu, solange die Kabine überladen ist."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["ueberlast"]

    def pruefe(self, lauf: AufzugLauf) -> list[Befund]:
        return _verstoesse(lauf, ("ueberlast",))


class Bedient(BaseModel):
    """Niemand wartet länger als so viele Sekunden, und alle kommen an (außer wer zu spät kam oder Feueralarm war)."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["bedient"]
    hoechstens: int = Field(ge=1)
    # wer so kurz vor dem Ende kommt, muss nicht mehr ankommen
    spielraum: int = Field(default=40, ge=0)

    def pruefe(self, lauf: AufzugLauf) -> list[Befund]:
        befunde = []
        for f in lauf.fahrgaeste:
            if not lauf.vor_feuer(f["ankunft"]):
                continue
            wohin = f"von {ETAGE[f['von']]} nach {ETAGE[f['nach']]}"
            if f["warten"] > self.hoechstens and (lauf.feuer_ab is None or f["ankunft"] + self.hoechstens < lauf.feuer_ab):
                befunde.append(Befund(round(f["ankunft"]), f"Fahrgast {wohin} wartet {f['warten']:.0f} s, "
                                      f"höchstens {self.hoechstens} s"))
            elif f["angekommen"] is None and f["ankunft"] < lauf.dauer - self.spielraum and lauf.feuer_ab is None:
                befunde.append(Befund(round(f["ankunft"]), f"Fahrgast {wohin} kommt nie an"))
        return befunde[:BEFUNDE_JE_REGEL]


class Mitnehmen(BaseModel):
    """Wer an einer Etage in Fahrtrichtung wartet, wird mitgenommen, wenn noch Platz ist (nur nach oben, nur nach
    unten oder in beide Richtungen)."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["mitnehmen"]
    richtung: Literal[1, -1] | None = None

    def pruefe(self, lauf: AufzugLauf) -> list[Befund]:
        befunde = []
        for name in lauf.aufzuege():
            folge = lauf.von(name)
            for i, e in enumerate(folge):
                if e["art"] != "ankunft" or not e["wartend"] or e["voll"] or not lauf.vor_feuer(e["t"]):
                    continue
                naechste = next((x for x in folge[i + 1:] if x["art"] in ("auf", "fahrt")), None)
                fahrtrichtung = next((x["nach"] - x["etage"] for x in reversed(folge[:i]) if x["art"] == "fahrt"), 0)
                if self.richtung is not None and fahrtrichtung != self.richtung:
                    continue
                if naechste is not None and naechste["art"] == "fahrt":
                    wohin = "nach oben" if fahrtrichtung > 0 else "nach unten"
                    befunde.append(Befund(e["t"], f"Aufzug {name} fährt {etage(e['etage'])} vorbei, obwohl dort "
                                          f"jemand {wohin} mitwollte"))
        return befunde[:BEFUNDE_JE_REGEL]


class Umkehren(BaseModel):
    """Die Kabine kehrt erst um, wenn in ihrer Richtung niemand mehr wartet und kein Ziel mehr liegt. Es zählt, was
    schon vor ihrer Ankunft an der Etage der Wende bestand; wer erst dort einsteigt oder ruft, zählt nicht."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["umkehren"]

    def pruefe(self, lauf: AufzugLauf) -> list[Befund]:
        return [
            Befund(e["t"], f"Aufzug {e['aufzug']} kehrt {etage(e['etage'])} um, obwohl "
                           f"{', '.join(ETAGE[x] for x in e['weiter'])} noch in der alten Richtung liegt")
            for e in lauf.ereignisse if e["art"] == "wende" and e["weiter"] and lauf.vor_feuer(e["t"])
        ][:BEFUNDE_JE_REGEL]


class Zuegig(BaseModel):
    """Die Tür steht nicht länger offen als nötig: höchstens so viele Sekunden, ohne dass jemand kommt oder geht."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["zuegig"]
    sekunden: int = Field(ge=1)

    def pruefe(self, lauf: AufzugLauf) -> list[Befund]:
        return [
            Befund(e["t"], f"Aufzug {e['aufzug']} stand {etage(e['etage'])} {e['leer']:.0f} s mit offener Tür, "
                           f"ohne dass jemand kam, höchstens {self.sekunden} s")
            for e in lauf.ereignisse if e["art"] == "zu" and e["leer"] > self.sekunden
        ][:BEFUNDE_JE_REGEL]


class Feuer(BaseModel):
    """Bei Feueralarm fahren alle Kabinen ohne Halt ins Erdgeschoss, öffnen dort und bleiben stehen."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["feuer"]
    # so lange darf es dauern, bis jede Kabine offen im EG steht
    sekunden: int = Field(ge=1)

    def pruefe(self, lauf: AufzugLauf) -> list[Befund]:
        if lauf.feuer_ab is None:
            return []
        befunde = []
        for name in lauf.aufzuege():
            nachher = [e for e in lauf.von(name) if e["t"] >= lauf.feuer_ab]
            unten = next((e for e in nachher if e["art"] == "offen" and e["etage"] == 0), None)
            for e in nachher:
                if e["art"] == "auf" and e["etage"] != 0:
                    befunde.append(Befund(e["t"], f"Aufzug {name} hält bei Feueralarm {etage(e['etage'])}"))
                    break
            if unten is None or unten["t"] - lauf.feuer_ab > self.sekunden:
                befunde.append(Befund(lauf.feuer_ab, f"Aufzug {name} steht nicht binnen {self.sekunden} s offen im EG"))
            elif any(e["art"] in ("fahrt", "zu") and e["t"] > unten["t"] for e in nachher):
                befunde.append(Befund(unten["t"], f"Aufzug {name} verlässt das EG wieder trotz Feueralarm"))
        return befunde[:BEFUNDE_JE_REGEL]


class Parken(BaseModel):
    """Ist nichts zu tun, wartet die Kabine in dieser Etage (nach so vielen ruhigen Sekunden)."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["parken"]
    etage: int = Field(ge=0)
    nach: int = Field(default=10, ge=0)

    def pruefe(self, lauf: AufzugLauf) -> list[Befund]:
        befunde = []
        noetig = self.nach + int(TEMPO * lauf.etagen) + 4
        for k in range(len(lauf.protokoll[0][1]) if lauf.protokoll else 0):
            ruhig = 0
            for s, (wartend, kabinen) in enumerate(lauf.protokoll):
                hier, ziele, _ = kabinen[k]
                if wartend == 0 and ziele == 0:
                    ruhig += 1
                    if ruhig == noetig and hier != self.etage:
                        befunde.append(Befund(s, f"nach {noetig} ruhigen Sekunden steht die Kabine {etage(hier)}, "
                                              f"nicht {etage(self.etage)}"))
                else:
                    ruhig = 0
        return befunde[:BEFUNDE_JE_REGEL]


Regel = Annotated[
    TuerSicher | KeinEinklemmen | Ueberlast | Bedient | Mitnehmen | Umkehren | Zuegig | Feuer | Parken,
    Field(discriminator="art"),
]


def pruefe(regel: Regel, lauf: AufzugLauf) -> list[Befund]:
    return regel.pruefe(lauf)
