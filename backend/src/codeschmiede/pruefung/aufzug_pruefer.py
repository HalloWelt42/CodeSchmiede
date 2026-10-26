"""Prüfer für `task_type: aufzug` (Steuerungsspiel Aufzugsteuerung).

Das Python-Programm hat eine Funktion takt(lage). Jede Kabine fragt sie, sobald sie mit ihrem letzten Befehl fertig
ist, und bekommt "hoch", "runter", "auf", "zu" oder "warten" zurück. In der Sandbox läuft das Programm einmal je
Ablauf (steuerung/sandbox_lauf.py), heraus kommt die Folge der Befehle; Fahrt, Fahrgäste und Verstöße rechnet das
Backend mit derselben Welt nach (steuerung/aufzug_welt.py), die Regeln der Teilschritte urteilen darauf.

Sterne: einer, wenn alle Teilschritte in allen Abläufen erfüllt sind; zwei, wenn dazu im ersten sichtbaren Ablauf
die Fahrgäste im Mittel höchstens so lange warten; drei, wenn dazu der Code höchstens so viele Zeichen hat.

Im Frontmatter:
  aufzug:
    haus: {etagen: 6, aufzuege: [a], plaetze: 6}
    sensoren: [lichtschranke, voll]                was die Aufgabe unter "Sensoren" zeigt
    aufbauend_auf: e001-...
    sichtbar: [{name, dauer, fahrgaeste: [...], feuer}]
    versteckt: [...]                               gehen nie an den Browser
    teilschritte: [{titel, text, regeln: [...], ablaeufe: [name, ...] | alle}, ...]
    sterne: {warten: 15, zeichen: 400}
"""

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from ..steuerung import aufzug_ablauf, aufzug_regeln, aufzug_welt, sandbox_lauf
from ..steuerung.aufzug_ablauf import Ablauf, Haus
from ..steuerung.aufzug_regeln import AufzugLauf, Regel
from ..steuerung.sandbox_lauf import Gemeldet
from ..steuerung.teilschritte import Befund, TeilschrittStand, ablauf_befunde, ablauf_mengen, auswerten
from .ergebnis import Kennwerte, PruefErgebnis, SternKriterium, TestErgebnis, Wertung
from .registry import registriere
from .roboter_pruefer import zeichen_code, zeilen_code

Sensor = Literal["wartend", "lichtschranke", "voll", "ueberlast", "feuer", "aufzuege"]

WELT_QUELLE = Path(aufzug_welt.__file__).read_text(encoding="utf-8")


class AufzugTeilschritt(BaseModel):
    model_config = ConfigDict(extra="forbid")

    titel: str
    text: str
    regeln: list[Regel] = Field(default_factory=list)
    ablaeufe: Literal["alle"] | list[str] | None = None


