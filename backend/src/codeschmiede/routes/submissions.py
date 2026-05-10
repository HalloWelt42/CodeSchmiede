"""HTTP-Routen für Submissions und Probelauf -- Code abschicken,
ausführen, bewerten oder probieren.
"""

import json
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..models.progress import Progress
from ..pruefung.ergebnis import PruefErgebnis
from ..pruefung.orchestrator import pruefe
from ..sandbox.result import RunLimits
from ..state import AppState


PROBELAUF_MARKER = "===CODESCHMIEDE_PROBELAUF===\n"


class SubmissionAnfrage(BaseModel):
    aufgabe_id: str
    code: str = Field(min_length=1, max_length=50_000)


class SubmissionAntwort(BaseModel):
    bestanden: bool
    pruefung: PruefErgebnis
    codelaenge_zeichen: int
    submission_id: int
    progress: Progress


class ProbelaufAnfrage(BaseModel):
    aufgabe_id: str
    code: str = Field(min_length=1, max_length=50_000)
    input: list[Any] = Field(default_factory=list)


class ProbelaufAntwort(BaseModel):
    rückgabe: Any = None
    stdout: str = ""
    stderr: str = ""
    laufzeit_ms: float
    timeout: bool = False
    fehler: str | None = None


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
            aufgabe, ergebnis.bestanden
        )

        return SubmissionAntwort(
            bestanden=ergebnis.bestanden,
            pruefung=ergebnis,
            codelaenge_zeichen=codelaenge,
            submission_id=submission_id,
            progress=progress,
        )

    @router.post("/probelauf", response_model=ProbelaufAntwort)
    def probelauf(anfrage: ProbelaufAnfrage) -> ProbelaufAntwort:
        """Fuehrt die Funktion mit benutzerdefiniertem Input aus, ohne
        Bewertung. Liefert Rückgabe + stdout zurück.
        """
        aufgabe = state.aufgaben.aufgabe(anfrage.aufgabe_id)
        if not aufgabe:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        if not aufgabe.funktion:
            raise HTTPException(
                status_code=400, detail="Aufgabe definiert keine Funktion"
            )

        skript = _baue_probelauf_skript(
            anfrage.code, aufgabe.funktion, anfrage.input
        )
        limits = RunLimits(timeout_sekunden=aufgabe.zeitlimit_sekunden)
        run = state.runner.run_code(skript, limits=limits)

        if PROBELAUF_MARKER not in run.stdout:
            return ProbelaufAntwort(
                rückgabe=None,
                stdout=run.stdout,
                stderr=run.stderr,
                laufzeit_ms=run.laufzeit_ms,
                timeout=run.timeout,
                fehler="Code wurde nicht vollständig ausgeführt",
            )

        nutzer_stdout, _, json_teil = run.stdout.partition(PROBELAUF_MARKER)
        try:
            ergebnis = json.loads(json_teil.strip())
        except json.JSONDecodeError:
            return ProbelaufAntwort(
                rückgabe=None,
                stdout=nutzer_stdout,
                stderr=run.stderr or "Ergebnis konnte nicht geparst werden",
                laufzeit_ms=run.laufzeit_ms,
                timeout=run.timeout,
                fehler="Ergebnis nicht parsebar",
            )

        return ProbelaufAntwort(
            rückgabe=ergebnis.get("rückgabe"),
            stdout=nutzer_stdout,
            stderr=run.stderr,
            laufzeit_ms=run.laufzeit_ms,
            timeout=run.timeout,
            fehler=ergebnis.get("fehler"),
        )

    return router


def _baue_probelauf_skript(code: str, funktion: str, eingabe: list[Any]) -> str:
    eingabe_json = json.dumps(eingabe)
    return (
        f"{code}\n\n"
        "# === codeschmiede probelauf (auto generated) ===\n"
        "import json as _json\n"
        "import sys as _sys\n"
        f"_eingabe = _json.loads({eingabe_json!r})\n"
        "try:\n"
        f"    _rueckgabe = {funktion}(*_eingabe)\n"
        "    _ergebnis = {'rückgabe': _rueckgabe, 'fehler': None}\n"
        "except Exception as _e:\n"
        "    _ergebnis = {'rückgabe': None,\n"
        "                 'fehler': type(_e).__name__ + ': ' + str(_e)}\n"
        f"_sys.stdout.write({PROBELAUF_MARKER!r})\n"
        "_sys.stdout.write(_json.dumps(_ergebnis, default=str))\n"
        "_sys.stdout.flush()\n"
    )
