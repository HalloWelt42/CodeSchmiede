"""Route fuer SQL-Dataset-Vorschau.

Liefert pro Dataset alle Tabellen mit Spalten + ersten N Zeilen. Der
Frontend zeigt das als frei bewegliches Schema-Panel ueber dem Editor.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..state import AppState


class TabellenVorschau(BaseModel):
    name: str
    spalten: list[str]
    zeilen: list[list[Any]]
    gesamt_zeilen: int


class DatasetVorschau(BaseModel):
    name: str
    tabellen: list[TabellenVorschau]


def baue_sql_dataset_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/sql", tags=["sql"])

    def _datasets_dir() -> Path:
        return state.settings.aufgaben_pfad / "sql" / "datasets"

    @router.get("/datasets/{name}/vorschau", response_model=DatasetVorschau)
    def vorschau(name: str, limit: int = 5) -> DatasetVorschau:
        datei = _datasets_dir() / f"{name}.sql"
        if not datei.exists():
            raise HTTPException(status_code=404, detail=f"Dataset '{name}' nicht gefunden")
        schema_sql = datei.read_text(encoding="utf-8")
        conn = sqlite3.connect(":memory:")
        try:
            conn.executescript(schema_sql)
            namen = [
                row[0] for row in conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY rowid"
                ).fetchall()
            ]
            tabellen: list[TabellenVorschau] = []
            for tab in namen:
                cur = conn.execute(f"SELECT * FROM {tab} LIMIT ?", (limit,))
                spalten = [d[0] for d in (cur.description or [])]
                zeilen = [list(r) for r in cur.fetchall()]
                gesamt = conn.execute(f"SELECT COUNT(*) FROM {tab}").fetchone()[0]
                tabellen.append(TabellenVorschau(
                    name=tab, spalten=spalten, zeilen=zeilen, gesamt_zeilen=gesamt,
                ))
        finally:
            conn.close()
        return DatasetVorschau(name=name, tabellen=tabellen)

    return router
