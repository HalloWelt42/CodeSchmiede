"""Prüfer für `task_type: kv` (KV-Werkstatt).

Abgegeben wird je Ausgang eine Formel aus Blöcken (steuerung/kv.py), gezeichnet im KV-Diagramm oder als Text. Der
Server rechnet sie für alle Belegungen nach, ohne Sandbox. Die vier Teilschritte sind in jedem Level dieselben und
bauen aufeinander auf: alle Einsen abgedeckt, keine Null erwischt, jeder Block so groß wie möglich, keiner zu viel.

Sterne: einer, wenn alle vier Teilschritte stimmen; zwei, wenn dazu nicht mehr Blöcke nötig sind als in der kleinsten
Lösung; drei, wenn dazu auch nicht mehr Buchstaben. Die kleinste Lösung rechnet der Server aus der Funktion selbst
aus (bei höchstens vier Eingängen durch Probieren), im Level steht dafür nichts.

Im Frontmatter:
  kv:
    eingaenge: [A, B, C, D]          2 bis 4, der erste ist die höchste Stelle
    ausgaenge: [e]
    werte: {e: "1010001010xxxxxx"}   je Ausgang je Belegung 0, 1 oder x (egal), binär gezählt
    namen: ["0", "1", ...]           wie eine Belegung heißt (etwa die Ziffer), sonst ihre Bits
"""

import time
from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from ..steuerung import kv
from ..steuerung.teilschritte import Befund, TeilschrittStand, ablauf_befunde, auswerten
from .ergebnis import PruefErgebnis, SternKriterium, TestErgebnis, Wertung
from .registry import registriere

TABELLE = "Tabelle"


class KvLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    eingaenge: list[str] = Field(min_length=2, max_length=4)
    ausgaenge: list[str] = Field(min_length=1, max_length=7)
    werte: dict[str, str]
    namen: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _stimmig(self) -> "KvLevel":
        zeilen = 2 ** len(self.eingaenge)
        if set(self.werte) != set(self.ausgaenge):
            raise ValueError("werte braucht genau eine Folge je Ausgang")
        for name, folge in self.werte.items():
            if len(folge) != zeilen or set(folge) - set("01x"):
                raise ValueError(f"werte {name}: {zeilen} Zeichen aus 0, 1 und x")
        if self.namen and len(self.namen) != zeilen:
            raise ValueError(f"namen: genau {zeilen} Namen, einer je Belegung")
        return self

    @property
    def n(self) -> int:
        return len(self.eingaenge)

    def name(self, belegung: int) -> str:
        bits = "".join(str((belegung >> (self.n - 1 - i)) & 1) for i in range(self.n))
        return f"{self.namen[belegung]} ({bits})" if self.namen else bits

    def kleinste(self) -> tuple[int, int]:
        """Blöcke und Buchstaben der kleinsten Lösung über alle Ausgänge."""
        teile = [kv.kleinste_abdeckung(self.werte[a], self.n) for a in self.ausgaenge]
        return sum(b for b, _ in teile), sum(z for _, z in teile)


@dataclass
class KvLauf:
    name: str
    sichtbar: bool
    level: KvLevel
    formel: kv.Formel
    fehler: str | None = None

    def bloecke(self) -> list[tuple[str, kv.Block]]:
        return [(a, b) for a in self.level.ausgaenge for b in self.formel.bloecke.get(a, [])]

    def bezeichnung(self, ausgang: str, block: kv.Block) -> str:
        vorne = f"{ausgang}: " if len(self.level.ausgaenge) > 1 else ""
        return f"{vorne}Block {block.text(self.level.eingaenge)}"


class Abgedeckt:
    """Jede 1 liegt in mindestens einem Block."""

    def pruefe(self, lauf: KvLauf) -> list[Befund]:
        befunde = []
        for a in lauf.level.ausgaenge:
            bloecke = lauf.formel.bloecke.get(a, [])
            offen = [x for x, w in enumerate(lauf.level.werte[a]) if w == "1" and not kv.wert(bloecke, x, lauf.level.n)]
            if offen:
                vorne = f"{a}: " if len(lauf.level.ausgaenge) > 1 else ""
                mehr = f" (und {len(offen) - 1} weitere)" if len(offen) > 1 else ""
                befunde.append(Befund(None, f"{vorne}die 1 bei {lauf.level.name(offen[0])} liegt in keinem Block{mehr}"))
        return befunde


