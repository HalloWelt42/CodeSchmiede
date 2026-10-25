"""HTTP-Routen der Spielmechanik: Spielstand für Kopf und Startseite,
Erfolge für ihre Seite. Die Belohnung einer Abgabe kommt mit der Abgabe."""

from fastapi import APIRouter

from ..models.spiel import ErfolgsListe, Spielstand
from ..state import AppState


def baue_spiel_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/spiel", tags=["spiel"])

    @router.get("/stand", response_model=Spielstand)
    def stand() -> Spielstand:
        return state.spiel.stand(state.bestand())

    @router.get("/erfolge", response_model=ErfolgsListe)
    def erfolge() -> ErfolgsListe:
        return state.spiel.erfolge(state.bestand())

    return router
