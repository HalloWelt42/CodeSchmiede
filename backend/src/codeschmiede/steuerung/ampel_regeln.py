"""Regeln der Ampelschule: kleine Prüfungen auf einem nachgespielten Ablauf.

Eine Regel steht mit ihren Werten in der Level-Datei, etwa `{art: gelb, mindestens: 3}`. Sie liest die Folge der
Signale (eine je Sekunde), den Bedarf je Sekunde (wer wartete), die Teilnehmer mit ihren Wartezeiten und die Unfälle,
und liefert Befunde mit der Stelle. Welche Gruppen einander feind sind, folgt aus der Anlage (Wege, die sich kreuzen
oder zusammenlaufen).
"""

from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field

from .ampel_welt import OFFEN
from .teilschritte import Befund

# so viele Befunde liefert eine Regel je Ablauf höchstens
BEFUNDE_JE_REGEL = 3

ART_NAME = {"auto": "Auto", "lkw": "Lkw", "einsatz": "Einsatzfahrzeug", "fuss": "Fußgänger"}
ZUSTAND_NAME = {"rot": "Rot", "rotgelb": "Rot-Gelb", "gruen": "Grün", "gelb": "Gelb", "gelb_blinkt": "gelbes Blinken",
                "aus": "aus"}


@dataclass
class AmpelLauf:
    """Ein nachgespielter Ablauf, wie die Regeln ihn lesen."""

    name: str
    sichtbar: bool
    dauer: int
    arten: dict[str, str]
    feindlich: dict[str, set[str]]
    signale: list[dict[str, str]]
    verlauf: list[dict]
    teilnehmer: list[dict]
    unfaelle: list[dict]
    fehler: str | None = None
    _phasen: dict[str, list[tuple[str, int, int]]] = field(default_factory=dict)

    def offen(self, gruppe: str, sekunde: int) -> bool:
        return self.signale[sekunde][gruppe] in OFFEN[self.arten[gruppe]]

    def phasen(self, gruppe: str) -> list[tuple[str, int, int]]:
        """Die Signale einer Gruppe als Folge (Zustand, Beginn, Dauer)."""
        if gruppe not in self._phasen:
            folge: list[tuple[str, int, int]] = []
            for s, signale in enumerate(self.signale):
                z = signale[gruppe]
                if folge and folge[-1][0] == z:
                    folge[-1] = (z, folge[-1][1], folge[-1][2] + 1)
                else:
                    folge.append((z, s, 1))
            self._phasen[gruppe] = folge
        return self._phasen[gruppe]

    def autos(self) -> list[str]:
        return [g for g, a in self.arten.items() if a == "auto"]

    def paare(self) -> Iterator[tuple[str, str]]:
        for g in self.arten:
            for h in sorted(self.feindlich[g]):
                if g < h:
                    yield g, h


class Feindlich(BaseModel):
    """Gruppen, deren Wege sich kreuzen, sind nie zugleich offen (Grün, Gelb oder Rot-Gelb)."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["feindlich"]

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        befunde = []
        for g, h in lauf.paare():
            for s in range(len(lauf.signale)):
                if lauf.offen(g, s) and lauf.offen(h, s):
                    befunde.append(Befund(s, f"{g} und {h} sind zugleich offen, ihre Wege kreuzen sich"))
                    break
        return befunde


class Gelb(BaseModel):
    """Nach Grün kommt Gelb, mindestens so lange, und danach Rot."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["gelb"]
    mindestens: int = Field(default=3, ge=1)

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        befunde = []
        for g in lauf.autos():
            folge = lauf.phasen(g)
            for (z, beginn, dauer), (weiter, s, _) in zip(folge, folge[1:]):
                if z == "gruen" and weiter != "gelb":
                    befunde.append(Befund(s, f"{g} springt von Grün auf {ZUSTAND_NAME[weiter]}, ohne Gelb"))
                elif z == "gelb" and weiter not in ("rot", "gelb_blinkt"):
                    befunde.append(Befund(s, f"{g}: nach Gelb kommt {ZUSTAND_NAME[weiter]} statt Rot"))
                elif z == "gelb" and dauer < self.mindestens:
                    befunde.append(Befund(beginn, f"{g}: Gelb nur {dauer} s, mindestens {self.mindestens} s"))
        return befunde[:BEFUNDE_JE_REGEL]


