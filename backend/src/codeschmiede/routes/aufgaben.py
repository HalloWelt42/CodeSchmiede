"""HTTP-Routen für Aufgaben."""

from fastapi import APIRouter, HTTPException

from ..models.aufgabe import Aufgabe, AufgabeDetail, AufgabeKurz
from ..models.progress import Progress
from ..state import AppState


# Frontmatter-Felder, die direkt in `Aufgabe` modelliert sind. Was hier
# nicht steht und im Frontmatter vorkommt, landet in `extra` und ist für
# die jeweilige task_type-View bestimmt (z.B. `quiz`).
KERNFELDER_FRONTMATTER = {
    "schema_version", "id", "revision", "titel", "sprache", "task_type",
    "runner_type", "schwierigkeit", "schwierigkeit_score", "schaetz_minuten",
    "tags", "pfade", "voraussetzungen", "quelle", "lizenz", "autor",
    "erstellt_am", "zeitlimit_sekunden", "funktion", "hints",
    "tests_sichtbar", "tests_versteckt", "starter_code",
    "beschreibung_md", "dateipfad", "hash",
}


def _voraussetzungen_offen(a: Aufgabe, geloeste_ids: set[str]) -> list[str]:
    """Liefert die Liste der nicht-gelösten Voraussetzungen."""
    return [v for v in a.voraussetzungen if v not in geloeste_ids]


def _extra_aus_frontmatter(a: Aufgabe) -> dict:
    """Sammelt zusätzliche Frontmatter-Felder (extra='allow') ein.

    Pydantic legt sie in `model_extra` ab. Damit die jeweilige
    Aufgabentyp-View darauf zugreifen kann.
    """
    return getattr(a, "model_extra", {}) or {}


def baue_aufgaben_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/aufgaben", tags=["aufgaben"])

    def hole_geloeste_ids() -> set[str]:
        return {
            p.aufgabe_id
            for p in state.progress.hole_alle_progress()
            if p.status == "geloest"
        }

    @router.get("", response_model=list[AufgabeKurz])
    def liste(
        sprache: str | None = None,
        pfad: str | None = None,
        schwierigkeit: str | None = None,
    ) -> list[AufgabeKurz]:
        geloest = hole_geloeste_ids()
        ergebnis: list[AufgabeKurz] = []
        for a in state.aufgaben.alle_aufgaben():
            if sprache and a.sprache != sprache:
                continue
            if pfad and pfad not in a.pfade:
                continue
            if schwierigkeit and a.schwierigkeit != schwierigkeit:
                continue
            offen = _voraussetzungen_offen(a, geloest)
            ergebnis.append(
                AufgabeKurz(
                    id=a.id,
                    titel=a.titel,
                    sprache=a.sprache,
                    schwierigkeit=a.schwierigkeit,
                    schwierigkeit_score=a.schwierigkeit_score,
                    schaetz_minuten=a.schaetz_minuten,
                    tags=a.tags,
                    pfade=a.pfade,
                    revision=a.revision,
                    voraussetzungen=a.voraussetzungen,
                    voraussetzungen_offen=offen,
                    gesperrt=len(offen) > 0,
                )
            )
        ergebnis.sort(key=lambda x: x.schwierigkeit_score)
        return ergebnis

    @router.get("/{aufgabe_id}", response_model=AufgabeDetail)
    def detail(aufgabe_id: str) -> AufgabeDetail:
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")

        offen = _voraussetzungen_offen(a, hole_geloeste_ids())

        return AufgabeDetail(
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
            voraussetzungen_offen=offen,
            gesperrt=len(offen) > 0,
            quelle=a.quelle,
            lizenz=a.lizenz,
            autor=a.autor,
            erstellt_am=a.erstellt_am,
            zeitlimit_sekunden=a.zeitlimit_sekunden,
            funktion=a.funktion,
            hints=a.hints,
            tests_sichtbar=a.tests_sichtbar,
            starter_code=a.starter_code,
            beschreibung_md=a.beschreibung_md,
            anzahl_versteckte_tests=len(a.tests_versteckt),
            extra=_extra_aus_frontmatter(a),
        )

    @router.get("/{aufgabe_id}/musterloesungen")
    def musterloesungen(aufgabe_id: str) -> list[dict[str, str]]:
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        return state.loader.lade_musterloesungen(aufgabe_id)

    @router.post("/{aufgabe_id}/hints/{hint_index}", response_model=Progress)
    def hint_geoeffnet(aufgabe_id: str, hint_index: int) -> Progress:
        """Markiert Hint Nr. `hint_index` (0-basiert) als gesehen.
        Idempotent: mehrfaches Aufrufen schadet nicht.
        """
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        if hint_index < 0 or hint_index >= len(a.hints):
            raise HTTPException(status_code=400, detail="Hint-Index ungültig")
        return state.progress.markiere_hint_gesehen(aufgabe_id, hint_index)

    @router.get("/{aufgabe_id}/submissions")
    def submissions_verlauf(aufgabe_id: str, limit: int = 20) -> list[dict]:
        """Letzte N Submissions zu einer Aufgabe -- für den Verlauf im
        Detail-View. Code wird mitgeliefert, damit Re-Open trivial ist.
        """
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        with state.db.connect() as conn:
            rows = conn.execute(
                """
                SELECT id, datetime(zeitstempel) AS zeitstempel,
                       bestanden, laufzeit_ms, codelaenge_zeichen, code
                FROM submissions
                WHERE aufgabe_id = ?
                ORDER BY id DESC
                LIMIT ?
                """,
                (aufgabe_id, max(1, min(100, limit))),
            ).fetchall()
        return [
            {
                "id": r["id"],
                "zeitstempel": r["zeitstempel"],
                "bestanden": bool(r["bestanden"]),
                "laufzeit_ms": r["laufzeit_ms"],
                "codelaenge_zeichen": r["codelaenge_zeichen"],
                "code": r["code"],
            }
            for r in rows
        ]

    @router.get("/{aufgabe_id}/letzte-submission")
    def letzte_submission(aufgabe_id: str) -> dict:
        """Letzte abgeschickte Lösung (egal ob bestanden) -- damit der
        Editor beim erneuten Öffnen den letzten Stand zeigt statt der
        Starter-Boilerplate.
        """
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        with state.db.connect() as conn:
            row = conn.execute(
                """
                SELECT code, bestanden, zeitstempel
                FROM submissions
                WHERE aufgabe_id = ?
                ORDER BY id DESC
                LIMIT 1
                """,
                (aufgabe_id,),
            ).fetchone()
        if not row:
            return {"code": None, "bestanden": None, "zeitstempel": None}
        return {
            "code": row["code"],
            "bestanden": bool(row["bestanden"]),
            "zeitstempel": row["zeitstempel"],
        }

    return router
