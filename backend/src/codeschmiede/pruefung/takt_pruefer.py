"""Prüfer für `task_type: takt` (Spiel Digitale Schaltungen, mit Takt).

Abgegeben wird ein Schaltplan als Text wie bei den Schaltungen (steuerung/schaltung.py), dazu gibt es Flipflops. Statt
der Wahrheitstabelle laufen Abläufe: Folgen von Takten mit den Eingängen je Takt und dem Soll der Ausgänge je Takt.
Gerechnet wird im Backend ohne Sandbox. Versteckte Abläufe drücken die Eingänge zu anderen Zeiten.

Die Teilschritte nennen Ausgänge, die ab ihnen stimmen müssen, und Abläufe, in denen sie gelten (wie bei den
Steuerungsspielen: der erste gilt im ersten sichtbaren Ablauf, "alle" nimmt die versteckten dazu).

Sterne: einer, wenn alle Takte aller Abläufe stimmen; zwei, wenn dazu höchstens so viele Bausteine außer den
Flipflops; drei, wenn dazu der längste Weg zwischen Eingängen, Flipflops und Ausgängen höchstens so viele Bausteine
lang ist (er bestimmt, wie schnell der Takt sein darf).

Im Frontmatter:
  takt:
    eingaenge: [R]                       auch leer
    ausgaenge: [Q1, Q0]
    bausteine: [FF, NICHT, XOR]          erlaubte Arten, FF gehört dazu
    vorgabe: [...]                       beim Verdrahten wie bei den Schaltungen; leer heißt frei bauen
    zahl: [Q1, Q0]                       Ausgänge, die zusammen eine Zahl zeigen (höchste Stelle vorn), nur für die Anzeige
    sichtbar: [{name, takte: 8, eingaben: {R: "00010000"}, soll: {Q0: "01010101", ...}}, ...]
    versteckt: [...]                     gehen nie an den Browser
    teilschritte: [{titel, text, ausgaenge: [Q0] | alle, ablaeufe: [name, ...] | alle}, ...]
    sterne: {bausteine: 2, tiefe: 1}
Fehlt ein Eingang in `eingaben`, ist er in jedem Takt 0. Im Soll heißt x: egal.
"""

import time
from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from ..steuerung import schaltung
from ..steuerung.teilschritte import Befund, TeilschrittStand, ablauf_befunde, ablauf_mengen, auswerten
from .ergebnis import PruefErgebnis, SternKriterium, TestErgebnis, Wertung
from .registry import registriere
from .schaltung_pruefer import WIE_VORGEGEBEN, Vorgabe


