"""Pruefer für `task_type: sql_abfrage`.

Frontmatter-Erwartungen:
  dataset: <name>            # zeigt auf aufgaben/sql/datasets/<name>.sql
  erwartete_spalten: [...]   # optional, Reihenfolge der Spalten
  erwartetes_ergebnis: [[...], [...], ...]   # Liste von Zeilen
  sortierung_egal: bool      # default false

Die Abfrage läuft in der Sandbox (Python-Image mit SQLite im Speicher),
nie im Backend: Zeit, Speicher und Ausgabe sind dort begrenzt, ATTACH
und DETACH sind verboten.

Das erwartete Ergebnis ist der sichtbare Test (die Zieltabelle gehört
zur Aufgabe). Gegen fest eingetippte Werte gibt es die Gegenprobe als
versteckte Tests: Abfrage und Musterlösung laufen zusätzlich auf
ausgedünnten Fassungen des Datensatzes (jede n-te Zeile jeder Tabelle
entfernt) und müssen dort dasselbe liefern.
"""

import json
import re
from pathlib import Path
from typing import Any

from ..aufgaben.loader import AufgabenLoader
from ..models.aufgabe import Aufgabe
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis, TestErgebnis
from .registry import registriere
from .testlauf import hinweise, lies_block, neue_marke

DATASET_NAME = re.compile(r"^[a-z0-9_]+$")
MAX_ZEILEN = 10_000
# Jede n-te Zeile entfernen: zwei verschiedene Gegenproben.
AUSDUENNUNGEN = (2, 3)


def _datasets_dir(aufgabe: Aufgabe) -> Path:
    # aufgabe.dateipfad: .../aufgaben/sql/<id>/aufgabe.md
    return aufgabe.dateipfad.parent.parent / "datasets"


def _skript(schema_sql: str, laeufe: list[dict[str, Any]], marke: str) -> str:
    return (
        "import json, sqlite3, sys\n"
        f"SCHEMA = json.loads({json.dumps(schema_sql)!r})\n"
        f"LAEUFE = json.loads({json.dumps(laeufe)!r})\n"
        f"MAX_ZEILEN = {MAX_ZEILEN}\n"
        "VERBOTEN = (sqlite3.SQLITE_ATTACH, sqlite3.SQLITE_DETACH)\n"
        "def lauf(sql, n):\n"
        "    conn = sqlite3.connect(':memory:')\n"
        "    conn.executescript(SCHEMA)\n"
        "    if n:\n"
        "        for (t,) in conn.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'\").fetchall():\n"
        "            conn.execute(f'DELETE FROM \"{t}\" WHERE rowid % {n} = 0')\n"
        "    conn.set_authorizer(lambda aktion, *_: sqlite3.SQLITE_DENY if aktion in VERBOTEN else sqlite3.SQLITE_OK)\n"
        "    try:\n"
        "        cur = conn.execute(sql)\n"
        "        zeilen = cur.fetchmany(MAX_ZEILEN + 1)\n"
        "    except (sqlite3.Error, sqlite3.Warning) as e:\n"
        "        return {'fehler': 'SQL-Fehler: ' + str(e)}\n"
        "    if len(zeilen) > MAX_ZEILEN:\n"
        "        return {'fehler': f'Mehr als {MAX_ZEILEN} Zeilen'}\n"
        "    return {'spalten': [d[0] for d in (cur.description or [])], 'zeilen': [list(z) for z in zeilen]}\n"
        "ergebnisse = [lauf(l['sql'], l['ausduennen']) for l in LAEUFE]\n"
        f"sys.stdout.write({marke!r} + json.dumps(ergebnisse, default=repr) + '\\n')\n"
    )


def _zeilen(rows: list[Any]) -> list[tuple[Any, ...]]:
    return [tuple(r) if isinstance(r, (list, tuple)) else (r,) for r in rows]


def _vergleichbar(zeilen: list[tuple[Any, ...]], sortierung_egal: bool) -> list[tuple[Any, ...]]:
    if sortierung_egal:
        return sorted(zeilen, key=lambda r: tuple(str(x) for x in r))
    return zeilen


