"""HTTP-Routen für Progress, Tagesziel, Streak, Reset und Weiter-Vorschlag."""

from datetime import date

from fastapi import APIRouter, HTTPException

from ..models.progress import (
    GesamtFortschritt,
    Progress,
    Streak,
    Tagesziel,
    WeiterVorschlag,
)
from ..progress.streak import streak_aktiv
from ..state import AppState


def baue_progress_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/progress", tags=["progress"])

    @router.get("", response_model=GesamtFortschritt)
    def gesamt() -> GesamtFortschritt:
        return state.progress.gesamt_fortschritt(state.aufgaben.alle_aufgaben())

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

    @router.delete("/{aufgabe_id}")
    def reset(aufgabe_id: str) -> dict[str, str]:
        if not state.aufgaben.aufgabe(aufgabe_id):
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        state.progress.reset_aufgabe(aufgabe_id)
        return {"status": "reset", "aufgabe_id": aufgabe_id}

    @router.get("/weiter/{aufgabe_id}", response_model=WeiterVorschlag)
    def weiter_vorschlag(aufgabe_id: str) -> WeiterVorschlag:
        """Naechste offene Aufgabe -- bevorzugt im selben Pfad."""
        aktuell = state.aufgaben.aufgabe(aufgabe_id)
        if not aktuell:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")

        progress_dict = {p.aufgabe_id: p for p in state.progress.hole_alle_progress()}

        def ist_offen(aid: str) -> bool:
            return aid not in progress_dict or progress_dict[aid].status != "geloest"

        # Erstens: gleichen Pfad nehmen, nächste offene nach der aktuellen
        for pfad_id in aktuell.pfade:
            pfad = state.aufgaben.pfad(pfad_id)
            if not pfad:
                continue
            try:
                idx = pfad.reihenfolge.index(aufgabe_id)
            except ValueError:
                continue
            for kandidat in pfad.reihenfolge[idx + 1 :]:
                if ist_offen(kandidat):
                    return WeiterVorschlag(
                        naechste_id=kandidat, quelle="pfad", pfad_id=pfad_id
                    )

        # Zweitens: global nächste offene Aufgabe nach Schwierigkeitsscore,
        # die schwerer ist als die aktuelle (oder die erste offene insgesamt).
        offene = sorted(
            (a for a in state.aufgaben.alle_aufgaben() if ist_offen(a.id) and a.id != aufgabe_id),
            key=lambda x: x.schwierigkeit_score,
        )
        nach_aktuell = [a for a in offene if a.schwierigkeit_score >= aktuell.schwierigkeit_score]
        kandidaten = nach_aktuell or offene
        if kandidaten:
            return WeiterVorschlag(naechste_id=kandidaten[0].id, quelle="global")

        return WeiterVorschlag(naechste_id=None, quelle="keine")

    return router
