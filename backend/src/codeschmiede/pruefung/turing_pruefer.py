"""Prüfer für `task_type: turing` (Spiel Turingmaschine).

Abgegeben wird eine Übergangstabelle als Text (steuerung/turing.py). Sie läuft auf sichtbaren und versteckten Bändern,
ganz ohne Sandbox, mit einer Grenze an Schritten. Ein Band gilt, wenn die Maschine in einem Endzustand hält und das
Band dann das Erwartete trägt (oder bei Entscheidern im richtigen Endzustand hält, etwa ja oder nein).

Die Teilschritte nennen Bänder beim Namen (wie die Abläufe der Steuerungsspiele): der erste gilt im ersten sichtbaren
Band, "alle" nimmt die versteckten dazu.

Sterne: einer, wenn alle Bänder stimmen; zwei, wenn dazu höchstens so viele Zustände nötig sind (ohne Endzustände);
drei, wenn dazu die Tabelle höchstens so viele Zeilen hat.

Im Frontmatter:
  turing:
    zeichen: ["0", "1"]          Zeichen auf dem Band außer _ (leer)
    start: plus
    ende: [fertig]               oder [ja, nein] bei Entscheidern
    kopf: anfang | ende          wo der Kopf zu Beginn steht (erstes oder letztes Zeichen)
    grenze: 500                  höchstens so viele Schritte je Band
    sichtbar: [{band: "1011", soll: "1100"}, {band: "0110", soll_zustand: ja}, ...]
    versteckt: [...]             gehen nie an den Browser
    teilschritte: [{titel, text, baender: [name, ...] | alle}, ...]
    sterne: {zustaende: 1, zeilen: 3}
"""

import time
from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from ..steuerung import turing
from ..steuerung.teilschritte import Befund, TeilschrittStand, ablauf_befunde, ablauf_mengen, auswerten
from .ergebnis import Kennwerte, PruefErgebnis, SternKriterium, TestErgebnis, Wertung
from .registry import registriere


class Band(BaseModel):
    model_config = ConfigDict(extra="forbid")

    band: str
    name: str | None = None
    soll: str | None = None
    soll_zustand: str | None = None

    @model_validator(mode="after")
    def _ein_ziel(self) -> "Band":
        if (self.soll is None) == (self.soll_zustand is None):
            raise ValueError("genau eins von soll und soll_zustand")
        return self

    @property
    def titel(self) -> str:
        return self.name or self.band or "leer"


class TuringTeilschritt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    titel: str
    text: str
    baender: Literal["alle"] | list[str] | None = None


class TuringSterne(BaseModel):
    model_config = ConfigDict(extra="forbid")

    zustaende: int = Field(ge=1)
    zeilen: int = Field(ge=1)


class TuringLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    zeichen: list[str] = Field(min_length=1)
    start: str
    ende: list[str] = Field(min_length=1)
    kopf: Literal["anfang", "ende"] = "anfang"
    grenze: int = Field(default=500, ge=10, le=20_000)
    aufbauend_auf: str | None = None
    sichtbar: list[Band] = Field(min_length=1)
    versteckt: list[Band] = Field(default_factory=list)
    teilschritte: list[TuringTeilschritt] = Field(min_length=1)
    sterne: TuringSterne

    def baender(self) -> list[Band]:
        return [*self.sichtbar, *self.versteckt]

    def schritte(self) -> list["_Schritt"]:
        """Die Teilschritte im Format der gemeinsamen Auswertung; die eine Regel (Band stimmt) gilt ab dem ersten."""
        return [_Schritt(t.titel, t.text, [RICHTIG] if i == 0 else [], t.baender) for i, t in enumerate(self.teilschritte)]

    def mengen(self) -> list[set[str]]:
        return ablauf_mengen(self.schritte(), [b.titel for b in self.baender()], self.sichtbar[0].titel)


@dataclass
class _Schritt:
    titel: str
    text: str
    regeln: list
    ablaeufe: Literal["alle"] | list[str] | None


@dataclass
class TuringLauf:
    """Ein Band nach dem Lauf, wie die Regel es liest."""

    name: str
    sichtbar: bool
    band: Band
    lauf: turing.Lauf
    fehler: str | None = None