class TaktAblauf(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    takte: int = Field(ge=1, le=64)
    eingaben: dict[str, str] = Field(default_factory=dict)
    soll: dict[str, str]

    def eingabe_folge(self, eingaenge: list[str]) -> list[dict[str, int]]:
        """Je Takt die Werte aller Eingänge; ein Eingang ohne Folge ist 0."""
        folgen = {e: self.eingaben.get(e, "0" * self.takte) for e in eingaenge}
        return [{e: int(folgen[e][i]) for e in eingaenge} for i in range(self.takte)]


class TaktTeilschritt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    titel: str
    text: str
    ausgaenge: Literal["alle"] | list[str] | None = None
    ablaeufe: Literal["alle"] | list[str] | None = None


class TaktSterne(BaseModel):
    model_config = ConfigDict(extra="forbid")

    bausteine: int = Field(ge=0)
    tiefe: int = Field(ge=1)


class TaktLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    eingaenge: list[str] = Field(default_factory=list, max_length=8)
    ausgaenge: list[str] = Field(min_length=1, max_length=8)
    bausteine: list[str] = Field(min_length=1)
    vorgabe: list[Vorgabe] = Field(default_factory=list)
    zahl: list[str] = Field(default_factory=list)
    aufbauend_auf: str | None = None
    sichtbar: list[TaktAblauf] = Field(min_length=1)
    versteckt: list[TaktAblauf] = Field(default_factory=list)
    teilschritte: list[TaktTeilschritt] = Field(min_length=1)
    sterne: TaktSterne

    @model_validator(mode="after")
    def _stimmig(self) -> "TaktLevel":
        for a in self.ablaeufe():
            if set(a.soll) != set(self.ausgaenge):
                raise ValueError(f"Ablauf {a.name}: soll braucht genau eine Folge je Ausgang")
            for name, folge in a.soll.items():
                if len(folge) != a.takte or set(folge) - set("01x"):
                    raise ValueError(f"Ablauf {a.name}, soll {name}: {a.takte} Zeichen aus 0, 1 und x")
            for name, folge in a.eingaben.items():
                if name not in self.eingaenge:
                    raise ValueError(f"Ablauf {a.name}: einen Eingang {name} gibt es nicht")
                if len(folge) != a.takte or set(folge) - set("01"):
                    raise ValueError(f"Ablauf {a.name}, Eingang {name}: {a.takte} Zeichen aus 0 und 1")
        return self

    def ablaeufe(self) -> list[TaktAblauf]:
        return [*self.sichtbar, *self.versteckt]

    def schritte(self) -> list["_Schritt"]:
        """Die Teilschritte im Format der gemeinsamen Auswertung; der erste prüft auch die Vorgabe beim Verdrahten."""
        liste = []
        for i, t in enumerate(self.teilschritte):
            namen = self.ausgaenge if t.ausgaenge == "alle" else (t.ausgaenge or [])
            regeln: list = [Ausgaenge(namen)] if namen else []
            if i == 0 and self.vorgabe:
                regeln.insert(0, WIE_VORGEGEBEN)
            liste.append(_Schritt(t.titel, t.text, regeln, t.ablaeufe))
        return liste

    def mengen(self) -> list[set[str]]:
        return ablauf_mengen(self.schritte(), [a.name for a in self.ablaeufe()], self.sichtbar[0].name)


@dataclass
class _Schritt:
    titel: str
    text: str
    regeln: list
    ablaeufe: Literal["alle"] | list[str] | None


@dataclass
class TaktLauf:
    """Ein Ablauf nach dem Lauf, wie die Regeln ihn lesen."""

    name: str
    sichtbar: bool
    level: TaktLevel
    ablauf: TaktAblauf
    plan: schaltung.Plan
    verlauf: list[dict[str, int]]
    fehler: str | None = None

    def falsch(self, namen: list[str]) -> list[tuple[int, str]]:
        """Je Takt, in dem einer dieser Ausgänge vom Soll abweicht: (Takt, Ausgang), der erste je Takt."""
        stellen = []
        for nr, werte in enumerate(self.verlauf):
            name = next((n for n in namen if self.ablauf.soll[n][nr] not in ("x", str(werte[n]))), None)
            if name is not None:
                stellen.append((nr, name))
        return stellen


@dataclass(frozen=True)
class Ausgaenge:
    """Diese Ausgänge stimmen in jedem Takt."""

    namen: list[str]

    def pruefe(self, lauf: TaktLauf) -> list[Befund]:
        befunde = []
        for name in self.namen:
            stelle = next(iter(lauf.falsch([name])), None)
            if stelle is not None:
                nr = stelle[0]
                befunde.append(Befund(None, f"Takt {nr}: {name} ist {lauf.verlauf[nr][name]}, soll {lauf.ablauf.soll[name][nr]}"))
        return befunde


def _pruefe_regel(regel, lauf: TaktLauf) -> list[Befund]:
    return regel.pruefe(lauf)


# --- Antworten -----------------------------------------------------------------


class Kennzahlen(BaseModel):
    bausteine: int
    flipflops: int
    tiefe: int
    richtig: int
    takte: int


class Wiedergabe(BaseModel):
    """Ein Ablauf zum Abspielen: je Takt [Nummer, Werte aller Signale, Flipflops und Ausgänge], dazu Eingaben und
    Soll als Folgen aus 0, 1 (und x)."""

    name: str
    sichtbar: bool
    dauer: int
    bilder: list[tuple[int, dict[str, int]]]
    eingaben: dict[str, str]
    soll: dict[str, str]
    kennzahlen: Kennzahlen
    fehler: str | None = None


class AblaufStand(BaseModel):
    name: str
    sichtbar: bool
    ok: bool
    kennzahlen: Kennzahlen
    erste_stelle: float | None = None
    erster_befund: str | None = None


class TaktAuswertung(BaseModel):
    teilschritte: list[TeilschrittStand]
    ablaeufe: list[AblaufStand]
    wiedergaben: list[Wiedergabe]


class TaktLaeufe(BaseModel):
    auswertung: TaktAuswertung | None
    stdout: str = ""
    stderr: str = ""
    laufzeit_ms: float = 0
    timeout: bool = False


# --- Ablauf --------------------------------------------------------------------


def level_von(aufgabe: Aufgabe) -> TaktLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return TaktLevel.model_validate(extra.get("takt"))


def laufe(code: str, level: TaktLevel, ablaeufe: list[TaktAblauf]) -> TaktLaeufe:
    """Liest den Plan und lässt ihn durch die Abläufe laufen (zuerst die sichtbaren)."""
    beginn = time.perf_counter()
    plan = schaltung.lies(code, level.eingaenge, level.ausgaenge, level.bausteine)
    if plan.fehler:
        return TaktLaeufe(auswertung=None, stderr="\n".join(plan.fehler[:6]))
    ff = len(schaltung.flipflops(plan))
    gatter = len(plan.bausteine) - ff
    tiefe = schaltung.tiefe(plan, level.eingaenge)
    sichtbar = {a.name for a in level.sichtbar}
    laeufe = [TaktLauf(a.name, a.name in sichtbar, level, a, plan,
                       schaltung.takte(plan, level.eingaenge, a.eingabe_folge(level.eingaenge)))
              for a in ablaeufe]
    regeln = [Ausgaenge(level.ausgaenge), *([WIE_VORGEGEBEN] if level.vorgabe else [])]
    staende, wiedergaben = [], []
    versteckt_gezeigt = False
    for tl in laeufe:
        befunde = ablauf_befunde(regeln, tl, _pruefe_regel)
        falsch = tl.falsch(level.ausgaenge)
        kennzahlen = Kennzahlen(bausteine=gatter, flipflops=ff, tiefe=tiefe, richtig=tl.ablauf.takte - len(falsch),
                                takte=tl.ablauf.takte)
        stand = AblaufStand(name=tl.name, sichtbar=tl.sichtbar, ok=not befunde, kennzahlen=kennzahlen,
                            erste_stelle=falsch[0][0] if falsch else None,
                            erster_befund=befunde[0].als_text(None) if befunde else None)
        staende.append(stand)
        if tl.sichtbar or (not stand.ok and not versteckt_gezeigt):
            versteckt_gezeigt = versteckt_gezeigt or not tl.sichtbar
            wiedergaben.append(Wiedergabe(
                name=tl.name, sichtbar=tl.sichtbar, dauer=tl.ablauf.takte,
                bilder=[(nr, werte) for nr, werte in enumerate(tl.verlauf)],
                eingaben={e: tl.ablauf.eingaben.get(e, "0" * tl.ablauf.takte) for e in level.eingaenge},
                soll=tl.ablauf.soll, kennzahlen=kennzahlen,
            ))
    teilschritte = auswerten(level.schritte(), laeufe, _pruefe_regel, level.mengen())
    return TaktLaeufe(auswertung=TaktAuswertung(teilschritte=teilschritte, ablaeufe=staende, wiedergaben=wiedergaben),
                      laufzeit_ms=(time.perf_counter() - beginn) * 1000)


def lauf_sichtbar(aufgabe: Aufgabe, code: str) -> TaktLaeufe:
    """Probelauf: nur die sichtbaren Abläufe, ohne Wertung."""
    level = level_von(aufgabe)
    return laufe(code, level, level.sichtbar)


def _bausteine(n: int) -> str:
    return f"{n} {'Baustein' if n == 1 else 'Bausteine'}"


def kriterien(level: TaktLevel, geschafft: bool, kennzahlen: Kennzahlen | None) -> list[SternKriterium]:
    s = level.sterne
    sparsam = geschafft and kennzahlen is not None and kennzahlen.bausteine <= s.bausteine
    return [
        SternKriterium(text="alle Takte stimmen, auch in den versteckten Abläufen", erreicht=geschafft),
        SternKriterium(text=f"höchstens {_bausteine(s.bausteine)} außer den Flipflops", erreicht=sparsam),
        SternKriterium(text=f"dazu höchstens {_bausteine(s.tiefe)} auf dem längsten Weg", erreicht=sparsam and kennzahlen.tiefe <= s.tiefe),
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
        return [f"takt: {e['loc']} {e['msg']}" for e in fehler.errors()]
    meldungen = [f"Baustein {b} gibt es nicht" for b in level.bausteine if b not in schaltung.EINGAENGE]
    if schaltung.SPEICHER not in level.bausteine:
        meldungen.append(f"ohne {schaltung.SPEICHER} gibt es keinen Takt")
    meldungen += [f"Vorgabe {v.name}: {v.art} ist nicht erlaubt" for v in level.vorgabe if v.art not in level.bausteine]
    if len(set(level.eingaenge) | set(level.ausgaenge)) != len(level.eingaenge) + len(level.ausgaenge):
        meldungen.append("Eingänge und Ausgänge brauchen verschiedene Namen")
    meldungen += [f"zahl: einen Ausgang {z} gibt es nicht" for z in level.zahl if z not in level.ausgaenge]
    namen = [a.name for a in level.ablaeufe()]
    if len(set(namen)) != len(namen):
        meldungen.append("Abläufe brauchen verschiedene Namen")
    for t in level.teilschritte:
        if isinstance(t.ausgaenge, list):
            meldungen += [f"Teilschritt {t.titel}: Ausgang {a} gibt es nicht" for a in t.ausgaenge if a not in level.ausgaenge]
        if isinstance(t.ablaeufe, list):
            meldungen += [f"Teilschritt {t.titel}: Ablauf {a} gibt es nicht" for a in t.ablaeufe if a not in namen]
    if level.mengen()[-1] != set(namen):
        meldungen.append("der letzte Teilschritt prüft alle Abläufe (ablaeufe: alle)")
    geprueft = {a for t in level.teilschritte for a in (level.ausgaenge if t.ausgaenge == "alle" else t.ausgaenge or [])}
    if geprueft != set(level.ausgaenge):
        meldungen.append("die Teilschritte prüfen nicht alle Ausgänge")
    return meldungen


@registriere(
    "takt",
    verbirgt=("takt.versteckt",),
    zaehle_versteckt=_anzahl_versteckt,
    vergleicht_zeichen=False,
    pruefe_aufbau=_pruefe_aufbau,
)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    level = level_von(aufgabe)
    ergebnis = laufe(code, level, level.ablaeufe())
    a = ergebnis.auswertung
    if a is None:
        return PruefErgebnis(
            bestanden=False,
            sichtbar=[TestErgebnis(index=0, bestanden=False, eingabe=[level.sichtbar[0].name], fehler=ergebnis.stderr)],
            versteckt_pass=0, versteckt_fail=len(level.versteckt), laufzeit_ms=ergebnis.laufzeit_ms,
            stderr=ergebnis.stderr, wertung=Wertung(sterne=0, kriterien=kriterien(level, False, None)),
        )
    erstes = a.ablaeufe[0]
    versteckt = a.ablaeufe[len(level.sichtbar):]
    geschafft = all(t.erfuellt for t in a.teilschritte)
    k = kriterien(level, geschafft, erstes.kennzahlen)
    return PruefErgebnis(
        bestanden=geschafft,
        sichtbar=[TestErgebnis(index=0, bestanden=erstes.ok, eingabe=[erstes.name], erwartet="alle Takte stimmen",
                               tatsaechlich=a.model_dump(), fehler=erstes.erster_befund)],
        versteckt_pass=sum(1 for x in versteckt if x.ok),
        versteckt_fail=sum(1 for x in versteckt if not x.ok),
        laufzeit_ms=ergebnis.laufzeit_ms,
        wertung=Wertung(sterne=sum(1 for x in k if x.erreicht), kriterien=k),
    )