class Rotgelb(BaseModel):
    """Vor Grün kommt Rot-Gelb, genau so lange, und davor Rot."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["rotgelb"]
    dauer: int = Field(default=1, ge=1)

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        befunde = []
        for g in lauf.autos():
            folge = lauf.phasen(g)
            for i, (z, beginn, dauer) in enumerate(folge):
                vorher = folge[i - 1][0] if i > 0 else None
                nachher = folge[i + 1][0] if i + 1 < len(folge) else None
                if z == "gruen" and vorher is not None and vorher != "rotgelb":
                    befunde.append(Befund(beginn, f"{g}: Grün ohne Rot-Gelb davor"))
                elif z == "rotgelb" and vorher not in (None, "rot"):
                    befunde.append(Befund(beginn, f"{g}: Rot-Gelb nach {ZUSTAND_NAME[vorher]} statt nach Rot"))
                elif z == "rotgelb" and nachher is not None and nachher != "gruen":
                    befunde.append(Befund(beginn + dauer, f"{g}: nach Rot-Gelb kommt {ZUSTAND_NAME[nachher]} statt Grün"))
                elif z == "rotgelb" and nachher is not None and dauer != self.dauer:
                    befunde.append(Befund(beginn, f"{g}: Rot-Gelb dauert {dauer} s, soll {self.dauer} s"))
        return befunde[:BEFUNDE_JE_REGEL]


class Raeumzeit(BaseModel):
    """Schließt eine Gruppe, bleiben ihre Feinde noch so lange zu, bis die Fläche frei ist (je nach Art der Gruppe,
    die schließt)."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["raeumzeit"]
    auto: int = Field(default=2, ge=0)
    fuss: int = Field(default=3, ge=0)

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        zu: dict[str, int] = {}
        befunde = []
        for s in range(1, len(lauf.signale)):
            for g in lauf.arten:
                if lauf.offen(g, s - 1) and not lauf.offen(g, s):
                    zu[g] = s
            for h in lauf.arten:
                if lauf.offen(h, s) and not lauf.offen(h, s - 1):
                    for g in lauf.feindlich[h]:
                        noetig = self.auto if lauf.arten[g] == "auto" else self.fuss
                        if g in zu and s - zu[g] < noetig:
                            befunde.append(Befund(s, f"{h} öffnet {s - zu[g]} s nach {g}, Räumzeit mindestens {noetig} s"))
        return befunde[:BEFUNDE_JE_REGEL]


class Mindestgruen(BaseModel):
    """Grün dauert mindestens so lange (außer am Ende des Ablaufs)."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["mindestgruen"]
    sekunden: int = Field(ge=1)
    gruppen: list[str] = Field(min_length=1)

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        befunde = []
        for g in self.gruppen:
            for z, beginn, dauer in lauf.phasen(g):
                if z == "gruen" and dauer < self.sekunden and beginn + dauer < len(lauf.signale):
                    befunde.append(Befund(beginn, f"{g}: Grün nur {dauer} s, mindestens {self.sekunden} s"))
        return befunde[:BEFUNDE_JE_REGEL]


def _nacht_nah(lauf: AmpelLauf, s: int, abstand: int) -> bool:
    return any(v["nacht"] for v in lauf.verlauf[max(0, s - abstand):s + 1])


class Ruhe(BaseModel):
    """Wartet bei den Feinden niemand (und war dort eben nichts offen), hat diese Gruppe Grün. Nachts und solange
    eine Kontaktschleife gestört ist, weiß niemand sicher, wer wartet; dann gilt die Regel nicht."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["ruhe"]
    gruppe: str
    nach: int = Field(default=6, ge=0)

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        feinde = lauf.feindlich[self.gruppe]
        for s in range(len(lauf.signale)):
            if lauf.signale[s][self.gruppe] == "gruen" or _nacht_nah(lauf, s, 10) or lauf.verlauf[s]["stoerung"]:
                continue
            von = max(0, s - self.nach)
            bedarf = any(lauf.verlauf[t]["bedarf"][h] for t in range(von, s + 1) for h in feinde)
            offen = any(lauf.offen(h, t) for t in range(von, s + 1) for h in feinde)
            if not bedarf and not offen:
                return [Befund(s, f"niemand wartet, trotzdem kein Grün für {self.gruppe}")]
        return []


class Reagiert(BaseModel):
    """Wartet bei den Feinden jemand, gibt diese Gruppe ihr Grün binnen so vieler Sekunden ab."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["reagiert"]
    gruppe: str
    binnen: int = Field(ge=1)

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        feinde = lauf.feindlich[self.gruppe]
        seit: int | None = None
        for s in range(len(lauf.signale)):
            if not any(lauf.verlauf[s]["bedarf"][h] for h in feinde):
                seit = None
                continue
            seit = s if seit is None else seit
            if lauf.signale[s][self.gruppe] != "gruen":
                seit = s
            elif s - seit >= self.binnen:
                return [Befund(s, f"jemand wartet seit {self.binnen} s, {self.gruppe} hat immer noch Grün")]
        return []


class NurBeiBedarf(BaseModel):
    """Diese Gruppen öffnen nur, wenn dort gerade jemand wartet (Taster, Kontaktschleife, Einsatzfahrzeug); außer
    ihre Kontaktschleife ist gestört."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["nur_bei_bedarf"]
    gruppen: list[str] = Field(min_length=1)

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        befunde = []
        for g in self.gruppen:
            for s in range(len(lauf.signale)):
                if lauf.offen(g, s) and (s == 0 or not lauf.offen(g, s - 1)) and lauf.verlauf[s]["stoerung"] != g:
                    vorher = lauf.verlauf[max(0, s - 1)]["bedarf"][g] or lauf.verlauf[s]["bedarf"][g]
                    if not vorher:
                        befunde.append(Befund(s, f"{g} öffnet, obwohl dort niemand wartet"))
        return befunde[:BEFUNDE_JE_REGEL]


