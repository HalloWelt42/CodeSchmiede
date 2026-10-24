"""HTTP-Routen für die Verwaltungs-Übersicht.

Eigener Präfix `/api/admin`, eigene Pydantic-Modelle. Liefert die
komplette Sicht auf Aufgaben (inkl. versteckter Tests, Hints,
Musterlösungen, Statistik), die Befunde der Bestandsprüfung und erlaubt
CRUD: Aufgaben, Musterlösungen und Pfade anlegen, ändern, löschen,
gegen ihre eigenen Tests validieren.

Schreiben geht nur, wenn `aufgaben_schreibbar` gesetzt ist; auf dem Pi
kommen die Aufgaben aus dem Repo und werden am Mac bearbeitet.
"""

from datetime import datetime
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Response
from pydantic import BaseModel, Field

from .. import __version__
from ..aufgaben.bestandspruefung import Befund
from ..aufgaben.schreiber import AufgabenSchreiberFehler
from ..models.aufgabe import Aufgabe
from ..models.konfig import Konfiguration
from ..models.pfad import Pfad
from ..models.progress import Progress
from ..progress.submissions import SubmissionStatistik
from ..pruefung.orchestrator import pruefe
from ..sandbox.runner import SandboxFehler
from ..state import AppState


class AufgabenStatistik(BaseModel):
    submissions_gesamt: int = 0
    bestandene_submissions: int = 0
    versuche: int = 0
    hints_genutzt: int = 0
    punkte_erreicht: int = 0
    status: str = "neu"


class VerwaltungsEintrag(BaseModel):
    """Komplette Sicht auf eine Aufgabe für die Verwaltungsansicht."""

    schema_version: int
    id: str
    revision: int
    titel: str
    sprache: str
    task_type: str
    runner_type: str
    schwierigkeit: str
    schwierigkeit_score: int
    schaetz_minuten: int
    tags: list[str]
    pfade: list[str]
    voraussetzungen: list[str]
    quelle: dict[str, Any]
    lizenz: str
    autor: str | None
    erstellt_am: str | None
    zeitlimit_sekunden: int
    funktion: str | None
    hints: list[dict[str, Any]]
    tests_sichtbar: list[dict[str, Any]]
    tests_versteckt: list[dict[str, Any]]
    starter_code: str
    beschreibung_md: str
    musterloesungen_anzahl: int
    dateipfad: str
    hash: str
    statistik: AufgabenStatistik


class AufgabeVersion(BaseModel):
    revision: int
    hash: str
    gueltig_ab: str


class PfadSchreibAnfrage(BaseModel):
    id: str
    titel: str
    beschreibung: str = ""
    reihenfolge: list[str] = Field(default_factory=list)


class PfadEintrag(BaseModel):
    id: str
    titel: str
    beschreibung: str
    reihenfolge: list[str]
    aufgaben_anzahl: int


class AufgabeSchreibAnfrage(BaseModel):
    """Was das Frontend zum Anlegen / Ändern einer Aufgabe schickt.

    `frontmatter` ist ein freies Dict, weil verschiedene `task_type`s
    unterschiedliche Felder haben (z.B. `quiz` für Output-Quiz).
    Validierung gegen das Pydantic-Modell passiert im Schreiber.
    """

    frontmatter: dict[str, Any] = Field(default_factory=dict)
    beschreibung_md: str = ""


class MusterloesungEintrag(BaseModel):
    variante: str
    code: str


class MusterloesungInhalt(BaseModel):
    code: str


class VarianteErgebnis(BaseModel):
    variante: str
    bestanden: bool
    sichtbar_pass: int
    sichtbar_total: int
    versteckt_pass: int
    versteckt_fail: int
    laufzeit_ms: float
    fehler_text: str | None = None


class ValidierungsErgebnis(BaseModel):
    varianten: list[VarianteErgebnis]


def _statistik(sub: SubmissionStatistik | None, p: Progress | None) -> AufgabenStatistik:
    sub = sub or SubmissionStatistik()
    return AufgabenStatistik(
        submissions_gesamt=sub.gesamt,
        bestandene_submissions=sub.bestanden,
        versuche=p.versuche if p else 0,
        hints_genutzt=p.hints_genutzt if p else 0,
        punkte_erreicht=p.punkte_erreicht if p else 0,
        status=p.status if p else "neu",
    )


