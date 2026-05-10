"""HTTP-Routen für die Verwaltungs-Übersicht.

Bewusst entkoppelt vom übrigen API-Schnitt: eigener Praefix
`/api/admin`, eigene Pydantic-Modelle. Liefert die komplette Sicht auf
Aufgaben (inkl. versteckter Tests, Hints, Musterlösungen, Statistik)
und erlaubt CRUD: Aufgaben + Musterloesungen anlegen, aendern, loeschen,
gegen ihre eigenen Tests validieren. Im Single-User-MVP gibt es kein
Auth -- das Endpoint ist genauso geschützt wie die App selbst.
"""

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..aufgaben.schreiber import AufgabenSchreiberFehler
from ..models.konfig import Konfiguration
from ..pruefung.orchestrator import pruefe
from ..state import AppState


class AufgabenStatistik(BaseModel):
    submissions_gesamt: int = 0
    bestandene_submissions: int = 0
    versuche: int = 0
    hints_genutzt: int = 0
    punkte_erreicht: int = 0
    status: str = "neu"


class VerwaltungsEintrag(BaseModel):
    """Komplette Sicht auf eine Aufgabe für die Verwaltungsansicht.

    Bewusst breit -- die Tabelle zeigt alles, was über das Frontmatter
    einkommt, plus Statistik aus den Tabellen `submissions` + `progress`.
    """

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