class KeineNull:
    """Kein Block erwischt eine 0."""

    def pruefe(self, lauf: KvLauf) -> list[Befund]:
        befunde = []
        for a, b in lauf.bloecke():
            nullen = sorted(x for x in b.felder(lauf.level.n) if lauf.level.werte[a][x] == "0")
            if nullen:
                befunde.append(Befund(None, f"{lauf.bezeichnung(a, b)} erwischt die 0 bei {lauf.level.name(nullen[0])}"))
        return befunde


class SoGrossWieMoeglich:
    """Jeder Block ist ein Primblock: kein Buchstabe kann wegfallen."""

    def pruefe(self, lauf: KvLauf) -> list[Befund]:
        befunde = []
        for a, b in lauf.bloecke():
            i = kv.vergroesserbar(b, lauf.level.werte[a], lauf.level.n)
            if i is not None:
                befunde.append(Befund(None, f"{lauf.bezeichnung(a, b)} lässt sich verdoppeln: ohne "
                                            f"{lauf.level.eingaenge[i]} erwischt er noch keine 0"))
        return befunde


class KeinerZuViel:
    """Kein Block, den man weglassen kann: jeder hat eine 1, die nur er abdeckt."""

    def pruefe(self, lauf: KvLauf) -> list[Befund]:
        befunde = []
        n = lauf.level.n
        for a in lauf.level.ausgaenge:
            bloecke = lauf.formel.bloecke.get(a, [])
            einsen = {x for x, w in enumerate(lauf.level.werte[a]) if w == "1"}
            for i, b in enumerate(bloecke):
                andere = set().union(*(c.felder(n) for j, c in enumerate(bloecke) if j != i))
                if not (b.felder(n) & einsen) - andere:
                    befunde.append(Befund(None, f"{lauf.bezeichnung(a, b)} lässt sich weglassen: "
                                                "alle seine Einsen liegen auch in anderen Blöcken"))
        return befunde


REGELN = [Abgedeckt(), KeineNull(), SoGrossWieMoeglich(), KeinerZuViel()]
TEILSCHRITTE = [
    ("Alle Einsen abgedeckt", "Jede 1 liegt in mindestens einem Block."),
    ("Keine Null erwischt", "Kein Block enthält eine 0; ein x darf drin sein."),
    ("So groß wie möglich", "Jeder Block hat 1, 2, 4, 8 oder 16 Felder und geht nicht größer, auch nicht über den Rand."),
    ("Keiner zu viel", "Kein Block lässt sich weglassen."),
]


@dataclass
class _Schritt:
    titel: str
    text: str
    regeln: list
    ablaeufe: None


def _schritte() -> list[_Schritt]:
    return [_Schritt(titel, text, [regel], None) for (titel, text), regel in zip(TEILSCHRITTE, REGELN)]


def _pruefe_regel(regel, lauf: KvLauf) -> list[Befund]:
    return regel.pruefe(lauf)


# --- Antworten -----------------------------------------------------------------


class Kennzahlen(BaseModel):
    bloecke: int
    buchstaben: int
    richtig: int
    zeilen: int
    bausteine: int
    tiefe: int


class Wiedergabe(BaseModel):
    """Die Tabelle: je Belegung [Nummer, Wert je Ausgang]; dazu die Formel als Schaltplan."""

    name: str
    sichtbar: bool
    dauer: int
    bilder: list[tuple[int, dict[str, int]]]
    plan: str
    kennzahlen: Kennzahlen
    fehler: str | None = None


class AblaufStand(BaseModel):
    name: str
    sichtbar: bool
    ok: bool
    kennzahlen: Kennzahlen
    erste_stelle: float | None = None
    erster_befund: str | None = None


class KvAuswertung(BaseModel):
    teilschritte: list[TeilschrittStand]
    ablaeufe: list[AblaufStand]
    wiedergaben: list[Wiedergabe]


class KvLaeufe(BaseModel):
    auswertung: KvAuswertung | None
    stdout: str = ""
    stderr: str = ""
    laufzeit_ms: float = 0
    timeout: bool = False


