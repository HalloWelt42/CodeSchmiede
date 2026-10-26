"""Prüfer für `task_type: ampel` (Steuerungsspiel Ampelschule).

Das Python-Programm hat eine Funktion takt(lage), die jede Sekunde die Sensoren bekommt und das Signal je Gruppe
zurückgibt. In der Sandbox läuft es einmal je Ablauf (sichtbar und versteckt), jeweils mit frischem Zustand
(steuerung/sandbox_lauf.py); die Welt dort ist dieselbe Quelle wie im Backend (steuerung/ampel_welt.py) und liefert
nur die Sensoren. Aus der Sandbox
kommt je Ablauf die Folge der Signale; Verkehr, Unfälle und Wartezeiten rechnet das Backend nach, die Regeln der
Teilschritte urteilen darauf.

Sterne: einer, wenn alle Teilschritte in allen Abläufen erfüllt sind; zwei, wenn dazu im sichtbaren Ablauf die
Fußgänger höchstens so lange und die Fahrzeuge im Mittel höchstens so lange warten; drei, wenn dazu der Code
höchstens so viele Zeichen hat (ohne Leerraum und Kommentare).

Im Frontmatter:
  ampel:
    anlage: {vorlage: ueberweg}                  oder {vorlage: kreuzung, zufahrten: ..., ueberwege: ...}
    sensoren: [taster, frei]                     was die Aufgabe unter "Sensoren" zeigt
    aufbauend_auf: v001-...                      dessen bestandenes Programm ist der Anfang (sonst starter_code)
    sichtbar: [{name, dauer, verkehr: [...]}]    sichtbare Abläufe, der erste gilt ab dem ersten Teilschritt
    versteckt: [{...}, ...]                      weitere Abläufe, gehen nie an den Browser
    teilschritte: [{titel, text, regeln: [...], ablaeufe: [name, ...] | alle}, ...]
    sterne: {fuss: 25, autos: 6, zeichen: 320}
"""

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from ..steuerung import ampel_ablauf, ampel_anlage, ampel_regeln, ampel_welt, sandbox_lauf
from ..steuerung.ampel_ablauf import Ablauf
from ..steuerung.ampel_anlage import Anlage, AnlageVorgabe
from ..steuerung.ampel_regeln import AmpelLauf, Regel
from ..steuerung.sandbox_lauf import Gemeldet
from ..steuerung.teilschritte import Befund, TeilschrittStand, ablauf_befunde, ablauf_mengen, auswerten
from .ergebnis import Kennwerte, PruefErgebnis, SternKriterium, TestErgebnis, Wertung
from .registry import registriere
from .roboter_pruefer import zeichen_code, zeilen_code

Sensor = Literal["taster", "schleife", "wartend", "frei", "einsatz", "nacht", "stoerung"]

WELT_QUELLE = Path(ampel_welt.__file__).read_text(encoding="utf-8")

class AmpelTeilschritt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    titel: str
    text: str
    regeln: list[Regel] = Field(default_factory=list)
    # weitere Abläufe beim Namen oder "alle"
    ablaeufe: Literal["alle"] | list[str] | None = None


