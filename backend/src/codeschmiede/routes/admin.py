"""HTTP-Routen für die Verwaltungs-Übersicht.

Bewusst entkoppelt vom übrigen API-Schnitt: nur Read-Only-Endpoints,
eigener Praefix `/api/admin`, eigene Pydantic-Modelle. Liefert die
**komplette** Sicht auf Aufgaben (inkl. versteckter Tests, Hints,
Musterlösungen-Anzahl, Statistik). Im Single-User-MVP gibt es kein
Auth -- das Endpoint ist genauso geschützt wie die App selbst.
"""

import json
from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from ..state import AppState


class AufgabenStatistik(BaseModel):
    submissions_gesamt: int = 0
    bestandene_submissions: int = 0
    versuche: int = 0
    hints_genutzt: int = 0
    punkte_erreicht: int = 0
    status: str = "neu"


class VerwaltungsEintrag(BaseModel):
    """Komplette Sicht auf eine Aufgabe für die Verwaltungsansicht.

    Bewusst breit -- die Tabelle zeigt alles, was über das Frontmatter
    einkommt, plus Statistik aus den Tabellen `submissions` + `progress`.
    """

    schema_version: int
    id: str
    revision: int
    titel: str
    sprache: str
    task_type: str
    runner_type: str
    schwierigkeit: str
    schwierigkeit_score: int
    schaetz_minuten: int
    tags: list[str]
    pfade: list[str]
    voraussetzungen: list[str]
    quelle: dict[str, Any]
    lizenz: str
    autor: str | None
    erstellt_am: str | None
    zeitlimit_sekunden: int
    funktion: str | None
    hints: list[dict[str, Any]]
    tests_sichtbar: list[dict[str, Any]]
    tests_versteckt: list[dict[str, Any]]
    starter_code: str
    beschreibung_md: str
    musterloesungen_anzahl: int
    dateipfad: str
    hash: str
    statistik: AufgabenStatistik


def baue_admin_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/admin", tags=["admin"])

    @router.get("/aufgaben", response_model=list[VerwaltungsEintrag])
    def aufgaben() -> list[VerwaltungsEintrag]:
        eintraege: list[VerwaltungsEintrag] = []

        # Statistik vorab in einem Query holen, dann pro Aufgabe zuordnen
        with state.db.connect() as conn:
            sub_rows = conn.execute(
                """
                SELECT aufgabe_id,
                       COUNT(*) AS gesamt,
                       SUM(CASE WHEN bestanden = 1 THEN 1 ELSE 0 END) AS bestanden
                FROM submissions
                GROUP BY aufgabe_id
                """
            ).fetchall()
            sub_stats = {
                r["aufgabe_id"]: (r["gesamt"], r["bestanden"] or 0) for r in sub_rows
            }

            progress_rows = conn.execute("SELECT * FROM progress").fetchall()
            progress_by_id = {r["aufgabe_id"]: r for r in progress_rows}

        for a in sorted(
            state.aufgaben.alle_aufgaben(),
            key=lambda x: (x.sprache, x.schwierigkeit_score, x.id),
        ):
            sub_gesamt, sub_bestanden = sub_stats.get(a.id, (0, 0))
            p = progress_by_id.get(a.id)
            statistik = AufgabenStatistik(
                submissions_gesamt=sub_gesamt,
                bestandene_submissions=sub_bestanden,
                versuche=p["versuche"] if p else 0,
                hints_genutzt=p["hints_genutzt"] if p else 0,
                punkte_erreicht=p["punkte_erreicht"] if p else 0,
                status=p["status"] if p else "neu",
            )
            ml = state.loader.lade_musterloesungen(a.id)
            eintraege.append(
                VerwaltungsEintrag(
                    schema_version=a.schema_version,
                    id=a.id,
                    revision=a.revision,
                    titel=a.titel,
                    sprache=a.sprache,
                    task_type=a.task_type,
                    runner_type=a.runner_type,
                    schwierigkeit=a.schwierigkeit,
                    schwierigkeit_score=a.schwierigkeit_score,
                    schaetz_minuten=a.schaetz_minuten,
                    tags=a.tags,
                    pfade=a.pfade,
                    voraussetzungen=a.voraussetzungen,
                    quelle=a.quelle.model_dump(),
                    lizenz=a.lizenz,
                    autor=a.autor,
                    erstellt_am=a.erstellt_am.isoformat() if a.erstellt_am else None,
                    zeitlimit_sekunden=a.zeitlimit_sekunden,
                    funktion=a.funktion,
                    hints=[h.model_dump() for h in a.hints],
                    tests_sichtbar=[t.model_dump() for t in a.tests_sichtbar],
                    tests_versteckt=[t.model_dump() for t in a.tests_versteckt],
                    starter_code=a.starter_code,
                    beschreibung_md=a.beschreibung_md,
                    musterloesungen_anzahl=len(ml),
                    dateipfad=str(a.dateipfad),
                    hash=a.hash,
                    statistik=statistik,
                )
            )
        return eintraege

    return router
