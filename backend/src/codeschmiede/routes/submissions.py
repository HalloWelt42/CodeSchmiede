"""HTTP-Routen für Submissions und Probelauf -- Code abschicken,
ausführen, bewerten oder probieren.

Bei einem bestandenen Submit liefern wir einen Performance-Vergleich
mit den Musterlösungen mit. Die werden einmal pro Aufgabe durch die
Sandbox geschickt und im AufgabenRepository gecacht; ein Reindex über
den Watcher leert den Cache.

Geprüft wird auf dem Server. Nur Aufgabentypen, deren Pruefer
`im_browser` ist (CSS-Nachbauten), schicken ein fertiges Ergebnis über
`/lokal`; alle anderen nehmen nur diesen Weg.
"""

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..models.aufgabe import Aufgabe
from ..models.progress import Progress
from ..progress.submissions import codelaenge
from ..pruefung.ergebnis import PruefErgebnis
from ..pruefung.kodierung import anzeigen
from ..pruefung.orchestrator import UnbekannterAufgabentyp, pruefe, pruefer_fuer
from ..pruefung.testlauf import fuehre_aus
from ..sandbox.result import RunLimits
from ..sandbox.runner import SandboxFehler
from ..state import AppState


class SubmissionAnfrage(BaseModel):
    aufgabe_id: str
    code: str = Field(min_length=1, max_length=50_000)


class VergleichEintrag(BaseModel):
    variante: str
    laufzeit_ms: float
    codelaenge_zeichen: int


class SubmissionAntwort(BaseModel):
    bestanden: bool
    pruefung: PruefErgebnis
    codelaenge_zeichen: int
    submission_id: int
    progress: Progress
    vergleich: list[VergleichEintrag] = Field(default_factory=list)


class LokaleSubmissionAnfrage(BaseModel):
    """Submission eines Aufgabentyps, der im Browser geprüft wird."""

    aufgabe_id: str
    code: str = Field(min_length=1, max_length=50_000)
    pruefung: PruefErgebnis


class ProbelaufAnfrage(BaseModel):
    aufgabe_id: str
    code: str = Field(min_length=1, max_length=50_000)
    input: list[Any] = Field(default_factory=list)


class ProbelaufAntwort(BaseModel):
    rueckgabe: Any = None
    stdout: str = ""
    stderr: str = ""
    laufzeit_ms: float
    timeout: bool = False
    fehler: str | None = None


