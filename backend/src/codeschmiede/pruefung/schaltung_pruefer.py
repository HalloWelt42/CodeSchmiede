"""Prüfer für `task_type: schaltung` (Spiel Digitale Schaltungen).

Abgegeben wird ein Schaltplan als Text (steuerung/schaltung.py). Der Server rechnet die ganze Wahrheitstabelle aus,
ohne Sandbox, und vergleicht jeden Ausgang mit seiner Spalte. Beim Verdrahten stehen die Bausteine fest: es dürfen
genau die vorgegebenen sein, nur die Leitungen sind offen.

Teilschritte nennen die Ausgänge, die ab ihnen stimmen müssen (oder "alle"); jeder schließt die vorigen ein.

Sterne: einer, wenn die ganze Tabelle stimmt; zwei, wenn dazu höchstens so viele Bausteine; drei, wenn dazu der
längste Weg höchstens so viele Bausteine lang ist (Tiefe, also Laufzeit).

Im Frontmatter:
  schaltung:
    eingaenge: [A, B]
    ausgaenge: [S, C]
    bausteine: [UND, XOR]                        erlaubte Arten
    vorgabe: [{name: x1, art: XOR, x: 230, y: 54}, ...]   beim Verdrahten; leer heißt frei bauen
    soll: {S: "0110", C: "0001"}                 je Ausgang die Spalte (Zeilen binär gezählt, erster Eingang vorn;
                                                 x heißt egal)
    teilschritte: [{titel, text, ausgaenge: [S] | alle}, ...]
    sterne: {bausteine: 2, tiefe: 1}
"""

import time
from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from ..steuerung import schaltung
from ..steuerung.teilschritte import Befund, TeilschrittStand, ablauf_befunde, auswerten
from .ergebnis import PruefErgebnis, SternKriterium, TestErgebnis, Wertung
from .registry import registriere

TABELLE = "Wahrheitstabelle"


