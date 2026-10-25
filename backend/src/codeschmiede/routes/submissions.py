"""HTTP-Routen für Submissions und Probelauf -- Code abschicken,
ausführen, bewerten oder probieren.

Bei einem bestandenen Submit liefern wir einen Performance-Vergleich
mit den Musterlösungen mit. Die werden einmal pro Aufgabe durch die
Sandbox geschickt und im AufgabenRepository gecacht; ein Reindex über
den Watcher leert den Cache.

Geprüft wird auf dem Server. Aufgabentypen mit Abgabeweg "browser"
(CSS-Nachbauten) schicken über `/lokal` nur eine Messung; das Ergebnis
macht daraus der Prüfer des Typs. Solche mit "runde" (Sprint) geben über
ihre Spielrunde ab (routes/spiel.py).
"""

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..models.aufgabe import Aufgabe
from ..models.progress import Progress
from ..models.spiel import Belohnung
from ..progress.submissions import codelaenge
from ..pruefung.ergebnis import Messung, PruefErgebnis
from ..pruefung.kodierung import anzeigen
from ..pruefung.orchestrator import UnbekannterAufgabentyp, pruefe, pruefer_fuer
from ..pruefung.registry import Abgabeweg
from ..pruefung.testlauf import fuehre_aus
from ..sandbox.result import RunLimits
from ..sandbox.runner import SandboxFehler
from ..state import AppState


WEG_HINWEIS: dict[Abgabeweg, str] = {
    "server": "Diese Aufgabe wird auf dem Server geprüft",
    "browser": "Diese Aufgabe wird im Browser geprüft",
    "runde": "Diese Aufgabe wird über eine Spielrunde abgegeben",
}


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
    # nur bei bestandenen Abgaben
    belohnung: Belohnung | None = None


class LokaleSubmissionAnfrage(BaseModel):
    """Submission eines Aufgabentyps, den nur der Browser messen kann."""

    aufgabe_id: str
    code: str = Field(min_length=1, max_length=50_000)
    messung: Messung


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

    def verlange_weg(aufgabe: Aufgabe, weg: Abgabeweg) -> None:
        try:
            abgabe = pruefer_fuer(aufgabe).abgabe
        except UnbekannterAufgabentyp as fehler:
            raise HTTPException(status_code=422, detail=str(fehler)) from fehler
        if abgabe != weg:
            raise HTTPException(status_code=400, detail=WEG_HINWEIS[abgabe])

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

    def antwort(aufgabe: Aufgabe, code: str, ergebnis: PruefErgebnis) -> SubmissionAntwort:
        verbucht = state.spiel.verbuche(state.bestand(), aufgabe, code, ergebnis)
        return SubmissionAntwort(
            bestanden=ergebnis.bestanden,
            pruefung=verbucht.pruefung,
            codelaenge_zeichen=codelaenge(code),
            submission_id=verbucht.submission_id,
            progress=verbucht.progress,
            vergleich=vergleich(aufgabe) if ergebnis.bestanden else [],
            belohnung=verbucht.belohnung,
        )

    @router.post("", response_model=SubmissionAntwort)
    def submit(anfrage: SubmissionAnfrage) -> SubmissionAntwort:
        aufgabe = hole_aufgabe(anfrage.aufgabe_id)
        verlange_weg(aufgabe, "server")

        return antwort(aufgabe, anfrage.code, pruefe_sicher(aufgabe, anfrage.code))

    @router.post("/lokal", response_model=SubmissionAntwort)
    def submit_lokal(anfrage: LokaleSubmissionAnfrage) -> SubmissionAntwort:
        """Wertet die Messung einer im Browser gerenderten Aufgabe."""
        aufgabe = hole_aufgabe(anfrage.aufgabe_id)
        verlange_weg(aufgabe, "browser")
        werte = pruefer_fuer(aufgabe).werte
        assert werte is not None  # die Registry verlangt sie für "browser"
        muster = state.aufgaben.kuerzeste_musterloesung(aufgabe.id)
        return antwort(aufgabe, anfrage.code, werte(aufgabe, anfrage.code, anfrage.messung, muster))

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
