"""HTTP-Routen für Progress, Tagesziel, Streak, Reset und Weiter-Vorschlag."""

from datetime import date

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..models.progress import (
    GesamtFortschritt,
    Progress,
    Streak,
    Tagesziel,
    WeiterVorschlag,
)
from ..progress.streak import streak_aktiv
from ..state import AppState


class HeatmapTag(BaseModel):
    datum: str
    submissions: int
    bestanden: int


class HeatmapAntwort(BaseModel):
    tage: list[HeatmapTag]


class Achievement(BaseModel):
    id: str
    titel: str
    beschreibung: str
    icon: str
    erreicht: bool
    fortschritt: int = 0
    ziel: int = 1


class AchievementsAntwort(BaseModel):
    eintraege: list[Achievement]
    erreicht_anzahl: int
    gesamt_anzahl: int


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

    @router.post("/reset-alles")
    def reset_alles() -> dict[str, str]:
        """Globaler Reset: löscht alle Submissions, Progress und Streak.
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

    @router.get("/heatmap", response_model=HeatmapAntwort)
    def heatmap(tage: int = 90) -> HeatmapAntwort:
        """Submissions pro Tag für die letzten N Tage."""
        if tage < 1 or tage > 365:
            raise HTTPException(400, "tage muss zwischen 1 und 365 sein")
        with state.db.connect() as conn:
            rows = conn.execute(
                """
                SELECT date(zeitstempel) AS datum,
                       COUNT(*) AS submissions,
                       SUM(CASE WHEN bestanden = 1 THEN 1 ELSE 0 END) AS bestanden
                FROM submissions
                WHERE date(zeitstempel) >= date('now', ?)
                GROUP BY date(zeitstempel)
                ORDER BY datum
                """,
                (f"-{tage - 1} days",),
            ).fetchall()
        eintraege = [
            HeatmapTag(
                datum=r["datum"],
                submissions=r["submissions"],
                bestanden=r["bestanden"] or 0,
            )
            for r in rows
        ]
        return HeatmapAntwort(tage=eintraege)

    @router.get("/achievements", response_model=AchievementsAntwort)
    def achievements() -> AchievementsAntwort:
        """Berechnet alle Achievements zur Laufzeit aus DB-Daten."""
        gesamt = state.progress.gesamt_fortschritt(state.aufgaben.alle_aufgaben())
        streak = state.progress.hole_streak()

        with state.db.connect() as conn:
            sprachen_count = conn.execute(
                """
                SELECT COUNT(DISTINCT a.sprache) AS n
                FROM submissions s
                JOIN aufgaben a ON s.aufgabe_id = a.id
                WHERE s.bestanden = 1
                """
            ).fetchone()
            sprachen = sprachen_count["n"] if sprachen_count else 0

            pfade_voll = conn.execute(
                """
                SELECT COUNT(*) AS n FROM (
                  SELECT a.pfade FROM aufgaben a
                ) WHERE pfade IS NOT NULL AND pfade != '[]'
                """
            ).fetchone()
            _ = pfade_voll  # Detail-Pruefung folgt in Python

        # Pfad-Vollendung in Python (einfacher mit Pfad-Modellen)
        progress_dict = {p.aufgabe_id: p for p in state.progress.hole_alle_progress()}

        def aufgabe_geloest(aid: str) -> bool:
            p = progress_dict.get(aid)
            return p is not None and p.status == "geloest"

        pfade_komplett = sum(
            1
            for p in state.aufgaben.alle_pfade()
            if p.reihenfolge and all(aufgabe_geloest(a) for a in p.reihenfolge)
        )

        eintraege = [
            Achievement(
                id="erste_aufgabe",
                titel="Erste Aufgabe",
                beschreibung="Loese deine erste Aufgabe",
                icon="fa-flag-checkered",
                erreicht=gesamt.aufgaben_geloest >= 1,
                fortschritt=min(gesamt.aufgaben_geloest, 1),
                ziel=1,
            ),
            Achievement(
                id="zehn_aufgaben",
                titel="Aufgewärmt",
                beschreibung="10 Aufgaben gelöst",
                icon="fa-fire",
                erreicht=gesamt.aufgaben_geloest >= 10,
                fortschritt=min(gesamt.aufgaben_geloest, 10),
                ziel=10,
            ),
            Achievement(
                id="fuenfzig_aufgaben",
                titel="Halbprofi",
                beschreibung="50 Aufgaben gelöst",
                icon="fa-medal",
                erreicht=gesamt.aufgaben_geloest >= 50,
                fortschritt=min(gesamt.aufgaben_geloest, 50),
                ziel=50,
            ),
            Achievement(
                id="streak_3",
                titel="Drei am Stück",
                beschreibung="3 Tage Streak",
                icon="fa-bolt",
                erreicht=streak.aktuell >= 3 or streak.laengster >= 3,
                fortschritt=min(max(streak.aktuell, streak.laengster), 3),
                ziel=3,
            ),
            Achievement(
                id="streak_7",
                titel="Eine Woche",
                beschreibung="7 Tage Streak",
                icon="fa-calendar-week",
                erreicht=streak.aktuell >= 7 or streak.laengster >= 7,
                fortschritt=min(max(streak.aktuell, streak.laengster), 7),
                ziel=7,
            ),
            Achievement(
                id="streak_30",
                titel="Marathon",
                beschreibung="30 Tage Streak",
                icon="fa-trophy",
                erreicht=streak.aktuell >= 30 or streak.laengster >= 30,
                fortschritt=min(max(streak.aktuell, streak.laengster), 30),
                ziel=30,
            ),
            Achievement(
                id="pfad_komplett",
                titel="Erster Pfad voll",
                beschreibung="Einen ganzen Pfad gelöst",
                icon="fa-route",
                erreicht=pfade_komplett >= 1,
                fortschritt=min(pfade_komplett, 1),
                ziel=1,
            ),
            Achievement(
                id="drei_pfade",
                titel="Pfad-Sammler",
                beschreibung="Drei Pfade vollständig gelöst",
                icon="fa-map-location-dot",
                erreicht=pfade_komplett >= 3,
                fortschritt=min(pfade_komplett, 3),
                ziel=3,
            ),
            Achievement(
                id="hundert_submissions",
                titel="Fleissig",
                beschreibung="100 Submissions abgeschickt",
                icon="fa-paper-plane",
                erreicht=gesamt.submissions_gesamt >= 100,
                fortschritt=min(gesamt.submissions_gesamt, 100),
                ziel=100,
            ),
            Achievement(
                id="multilingual",
                titel="Polyglott",
                beschreibung="Aufgaben in 2 Sprachen gelöst",
                icon="fa-globe",
                erreicht=sprachen >= 2,
                fortschritt=min(sprachen, 2),
                ziel=2,
            ),
        ]
        return AchievementsAntwort(
            eintraege=eintraege,
            erreicht_anzahl=sum(1 for a in eintraege if a.erreicht),
            gesamt_anzahl=len(eintraege),
        )

    return router
