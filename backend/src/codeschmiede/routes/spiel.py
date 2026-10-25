"""HTTP-Routen der Spielmechanik: Spielstand für Kopf und Startseite,
Erfolge für ihre Seite, Spiele mit dem Stand ihrer Levels. Die Belohnung
einer Abgabe kommt mit der Abgabe."""

from fastapi import APIRouter

from ..models.spiel import ErfolgsListe, Spielstand, SpielUebersicht
from ..state import AppState


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

    return router