class Bedient(BaseModel):
    """Niemand wartet länger als so viele Sekunden (alle Gruppen oder die genannten)."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["bedient"]
    hoechstens: int = Field(ge=1)
    gruppen: list[str] = Field(default_factory=list)

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        befunde = []
        for t in lauf.teilnehmer:
            if self.gruppen and t["gruppe"] not in self.gruppen:
                continue
            if t["warten"] > self.hoechstens:
                befunde.append(Befund(round(t["ankunft"]), f"{ART_NAME[t['art']]} der Gruppe {t['gruppe']} wartet "
                                      f"{t['warten']:.0f} s, höchstens {self.hoechstens} s"))
        return befunde[:BEFUNDE_JE_REGEL]


class KeinUnfall(BaseModel):
    """Kein Fußgänger wird überfahren, kein Blech verbeult."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["kein_unfall"]

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        befunde = []
        for u in lauf.unfaelle:
            a, b = u["gruppen"]
            if u["art"] == "fuss":
                befunde.append(Befund(u["t"], f"Unfall: Fußgänger überfahren ({a} gegen {b})"))
            else:
                befunde.append(Befund(u["t"], f"Unfall: Zusammenstoß {a} gegen {b}"))
        return befunde[:BEFUNDE_JE_REGEL]


class Nacht(BaseModel):
    """Nachts blinken alle Autoampeln gelb und die Fußgängerampeln sind aus; tagsüber nie."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["nacht"]
    # so lange darf das Umschalten am Anfang und Ende der Nacht dauern
    wechsel: int = Field(default=6, ge=0)

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        for s, signale in enumerate(lauf.signale):
            nachts = lauf.verlauf[s]["nacht"]
            seit = 0
            while seit <= s and lauf.verlauf[s - seit]["nacht"] == nachts:
                seit += 1
            # kurz nach dem Wechsel (auch zu Beginn des Ablaufs) darf noch umgeschaltet werden
            if seit <= self.wechsel:
                continue
            for g, z in signale.items():
                soll = ("gelb_blinkt" if lauf.arten[g] == "auto" else "aus") if nachts else None
                if nachts and z != soll:
                    return [Befund(s, f"nachts soll {g} {ZUSTAND_NAME[soll]} zeigen, nicht {ZUSTAND_NAME[z]}")]
                if not nachts and z in ("gelb_blinkt", "aus"):
                    return [Befund(s, f"tagsüber zeigt {g} {ZUSTAND_NAME[z]}")]
        return []


class Einsatz(BaseModel):
    """Einsatzfahrzeuge stehen höchstens so lange vor Rot."""

    model_config = ConfigDict(extra="forbid")
    art: Literal["einsatz"]
    halt: int = Field(default=0, ge=0)

    def pruefe(self, lauf: AmpelLauf) -> list[Befund]:
        return [
            Befund(round(t["ankunft"]), f"Einsatzfahrzeug der Gruppe {t['gruppe']} stand {t['warten']:.0f} s")
            for t in lauf.teilnehmer
            if t["art"] == "einsatz" and t["warten"] > self.halt
        ][:BEFUNDE_JE_REGEL]


Regel = Annotated[
    Feindlich | Gelb | Rotgelb | Raeumzeit | Mindestgruen | Ruhe | Reagiert | NurBeiBedarf | Bedient | KeinUnfall | Nacht
    | Einsatz,
    Field(discriminator="art"),
]


def pruefe(regel: Regel, lauf: AmpelLauf) -> list[Befund]:
    return regel.pruefe(lauf)


def gruppen_der_regel(regel: Regel) -> list[str]:
    """Gruppen, die eine Regel beim Namen nennt (für die Bestandsprüfung)."""
    if isinstance(regel, (Ruhe, Reagiert)):
        return [regel.gruppe]
    if isinstance(regel, (Mindestgruen, NurBeiBedarf, Bedient)):
        return list(regel.gruppen)
    return []
