"""Pruefer fuer `task_type: sql_abfrage`.

Frontmatter-Erwartungen:
  dataset: <name>            # zeigt auf aufgaben/sql/datasets/<name>.sql
  erwartete_spalten: [...]   # optional, Reihenfolge der Spalten
  erwartetes_ergebnis: [[...], [...], ...]   # Liste von Zeilen (jede Zeile = Liste)
  sortierung_egal: bool      # default false -- sonst werden beide Listen sortiert verglichen

Ablauf pro Submission:
  1. Lade dataset-SQL in eine frische In-Memory-SQLite.
  2. Fuehre den Nutzer-SQL aus, lies cursor.fetchall().
  3. Vergleiche mit erwartetes_ergebnis.

Sicherheit:
  * In-Memory-DB pro Submission, keine Dateien.
  * Read-Only durch Konvention -- der Nutzer-SQL kann zwar INSERT/DROP
    schreiben, aber die DB lebt nur fuer diese Submission.
"""
from __future__ import annotations

import sqlite3
import time
from pathlib import Path
from typing import Any

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis, TestErgebnis
from .registry import registriere


# Datensaetze liegen relativ zur aufgaben-Wurzel. Wir suchen sie ueber
# den Pfad der Aufgabe selbst -- aufgabe.dateipfad zeigt auf die .md.
def _datasets_dir(aufgabe: Aufgabe) -> Path:
    # aufgabe.dateipfad: .../aufgaben/sql/<id>/aufgabe.md
    return aufgabe.dateipfad.parent.parent / "datasets"


def _zeilen_normalisiert(rows: list[Any]) -> list[tuple[Any, ...]]:
    """Macht Listen, Tupel oder rohe Werte vergleichbar."""
    out: list[tuple[Any, ...]] = []
    for r in rows:
        if isinstance(r, (list, tuple)):
            out.append(tuple(r))
        else:
            out.append((r,))
    return out


@registriere("sql_abfrage")
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    dataset = extra.get("dataset")
    erwartet_raw = extra.get("erwartetes_ergebnis", [])
    sortierung_egal = bool(extra.get("sortierung_egal", False))
    erwartete_spalten = extra.get("erwartete_spalten")

    if not dataset:
        return PruefErgebnis(
            bestanden=False, sichtbar=[], versteckt_pass=0, versteckt_fail=0,
            laufzeit_ms=0, stderr="Aufgabe ohne `dataset`-Feld",
        )

    dataset_pfad = _datasets_dir(aufgabe) / f"{dataset}.sql"
    if not dataset_pfad.exists():
        return PruefErgebnis(
            bestanden=False, sichtbar=[], versteckt_pass=0, versteckt_fail=0,
            laufzeit_ms=0, stderr=f"Datensatz '{dataset}' nicht gefunden",
        )

    schema_sql = dataset_pfad.read_text(encoding="utf-8")
    start = time.perf_counter()
    conn = sqlite3.connect(":memory:")
    try:
        conn.executescript(schema_sql)
        cursor = conn.execute(code)
        zeilen = cursor.fetchall()
        spalten = [d[0] for d in (cursor.description or [])]
    except sqlite3.Error as e:
        return PruefErgebnis(
            bestanden=False, sichtbar=[], versteckt_pass=0, versteckt_fail=0,
            laufzeit_ms=(time.perf_counter() - start) * 1000,
            stderr=f"SQL-Fehler: {e}",
        )
    finally:
        conn.close()
    laufzeit_ms = (time.perf_counter() - start) * 1000

    ist = _zeilen_normalisiert(zeilen)
    soll = _zeilen_normalisiert(erwartet_raw)

    if sortierung_egal:
        ist_v = sorted(ist, key=lambda r: tuple(str(x) for x in r))
        soll_v = sorted(soll, key=lambda r: tuple(str(x) for x in r))
    else:
        ist_v, soll_v = ist, soll

    spalten_ok = True
    if erwartete_spalten and spalten != list(erwartete_spalten):
        spalten_ok = False

    bestanden = ist_v == soll_v and spalten_ok
    sichtbar = [
        TestErgebnis(
            index=0,
            bestanden=bestanden,
            eingabe=[dataset],
            erwartet={"spalten": erwartete_spalten, "zeilen": list(soll)},
            tatsaechlich={"spalten": spalten, "zeilen": [list(r) for r in ist]},
            fehler=None if bestanden else "Ergebnis weicht ab.",
        )
    ]
    return PruefErgebnis(
        bestanden=bestanden,
        sichtbar=sichtbar,
        versteckt_pass=0,
        versteckt_fail=0,
        laufzeit_ms=laufzeit_ms,
    )
