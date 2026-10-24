"""HTTP-Routen für Aufgaben."""

from fastapi import APIRouter, HTTPException, Response

from ..models.aufgabe import Aufgabe, AufgabeDetail, AufgabeKurz
from ..models.progress import Progress
from ..progress.submissions import SubmissionEintrag
from ..pruefung.orchestrator import anzahl_versteckt, oeffentliches_extra
from ..state import AppState


def _voraussetzungen_offen(a: Aufgabe, geloeste_ids: set[str]) -> list[str]:
    """Liefert die Liste der nicht-gelösten Voraussetzungen."""
    return [v for v in a.voraussetzungen if v not in geloeste_ids]


def baue_aufgaben_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/aufgaben", tags=["aufgaben"])

    def hole_geloeste_ids() -> set[str]:
        return {
            p.aufgabe_id
            for p in state.progress.hole_alle_progress()
            if p.status == "geloest"
        }

    @router.get("", response_model=list[AufgabeKurz])
    def liste(
        response: Response,
        sprache: str | None = None,
        pfad: str | None = None,
        schwierigkeit: str | None = None,
        tag: str | None = None,
        status: str | None = None,
        suche: str | None = None,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[AufgabeKurz]:
        """Aufgaben-Liste mit Filtern + optionaler Pagination.

        Ohne `limit` → alle Treffer (kompatibel zum alten Verhalten).
        Mit `limit` → Slice von `offset` bis `offset+limit`. In jedem Fall
        wird `X-Total-Count` als Header gesetzt.

        Filter:
        - sprache, pfad, schwierigkeit, tag: exakte Filter
        - status: "geloest" / "in_arbeit" / "neu"
        - suche: Substring in id ODER titel (case-insensitive)
        """
        geloest = hole_geloeste_ids()
        in_arbeit = {
            p.aufgabe_id
            for p in state.progress.hole_alle_progress()
            if p.status == "in_arbeit"
        }
        such_lower = (suche or "").lower().strip()

        ergebnis: list[AufgabeKurz] = []
        for a in state.aufgaben.alle_aufgaben():
            if sprache and a.sprache != sprache:
                continue
            if pfad and pfad not in a.pfade:
                continue
            if schwierigkeit and a.schwierigkeit != schwierigkeit:
                continue
            if tag and tag not in a.tags:
                continue
            if status:
                if status == "geloest" and a.id not in geloest:
                    continue
                if status == "in_arbeit" and a.id not in in_arbeit:
                    continue
                if status == "neu" and (a.id in geloest or a.id in in_arbeit):
                    continue
            if such_lower and such_lower not in a.id.lower() and such_lower not in a.titel.lower():
                continue
            offen = _voraussetzungen_offen(a, geloest)
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
                    voraussetzungen=a.voraussetzungen,
                    voraussetzungen_offen=offen,
                    gesperrt=len(offen) > 0,
                )
            )
        ergebnis.sort(key=lambda x: x.schwierigkeit_score)
        response.headers["X-Total-Count"] = str(len(ergebnis))
        if limit is not None and limit > 0:
            start = max(0, offset)
            ergebnis = ergebnis[start:start + min(500, limit)]
        return ergebnis

    @router.get("/{aufgabe_id}", response_model=AufgabeDetail)
    def detail(aufgabe_id: str) -> AufgabeDetail:
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")

        offen = _voraussetzungen_offen(a, hole_geloeste_ids())
        progress = state.progress.hole_progress(aufgabe_id)

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
            voraussetzungen_offen=offen,
            gesperrt=len(offen) > 0,
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
            anzahl_versteckte_tests=anzahl_versteckt(a),
            musterloesungen_anzahl=len(state.loader.lade_musterloesungen(a.id)),
            musterloesungen_frei=bool(progress and progress.musterloesungen_frei),
            extra=oeffentliches_extra(a),
        )

    @router.get("/{aufgabe_id}/musterloesungen")
    def musterloesungen(aufgabe_id: str) -> list[dict[str, str]]:
        """Erst nach dem Bestehen oder nach dem Aufgeben."""
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        progress = state.progress.hole_progress(aufgabe_id)
        if not (progress and progress.musterloesungen_frei):
            raise HTTPException(
                status_code=403,
                detail="Musterlösungen gibt es nach dem Bestehen oder nach dem Aufgeben",
            )
        return state.loader.lade_musterloesungen(aufgabe_id)

    @router.post("/{aufgabe_id}/aufgeben", response_model=Progress)
    def aufgeben(aufgabe_id: str) -> Progress:
        """Gibt die Musterlösungen frei; ein späteres Bestehen bringt keine Punkte."""
        if not state.aufgaben.aufgabe(aufgabe_id):
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        return state.progress.gib_auf(aufgabe_id)

    @router.post("/{aufgabe_id}/hints/{hint_index}", response_model=Progress)
    def hint_geoeffnet(aufgabe_id: str, hint_index: int) -> Progress:
        """Markiert Hint Nr. `hint_index` (0-basiert) als gesehen.
        Idempotent: mehrfaches Aufrufen schadet nicht.
        """
        a = state.aufgaben.aufgabe(aufgabe_id)
        if not a:
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        if hint_index < 0 or hint_index >= len(a.hints):
            raise HTTPException(status_code=400, detail="Hint-Index ungültig")
        return state.progress.markiere_hint_gesehen(aufgabe_id, hint_index)

    @router.get("/{aufgabe_id}/submissions", response_model=list[SubmissionEintrag])
    def submissions_verlauf(aufgabe_id: str, limit: int = 20) -> list[SubmissionEintrag]:
        """Letzte N Submissions zu einer Aufgabe -- für den Verlauf im
        Detail-View. Code wird mitgeliefert, damit Re-Open trivial ist.
        """
        if not state.aufgaben.aufgabe(aufgabe_id):
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        return state.submissions.verlauf(aufgabe_id, limit)

    @router.get("/{aufgabe_id}/letzte-submission")
    def letzte_submission(aufgabe_id: str) -> dict:
        """Letzte abgeschickte Lösung (egal ob bestanden) -- damit der
        Editor beim erneuten Öffnen den letzten Stand zeigt statt der
        Starter-Boilerplate.
        """
        if not state.aufgaben.aufgabe(aufgabe_id):
            raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
        letzte = state.submissions.letzte(aufgabe_id)
        if not letzte:
            return {"code": None, "bestanden": None, "zeitstempel": None}
        return {"code": letzte.code, "bestanden": letzte.bestanden, "zeitstempel": letzte.zeitstempel}

    return router