class AufgabeSchreibAnfrage(BaseModel):
    """Was das Frontend zum Anlegen / Aendern einer Aufgabe schickt.

    `frontmatter` ist ein freies Dict, weil verschiedene `task_type`s
    unterschiedliche Felder haben (z.B. `quiz` fuer Output-Quiz).
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


def baue_admin_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/admin", tags=["admin"])

    @router.get("/konfig", response_model=Konfiguration)
    def konfig() -> Konfiguration:
        """Liefert die zentrale Konfiguration (Schwierigkeiten, Sprachen,
        Aufgabentypen). Frontend zieht das beim Start und nutzt es reaktiv."""
        return state.konfig

    @router.get("/export")
    def export() -> dict:
        """Vollständiger Backup als JSON: alle Submissions, Progress,
        Streak, Konfig. Aufgaben sind als Dateien im Repo, hier nur die
        ID-Referenzen.
        """
        with state.db.connect() as conn:
            submissions = [
                dict(row)
                for row in conn.execute(
                    """
                    SELECT id, aufgabe_id, aufgabe_revision,
                           datetime(zeitstempel) AS zeitstempel,
                           code, bestanden, laufzeit_ms, codelaenge_zeichen
                    FROM submissions ORDER BY id
                    """
                ).fetchall()
            ]
            progress = [
                dict(row)
                for row in conn.execute("SELECT * FROM progress").fetchall()
            ]
            kv = {
                row["key"]: row["value"]
                for row in conn.execute("SELECT key, value FROM kv_state").fetchall()
            }
        return {
            "version": __import__("codeschmiede").__version__,
            "exportiert_am": __import__("datetime").datetime.now().isoformat(),
            "submissions": submissions,
            "progress": progress,
            "kv_state": kv,
            "konfig": state.konfig.model_dump(),
            "aufgaben_ids": [a.id for a in state.aufgaben.alle_aufgaben()],
        }

    @router.get("/aufgaben", response_model=list[VerwaltungsEintrag])
    def aufgaben() -> list[VerwaltungsEintrag]:
        eintraege: list[VerwaltungsEintrag] = []

        # Statistik vorab in einem Query holen, dann pro Aufgabe zuordnen
        with state.db.connect() as conn:
            sub_rows = conn.execute(
                """
                SELECT aufgabe_id,
                       COUNT(*) AS gesamt,
                       SUM(CASE WHEN bestanden = 1 THEN 1 ELSE 0 END) AS bestanden
                FROM submissions
                GROUP BY aufgabe_id
                """
            ).fetchall()
            sub_stats = {
                r["aufgabe_id"]: (r["gesamt"], r["bestanden"] or 0) for r in sub_rows
            }

            progress_rows = conn.execute("SELECT * FROM progress").fetchall()
            progress_by_id = {r["aufgabe_id"]: r for r in progress_rows}

        for a in sorted(
            state.aufgaben.alle_aufgaben(),
            key=lambda x: (x.sprache, x.schwierigkeit_score, x.id),
        ):
            sub_gesamt, sub_bestanden = sub_stats.get(a.id, (0, 0))
            p = progress_by_id.get(a.id)
            statistik = AufgabenStatistik(
                submissions_gesamt=sub_gesamt,
                bestandene_submissions=sub_bestanden,
                versuche=p["versuche"] if p else 0,
                hints_genutzt=p["hints_genutzt"] if p else 0,
                punkte_erreicht=p["punkte_erreicht"] if p else 0,
                status=p["status"] if p else "neu",
            )
            ml = state.loader.lade_musterloesungen(a.id)
            eintraege.append(
                VerwaltungsEintrag(
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
                    hints=[h.model_dump() for h in a.hints],
                    tests_sichtbar=[t.model_dump() for t in a.tests_sichtbar],
                    tests_versteckt=[t.model_dump() for t in a.tests_versteckt],
                    starter_code=a.starter_code,
                    beschreibung_md=a.beschreibung_md,
                    musterloesungen_anzahl=len(ml),
                    dateipfad=str(a.dateipfad),
                    hash=a.hash,
                    statistik=statistik,
                )
            )
        return eintraege

    @router.get("/aufgaben/{aufgabe_id}", response_model=VerwaltungsEintrag)
    def aufgabe_einzeln(aufgabe_id: str) -> VerwaltungsEintrag:
        """Einzelne Verwaltungs-Sicht -- nuetzlich nach Edit, um den
        frischen Zustand zu holen ohne die ganze Liste neu zu fetchen."""
        a = state.aufgaben.aufgabe(aufgabe_id)
        if a is None:
            raise HTTPException(404, f"Aufgabe '{aufgabe_id}' nicht gefunden")
        with state.db.connect() as conn:
            sub_row = conn.execute(
                """
                SELECT COUNT(*) AS gesamt,
                       SUM(CASE WHEN bestanden = 1 THEN 1 ELSE 0 END) AS bestanden
                FROM submissions WHERE aufgabe_id = ?
                """,
                (aufgabe_id,),
            ).fetchone()
            p = conn.execute(
                "SELECT * FROM progress WHERE aufgabe_id = ?", (aufgabe_id,)
            ).fetchone()
        statistik = AufgabenStatistik(
            submissions_gesamt=sub_row["gesamt"] if sub_row else 0,
            bestandene_submissions=(sub_row["bestanden"] or 0) if sub_row else 0,
            versuche=p["versuche"] if p else 0,
            hints_genutzt=p["hints_genutzt"] if p else 0,
            punkte_erreicht=p["punkte_erreicht"] if p else 0,
            status=p["status"] if p else "neu",
        )
        ml = state.loader.lade_musterloesungen(aufgabe_id)
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
            hints=[h.model_dump() for h in a.hints],
            tests_sichtbar=[t.model_dump() for t in a.tests_sichtbar],
            tests_versteckt=[t.model_dump() for t in a.tests_versteckt],
            starter_code=a.starter_code,
            beschreibung_md=a.beschreibung_md,
            musterloesungen_anzahl=len(ml),
            dateipfad=str(a.dateipfad),
            hash=a.hash,
            statistik=statistik,
        )

    @router.post("/aufgaben", response_model=VerwaltungsEintrag, status_code=201)
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
        state.aufgaben.neu_aufbauen()
        return aufgabe_einzeln(daten.frontmatter["id"])

    @router.put("/aufgaben/{aufgabe_id}", response_model=VerwaltungsEintrag)
    def aufgabe_aendern(
        aufgabe_id: str, daten: AufgabeSchreibAnfrage
    ) -> VerwaltungsEintrag:
        if daten.frontmatter.get("id") != aufgabe_id:
            raise HTTPException(
                400,
                "ID im Pfad und im Frontmatter muessen uebereinstimmen",
            )
        if state.aufgaben.aufgabe(aufgabe_id) is None:
            raise HTTPException(404, f"Aufgabe '{aufgabe_id}' nicht gefunden")
        try:
            state.schreiber.schreibe_aufgabe(
                frontmatter=daten.frontmatter,
                beschreibung_md=daten.beschreibung_md,
                sprache=daten.frontmatter.get("sprache", ""),
                existiert_pruefen=False,
            )
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(400, str(exc)) from exc
        state.aufgaben.neu_aufbauen()
        return aufgabe_einzeln(aufgabe_id)

    @router.delete("/aufgaben/{aufgabe_id}", status_code=204)
    def aufgabe_loeschen(aufgabe_id: str) -> None:
        try:
            state.schreiber.loesche_aufgabe(aufgabe_id)
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(404, str(exc)) from exc
        state.aufgaben.neu_aufbauen()

    @router.get(
        "/aufgaben/{aufgabe_id}/musterloesungen",
        response_model=list[MusterloesungEintrag],
    )
    def musterloesungen(aufgabe_id: str) -> list[MusterloesungEintrag]:
        if state.aufgaben.aufgabe(aufgabe_id) is None:
            raise HTTPException(404, f"Aufgabe '{aufgabe_id}' nicht gefunden")
        return [
            MusterloesungEintrag(variante=m["variante"], code=m["code"])
            for m in state.loader.lade_musterloesungen(aufgabe_id)
        ]

    @router.put(
        "/aufgaben/{aufgabe_id}/musterloesungen/{variante}",
        response_model=MusterloesungEintrag,
    )
    def musterloesung_speichern(
        aufgabe_id: str, variante: str, daten: MusterloesungInhalt
    ) -> MusterloesungEintrag:
        try:
            state.schreiber.schreibe_musterloesung(aufgabe_id, variante, daten.code)
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(400, str(exc)) from exc
        state.aufgaben.leere_metriken_cache()
        return MusterloesungEintrag(variante=variante, code=daten.code)

    @router.delete(
        "/aufgaben/{aufgabe_id}/musterloesungen/{variante}", status_code=204
    )
    def musterloesung_loeschen(aufgabe_id: str, variante: str) -> None:
        try:
            state.schreiber.loesche_musterloesung(aufgabe_id, variante)
        except AufgabenSchreiberFehler as exc:
            raise HTTPException(404, str(exc)) from exc
        state.aufgaben.leere_metriken_cache()

    @router.post(
        "/aufgaben/{aufgabe_id}/validieren",
        response_model=ValidierungsErgebnis,
    )
    def aufgabe_validieren(aufgabe_id: str) -> ValidierungsErgebnis:
        """Laesst alle Musterloesungen gegen alle Tests laufen.

        Antwort enthaelt pro Variante: bestanden ja/nein, Anzahl
        sichtbarer + versteckter Pass/Fail. Hilft beim Aufgaben-Bauen,
        um zu sehen, ob die Tests konsistent sind.
        """
        a = state.aufgaben.aufgabe(aufgabe_id)
        if a is None:
            raise HTTPException(404, f"Aufgabe '{aufgabe_id}' nicht gefunden")
        loesungen = state.loader.lade_musterloesungen(aufgabe_id)
        if not loesungen:
            return ValidierungsErgebnis(varianten=[])
        ergebnisse: list[VarianteErgebnis] = []
        for ml in loesungen:
            erg = pruefe(a, ml["code"], state.runner)
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
                        t.fehler for t in erg.sichtbar if t.fehler
                    ) or None,
                )
            )
        return ValidierungsErgebnis(varianten=ergebnisse)

    return router