def _eintrag(
    a: Aufgabe, statistik: AufgabenStatistik, musterloesungen_anzahl: int, slim: bool = False
) -> VerwaltungsEintrag:
    """Slim: große Felder leer, Anzahlen bleiben (die Tabelle zeigt "Hints (4)")."""
    return VerwaltungsEintrag(
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
        quelle=a.quelle.model_dump(),
        lizenz=a.lizenz,
        autor=a.autor,
        erstellt_am=a.erstellt_am.isoformat() if a.erstellt_am else None,
        zeitlimit_sekunden=a.zeitlimit_sekunden,
        funktion=a.funktion,
        hints=[{"kosten": 0, "text": ""} if slim else h.model_dump() for h in a.hints],
        tests_sichtbar=[{"input": [], "expected": None} if slim else t.model_dump() for t in a.tests_sichtbar],
        tests_versteckt=[{"input": [], "expected": None} if slim else t.model_dump() for t in a.tests_versteckt],
        starter_code="" if slim else a.starter_code,
        beschreibung_md="" if slim else a.beschreibung_md,
        musterloesungen_anzahl=musterloesungen_anzahl,
        dateipfad=str(a.dateipfad),
        hash=a.hash,
        statistik=statistik,
    )


def _pfad_eintrag(p: Pfad) -> PfadEintrag:
    return PfadEintrag(
        id=p.id,
        titel=p.titel,
        beschreibung=p.beschreibung,
        reihenfolge=p.reihenfolge,
        aufgaben_anzahl=len(p.reihenfolge),
    )


