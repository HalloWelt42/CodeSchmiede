"""HTTP-Routen fuer Pfade."""

from fastapi import APIRouter, HTTPException

from ..models.pfad import Pfad
from ..state import AppState


def baue_pfade_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/pfade", tags=["pfade"])

    @router.get("", response_model=list[Pfad])
    def liste() -> list[Pfad]:
        return state.aufgaben.alle_pfade()

    @router.get("/{pfad_id}", response_model=Pfad)
    def detail(pfad_id: str) -> Pfad:
        p = state.aufgaben.pfad(pfad_id)
        if not p:
            raise HTTPException(status_code=404, detail="Pfad nicht gefunden")
        return p

    return router