class AmpelSterne(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # längste Wartezeit eines Fußgängers und mittlere Wartezeit der Fahrzeuge im sichtbaren Ablauf
    fuss: float | None = Field(default=None, ge=0)
    autos: float | None = Field(default=None, ge=0)
    zeichen: int = Field(ge=1)


class AmpelLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    anlage: AnlageVorgabe
    sensoren: list[Sensor] = Field(default_factory=list)
    aufbauend_auf: str | None = None
    sichtbar: list[Ablauf] = Field(min_length=1)
    versteckt: list[Ablauf] = Field(default_factory=list)
    teilschritte: list[AmpelTeilschritt] = Field(min_length=1)
    sterne: AmpelSterne

    def ablaeufe(self) -> list[Ablauf]:
        return [*self.sichtbar, *self.versteckt]

    def mengen(self) -> list[set[str]]:
        return ablauf_mengen(self.teilschritte, [a.name for a in self.ablaeufe()], self.sichtbar[0].name)

    def regeln(self) -> list[Regel]:
        return [r for t in self.teilschritte for r in t.regeln]


# --- Antworten -----------------------------------------------------------------


class Kennzahlen(BaseModel):
    unfaelle: int
    verstoesse: int
    # längste Wartezeit eines Fußgängers, mittlere der Fahrzeuge (Sekunden)
    fuss_max: float
    autos_mittel: float


class TeilnehmerBild(BaseModel):
    id: int
    art: str
    weg: str


class Wiedergabe(BaseModel):
    """Ein Ablauf zum Abspielen: Signale je Sekunde, Lage der Teilnehmer je Takt ([zeit, [[id, strecke], ...]])."""

    name: str
    sichtbar: bool
    dauer: int
    signale: list[dict[str, str]]
    teilnehmer: list[TeilnehmerBild]
    bilder: list[tuple[float, list[tuple[int, float]]]]
    unfaelle: list[dict]
    nacht: list[tuple[int, int]]
    # je Sekunde die Gruppen, bei denen jemand auf Grün wartete
    bedarf: list[list[str]]
    kennzahlen: Kennzahlen
    fehler: str | None = None


class AblaufStand(BaseModel):
    name: str
    sichtbar: bool
    ok: bool
    kennzahlen: Kennzahlen
    # erste Stelle mit Unfall oder Verstoß (Sekunden), zum Hinspringen
    erste_stelle: float | None = None
    erster_befund: str | None = None


class AmpelAuswertung(BaseModel):
    teilschritte: list[TeilschrittStand]
    ablaeufe: list[AblaufStand]
    # die sichtbaren Abläufe und, falls einer misslingt, der erste misslungene versteckte
    wiedergaben: list[Wiedergabe]


class AmpelLaeufe(BaseModel):
    auswertung: AmpelAuswertung | None
    stdout: str
    stderr: str
    laufzeit_ms: float
    timeout: bool


# --- Ablauf --------------------------------------------------------------------


def level_von(aufgabe: Aufgabe) -> AmpelLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return AmpelLevel.model_validate(extra.get("ampel"))


def anlage_von(level: AmpelLevel) -> Anlage:
    return ampel_anlage.baue(level.anlage)


def _kennzahlen(lauf: AmpelLauf, befunde: list[Befund]) -> Kennzahlen:
    fuss = [t["warten"] for t in lauf.teilnehmer if t["art"] == "fuss"]
    fahrzeuge = [t["warten"] for t in lauf.teilnehmer if t["art"] != "fuss"]
    return Kennzahlen(
        unfaelle=len(lauf.unfaelle),
        verstoesse=sum(1 for b in befunde if not b.text.startswith("Unfall")),
        fuss_max=round(max(fuss, default=0.0), 1),
        autos_mittel=round(sum(fahrzeuge) / len(fahrzeuge), 1) if fahrzeuge else 0.0,
    )


def _nachspielen(anlage: Anlage, ablauf: dict, gemeldet: Gemeldet, sichtbar: bool) -> tuple[AmpelLauf, ampel_welt.Welt]:
    welt = sandbox_lauf.nachspielen(ampel_welt.Welt(anlage.fuer_welt(), ablauf, aufzeichnen=True), gemeldet.befehle)
    lauf = AmpelLauf(
        name=ablauf["name"],
        sichtbar=sichtbar,
        dauer=ablauf["dauer"],
        arten={g: d["art"] for g, d in welt.gruppen.items()},
        feindlich=welt.feindlich,
        signale=welt.signalfolge,
        verlauf=welt.verlauf,
        teilnehmer=welt.bilanz(),
        unfaelle=welt.unfaelle,
        fehler=gemeldet.fehler,
    )
    return lauf, welt


def _wiedergabe(lauf: AmpelLauf, welt: ampel_welt.Welt, kennzahlen: Kennzahlen, ablauf: dict) -> Wiedergabe:
    return Wiedergabe(
        name=lauf.name,
        sichtbar=lauf.sichtbar,
        dauer=lauf.dauer,
        signale=lauf.signale,
        teilnehmer=[TeilnehmerBild(id=t.id, art=t.art, weg=t.weg.id) for t in welt.alle],
        bilder=welt.bilder,
        unfaelle=lauf.unfaelle,
        nacht=[tuple(n) for n in ablauf["nacht"]],
        bedarf=[[g for g, b in v["bedarf"].items() if b] for v in lauf.verlauf],
        kennzahlen=kennzahlen,
        fehler=lauf.fehler,
    )


def laufe(code: str, level: AmpelLevel, ablaeufe: list[Ablauf], runner: Runner, sekunden: int) -> AmpelLaeufe:
    """Lässt das Programm in den Abläufen laufen (zuerst die sichtbaren), spielt jeden nach und wertet aus."""
    anlage = anlage_von(level)
    breit = [ampel_ablauf.ausbreiten(a, anlage) for a in ablaeufe]
    lauf = sandbox_lauf.laufe(WELT_QUELLE, code, anlage.fuer_welt(), breit, runner, sekunden)
    auswertung = _auswerten(level, anlage, breit, lauf.gemeldet) if lauf.gemeldet is not None else None
    return AmpelLaeufe(auswertung=auswertung, stdout=lauf.stdout, stderr=lauf.stderr, laufzeit_ms=lauf.laufzeit_ms,
                       timeout=lauf.timeout)


def _auswerten(level: AmpelLevel, anlage: Anlage, breit: list[dict], gemeldet: list[Gemeldet]) -> AmpelAuswertung:
    regeln = level.regeln()
    sichtbar = len(level.sichtbar)
    gespielt = [_nachspielen(anlage, a, g, sichtbar=i < sichtbar) for i, (a, g) in enumerate(zip(breit, gemeldet))]
    staende, wiedergaben = [], []
    versteckt_gezeigt = False
    for (lauf, welt), ablauf in zip(gespielt, breit):
        befunde = ablauf_befunde(regeln, lauf, ampel_regeln.pruefe)
        kennzahlen = _kennzahlen(lauf, befunde)
        erste = next((b for b in befunde if b.sekunde is not None), None)
        stand = AblaufStand(
            name=lauf.name, sichtbar=lauf.sichtbar, ok=not befunde, kennzahlen=kennzahlen,
            erste_stelle=erste.sekunde if erste else None,
            erster_befund=befunde[0].als_text(None) if befunde else None,
        )
        staende.append(stand)
        if lauf.sichtbar or (not stand.ok and not versteckt_gezeigt):
            versteckt_gezeigt = versteckt_gezeigt or not lauf.sichtbar
            wiedergaben.append(_wiedergabe(lauf, welt, kennzahlen, ablauf))
    teilschritte = auswerten(level.teilschritte, [lauf for lauf, _ in gespielt], ampel_regeln.pruefe, level.mengen())
    return AmpelAuswertung(teilschritte=teilschritte, ablaeufe=staende, wiedergaben=wiedergaben)


def lauf_sichtbar(aufgabe: Aufgabe, code: str, runner: Runner) -> AmpelLaeufe:
    """Probelauf: nur die sichtbaren Abläufe, ohne Wertung."""
    level = level_von(aufgabe)
    return laufe(code, level, level.sichtbar, runner, aufgabe.zeitlimit_sekunden)


def kriterien(level: AmpelLevel, geschafft: bool, kennzahlen: Kennzahlen | None, zeichen: int) -> list[SternKriterium]:
    s = level.sterne
    teile = []
    if s.fuss is not None:
        teile.append(f"Fußgänger warten höchstens {s.fuss:g} s")
    if s.autos is not None:
        teile.append(f"Fahrzeuge im Mittel höchstens {s.autos:g} s")
    zuegig = geschafft and kennzahlen is not None
    if zuegig and s.fuss is not None:
        zuegig = kennzahlen.fuss_max <= s.fuss
    if zuegig and s.autos is not None:
        zuegig = kennzahlen.autos_mittel <= s.autos
    return [
        SternKriterium(text="alle Teilschritte erfüllt, kein Unfall, kein Verstoß, in allen Abläufen", erreicht=geschafft),
        SternKriterium(text=", ".join(teile) + " (sichtbarer Ablauf)" if teile else "zügig im sichtbaren Ablauf",
                       erreicht=zuegig),
        SternKriterium(text=f"dazu höchstens {s.zeichen} Zeichen Code", erreicht=zuegig and zeichen <= s.zeichen),
    ]


# --- Bestand -------------------------------------------------------------------


def _anzahl_versteckt(aufgabe: Aufgabe) -> int:
    try:
        return len(level_von(aufgabe).versteckt)
    except ValidationError:
        return 0  # meldet die Bestandsprüfung


def _pruefe_aufbau(aufgabe: Aufgabe) -> list[str]:
    try:
        level = level_von(aufgabe)
    except ValidationError as fehler:
        return [f"ampel: {e['loc']} {e['msg']}" for e in fehler.errors()]
    meldungen = [] if aufgabe.sprache == "python" else ["Ampelschule läuft mit Python: sprache python"]
    meldungen += ampel_anlage.befunde(level.anlage)
    if meldungen:
        return meldungen
    anlage = anlage_von(level)
    gruppen = {g.name for g in anlage.gruppen}
    for ablauf in level.ablaeufe():
        meldungen += ampel_ablauf.befunde(ablauf, anlage)
    if level.mengen()[-1] != {a.name for a in level.ablaeufe()}:
        meldungen.append("der letzte Teilschritt prüft alle Abläufe (ablaeufe: alle)")
    namen = [a.name for a in level.ablaeufe()]
    if len(set(namen)) != len(namen):
        meldungen.append("Abläufe brauchen verschiedene Namen")
    for schritt in level.teilschritte:
        if isinstance(schritt.ablaeufe, list):
            meldungen += [f"Teilschritt {schritt.titel}: Ablauf {n} gibt es nicht" for n in schritt.ablaeufe if n not in namen]
    for regel in level.regeln():
        meldungen += [f"Regel {regel.art}: unbekannte Gruppe {g}" for g in ampel_regeln.gruppen_der_regel(regel)
                      if g not in gruppen]
    return meldungen


@registriere(
    "ampel",
    verbirgt=("ampel.versteckt",),
    zaehle_versteckt=_anzahl_versteckt,
    pruefe_aufbau=_pruefe_aufbau,
)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    level = level_von(aufgabe)
    ergebnis = laufe(code, level, level.ablaeufe(), runner, aufgabe.zeitlimit_sekunden)
    zeichen = zeichen_code(code)
    a = ergebnis.auswertung
    if a is None:
        return PruefErgebnis(
            bestanden=False,
            sichtbar=[TestErgebnis(index=0, bestanden=False, eingabe=[level.sichtbar[0].name],
                                   fehler="Programm lief nicht bis zum Ende")],
            versteckt_pass=0,
            versteckt_fail=len(level.versteckt),
            laufzeit_ms=ergebnis.laufzeit_ms,
            stdout=ergebnis.stdout,
            stderr=ergebnis.stderr,
            timeout=ergebnis.timeout,
            wertung=Wertung(sterne=0, kriterien=kriterien(level, False, None, zeichen)),
        )
    sichtbar = a.ablaeufe[0]
    versteckt = a.ablaeufe[len(level.sichtbar):]
    geschafft = all(t.erfuellt for t in a.teilschritte)
    k = kriterien(level, geschafft, sichtbar.kennzahlen, zeichen)
    return PruefErgebnis(
        bestanden=geschafft,
        sichtbar=[TestErgebnis(
            index=0,
            bestanden=sichtbar.ok,
            eingabe=[sichtbar.name],
            erwartet="kein Unfall, kein Verstoß",
            tatsaechlich=a.model_dump(),
            fehler=sichtbar.erster_befund,
        )],
        versteckt_pass=sum(1 for x in versteckt if x.ok),
        versteckt_fail=sum(1 for x in versteckt if not x.ok),
        laufzeit_ms=ergebnis.laufzeit_ms,
        stdout=ergebnis.stdout,
        stderr=ergebnis.stderr,
        timeout=ergebnis.timeout,
        wertung=Wertung(
            sterne=sum(1 for x in k if x.erreicht),
            kriterien=k,
            kennwerte=Kennwerte(zeilen=zeilen_code(code)),
        ),
    )
