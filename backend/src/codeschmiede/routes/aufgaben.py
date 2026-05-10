"""HTTP-Routen fuer Aufgaben."""

from fastapi import APIRouter, HTTPException

from ..models.aufgabe import AufgabeDetail, AufgabeKurz
from ..models.progress import Progress
from ..state import AppState


def baue_aufgaben_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/aufgaben", tags=["aufgaben"])

    @router.get("", response_model=list[AufgabeKurz])
    def liste(
        sprache: str | None = None,
        pfad: str | None = None,
        schwierigkeit: str | None = None,
    ) -> list[AufgabeKurz]:
        ergebnis: list[AufgabeKurz] = []
        for a in state.aufgaben.alle_aufgaben():
            if sprache and a.sprache != sprache:
                continue
            if pfad and pfad not in a.pfade:
                continue
            if schwierigkeit and a.schwierigkeit != schwierigkeit:
                continue
            ergebnis.append(
                AufgabeKurz(
                    id=a.id,
                    titel=a.titel,
                    sprache=a.sprache,
                    schwierigkeit=a.schwierigkeit,
                    schwierigkeit_score=a.schwierigkeit_score,
                    schaetz_minuten=a.schaetz_minuten,
                    tags=a.tags,
                    pfade=a.pfade,
                    revision=a.revision,
                )
            )
        ergebnis.sort(key=lambda x: x.schwierigkeit_score)
        return ergebnis

    @router.get("/{aufgabe_id}", response_model=AufgabeDetail)
    def detail(aufgabe_id: str) -> AufgabeDetail:
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")

        return AufgabeDetail(
            schema_version=a.schema_version,
            id=a.id,
            revision=a.revision,
            titel=a.titel,
            sprache=a.sprache,
            task_type=a.task_type,
            runner_type=a.runner_type,
            schwierigkeit=a.schwierigkeit,
            schwierigkeit_score=a.schwierigkeit_score,
            schaetz_minuten=a.schaetz_minuten,
            tags=a.tags,
            pfade=a.pfade,
            voraussetzungen=a.voraussetzungen,
            quelle=a.quelle,
            lizenz=a.lizenz,
            autor=a.autor,
            erstellt_am=a.erstellt_am,
            zeitlimit_sekunden=a.zeitlimit_sekunden,
            funktion=a.funktion,
            hints=a.hints,
            tests_sichtbar=a.tests_sichtbar,
            starter_code=a.starter_code,
            beschreibung_md=a.beschreibung_md,
            anzahl_versteckte_tests=len(a.tests_versteckt),
        )

    @router.get("/{aufgabe_id}/musterloesungen")
    def musterloesungen(aufgabe_id: str) -> list[dict[str, str]]:
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        return state.loader.lade_musterloesungen(aufgabe_id)

    @router.post("/{aufgabe_id}/hints/{hint_index}", response_model=Progress)
    def hint_geoeffnet(aufgabe_id: str, hint_index: int) -> Progress:
        """Markiert Hint Nr. `hint_index` (0-basiert) als gesehen.
        Idempotent: mehrfaches Aufrufen schadet nicht.
        """
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        if hint_index < 0 or hint_index >= len(a.hints):
            raise HTTPException(status_code=400, detail="Hint-Index ungueltig")
        return state.progress.markiere_hint_gesehen(aufgabe_id, hint_index)

    return router