class Vorgabe(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    art: str
    x: int
    y: int


class SchaltungTeilschritt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    titel: str
    text: str
    ausgaenge: Literal["alle"] | list[str] | None = None


class SchaltungSterne(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bausteine: int = Field(ge=1)
    tiefe: int = Field(ge=1)


class SchaltungLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    eingaenge: list[str] = Field(min_length=1, max_length=8)
    ausgaenge: list[str] = Field(min_length=1, max_length=8)
    bausteine: list[str] = Field(min_length=1)
    vorgabe: list[Vorgabe] = Field(default_factory=list)
    soll: dict[str, str]
    aufbauend_auf: str | None = None
    teilschritte: list[SchaltungTeilschritt] = Field(min_length=1)
    sterne: SchaltungSterne

    @model_validator(mode="after")
    def _stimmig(self) -> "SchaltungLevel":
        zeilen = 2 ** len(self.eingaenge)
        if set(self.soll) != set(self.ausgaenge):
            raise ValueError("soll braucht genau eine Spalte je Ausgang")
        for name, spalte in self.soll.items():
            if len(spalte) != zeilen or set(spalte) - set("01x"):
                raise ValueError(f"soll {name}: {zeilen} Zeichen aus 0, 1 und x")
        return self

    def schritte(self) -> list["_Schritt"]:
        """Die Teilschritte im Format der gemeinsamen Auswertung; der erste prüft auch die Vorgabe beim Verdrahten."""
        liste = []
        for i, t in enumerate(self.teilschritte):
            namen = self.ausgaenge if t.ausgaenge == "alle" else (t.ausgaenge or [])
            regeln: list = [Ausgaenge(namen)] if namen else []
            if i == 0 and self.vorgabe:
                regeln.insert(0, WIE_VORGEGEBEN)
            liste.append(_Schritt(t.titel, t.text, regeln, None))
        return liste


@dataclass
class _Schritt:
    titel: str
    text: str
    regeln: list
    ablaeufe: None


@dataclass
class SchaltungLauf:
    name: str
    sichtbar: bool
    level: SchaltungLevel
    plan: schaltung.Plan
    tabelle: list[dict[str, int]]
    fehler: str | None = None


@dataclass(frozen=True)
class Ausgaenge:
    """Diese Ausgänge stimmen in jeder Zeile der Wahrheitstabelle."""

    namen: list[str]

    def pruefe(self, lauf: SchaltungLauf) -> list[Befund]:
        befunde = []
        for name in self.namen:
            spalte = lauf.level.soll[name]
            for nr, zeile in enumerate(lauf.tabelle):
                if spalte[nr] != "x" and str(zeile[name]) != spalte[nr]:
                    belegung = ", ".join(f"{e} = {zeile[e]}" for e in lauf.level.eingaenge)
                    befunde.append(Befund(None, f"bei {belegung} ist {name} {zeile[name]}, soll {spalte[nr]}"))
                    break
        return befunde


class WieVorgegeben:
    """Beim Verdrahten genau die vorgegebenen Bausteine, keiner mehr und keiner weniger."""

    def pruefe(self, lauf: SchaltungLauf) -> list[Befund]:
        soll = {(v.name, v.art) for v in lauf.level.vorgabe}
        ist = {(b.name, b.art) for b in lauf.plan.bausteine}
        if soll == ist:
            return []
        fehlt = ", ".join(f"{n} ({a})" for n, a in sorted(soll - ist))
        zuviel = ", ".join(f"{n} ({a})" for n, a in sorted(ist - soll))
        teile = [f"es fehlt {fehlt}" if fehlt else "", f"dazugekommen ist {zuviel}" if zuviel else ""]
        return [Befund(None, "Hier wird nur verdrahtet: " + "; ".join(t for t in teile if t))]


WIE_VORGEGEBEN = WieVorgegeben()


def _pruefe_regel(regel, lauf: SchaltungLauf) -> list[Befund]:
    return regel.pruefe(lauf)


# --- Antworten -----------------------------------------------------------------


class Kennzahlen(BaseModel):
    bausteine: int
    tiefe: int
    richtig: int
    zeilen: int


class Wiedergabe(BaseModel):
    """Die Wahrheitstabelle: je Zeile [Nummer, Werte aller Signale und Ausgänge]."""

    name: str
    sichtbar: bool
    dauer: int
    bilder: list[tuple[int, dict[str, int]]]
    kennzahlen: Kennzahlen
    fehler: str | None = None


class AblaufStand(BaseModel):
    name: str
    sichtbar: bool
    ok: bool
    kennzahlen: Kennzahlen
    erste_stelle: float | None = None
    erster_befund: str | None = None


class SchaltungAuswertung(BaseModel):
    teilschritte: list[TeilschrittStand]
    ablaeufe: list[AblaufStand]
    wiedergaben: list[Wiedergabe]


class SchaltungLaeufe(BaseModel):
    auswertung: SchaltungAuswertung | None
    stdout: str = ""
    stderr: str = ""
    laufzeit_ms: float = 0
    timeout: bool = False


# --- Ablauf --------------------------------------------------------------------


def level_von(aufgabe: Aufgabe) -> SchaltungLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return SchaltungLevel.model_validate(extra.get("schaltung"))


def laufe(code: str, level: SchaltungLevel) -> SchaltungLaeufe:
    beginn = time.perf_counter()
    plan = schaltung.lies(code, level.eingaenge, level.ausgaenge, level.bausteine)
    if plan.fehler:
        return SchaltungLaeufe(auswertung=None, stderr="\n".join(plan.fehler[:6]))
    tabelle = schaltung.wahrheitstabelle(plan, level.eingaenge)
    lauf = SchaltungLauf(TABELLE, True, level, plan, tabelle)
    alle = Ausgaenge(level.ausgaenge)
    richtig = sum(1 for nr, zeile in enumerate(tabelle)
                  if all(level.soll[a][nr] in ("x", str(zeile[a])) for a in level.ausgaenge))
    kennzahlen = Kennzahlen(bausteine=len(plan.bausteine), tiefe=schaltung.tiefe(plan, level.eingaenge),
                            richtig=richtig, zeilen=len(tabelle))
    befunde = ablauf_befunde([alle, *([WIE_VORGEGEBEN] if level.vorgabe else [])], lauf, _pruefe_regel)
    stand = AblaufStand(name=TABELLE, sichtbar=True, ok=not befunde, kennzahlen=kennzahlen,
                        erster_befund=befunde[0].als_text(None) if befunde else None)
    wiedergabe = Wiedergabe(name=TABELLE, sichtbar=True, dauer=len(tabelle),
                            bilder=[(nr, zeile) for nr, zeile in enumerate(tabelle)], kennzahlen=kennzahlen)
    teilschritte = auswerten(level.schritte(), [lauf], _pruefe_regel, [{TABELLE}] * len(level.teilschritte))
    return SchaltungLaeufe(auswertung=SchaltungAuswertung(teilschritte=teilschritte, ablaeufe=[stand],
                                                          wiedergaben=[wiedergabe]),
                           laufzeit_ms=(time.perf_counter() - beginn) * 1000)


def lauf_sichtbar(aufgabe: Aufgabe, code: str) -> SchaltungLaeufe:
    return laufe(code, level_von(aufgabe))


def kriterien(level: SchaltungLevel, geschafft: bool, kennzahlen: Kennzahlen | None) -> list[SternKriterium]:
    s = level.sterne
    sparsam = geschafft and kennzahlen is not None and kennzahlen.bausteine <= s.bausteine
    return [
        SternKriterium(text="die ganze Wahrheitstabelle stimmt", erreicht=geschafft),
        SternKriterium(text=f"höchstens {s.bausteine} {'Baustein' if s.bausteine == 1 else 'Bausteine'}",
                       erreicht=sparsam),
        SternKriterium(text=f"dazu höchstens {s.tiefe} {'Baustein' if s.tiefe == 1 else 'Bausteine'} auf dem längsten Weg",
                       erreicht=sparsam and kennzahlen.tiefe <= s.tiefe),
    ]


# --- Bestand -------------------------------------------------------------------


def _pruefe_aufbau(aufgabe: Aufgabe) -> list[str]:
    try:
        level = level_von(aufgabe)
    except ValidationError as fehler:
        return [f"schaltung: {e['loc']} {e['msg']}" for e in fehler.errors()]
    meldungen = [f"Baustein {b} gibt es nicht" for b in level.bausteine if b not in schaltung.ARTEN]
    meldungen += [f"Vorgabe {v.name}: {v.art} ist nicht erlaubt" for v in level.vorgabe if v.art not in level.bausteine]
    namen = set(level.eingaenge) | set(level.ausgaenge)
    meldungen += [f"Eingänge und Ausgänge brauchen verschiedene Namen"] if len(namen) != len(level.eingaenge) + len(level.ausgaenge) else []
    for t in level.teilschritte:
        if isinstance(t.ausgaenge, list):
            meldungen += [f"Teilschritt {t.titel}: Ausgang {a} gibt es nicht" for a in t.ausgaenge if a not in level.ausgaenge]
    if level.teilschritte[-1].ausgaenge != "alle":
        meldungen.append("der letzte Teilschritt prüft alle Ausgänge (ausgaenge: alle)")
    return meldungen


@registriere(
    "schaltung",
    zaehle_versteckt=lambda aufgabe: 0,
    vergleicht_zeichen=False,
    pruefe_aufbau=_pruefe_aufbau,
)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    level = level_von(aufgabe)
    ergebnis = laufe(code, level)
    a = ergebnis.auswertung
    if a is None:
        return PruefErgebnis(
            bestanden=False,
            sichtbar=[TestErgebnis(index=0, bestanden=False, eingabe=[TABELLE], fehler=ergebnis.stderr)],
            versteckt_pass=0, versteckt_fail=0, laufzeit_ms=ergebnis.laufzeit_ms, stderr=ergebnis.stderr,
            wertung=Wertung(sterne=0, kriterien=kriterien(level, False, None)),
        )
    stand = a.ablaeufe[0]
    geschafft = all(t.erfuellt for t in a.teilschritte)
    k = kriterien(level, geschafft, stand.kennzahlen)
    return PruefErgebnis(
        bestanden=geschafft,
        sichtbar=[TestErgebnis(index=0, bestanden=stand.ok, eingabe=[TABELLE], erwartet="die ganze Tabelle stimmt",
                               tatsaechlich=a.model_dump(), fehler=stand.erster_befund)],
        versteckt_pass=0, versteckt_fail=0, laufzeit_ms=ergebnis.laufzeit_ms,
        wertung=Wertung(sterne=sum(1 for x in k if x.erreicht), kriterien=k),
    )