def _fehler(text: str, laufzeit_ms: float = 0) -> PruefErgebnis:
    return PruefErgebnis(
        bestanden=False, sichtbar=[], versteckt_pass=0, versteckt_fail=0,
        laufzeit_ms=laufzeit_ms, stderr=text,
    )


def anzahl_versteckt(aufgabe: Aufgabe) -> int:
    """Gegenproben zählen als versteckte Tests, sofern es eine Musterlösung gibt."""
    hat_loesung = bool(AufgabenLoader.musterloesungen_neben(aufgabe.dateipfad.parent))
    return len(AUSDUENNUNGEN) if hat_loesung else 0


@registriere("sql_abfrage", zaehle_versteckt=anzahl_versteckt)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    dataset = str(extra.get("dataset") or "")
    sortierung_egal = bool(extra.get("sortierung_egal", False))
    erwartete_spalten = extra.get("erwartete_spalten")
    soll = _zeilen(extra.get("erwartetes_ergebnis", []))

    if not DATASET_NAME.match(dataset):
        return _fehler(f"Aufgabe ohne gültiges `dataset`-Feld ({dataset!r})")
    dataset_pfad = _datasets_dir(aufgabe) / f"{dataset}.sql"
    if not dataset_pfad.exists():
        return _fehler(f"Datensatz '{dataset}' nicht gefunden")

    loesungen = AufgabenLoader.musterloesungen_neben(aufgabe.dateipfad.parent)
    referenz = loesungen[0]["code"] if loesungen else None
    laeufe: list[dict[str, Any]] = [{"sql": code, "ausduennen": None}]
    if referenz:
        for n in AUSDUENNUNGEN:
            laeufe.append({"sql": code, "ausduennen": n})
            laeufe.append({"sql": referenz, "ausduennen": n})

    marke = neue_marke()
    erg = runner.run_code(
        _skript(dataset_pfad.read_text(encoding="utf-8"), laeufe, marke),
        "python",
        RunLimits(timeout_sekunden=aufgabe.zeitlimit_sekunden),
    )
    _, block = lies_block(erg, marke)
    if not isinstance(block, list) or len(block) != len(laeufe):
        if erg.timeout:
            return _fehler("Zeitgrenze überschritten", erg.laufzeit_ms)
        return _fehler(hinweise(erg) or "Abfrage wurde nicht vollständig ausgeführt", erg.laufzeit_ms)

    haupt = block[0]
    if "fehler" in haupt:
        return _fehler(haupt["fehler"], erg.laufzeit_ms)

    ist = _zeilen(haupt["zeilen"])
    spalten = haupt["spalten"]
    spalten_ok = not erwartete_spalten or spalten == list(erwartete_spalten)
    bestanden_sichtbar = spalten_ok and _vergleichbar(ist, sortierung_egal) == _vergleichbar(soll, sortierung_egal)

    versteckt_pass = 0
    versteckt_fail = 0
    for nutzer, muster in zip(block[1::2], block[2::2]):
        gleich = (
            "fehler" not in nutzer
            and "fehler" not in muster
            and _vergleichbar(_zeilen(nutzer["zeilen"]), sortierung_egal)
            == _vergleichbar(_zeilen(muster["zeilen"]), sortierung_egal)
        )
        if gleich:
            versteckt_pass += 1
        else:
            versteckt_fail += 1

    return PruefErgebnis(
        bestanden=bestanden_sichtbar and versteckt_fail == 0,
        sichtbar=[
            TestErgebnis(
                index=0,
                bestanden=bestanden_sichtbar,
                eingabe=[dataset],
                erwartet={"spalten": erwartete_spalten, "zeilen": [list(r) for r in soll]},
                tatsaechlich={"spalten": spalten, "zeilen": [list(r) for r in ist]},
                fehler=None if bestanden_sichtbar else "Ergebnis weicht ab.",
            )
        ],
        versteckt_pass=versteckt_pass,
        versteckt_fail=versteckt_fail,
        laufzeit_ms=erg.laufzeit_ms,
    )
