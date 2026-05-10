"""HTTP-Routen fuer Submissions -- Code abschicken, ausfuehren, bewerten."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..models.progress import Progress
from ..pruefung.ergebnis import PruefErgebnis
from ..pruefung.orchestrator import pruefe
from ..state import AppState


class SubmissionAnfrage(BaseModel):
    aufgabe_id: str
    code: str = Field(min_length=1, max_length=50_000)


class SubmissionAntwort(BaseModel):
    bestanden: bool
    pruefung: PruefErgebnis
    codelaenge_zeichen: int
    submission_id: int
    progress: Progress


def baue_submissions_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/submissions", tags=["submissions"])

    @router.post("", response_model=SubmissionAntwort)
    def submit(anfrage: SubmissionAnfrage) -> SubmissionAntwort:
        aufgabe = state.aufgaben.aufgabe(anfrage.aufgabe_id)
        if not aufgabe:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")

        ergebnis = pruefe(aufgabe, anfrage.code, state.runner)
        codelaenge = sum(1 for c in anfrage.code if not c.isspace())

        with state.db.connect() as conn:
            cursor = conn.execute(
                """
                INSERT INTO submissions (
                    aufgabe_id, aufgabe_revision, code, bestanden,
                    laufzeit_ms, codelaenge_zeichen
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    aufgabe.id,
                    aufgabe.revision,
                    anfrage.code,
                    1 if ergebnis.bestanden else 0,
                    ergebnis.laufzeit_ms,
                    codelaenge,
                ),
            )
            submission_id = cursor.lastrowid or 0

        progress = state.progress.aktualisiere_nach_submission(
            aufgabe.id, ergebnis.bestanden
        )

        return SubmissionAntwort(
            bestanden=ergebnis.bestanden,
            pruefung=ergebnis,
            codelaenge_zeichen=codelaenge,
            submission_id=submission_id,
            progress=progress,
        )

    return router