def level_von(aufgabe: Aufgabe) -> KvLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return KvLevel.model_validate(extra.get("kv"))


def laufe(code: str, level: KvLevel) -> KvLaeufe:
    beginn = time.perf_counter()
    formel = kv.lies(code, level.eingaenge, level.ausgaenge)
    if formel.fehler:
        return KvLaeufe(auswertung=None, stderr="\n".join(formel.fehler[:6]))
    lauf = KvLauf(TABELLE, True, level, formel)
    n = level.n
    bilder = [(x, {a: kv.wert(formel.bloecke[a], x, n) for a in level.ausgaenge}) for x in range(2 ** n)]
    richtig = sum(1 for x, ist in bilder if all(level.werte[a][x] in ("x", str(ist[a])) for a in level.ausgaenge))
    plan, bausteine, tiefe = kv.schaltplan(formel, level.eingaenge, level.ausgaenge)
    alle = lauf.bloecke()
    kennzahlen = Kennzahlen(bloecke=len(alle), buchstaben=sum(b.buchstaben() for _, b in alle), richtig=richtig,
                            zeilen=2 ** n, bausteine=bausteine, tiefe=tiefe)
    befunde = ablauf_befunde(REGELN, lauf, _pruefe_regel)
    stand = AblaufStand(name=TABELLE, sichtbar=True, ok=not befunde, kennzahlen=kennzahlen,
                        erster_befund=befunde[0].als_text(None) if befunde else None)
    teilschritte = auswerten(_schritte(), [lauf], _pruefe_regel, [{TABELLE}] * len(TEILSCHRITTE))
    return KvLaeufe(
        auswertung=KvAuswertung(teilschritte=teilschritte, ablaeufe=[stand], wiedergaben=[
            Wiedergabe(name=TABELLE, sichtbar=True, dauer=2 ** n, bilder=bilder, plan=plan, kennzahlen=kennzahlen)]),
        laufzeit_ms=(time.perf_counter() - beginn) * 1000,
    )


def lauf_sichtbar(aufgabe: Aufgabe, code: str) -> KvLaeufe:
    return laufe(code, level_von(aufgabe))


def kriterien(level: KvLevel, geschafft: bool, kennzahlen: Kennzahlen | None) -> list[SternKriterium]:
    bloecke, buchstaben = level.kleinste()
    knapp = geschafft and kennzahlen is not None and kennzahlen.bloecke <= bloecke
    return [
        SternKriterium(text="alle Einsen abgedeckt, keine Null, jeder Block so groß wie möglich, keiner zu viel",
                       erreicht=geschafft),
        SternKriterium(text=f"höchstens {bloecke} {'Block' if bloecke == 1 else 'Blöcke'}", erreicht=knapp),
        SternKriterium(text=f"dazu höchstens {buchstaben} Buchstaben", erreicht=knapp and kennzahlen.buchstaben <= buchstaben),
    ]


def _pruefe_aufbau(aufgabe: Aufgabe) -> list[str]:
    try:
        level = level_von(aufgabe)
    except ValidationError as fehler:
        return [f"kv: {e['loc']} {e['msg']}" for e in fehler.errors()]
    meldungen = []
    if len(set(level.eingaenge) | set(level.ausgaenge)) != len(level.eingaenge) + len(level.ausgaenge):
        meldungen.append("Eingänge und Ausgänge brauchen verschiedene Namen")
    meldungen += [f"Eingang {e} ist kein einzelner Buchstabe" for e in level.eingaenge if not (len(e) == 1 and e.isalpha())]
    meldungen += [f"Ausgang {a} hat keine 1" for a in level.ausgaenge if "1" not in level.werte[a]]
    return meldungen


@registriere(
    "kv",
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
        sichtbar=[TestErgebnis(index=0, bestanden=stand.ok, eingabe=[TABELLE], erwartet="alle vier Teilschritte",
                               tatsaechlich=a.model_dump(), fehler=stand.erster_befund)],
        versteckt_pass=0, versteckt_fail=0, laufzeit_ms=ergebnis.laufzeit_ms,
        wertung=Wertung(sterne=sum(1 for x in k if x.erreicht), kriterien=k),
    )