def baue_admin_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/admin", tags=["admin"])

    def schreibrecht() -> None:
        if not state.settings.aufgaben_schreibbar:
            raise HTTPException(
                409, "Aufgaben sind hier nur lesbar; bearbeitet wird am Mac, dann ausrollen"
            )

    schreibend = [Depends(schreibrecht)]

    def hole(aufgabe_id: str) -> Aufgabe:
        a = state.aufgaben.aufgabe(aufgabe_id)
        if a is None:
            raise HTTPException(404, f"Aufgabe '{aufgabe_id}' nicht gefunden")
        return a

    def endung(a: Aufgabe) -> str:
        for s in state.konfig.sprachen:
            if s.id == a.sprache:
                return s.endung
        raise HTTPException(400, f"Sprache '{a.sprache}' fehlt in _konfig.yml")

    @router.get("/konfig", response_model=Konfiguration)
    def konfig() -> Konfiguration:
        """Zentrale Konfiguration (Schwierigkeiten, Sprachen, Aufgabentypen)."""
        return state.konfig

    @router.get("/befunde", response_model=list[Befund])
    def befunde() -> list[Befund]:
        """Was die Bestandsprüfung beim letzten Einlesen gefunden hat."""
        return state.befunde

    @router.get("/export")
    def export() -> dict:
        """Vollständige Sicherung als JSON: Submissions, Progress, Streak,
        Konfig. Aufgaben sind Dateien im Repo, hier nur die IDs."""
        return {
            "version": __version__,
            "exportiert_am": datetime.now().isoformat(),
            "submissions": state.submissions.alle_fuer_export(),
            "progress": [p.model_dump(mode="json") for p in state.progress.hole_alle_progress()],
            "streak": state.progress.hole_streak().model_dump(mode="json"),
            "konfig": state.konfig.model_dump(),
            "aufgaben_ids": [a.id for a in state.aufgaben.alle_aufgaben()],
        }

    @router.get("/aufgaben", response_model=list[VerwaltungsEintrag])
    def aufgaben(
        response: Response,
        slim: bool = False,
        sprache: str | None = None,
        suche: str | None = None,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[VerwaltungsEintrag]:
        """Verwaltungs-Liste aller Aufgaben; `slim=true` lässt große Felder
        leer (Detail über `/api/admin/aufgaben/{id}`)."""
        such_lower = (suche or "").lower().strip()
        gefiltert = [
            a for a in state.aufgaben.alle_aufgaben()
            if (not sprache or a.sprache == sprache)
            and (not such_lower or such_lower in a.id.lower() or such_lower in a.titel.lower())
        ]
        gefiltert.sort(key=lambda x: (x.sprache, x.schwierigkeit_score, x.id))
        response.headers["X-Total-Count"] = str(len(gefiltert))
        if limit is not None and limit > 0:
            start = max(0, offset)
            gefiltert = gefiltert[start:start + min(500, limit)]

        sub_stats = state.submissions.statistik_je_aufgabe()
        progress = {p.aufgabe_id: p for p in state.progress.hole_alle_progress()}
        return [
            _eintrag(
                a,
                _statistik(sub_stats.get(a.id), progress.get(a.id)),
                0 if slim else len(state.loader.lade_musterloesungen(a.id)),
                slim=slim,
            )
            for a in gefiltert
        ]

    @router.get("/aufgaben/{aufgabe_id}", response_model=VerwaltungsEintrag)
    def aufgabe_einzeln(aufgabe_id: str) -> VerwaltungsEintrag:
        a = hole(aufgabe_id)
        return _eintrag(
            a,
            _statistik(
                state.submissions.statistik_je_aufgabe().get(a.id),
                state.progress.hole_progress(a.id),
            ),
            len(state.loader.lade_musterloesungen(a.id)),
        )

    @router.post("/aufgaben", response_model=VerwaltungsEintrag, status_code=201, dependencies=schreibend)
    def aufgabe_anlegen(daten: AufgabeSchreibAnfrage) -> VerwaltungsEintrag:
        try:
            state.schreiber.schreibe_aufgabe(
                frontmatter=daten.frontmatter,
                beschreibung_md=daten.beschreibung_md,
                sprache=daten.frontmatter.get("sprache", ""),
                existiert_pruefen=True,
            )
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(400, str(exc)) from exc
        state.neu_einlesen()
        return aufgabe_einzeln(daten.frontmatter["id"])

    @router.put("/aufgaben/{aufgabe_id}", response_model=VerwaltungsEintrag, dependencies=schreibend)
    def aufgabe_aendern(aufgabe_id: str, daten: AufgabeSchreibAnfrage) -> VerwaltungsEintrag:
        if daten.frontmatter.get("id") != aufgabe_id:
            raise HTTPException(400, "ID im Pfad und im Frontmatter müssen übereinstimmen")
        hole(aufgabe_id)
        try:
            state.schreiber.schreibe_aufgabe(
                frontmatter=daten.frontmatter,
                beschreibung_md=daten.beschreibung_md,
                sprache=daten.frontmatter.get("sprache", ""),
                existiert_pruefen=False,
            )
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(400, str(exc)) from exc
        state.neu_einlesen()
        return aufgabe_einzeln(aufgabe_id)

    @router.delete("/aufgaben/{aufgabe_id}", status_code=204, dependencies=schreibend)
    def aufgabe_loeschen(aufgabe_id: str) -> None:
        try:
            state.schreiber.loesche_aufgabe(aufgabe_id)
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(404, str(exc)) from exc
        state.neu_einlesen()

    @router.get("/aufgaben/{aufgabe_id}/musterloesungen", response_model=list[MusterloesungEintrag])
    def musterloesungen(aufgabe_id: str) -> list[MusterloesungEintrag]:
        hole(aufgabe_id)
        return [
            MusterloesungEintrag(variante=m["variante"], code=m["code"])
            for m in state.loader.lade_musterloesungen(aufgabe_id)
        ]

    @router.put(
        "/aufgaben/{aufgabe_id}/musterloesungen/{variante}",
        response_model=MusterloesungEintrag,
        dependencies=schreibend,
    )
    def musterloesung_speichern(
        aufgabe_id: str, variante: str, daten: MusterloesungInhalt
    ) -> MusterloesungEintrag:
        a = hole(aufgabe_id)
        try:
            state.schreiber.schreibe_musterloesung(aufgabe_id, variante, daten.code, endung(a))
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(400, str(exc)) from exc
        state.aufgaben.leere_metriken_cache()
        return MusterloesungEintrag(variante=variante, code=daten.code)

    @router.delete(
        "/aufgaben/{aufgabe_id}/musterloesungen/{variante}",
        status_code=204,
        dependencies=schreibend,
    )
    def musterloesung_loeschen(aufgabe_id: str, variante: str) -> None:
        try:
            state.schreiber.loesche_musterloesung(aufgabe_id, variante)
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(404, str(exc)) from exc
        state.aufgaben.leere_metriken_cache()

    @router.get("/aufgaben/{aufgabe_id}/versionen", response_model=list[AufgabeVersion])
    def aufgabe_versionen(aufgabe_id: str) -> list[AufgabeVersion]:
        """Frühere Revisionen einer Aufgabe aus `aufgaben_versionen`."""
        return [AufgabeVersion(**v) for v in state.aufgaben.versionen(aufgabe_id)]

    @router.get("/pfade", response_model=list[PfadEintrag])
    def pfade_liste() -> list[PfadEintrag]:
        return [_pfad_eintrag(p) for p in state.aufgaben.alle_pfade()]

    def pfad_schreiben(daten: PfadSchreibAnfrage, neu: bool) -> PfadEintrag:
        try:
            state.schreiber.schreibe_pfad(
                pfad_id=daten.id,
                titel=daten.titel,
                beschreibung=daten.beschreibung,
                reihenfolge=daten.reihenfolge,
                existiert_pruefen=neu,
            )
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(400, str(exc)) from exc
        state.neu_einlesen()
        p = state.aufgaben.pfad(daten.id)
        if p is None:
            raise HTTPException(500, "Pfad wurde geschrieben, aber nicht eingelesen")
        return _pfad_eintrag(p)

    @router.post("/pfade", response_model=PfadEintrag, status_code=201, dependencies=schreibend)
    def pfad_anlegen(daten: PfadSchreibAnfrage) -> PfadEintrag:
        return pfad_schreiben(daten, neu=True)

    @router.put("/pfade/{pfad_id}", response_model=PfadEintrag, dependencies=schreibend)
    def pfad_aendern(pfad_id: str, daten: PfadSchreibAnfrage) -> PfadEintrag:
        if daten.id != pfad_id:
            raise HTTPException(400, "ID im Pfad und im Body müssen übereinstimmen")
        if state.aufgaben.pfad(pfad_id) is None:
            raise HTTPException(404, f"Pfad '{pfad_id}' nicht gefunden")
        return pfad_schreiben(daten, neu=False)

    @router.delete("/pfade/{pfad_id}", status_code=204, dependencies=schreibend)
    def pfad_loeschen(pfad_id: str) -> None:
        try:
            state.schreiber.loesche_pfad(pfad_id)
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(404, str(exc)) from exc
        state.neu_einlesen()

    @router.post("/aufgaben/{aufgabe_id}/validieren", response_model=ValidierungsErgebnis)
    def aufgabe_validieren(aufgabe_id: str) -> ValidierungsErgebnis:
        """Lässt alle Musterlösungen gegen alle Tests laufen: zeigt beim
        Aufgabenbau, ob Tests und Lösungen zusammenpassen."""
        a = hole(aufgabe_id)
        ergebnisse: list[VarianteErgebnis] = []
        for ml in state.loader.lade_musterloesungen(aufgabe_id):
            try:
                erg = pruefe(a, ml["code"], state.runner)
            except SandboxFehler as fehler:
                raise HTTPException(503, str(fehler)) from fehler
            except ValueError as fehler:
                raise HTTPException(422, f"Aufgabe fehlerhaft: {fehler}") from fehler
            ergebnisse.append(
                VarianteErgebnis(
                    variante=ml["variante"],
                    bestanden=erg.bestanden,
                    sichtbar_pass=sum(1 for t in erg.sichtbar if t.bestanden),
                    sichtbar_total=len(erg.sichtbar),
                    versteckt_pass=erg.versteckt_pass,
                    versteckt_fail=erg.versteckt_fail,
                    laufzeit_ms=erg.laufzeit_ms,
                    fehler_text="\n".join(
                        [t.fehler for t in erg.sichtbar if t.fehler] + ([erg.stderr] if erg.stderr else [])
                    ) or None,
                )
            )
        return ValidierungsErgebnis(varianten=ergebnisse)

    return router
