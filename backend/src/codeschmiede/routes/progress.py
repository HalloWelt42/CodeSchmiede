"""HTTP-Routen für Progress, Tagesziel, Aktivität, Reset und Weiter-Vorschlag.
Serie und Erfolge gehören zur Spielmechanik (routes/spiel.py)."""

from datetime import date

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..models.progress import (
    GesamtFortschritt,
    Progress,
    Tagesziel,
    WeiterVorschlag,
)
from ..progress.submissions import TagesAktivitaet
from ..state import AppState


class HeatmapAntwort(BaseModel):
    tage: list[TagesAktivitaet]


def baue_progress_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/progress", tags=["progress"])

    @router.get("", response_model=GesamtFortschritt)
    def gesamt() -> GesamtFortschritt:
        return state.progress.gesamt_fortschritt(state.aufgaben.alle_aufgaben())

    @router.get("/heute", response_model=Tagesziel)
    def heute() -> Tagesziel:
        heute_dat = date.today()
        faellig = state.progress.faellige_aufgaben(heute_dat)

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
        )

    @router.get("/aufgaben", response_model=dict[str, Progress])
    def aufgaben_progress() -> dict[str, Progress]:
        return {p.aufgabe_id: p for p in state.progress.hole_alle_progress()}

    @router.delete("/{aufgabe_id}")
    def reset(aufgabe_id: str) -> dict[str, str]:
        if not state.aufgaben.aufgabe(aufgabe_id):
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        state.progress.reset_aufgabe(aufgabe_id)
        return {"status": "reset", "aufgabe_id": aufgabe_id}

    @router.post("/reset-alles")
    def reset_alles() -> dict[str, str]:
        """Globaler Reset: löscht alle Submissions, Progress und Tagesaufträge.
        Aufgaben-Dateien bleiben unangetastet -- man fängt komplett von
        vorne an.
        """
        state.progress.reset_alles()
        state.aufgaben.leere_metriken_cache()
        return {"status": "alles zurückgesetzt"}

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
        for pfad_id in state.aufgaben.pfade_von(aktuell.id):
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

    @router.get("/heatmap", response_model=HeatmapAntwort)
    def heatmap(jahr: int | None = None, tage: int | None = None) -> HeatmapAntwort:
        """Submissions pro Tag.

        Zwei Modi:
        - `jahr=YYYY`: liefert alle Tage des Jahres mit mind. einer Submission
          (GitHub-Style fuer einen Jahres-Block).
        - `tage=N`: liefert die letzten N Tage als rolling window. Backward-
          kompatibel zur ersten Heatmap-Variante.
        Kein Parameter -> aktuelles Jahr.
        """
        if jahr is None and tage is None:
            jahr = date.today().year

        if jahr is not None:
            if jahr < 2000 or jahr > 2100:
                raise HTTPException(400, "Jahr muss zwischen 2000 und 2100 sein")
            eintraege = state.submissions.je_tag_im_jahr(jahr)
        else:
            if tage is None or tage < 1 or tage > 730:
                raise HTTPException(400, "tage muss zwischen 1 und 730 sein")
            eintraege = state.submissions.je_tag_seit(tage)
        return HeatmapAntwort(tage=eintraege)

    return router
