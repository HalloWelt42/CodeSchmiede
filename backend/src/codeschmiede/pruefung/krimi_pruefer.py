"""Pruefer für `task_type: sql_krimi` (Spiel SQL-Krimi).

Ein Fall ist ein Pfad, jedes Kapitel eine Aufgabe mit einer Frage. Die
Antwort steckt in einem Abfrageergebnis: das Ergebnis gilt, wenn es eine
Spalte gibt, in der jeder Wert die gesuchte Antwort ist (mindestens eine
Zeile). Wer zu breit fragt, bekommt mehrere Werte und ist noch nicht am
Ziel.

Die Abfrage läuft in der Sandbox auf der Tatort-Datenbank und auf einer
anders befüllten Gegenprobe, in der dieselbe Frage eine andere Antwort
hat. So zählt nur eine Abfrage, die die Frage wirklich beantwortet, nicht
der eingetippte Name.

Sterne: einer für die Antwort (auch in der Gegenprobe), zwei ohne Hinweis,
drei dazu in höchstens so vielen Prüfversuchen wie angegeben; die beiden
letzten entscheidet die Verbuchung aus dem Verlauf.

Im Frontmatter:
  krimi:
    dataset: krimi_pokal              aufgaben/sql/datasets/<name>.sql
    gegenprobe: krimi_pokal_gegen
    kapitel: 4
    frage: Welcher Schlüsseldienst ...?
    antwort: Schlüssel Sommer          verborgen
    antwort_gegen: Rapid Schloss       verborgen
    notiz: Schlüssel Sommer, LK-447-B  verborgen, kommt nach dem Lösen auf die Pinnwand
    versuche: 1                        Prüfversuche für drei Sterne
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from ..models.aufgabe import Aufgabe
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis, SternKriterium, TestErgebnis, Wertung
from .registry import registriere
from .sql_pruefer import DATASET_NAME, datasets_dir, skript
from .testlauf import hinweise, lies_block, neue_marke


class KrimiLevel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    dataset: str = Field(pattern=DATASET_NAME.pattern)
    gegenprobe: str = Field(pattern=DATASET_NAME.pattern)
    kapitel: int = Field(ge=1)
    frage: str = Field(min_length=1)
    antwort: str = Field(min_length=1)
    antwort_gegen: str = Field(min_length=1)
    notiz: str = Field(min_length=1)
    versuche: int = Field(default=1, ge=1)


class Ergebnistabelle(BaseModel):
    spalten: list[str] = Field(default_factory=list)
    zeilen: list[list[Any]] = Field(default_factory=list)
    fehler: str | None = None


def level_von(aufgabe: Aufgabe) -> KrimiLevel:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    return KrimiLevel.model_validate(extra.get("krimi"))


def geheime_datensaetze(aufgaben: list[Aufgabe]) -> set[str]:
    """Gegenproben der Kapitel: die Vorschau zeigt sie nie."""
    namen = set()
    for a in aufgaben:
        if a.task_type == "sql_krimi":
            try:
                namen.add(level_von(a).gegenprobe)
            except ValidationError:
                continue  # meldet die Bestandsprüfung
    return namen


def _gleich(wert: Any, antwort: str) -> bool:
    return str(wert).strip().casefold() == antwort.strip().casefold()


def antwort_eindeutig(tabelle: Ergebnistabelle, antwort: str) -> bool:
    """Gibt es eine Spalte, in der jeder Wert die Antwort ist?"""
    if tabelle.fehler or not tabelle.zeilen:
        return False
    for i in range(len(tabelle.spalten)):
        werte = [z[i] for z in tabelle.zeilen if i < len(z) and z[i] is not None]
        if werte and all(_gleich(w, antwort) for w in werte):
            return True
    return False


def ausfuehren(aufgabe: Aufgabe, sql_texte: list[tuple[str, str]], runner: Runner) -> tuple[list[Ergebnistabelle] | None, str, float, bool]:
    """Führt je (Datensatz, Abfrage) die Abfrage in der Sandbox aus."""
    verzeichnis = datasets_dir(aufgabe)
    ergebnisse: list[Ergebnistabelle] = []
    stderr, laufzeit, timeout = "", 0.0, False
    for dataset, sql in sql_texte:
        datei = verzeichnis / f"{dataset}.sql"
        if not datei.exists():
            return None, f"Datensatz '{dataset}' nicht gefunden", laufzeit, False
        marke = neue_marke()
        erg = runner.run_code(
            skript(datei.read_text(encoding="utf-8"), [{"sql": sql, "ausduennen": None}], marke),
            "python",
            RunLimits(timeout_sekunden=aufgabe.zeitlimit_sekunden),
        )
        laufzeit += erg.laufzeit_ms
        timeout = timeout or erg.timeout
        _, block = lies_block(erg, marke)
        if not isinstance(block, list) or len(block) != 1:
            return None, ("Zeitgrenze überschritten" if erg.timeout else hinweise(erg) or "Abfrage lief nicht bis zum Ende"), laufzeit, timeout
        ergebnisse.append(Ergebnistabelle.model_validate(block[0]))
        stderr = hinweise(erg)
    return ergebnisse, stderr, laufzeit, timeout


def kriterien(level: KrimiLevel, gefunden: bool) -> list[SternKriterium]:
    versuche = "im ersten Prüfversuch" if level.versuche == 1 else f"in höchstens {level.versuche} Prüfversuchen"
    return [
        SternKriterium(text="Antwort eindeutig gefunden, auch in der Gegenprobe", erreicht=gefunden),
        SternKriterium(text="ohne Hinweis", erreicht=False, art="ohne_hinweis"),
        SternKriterium(text=versuche, erreicht=False, art="versuche", grenze=level.versuche),
    ]


def _pruefe_aufbau(aufgabe: Aufgabe) -> list[str]:
    try:
        level = level_von(aufgabe)
    except ValidationError as fehler:
        return [f"krimi: {e['loc']} {e['msg']}" for e in fehler.errors()]
    fehlt = [d for d in (level.dataset, level.gegenprobe) if not (datasets_dir(aufgabe) / f"{d}.sql").exists()]
    return [f"Datensatz '{d}' fehlt" for d in fehlt]


@registriere(
    "sql_krimi",
    verbirgt=("krimi.antwort", "krimi.antwort_gegen", "krimi.notiz"),
    zaehle_versteckt=lambda aufgabe: 1,
    pruefe_aufbau=_pruefe_aufbau,
)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    level = level_von(aufgabe)
    tabellen, stderr, laufzeit, timeout = ausfuehren(aufgabe, [(level.dataset, code), (level.gegenprobe, code)], runner)
    if tabellen is None:
        return PruefErgebnis(
            bestanden=False, sichtbar=[], versteckt_pass=0, versteckt_fail=1, laufzeit_ms=laufzeit,
            stderr=stderr, timeout=timeout, wertung=Wertung(sterne=0, kriterien=kriterien(level, False)),
        )
    tatort, gegen = tabellen
    am_tatort = antwort_eindeutig(tatort, level.antwort)
    in_gegenprobe = antwort_eindeutig(gegen, level.antwort_gegen)
    gefunden = am_tatort and in_gegenprobe
    if tatort.fehler:
        hinweis = tatort.fehler
    elif not tatort.zeilen:
        hinweis = "Die Abfrage liefert keine Zeile."
    elif not am_tatort:
        hinweis = "Die Antwort steht nicht eindeutig im Ergebnis: grenze weiter ein, bis in einer Spalte nur noch ein Wert übrig ist."
    else:
        hinweis = None
    return PruefErgebnis(
        bestanden=gefunden,
        sichtbar=[TestErgebnis(
            index=0,
            bestanden=am_tatort,
            eingabe=["Tatort-Datenbank"],
            tatsaechlich=tatort.model_dump(exclude={"fehler"}),
            fehler=hinweis,
        )],
        versteckt_pass=1 if in_gegenprobe else 0,
        versteckt_fail=0 if in_gegenprobe else 1,
        laufzeit_ms=laufzeit,
        stderr=stderr,
        timeout=timeout,
        wertung=Wertung(sterne=1 if gefunden else 0, kriterien=kriterien(level, gefunden)),
    )
