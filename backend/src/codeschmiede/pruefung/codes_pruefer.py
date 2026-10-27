"""Prüfer für `task_type: codes` (Spiel Codes knacken).

Abgegeben wird Python mit einer Funktion, meist `knacke(geheim)`, die aus einem Geheimtext den Klartext macht. Die
Nachrichten stehen im Level als Klartext und Schlüssel; den Geheimtext rechnet der Server (steuerung/codes.py). In die
Sandbox gehen nur Programm und Eingaben, nie ein Klartext: verglichen wird hier.

Eine Nachricht kann eine andere Funktion aufrufen (`funktion`, etwa `schiebe` im ersten Teilschritt) und weitere
Argumente nach dem Geheimtext mitgeben (`mit`). Mit `richtung: verschluesseln` bekommt sie den Klartext und soll den
Geheimtext liefern (etwa `pruefwert("1234")`). Bereit stehen dem Programm die Häufigkeiten des Deutschen, wenn das
Level sie nennt (`DEUTSCH` in Prozent je Buchstabe, `PAARE` in Promille je Buchstabenpaar).

Die Teilschritte nennen Nachrichten beim Namen (wie die Abläufe der Steuerungsspiele): der erste gilt in der ersten
sichtbaren, "alle" nimmt die versteckten dazu.

Sterne: einer, wenn alle Nachrichten stimmen (beim Knacken genügt ab `mindestens` der Anteil richtiger Zeichen); zwei,
wenn dazu alle Aufrufe zusammen höchstens so viele Millisekunden brauchen; drei, wenn dazu der Code höchstens so viele
Zeichen hat (ohne Leerraum und Kommentare).

Im Frontmatter:
  codes:
    verfahren: caesar            caesar | ersetzung | vigenere | xor | schichten | pin
    funktion: knacke
    bereit: [DEUTSCH]
    mindestens: 1.0              Anteil richtiger Zeichen je geknackter Nachricht
    sichtbar: [{name, klar, schluessel, funktion?, mit?, richtung?, mindestens?}, ...]
    versteckt: [...]             gehen nie an den Browser
    teilschritte: [{titel, text, nachrichten: [name, ...] | alle}, ...]
    sterne: {ms: 50, zeichen: 300}
"""

import json
from dataclasses import dataclass
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from ..models.aufgabe import Aufgabe
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner
from ..steuerung import codes
from ..steuerung.teilschritte import Befund, TeilschrittStand, ablauf_befunde, ablauf_mengen, auswerten
from .ergebnis import Kennwerte, PruefErgebnis, SternKriterium, TestErgebnis, Wertung
from .registry import registriere
from .roboter_pruefer import zeichen_code
from .testlauf import FUNKTIONSNAME, hinweise, lies_block, neue_marke

BEREIT = {"DEUTSCH": codes.DEUTSCH, "PAARE": codes.PAARE}
# so viele Zeichen eines Ergebnisses kommen zurück und in einen Befund
ERGEBNIS_ZEICHEN = 4000
BEFUND_ZEICHEN = 40