class Richtig:
    """Die Maschine hält in einem Endzustand, und das Band (oder der Endzustand) ist das erwartete."""

    def pruefe(self, lauf: TuringLauf) -> list[Befund]:
        l, b = lauf.lauf, lauf.band
        schritte = len(l.schritte) - 1
        if not l.gehalten:
            return [Befund(None, f"Band {b.titel}: {l.grund}")]
        if b.soll is not None and l.band != b.soll:
            return [Befund(None, f"Band {b.titel}: am Ende steht {l.band or 'nichts'}, soll {b.soll or 'nichts'} "
                                 f"(nach {schritte} Schritten)")]
        if b.soll_zustand is not None and l.zustand != b.soll_zustand:
            return [Befund(None, f"Band {b.titel}: hält in {l.zustand}, soll in {b.soll_zustand}")]
        return []


RICHTIG = Richtig()


def _pruefe_regel(regel: Richtig, lauf: TuringLauf) -> list[Befund]:
    return regel.pruefe(lauf)


# --- Antworten -----------------------------------------------------------------


class Kennzahlen(BaseModel):
    schritte: int
    zustaende: int
    zeilen: int


class Wiedergabe(BaseModel):
    """Ein Band zum Abspielen. Je Schritt: [Nummer, Band ab Feld `von`, von, Kopf, Zustand, Zeile der Regel]."""

    name: str
    sichtbar: bool
    dauer: int
    bilder: list[tuple[int, str, int, int, str, int | None]]
    start: str
    soll: str | None
    soll_zustand: str | None
    ergebnis: str
    kennzahlen: Kennzahlen
    fehler: str | None = None


class AblaufStand(BaseModel):
    name: str
    sichtbar: bool
    ok: bool
    kennzahlen: Kennzahlen
    erste_stelle: float | None = None
    erster_befund: str | None = None


class TuringAuswertung(BaseModel):
    teilschritte: list[TeilschrittStand]
    ablaeufe: list[AblaufStand]
    wiedergaben: list[Wiedergabe]


class TuringLaeufe(BaseModel):
    auswertung: TuringAuswertung | None
    stdout: str = ""
    stderr: str = ""
    laufzeit_ms: float = 0
    timeout: bool = False


# --- Ablauf --------------------------------------------------------------------


def level_von(aufgabe: Aufgabe) -> TuringLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return TuringLevel.model_validate(extra.get("turing"))


def _start_kopf(level: TuringLevel, band: str) -> int:
    return max(0, len(band) - 1) if level.kopf == "ende" else 0


def laufe(code: str, level: TuringLevel, baender: list[Band]) -> TuringLaeufe:
    """Liest die Tabelle und lässt sie auf den Bändern laufen (zuerst die sichtbaren)."""
    beginn = time.perf_counter()
    tabelle = turing.lies(code, set(level.zeichen))
    if tabelle.fehler:
        return TuringLaeufe(auswertung=None, stderr="\n".join(tabelle.fehler[:5]))
    ende = set(level.ende)
    zustaende = len(tabelle.zustaende(ende))
    sichtbar = {b.titel for b in level.sichtbar}
    laeufe = []
    for b in baender:
        lauf = turing.laufe(tabelle, b.band, _start_kopf(level, b.band), level.start, ende, level.grenze)
        laeufe.append(TuringLauf(name=b.titel, sichtbar=b.titel in sichtbar, band=b, lauf=lauf))
    staende, wiedergaben = [], []
    versteckt_gezeigt = False
    for tl in laeufe:
        befunde = ablauf_befunde([RICHTIG], tl, _pruefe_regel)
        kennzahlen = Kennzahlen(schritte=len(tl.lauf.schritte) - 1, zustaende=zustaende, zeilen=len(tabelle.regeln))
        stand = AblaufStand(name=tl.name, sichtbar=tl.sichtbar, ok=not befunde, kennzahlen=kennzahlen,
                            erste_stelle=0 if befunde else None,
                            erster_befund=befunde[0].als_text(None) if befunde else None)
        staende.append(stand)
        if tl.sichtbar or (not stand.ok and not versteckt_gezeigt):
            versteckt_gezeigt = versteckt_gezeigt or not tl.sichtbar
            wiedergaben.append(Wiedergabe(
                name=tl.name, sichtbar=tl.sichtbar, dauer=len(tl.lauf.schritte) - 1,
                bilder=[(i, s.band, s.von, s.kopf, s.zustand, s.regel) for i, s in enumerate(tl.lauf.schritte)],
                start=tl.band.band, soll=tl.band.soll, soll_zustand=tl.band.soll_zustand, ergebnis=tl.lauf.band,
                kennzahlen=kennzahlen, fehler=None,
            ))
    teilschritte = auswerten(level.schritte(), laeufe, _pruefe_regel, level.mengen())
    return TuringLaeufe(auswertung=TuringAuswertung(teilschritte=teilschritte, ablaeufe=staende, wiedergaben=wiedergaben),
                        laufzeit_ms=(time.perf_counter() - beginn) * 1000)


