"""HTTP-Routen der Spielmechanik: Spielstand für Kopf und Startseite,
Erfolge für ihre Seite, Spiele mit dem Stand ihrer Levels und die Runden
des Ausgabe-Sprints. Die Belohnung einer Abgabe kommt mit der Abgabe."""

from collections.abc import Iterator
from contextlib import contextmanager

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..models.spiel import ErfolgsListe, Spielstand, SpielUebersicht
from ..models.sprint import SprintAbschluss, SprintRueckmeldung, SprintRunde
from ..spiel.sprint import FalscheAntwort, RundeNichtGefunden, RundeVorbei
from ..state import AppState


class SprintAntwort(BaseModel):
    frage: int
    wahl: int


def baue_spiel_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/spiel", tags=["spiel"])

    @router.get("/stand", response_model=Spielstand)
    def stand() -> Spielstand:
        return state.spiel.stand(state.bestand())

    @router.get("/erfolge", response_model=ErfolgsListe)
    def erfolge() -> ErfolgsListe:
        return state.spiel.erfolge(state.bestand())

    @router.get("/spiele", response_model=list[SpielUebersicht])
    def spiele() -> list[SpielUebersicht]:
        return state.spiel.spiele(state.bestand())

    @router.post("/sprint/{aufgabe_id}/runde", response_model=SprintRunde)
    def sprint_runde(aufgabe_id: str) -> SprintRunde:
        aufgabe = state.aufgaben.aufgabe(aufgabe_id)
        if aufgabe is None or aufgabe.task_type != "ausgabe_sprint":
            raise HTTPException(status_code=404, detail="Kein Sprint-Level")
        return state.sprint.neue_runde(aufgabe)

    @router.post("/sprint/runde/{runde_id}/antwort", response_model=SprintRueckmeldung)
    def sprint_antwort(runde_id: str, anfrage: SprintAntwort) -> SprintRueckmeldung:
        with sprint_fehler():
            return state.sprint.antworte(runde_id, anfrage.frage, anfrage.wahl, state.bestand())

    @router.post("/sprint/runde/{runde_id}/abschluss", response_model=SprintAbschluss)
    def sprint_abschluss(runde_id: str) -> SprintAbschluss:
        with sprint_fehler():
            return state.sprint.abschliessen(runde_id, state.bestand())

    return router


@contextmanager
def sprint_fehler() -> Iterator[None]:
    """Fehler der Runde als HTTP-Antwort: unbekannt 404, vorbei 409, unpassend 422."""
    try:
        yield
    except RundeNichtGefunden as fehler:
        raise HTTPException(status_code=404, detail=str(fehler)) from fehler
    except RundeVorbei as fehler:
        raise HTTPException(status_code=409, detail=str(fehler)) from fehler
    except FalscheAntwort as fehler:
        raise HTTPException(status_code=422, detail=str(fehler)) from fehler