def baue_submissions_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/submissions", tags=["submissions"])

    def hole_aufgabe(aufgabe_id: str) -> Aufgabe:
        aufgabe = state.aufgaben.aufgabe(aufgabe_id)
        if not aufgabe:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        return aufgabe

    def pruefe_sicher(aufgabe: Aufgabe, code: str) -> PruefErgebnis:
        try:
            return pruefe(aufgabe, code, state.runner)
        except SandboxFehler as fehler:
            raise HTTPException(status_code=503, detail=str(fehler)) from fehler
        except ValueError as fehler:
            raise HTTPException(status_code=422, detail=f"Aufgabe fehlerhaft: {fehler}") from fehler

    def vergleich(aufgabe: Aufgabe) -> list[VergleichEintrag]:
        """Lazy-cached: einmal pro Aufgabe die Musterlösungen durch die Sandbox."""
        if aufgabe.task_type != "code_schreiben":
            return []
        cached = state.aufgaben.metriken_cache(aufgabe.id)
        if cached is None:
            cached = [
                {
                    "variante": ml["variante"],
                    "laufzeit_ms": pruefe_sicher(aufgabe, ml["code"]).laufzeit_ms,
                    "codelaenge_zeichen": codelaenge(ml["code"]),
                }
                for ml in state.loader.lade_musterloesungen(aufgabe.id)
            ]
            state.aufgaben.setze_metriken_cache(aufgabe.id, cached)
        return [VergleichEintrag(**m) for m in cached]

    def speichere(aufgabe: Aufgabe, code: str, ergebnis: PruefErgebnis) -> tuple[int, Progress]:
        submission_id = state.submissions.speichere(
            aufgabe, code, ergebnis.bestanden, ergebnis.laufzeit_ms
        )
        progress = state.progress.aktualisiere_nach_submission(aufgabe, ergebnis.bestanden)
        return submission_id, progress

    @router.post("", response_model=SubmissionAntwort)
    def submit(anfrage: SubmissionAnfrage) -> SubmissionAntwort:
        aufgabe = hole_aufgabe(anfrage.aufgabe_id)
        try:
            im_browser = pruefer_fuer(aufgabe).im_browser
        except UnbekannterAufgabentyp as fehler:
            raise HTTPException(status_code=422, detail=str(fehler)) from fehler
        if im_browser:
            raise HTTPException(status_code=400, detail="Diese Aufgabe wird im Browser geprüft")

        ergebnis = pruefe_sicher(aufgabe, anfrage.code)
        submission_id, progress = speichere(aufgabe, anfrage.code, ergebnis)
        return SubmissionAntwort(
            bestanden=ergebnis.bestanden,
            pruefung=ergebnis,
            codelaenge_zeichen=codelaenge(anfrage.code),
            submission_id=submission_id,
            progress=progress,
            vergleich=vergleich(aufgabe) if ergebnis.bestanden else [],
        )

    @router.post("/lokal", response_model=SubmissionAntwort)
    def submit_lokal(anfrage: LokaleSubmissionAnfrage) -> SubmissionAntwort:
        """Speichert das Ergebnis einer im Browser geprüften Aufgabe."""
        aufgabe = hole_aufgabe(anfrage.aufgabe_id)
        try:
            im_browser = pruefer_fuer(aufgabe).im_browser
        except UnbekannterAufgabentyp as fehler:
            raise HTTPException(status_code=422, detail=str(fehler)) from fehler
        if not im_browser:
            raise HTTPException(status_code=400, detail="Diese Aufgabe wird auf dem Server geprüft")

        submission_id, progress = speichere(aufgabe, anfrage.code, anfrage.pruefung)
        return SubmissionAntwort(
            bestanden=anfrage.pruefung.bestanden,
            pruefung=anfrage.pruefung,
            codelaenge_zeichen=codelaenge(anfrage.code),
            submission_id=submission_id,
            progress=progress,
        )

    @router.post("/probelauf", response_model=ProbelaufAntwort)
    def probelauf(anfrage: ProbelaufAnfrage) -> ProbelaufAntwort:
        """Führt die Funktion mit eigener Eingabe aus, ohne Bewertung."""
        aufgabe = hole_aufgabe(anfrage.aufgabe_id)
        if not aufgabe.funktion:
            raise HTTPException(status_code=400, detail="Aufgabe definiert keine Funktion")
        try:
            lauf = fuehre_aus(
                state.runner,
                aufgabe.sprache,
                anfrage.code,
                aufgabe.funktion,
                [anfrage.input],
                RunLimits(timeout_sekunden=aufgabe.zeitlimit_sekunden),
            )
        except SandboxFehler as fehler:
            raise HTTPException(status_code=503, detail=str(fehler)) from fehler
        except ValueError as fehler:
            raise HTTPException(status_code=422, detail=str(fehler)) from fehler

        if lauf.aufrufe is None:
            return ProbelaufAntwort(
                stdout=lauf.nutzer_stdout,
                stderr=lauf.stderr,
                laufzeit_ms=lauf.laufzeit_ms,
                timeout=lauf.timeout,
                fehler="Code wurde nicht vollständig ausgeführt",
            )
        aufruf = lauf.aufrufe[0]
        return ProbelaufAntwort(
            rueckgabe=anzeigen(aufruf.wert) if aufruf.ok else None,
            stdout=lauf.nutzer_stdout,
            stderr=lauf.stderr,
            laufzeit_ms=lauf.laufzeit_ms,
            timeout=lauf.timeout,
            fehler=aufruf.fehler,
        )

    return router