class Nachricht(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    klar: str
    schluessel: int | str | list[str] | None = None
    funktion: str | None = None
    mit: list[int | str] = Field(default_factory=list)
    richtung: Literal["knacken", "verschluesseln"] = "knacken"
    # eigener Anteil richtiger Zeichen statt dem des Levels (etwa für eine erste Vermutung)
    mindestens: float | None = Field(default=None, gt=0, le=1)


class CodesTeilschritt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    titel: str
    text: str
    nachrichten: Literal["alle"] | list[str] | None = None


class CodesSterne(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ms: int = Field(ge=1)
    zeichen: int = Field(ge=1)


class CodesLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    verfahren: codes.Verfahren
    funktion: str = "knacke"
    bereit: list[Literal["DEUTSCH", "PAARE"]] = Field(default_factory=list)
    mindestens: float = Field(default=1.0, gt=0, le=1)
    aufbauend_auf: str | None = None
    sichtbar: list[Nachricht] = Field(min_length=1)
    versteckt: list[Nachricht] = Field(default_factory=list)
    teilschritte: list[CodesTeilschritt] = Field(min_length=1)
    sterne: CodesSterne

    @model_validator(mode="after")
    def _namen(self) -> "CodesLevel":
        namen = [n.name for n in self.nachrichten()]
        if len(set(namen)) != len(namen):
            raise ValueError("Nachrichten brauchen verschiedene Namen")
        return self

    def nachrichten(self) -> list[Nachricht]:
        return [*self.sichtbar, *self.versteckt]

    def funktion_von(self, n: Nachricht) -> str:
        return n.funktion or self.funktion

    def geheim(self, n: Nachricht) -> str:
        return codes.verschluessele(self.verfahren, n.klar, n.schluessel)

    def eingabe(self, n: Nachricht) -> list[Any]:
        return [n.klar if n.richtung == "verschluesseln" else self.geheim(n), *n.mit]

    def soll(self, n: Nachricht) -> str:
        return self.geheim(n) if n.richtung == "verschluesseln" else n.klar

    def noetig(self, n: Nachricht) -> float:
        if n.richtung == "verschluesseln":
            return 1.0
        return n.mindestens if n.mindestens is not None else self.mindestens

    def schritte(self) -> list["_Schritt"]:
        """Die Teilschritte im Format der gemeinsamen Auswertung; die eine Regel (Nachricht stimmt) gilt ab dem ersten."""
        return [_Schritt(t.titel, t.text, [RICHTIG] if i == 0 else [], t.nachrichten)
                for i, t in enumerate(self.teilschritte)]

    def mengen(self) -> list[set[str]]:
        return ablauf_mengen(self.schritte(), [n.name for n in self.nachrichten()], self.sichtbar[0].name)


@dataclass
class _Schritt:
    titel: str
    text: str
    regeln: list
    ablaeufe: Literal["alle"] | list[str] | None


# --- Lauf in der Sandbox ------------------------------------------------------

# Läuft in der Sandbox hinter _DATEN und _MARKE (siehe skript()). Die Uhr wird vor dem Programm gegriffen, damit es sie
# nicht verstellen kann.
LAUF = r'''
import json as _j, sys as _s, time as _t
_uhr = _t.perf_counter


def _zeile(e):
    tb, nr = e.__traceback__, 0
    while tb is not None:
        if tb.tb_frame.f_code.co_filename == "<programm>":
            nr = tb.tb_lineno
        tb = tb.tb_next
    return nr


def _lauf():
    namen = dict(_DATEN["bereit"], __name__="__main__")
    try:
        exec(compile(_DATEN["code"], "<programm>", "exec"), namen)
    except SyntaxError as e:
        return {"fehler": "SyntaxError: %s (Zeile %s)" % (e.msg, e.lineno), "aufrufe": []}
    except Exception as e:
        return {"fehler": "%s: %s (Zeile %d)" % (type(e).__name__, e, _zeile(e)), "aufrufe": []}
    aufrufe = []
    for funktion, eingabe in _DATEN["aufrufe"]:
        f = namen.get(funktion)
        if not callable(f):
            aufrufe.append({"fehler": "Es fehlt die Funktion %s()." % funktion, "ms": 0})
            continue
        beginn = _uhr()
        try:
            wert = f(*eingabe)
        except Exception as e:
            aufrufe.append({"fehler": "%s: %s (Zeile %d)" % (type(e).__name__, e, _zeile(e)), "ms": (_uhr() - beginn) * 1000})
            continue
        ms = (_uhr() - beginn) * 1000
        if isinstance(wert, str):
            aufrufe.append({"wert": wert[:_DATEN["laenge"]], "ms": ms})
        else:
            aufrufe.append({"fehler": "%s() gibt %s zurück, keinen Text" % (funktion, type(wert).__name__), "ms": ms})
    return {"fehler": None, "aufrufe": aufrufe}


_ergebnis = _lauf()
_s.stdout.flush()
_s.stdout.write("\n" + _MARKE + _j.dumps(_ergebnis) + "\n")
'''


class Aufruf(BaseModel):
    wert: str | None = None
    fehler: str | None = None
    ms: float = Field(default=0, ge=0)


class Gemeldet(BaseModel):
    fehler: str | None
    aufrufe: list[Aufruf]


def skript(code: str, bereit: dict[str, Any], aufrufe: list[tuple[str, list[Any]]], marke: str) -> str:
    daten = {"code": code, "bereit": bereit, "aufrufe": aufrufe, "laenge": ERGEBNIS_ZEICHEN}
    return f"_DATEN = __import__('json').loads({json.dumps(daten)!r})\n_MARKE = {marke!r}\n{LAUF}"


# --- Urteil -------------------------------------------------------------------


@dataclass
class CodesLauf:
    """Eine Nachricht nach dem Aufruf, wie die Regel sie liest."""

    name: str
    sichtbar: bool
    nachricht: Nachricht
    soll: str
    noetig: float
    aufruf: Aufruf
    fehler: str | None = None

    @property
    def anteil(self) -> float:
        return codes.anteil_gleich(self.aufruf.wert, self.soll) if self.aufruf.wert is not None else 0.0


def _kurz(text: str) -> str:
    return text if len(text) <= BEFUND_ZEICHEN else text[:BEFUND_ZEICHEN] + " ..."


class Richtig:
    """Der Aufruf liefert das Soll, beim Knacken mindestens zum geforderten Anteil."""

    def pruefe(self, lauf: CodesLauf) -> list[Befund]:
        wert = lauf.aufruf.wert
        if wert is None:
            return [Befund(None, lauf.aufruf.fehler or "kein Ergebnis")]
        if wert == lauf.soll or lauf.anteil >= lauf.noetig:
            return []
        if lauf.noetig < 1:
            return [Befund(None, f"{round(lauf.anteil * 100)} % der Buchstaben stimmen, nötig sind {round(lauf.noetig * 100)} %")]
        stelle = next((i for i, (a, b) in enumerate(zip(wert, lauf.soll)) if a != b), min(len(wert), len(lauf.soll)))
        return [Befund(None, f"ergibt \"{_kurz(wert)}\", ab Zeichen {stelle + 1} anders als erwartet")]


RICHTIG = Richtig()


def _pruefe_regel(regel: Richtig, lauf: CodesLauf) -> list[Befund]:
    return regel.pruefe(lauf)


# --- Antworten -----------------------------------------------------------------


class Kennzahlen(BaseModel):
    ms: float
    anteil: float
    zeichen: int


class Wiedergabe(BaseModel):
    """Eine Nachricht zum Ansehen (ein Bild, nichts abzuspielen)."""

    name: str
    sichtbar: bool
    dauer: int = 0
    bilder: list[tuple[int]] = [(0,)]
    aufruf: str
    eingabe: str
    soll: str
    ergebnis: str | None
    kennzahlen: Kennzahlen
    fehler: str | None = None


class AblaufStand(BaseModel):
    name: str
    sichtbar: bool
    ok: bool
    kennzahlen: Kennzahlen
    erste_stelle: float | None = None
    erster_befund: str | None = None


class CodesAuswertung(BaseModel):
    teilschritte: list[TeilschrittStand]
    ablaeufe: list[AblaufStand]
    wiedergaben: list[Wiedergabe]
    # alle Aufrufe zusammen
    ms: float


class CodesLaeufe(BaseModel):
    auswertung: CodesAuswertung | None
    stdout: str = ""
    stderr: str = ""
    laufzeit_ms: float = 0
    timeout: bool = False


def level_von(aufgabe: Aufgabe) -> CodesLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return CodesLevel.model_validate(extra.get("codes"))


def aufruf_text(level: CodesLevel, n: Nachricht) -> str:
    """Der Aufruf, wie er im Programm stünde, mit dem Geheimtext als Platzhalter."""
    erstes = "klar" if n.richtung == "verschluesseln" else "geheim"
    return f"{level.funktion_von(n)}({', '.join([erstes, *map(repr, n.mit)])})"


def laufe(code: str, level: CodesLevel, nachrichten: list[Nachricht], runner: Runner, sekunden: int) -> CodesLaeufe:
    """Ruft die Funktionen des Programms mit jeder Nachricht auf (zuerst die sichtbaren) und urteilt."""
    marke = neue_marke()
    aufrufe = [(level.funktion_von(n), level.eingabe(n)) for n in nachrichten]
    bereit = {name: BEREIT[name] for name in level.bereit}
    erg = runner.run_code(skript(code, bereit, aufrufe, marke), "python", RunLimits(timeout_sekunden=sekunden))
    stdout, block = lies_block(erg, marke)
    try:
        gemeldet = Gemeldet.model_validate(block) if isinstance(block, dict) else None
    except ValidationError:
        gemeldet = None
    if gemeldet is None or (gemeldet.fehler is None and len(gemeldet.aufrufe) != len(nachrichten)):
        return CodesLaeufe(auswertung=None, stdout=stdout, stderr=hinweise(erg), laufzeit_ms=erg.laufzeit_ms,
                           timeout=erg.timeout)
    zeichen = zeichen_code(code)
    sichtbar = {n.name for n in level.sichtbar}
    laeufe = []
    for i, n in enumerate(nachrichten):
        aufruf = gemeldet.aufrufe[i] if not gemeldet.fehler else Aufruf(fehler=gemeldet.fehler)
        laeufe.append(CodesLauf(name=n.name, sichtbar=n.name in sichtbar, nachricht=n, soll=level.soll(n),
                                noetig=level.noetig(n), aufruf=aufruf))
    staende, wiedergaben = [], []
    versteckt_gezeigt = False
    for cl in laeufe:
        befunde = ablauf_befunde([RICHTIG], cl, _pruefe_regel)
        kennzahlen = Kennzahlen(ms=round(cl.aufruf.ms, 2), anteil=round(cl.anteil, 4), zeichen=zeichen)
        stand = AblaufStand(name=cl.name, sichtbar=cl.sichtbar, ok=not befunde, kennzahlen=kennzahlen,
                            erster_befund=befunde[0].als_text(None) if befunde else None)
        staende.append(stand)
        if cl.sichtbar or (not stand.ok and not versteckt_gezeigt):
            versteckt_gezeigt = versteckt_gezeigt or not cl.sichtbar
            wiedergaben.append(Wiedergabe(
                name=cl.name, sichtbar=cl.sichtbar, aufruf=aufruf_text(level, cl.nachricht),
                eingabe=str(level.eingabe(cl.nachricht)[0]), soll=cl.soll, ergebnis=cl.aufruf.wert,
                kennzahlen=kennzahlen, fehler=cl.aufruf.fehler,
            ))
    teilschritte = auswerten(level.schritte(), laeufe, _pruefe_regel, level.mengen())
    ms = round(sum(cl.aufruf.ms for cl in laeufe), 2)
    return CodesLaeufe(
        auswertung=CodesAuswertung(teilschritte=teilschritte, ablaeufe=staende, wiedergaben=wiedergaben, ms=ms),
        stdout=stdout, stderr=hinweise(erg), laufzeit_ms=erg.laufzeit_ms, timeout=erg.timeout,
    )


def lauf_sichtbar(aufgabe: Aufgabe, code: str, runner: Runner) -> CodesLaeufe:
    """Probelauf: nur die sichtbaren Nachrichten, ohne Wertung."""
    level = level_von(aufgabe)
    return laufe(code, level, level.sichtbar, runner, aufgabe.zeitlimit_sekunden)


def kriterien(level: CodesLevel, geschafft: bool, ms: float | None, zeichen: int) -> list[SternKriterium]:
    s = level.sterne
    flott = geschafft and ms is not None and ms <= s.ms
    return [
        SternKriterium(text="alle Nachrichten richtig, auch die versteckten", erreicht=geschafft),
        SternKriterium(text=f"alle zusammen in höchstens {s.ms} ms", erreicht=flott),
        SternKriterium(text=f"dazu höchstens {s.zeichen} Zeichen Code", erreicht=flott and zeichen <= s.zeichen),
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
        return [f"codes: {e['loc']} {e['msg']}" for e in fehler.errors()]
    meldungen = []
    namen = [n.name for n in level.nachrichten()]
    for n in level.nachrichten():
        meldungen += [f"Nachricht {n.name}: {m}" for m in codes.schluessel_fehler(level.verfahren, n.klar, n.schluessel)]
        if not FUNKTIONSNAME.match(level.funktion_von(n)):
            meldungen.append(f"Nachricht {n.name}: Funktion {level.funktion_von(n)} ist kein Name")
    if level.mengen()[-1] != set(namen):
        meldungen.append("der letzte Teilschritt prüft alle Nachrichten (nachrichten: alle)")
    for t in level.teilschritte:
        if isinstance(t.nachrichten, list):
            meldungen += [f"Teilschritt {t.titel}: Nachricht {x} gibt es nicht" for x in t.nachrichten if x not in namen]
    return meldungen


@registriere(
    "codes",
    verbirgt=("codes.versteckt",),
    zaehle_versteckt=_anzahl_versteckt,
    pruefe_aufbau=_pruefe_aufbau,
)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    level = level_von(aufgabe)
    ergebnis = laufe(code, level, level.nachrichten(), runner, aufgabe.zeitlimit_sekunden)
    a = ergebnis.auswertung
    zeichen = zeichen_code(code)
    if a is None:
        fehler = "Zeit abgelaufen: das Programm endete nicht." if ergebnis.timeout else ergebnis.stderr
        return PruefErgebnis(
            bestanden=False,
            sichtbar=[TestErgebnis(index=0, bestanden=False, eingabe=[level.sichtbar[0].name], fehler=fehler)],
            versteckt_pass=0,
            versteckt_fail=len(level.versteckt),
            laufzeit_ms=ergebnis.laufzeit_ms,
            stdout=ergebnis.stdout,
            stderr=ergebnis.stderr,
            timeout=ergebnis.timeout,
            wertung=Wertung(sterne=0, kriterien=kriterien(level, False, None, zeichen)),
        )
    erstes = a.ablaeufe[0]
    versteckt = a.ablaeufe[len(level.sichtbar):]
    geschafft = all(t.erfuellt for t in a.teilschritte)
    k = kriterien(level, geschafft, a.ms, zeichen)
    return PruefErgebnis(
        bestanden=geschafft,
        sichtbar=[TestErgebnis(index=0, bestanden=erstes.ok, eingabe=[erstes.name], erwartet="alle Nachrichten richtig",
                               tatsaechlich=a.model_dump(), fehler=erstes.erster_befund)],
        versteckt_pass=sum(1 for x in versteckt if x.ok),
        versteckt_fail=sum(1 for x in versteckt if not x.ok),
        laufzeit_ms=a.ms,
        stdout=ergebnis.stdout,
        stderr=ergebnis.stderr,
        timeout=ergebnis.timeout,
        wertung=Wertung(sterne=sum(1 for x in k if x.erreicht), kriterien=k, kennwerte=Kennwerte()),
    )