class AufzugSterne(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # mittlere Wartezeit der Fahrgäste im ersten sichtbaren Ablauf
    warten: float = Field(ge=0)
    zeichen: int = Field(ge=1)


class AufzugLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    haus: Haus
    sensoren: list[Sensor] = Field(default_factory=list)
    aufbauend_auf: str | None = None
    sichtbar: list[Ablauf] = Field(min_length=1)
    versteckt: list[Ablauf] = Field(default_factory=list)
    teilschritte: list[AufzugTeilschritt] = Field(min_length=1)
    sterne: AufzugSterne

    def ablaeufe(self) -> list[Ablauf]:
        return [*self.sichtbar, *self.versteckt]

    def regeln(self) -> list[Regel]:
        return [r for t in self.teilschritte for r in t.regeln]

    def mengen(self) -> list[set[str]]:
        return ablauf_mengen(self.teilschritte, [a.name for a in self.ablaeufe()], self.sichtbar[0].name)


# --- Antworten -----------------------------------------------------------------


class Kennzahlen(BaseModel):
    verstoesse: int
    bedient: int
    fahrgaeste: int
    warten_mittel: float
    warten_max: float


class FahrgastBild(BaseModel):
    id: int
    von: int
    nach: int
    ankunft: float


class Wiedergabe(BaseModel):
    """Eine Fahrt zum Abspielen. Je Takt: [Zeit, [[Lage, Tür 0 bis 1, Fahrgäste] je Kabine],
    [[id, Etage, Richtung] je Wartendem], [[id, Kabine, +1 rein oder -1 raus, Anteil] je Läufer]]."""

    name: str
    sichtbar: bool
    dauer: int
    bilder: list[list]
    fahrgaeste: list[FahrgastBild]
    # Türen, Verstöße und Ankünfte mit Zeit, für Klänge und Marken im Fahrdiagramm
    ereignisse: list[dict]
    feuer: int | None
    kennzahlen: Kennzahlen
    fehler: str | None = None


class AblaufStand(BaseModel):
    name: str
    sichtbar: bool
    ok: bool
    kennzahlen: Kennzahlen
    erste_stelle: float | None = None
    erster_befund: str | None = None


class AufzugAuswertung(BaseModel):
    teilschritte: list[TeilschrittStand]
    ablaeufe: list[AblaufStand]
    wiedergaben: list[Wiedergabe]


class AufzugLaeufe(BaseModel):
    auswertung: AufzugAuswertung | None
    stdout: str
    stderr: str
    laufzeit_ms: float
    timeout: bool


# --- Ablauf --------------------------------------------------------------------


def level_von(aufgabe: Aufgabe) -> AufzugLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return AufzugLevel.model_validate(extra.get("aufzug"))


def _kennzahlen(lauf: AufzugLauf, befunde: list[Befund]) -> Kennzahlen:
    warten = [f["warten"] for f in lauf.fahrgaeste]
    return Kennzahlen(
        verstoesse=len(befunde),
        bedient=sum(1 for f in lauf.fahrgaeste if f["angekommen"] is not None),
        fahrgaeste=len(lauf.fahrgaeste),
        warten_mittel=round(sum(warten) / len(warten), 1) if warten else 0.0,
        warten_max=round(max(warten, default=0.0), 1),
    )


def _nachspielen(haus: Haus, ablauf: dict, gemeldet: Gemeldet, sichtbar: bool) -> tuple[AufzugLauf, aufzug_welt.Welt]:
    welt = sandbox_lauf.nachspielen(aufzug_welt.Welt(haus.fuer_welt(), ablauf, aufzeichnen=True), gemeldet.befehle)
    lauf = AufzugLauf(
        name=ablauf["name"],
        sichtbar=sichtbar,
        dauer=ablauf["dauer"],
        etagen=haus.etagen,
        ereignisse=welt.ereignisse,
        protokoll=welt.protokoll,
        fahrgaeste=welt.bilanz(),
        feuer_ab=ablauf["feuer"],
        fehler=gemeldet.fehler,
    )
    return lauf, welt


def _wiedergabe(lauf: AufzugLauf, welt: aufzug_welt.Welt, kennzahlen: Kennzahlen) -> Wiedergabe:
    return Wiedergabe(
        name=lauf.name,
        sichtbar=lauf.sichtbar,
        dauer=lauf.dauer,
        bilder=welt.bilder,
        fahrgaeste=[FahrgastBild(id=f.id, von=f.von, nach=f.nach, ankunft=f.ankunft) for f in welt.alle],
        ereignisse=[e for e in lauf.ereignisse if e["art"] in ("auf", "zu", "offen", "verstoss")],
        feuer=lauf.feuer_ab,
        kennzahlen=kennzahlen,
        fehler=lauf.fehler,
    )


def laufe(code: str, level: AufzugLevel, ablaeufe: list[Ablauf], runner: Runner, sekunden: int) -> AufzugLaeufe:
    """Lässt das Programm in den Abläufen laufen (zuerst die sichtbaren), spielt jeden nach und wertet aus."""
    breit = [aufzug_ablauf.ausbreiten(a, level.haus) for a in ablaeufe]
    lauf = sandbox_lauf.laufe(WELT_QUELLE, code, level.haus.fuer_welt(), breit, runner, sekunden)
    auswertung = _auswerten(level, breit, lauf.gemeldet) if lauf.gemeldet is not None else None
    return AufzugLaeufe(auswertung=auswertung, stdout=lauf.stdout, stderr=lauf.stderr, laufzeit_ms=lauf.laufzeit_ms,
                        timeout=lauf.timeout)


def _auswerten(level: AufzugLevel, breit: list[dict], gemeldet: list[Gemeldet]) -> AufzugAuswertung:
    regeln = level.regeln()
    sichtbar = len(level.sichtbar)
    gespielt = [_nachspielen(level.haus, a, g, sichtbar=i < sichtbar) for i, (a, g) in enumerate(zip(breit, gemeldet))]
    staende, wiedergaben = [], []
    versteckt_gezeigt = False
    for lauf, welt in gespielt:
        befunde = ablauf_befunde(regeln, lauf, aufzug_regeln.pruefe)
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
            wiedergaben.append(_wiedergabe(lauf, welt, kennzahlen))
    teilschritte = auswerten(level.teilschritte, [lauf for lauf, _ in gespielt], aufzug_regeln.pruefe, level.mengen())
    return AufzugAuswertung(teilschritte=teilschritte, ablaeufe=staende, wiedergaben=wiedergaben)


def lauf_sichtbar(aufgabe: Aufgabe, code: str, runner: Runner) -> AufzugLaeufe:
    """Probelauf: nur die sichtbaren Abläufe, ohne Wertung."""
    level = level_von(aufgabe)
    return laufe(code, level, level.sichtbar, runner, aufgabe.zeitlimit_sekunden)


def kriterien(level: AufzugLevel, geschafft: bool, kennzahlen: Kennzahlen | None, zeichen: int) -> list[SternKriterium]:
    s = level.sterne
    zuegig = geschafft and kennzahlen is not None and kennzahlen.warten_mittel <= s.warten
    return [
        SternKriterium(text="alle Teilschritte erfüllt, kein Verstoß, in allen Abläufen", erreicht=geschafft),
        SternKriterium(text=f"Fahrgäste warten im Mittel höchstens {s.warten:g} s (erster sichtbarer Ablauf)",
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
        return [f"aufzug: {e['loc']} {e['msg']}" for e in fehler.errors()]
    meldungen = [] if aufgabe.sprache == "python" else ["Aufzugsteuerung läuft mit Python: sprache python"]
    for ablauf in level.ablaeufe():
        meldungen += aufzug_ablauf.befunde(ablauf, level.haus)
    namen = [a.name for a in level.ablaeufe()]
    if len(set(namen)) != len(namen):
        meldungen.append("Abläufe brauchen verschiedene Namen")
    if level.mengen()[-1] != set(namen):
        meldungen.append("der letzte Teilschritt prüft alle Abläufe (ablaeufe: alle)")
    for schritt in level.teilschritte:
        if isinstance(schritt.ablaeufe, list):
            meldungen += [f"Teilschritt {schritt.titel}: Ablauf {n} gibt es nicht" for n in schritt.ablaeufe if n not in namen]
    return meldungen


@registriere(
    "aufzug",
    verbirgt=("aufzug.versteckt",),
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
            erwartet="alle bedient, kein Verstoß",
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
