"""HTTP-Routen fuer Progress, Tagesziel und Streak."""

from datetime import date

from fastapi import APIRouter

from ..models.progress import GesamtFortschritt, Progress, Streak, Tagesziel
from ..progress.streak import streak_aktiv
from ..state import AppState


def baue_progress_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/progress", tags=["progress"])

    @router.get("", response_model=GesamtFortschritt)
    def gesamt() -> GesamtFortschritt:
        anzahl = len(state.aufgaben.alle_aufgaben())
        return state.progress.gesamt_fortschritt(anzahl)

    @router.get("/heute", response_model=Tagesziel)
    def heute() -> Tagesziel:
        heute_dat = date.today()
        faellig = state.progress.faellige_aufgaben(heute_dat)
        streak = state.progress.hole_streak()

        progress_dict = {p.aufgabe_id: p for p in state.progress.hole_alle_progress()}
        offen = [
            a
            for a in sorted(
                state.aufgaben.alle_aufgaben(), key=lambda x: x.schwierigkeit_score
            )
            if a.id not in progress_dict or progress_dict[a.id].status != "geloest"
        ]
        vorschlag = offen[0].id if offen else None

        return Tagesziel(
            datum=heute_dat,
            faellige_wiederholungen=faellig,
            vorgeschlagene_neue=vorschlag,
            letzte_aufgabe=state.progress.letzte_aktive_aufgabe(),
            streak_aktiv=streak_aktiv(streak, heute_dat),
            aktueller_streak=streak.aktuell,
            laengster_streak=streak.laengster,
        )

    @router.get("/streak", response_model=Streak)
    def get_streak() -> Streak:
        return state.progress.hole_streak()

    @router.get("/aufgaben", response_model=dict[str, Progress])
    def aufgaben_progress() -> dict[str, Progress]:
        return {p.aufgabe_id: p for p in state.progress.hole_alle_progress()}

    return router