def lauf_sichtbar(aufgabe: Aufgabe, code: str) -> TuringLaeufe:
    """Probelauf: nur die sichtbaren Bänder, ohne Wertung."""
    level = level_von(aufgabe)
    return laufe(code, level, level.sichtbar)


def kriterien(level: TuringLevel, geschafft: bool, kennzahlen: Kennzahlen | None) -> list[SternKriterium]:
    s = level.sterne
    knapp = geschafft and kennzahlen is not None and kennzahlen.zustaende <= s.zustaende
    return [
        SternKriterium(text=f"alle Bänder richtig, je höchstens {level.grenze} Schritte", erreicht=geschafft),
        SternKriterium(text=f"höchstens {s.zustaende} {'Zustand' if s.zustaende == 1 else 'Zustände'} "
                            f"(ohne {', '.join(level.ende)})", erreicht=knapp),
        SternKriterium(text=f"dazu höchstens {s.zeilen} Zeilen", erreicht=knapp and kennzahlen.zeilen <= s.zeilen),
    ]


# --- Bestand -------------------------------------------------------------------


def _anzahl_versteckt(aufgabe: Aufgabe) -> int:
    try:
        return len(level_von(aufgabe).versteckt)
    except ValidationError:
        return 0


def _pruefe_aufbau(aufgabe: Aufgabe) -> list[str]:
    try:
        level = level_von(aufgabe)
    except ValidationError as fehler:
        return [f"turing: {e['loc']} {e['msg']}" for e in fehler.errors()]
    meldungen = []
    erlaubt = set(level.zeichen) | {turing.LEER}
    for b in level.baender():
        meldungen += [f"Band {b.titel}: Zeichen {z} gibt es nicht" for z in set(b.band + (b.soll or "")) if z not in erlaubt]
        if b.soll_zustand is not None and b.soll_zustand not in level.ende:
            meldungen.append(f"Band {b.titel}: {b.soll_zustand} ist kein Endzustand")
    namen = [b.titel for b in level.baender()]
    if len(set(namen)) != len(namen):
        meldungen.append("Bänder brauchen verschiedene Namen")
    if level.mengen()[-1] != set(namen):
        meldungen.append("der letzte Teilschritt prüft alle Bänder (baender: alle)")
    for t in level.teilschritte:
        if isinstance(t.baender, list):
            meldungen += [f"Teilschritt {t.titel}: Band {n} gibt es nicht" for n in t.baender if n not in namen]
    return meldungen


@registriere(
    "turing",
    verbirgt=("turing.versteckt",),
    zaehle_versteckt=_anzahl_versteckt,
    vergleicht_zeichen=False,
    pruefe_aufbau=_pruefe_aufbau,
)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    level = level_von(aufgabe)
    ergebnis = laufe(code, level, level.baender())
    a = ergebnis.auswertung
    if a is None:
        return PruefErgebnis(
            bestanden=False,
            sichtbar=[TestErgebnis(index=0, bestanden=False, eingabe=[level.sichtbar[0].titel], fehler=ergebnis.stderr)],
            versteckt_pass=0,
            versteckt_fail=len(level.versteckt),
            laufzeit_ms=ergebnis.laufzeit_ms,
            stderr=ergebnis.stderr,
            wertung=Wertung(sterne=0, kriterien=kriterien(level, False, None)),
        )
    erstes = a.ablaeufe[0]
    versteckt = a.ablaeufe[len(level.sichtbar):]
    geschafft = all(t.erfuellt for t in a.teilschritte)
    k = kriterien(level, geschafft, erstes.kennzahlen)
    return PruefErgebnis(
        bestanden=geschafft,
        sichtbar=[TestErgebnis(index=0, bestanden=erstes.ok, eingabe=[erstes.name], erwartet="alle Bänder richtig",
                               tatsaechlich=a.model_dump(), fehler=erstes.erster_befund)],
        versteckt_pass=sum(1 for x in versteckt if x.ok),
        versteckt_fail=sum(1 for x in versteckt if not x.ok),
        laufzeit_ms=ergebnis.laufzeit_ms,
        wertung=Wertung(sterne=sum(1 for x in k if x.erreicht), kriterien=k,
                        kennwerte=Kennwerte(schritte=erstes.kennzahlen.schritte, zeilen=erstes.kennzahlen.zeilen)),
    )
