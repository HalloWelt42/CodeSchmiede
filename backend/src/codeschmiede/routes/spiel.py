"""HTTP-Routen der Spielmechanik: Spielstand für Kopf und Startseite,
Erfolge für ihre Seite, Spiele mit dem Stand ihrer Levels, Probeläufe des
Roboters, der Ampelschule und der Aufzugsteuerung und die Runden des Ausgabe-Sprints. Die Belohnung einer Abgabe kommt mit der Abgabe."""

from collections.abc import Iterator
from contextlib import contextmanager

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..models.spiel import ErfolgsListe, Spielstand, SpielUebersicht
from ..models.sprint import SprintAbschluss, SprintRueckmeldung, SprintRunde
from ..pruefung import krimi_pruefer
from ..pruefung.krimi_pruefer import Ergebnistabelle
from ..pruefung import ampel_pruefer, aufzug_pruefer
from ..pruefung.ampel_pruefer import AmpelLaeufe, AmpelSterne
from ..pruefung.aufzug_pruefer import AufzugLaeufe, AufzugSterne
from ..pruefung.roboter_pruefer import Laeufe, lauf_sichtbar
from ..steuerung import ampel_welt
from ..steuerung.ampel_anlage import Anlage
from ..sandbox.runner import SandboxFehler
from ..spiel.sprint import FalscheAntwort, RundeNichtGefunden, RundeVorbei
from ..state import AppState


class SprintAntwort(BaseModel):
    frage: int
    wahl: int


class ProgrammProbe(BaseModel):
    code: str = Field(min_length=1, max_length=50_000)


class TeilschrittText(BaseModel):
    titel: str
    text: str


class AmpelAnsicht(BaseModel):
    """Was die Ampelschule vor dem ersten Lauf zeigt: Anlage, Dauer des ersten sichtbaren Ablaufs und vom Level, was
    der Browser braucht (ohne Regeln und versteckte Abläufe)."""

    anlage: Anlage
    ablauf: str
    dauer: int
    # Maße je Art von Teilnehmer (Länge, Breite in Bildpunkten), für die Zeichnung
    arten: dict[str, dict[str, float]]
    sensoren: list[str]
    teilschritte: list[TeilschrittText]
    sterne: AmpelSterne
    aufbauend_auf: str | None


class HausBild(BaseModel):
    etagen: int
    namen: list[str]
    aufzuege: list[str]
    plaetze: int
    last: int


class AufzugAnsicht(BaseModel):
    """Was die Aufzugsteuerung vor dem ersten Lauf zeigt: das Haus und vom Level, was der Browser braucht."""

    haus: HausBild
    ablauf: str
    dauer: int
    sensoren: list[str]
    teilschritte: list[TeilschrittText]
    sterne: AufzugSterne
    aufbauend_auf: str | None


class KrimiAbfrage(BaseModel):
    code: str = Field(min_length=1, max_length=50_000)


class KrimiErgebnis(BaseModel):
    tabelle: Ergebnistabelle | None = None
    fehler: str | None = None
    laufzeit_ms: float = 0


class Notiz(BaseModel):
    kapitel: int
    titel: str
    text: str


def baue_spiel_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/spiel", tags=["spiel"])

    @router.get("/stand", response_model=Spielstand)
    def stand() -> Spielstand:
        return state.spiel.stand(state.bestand())

    @router.get("/erfolge", response_model=ErfolgsListe)
    def erfolge() -> ErfolgsListe:
        return state.spiel.erfolge(state.bestand())

    @router.get("/spiele", response_model=list[SpielUebersicht])
    def spiele() -> list[SpielUebersicht]:
        return state.spiel.spiele(state.bestand())

    @router.post("/roboter/{aufgabe_id}/lauf", response_model=Laeufe)
    def roboter_lauf(aufgabe_id: str, anfrage: ProgrammProbe) -> Laeufe:
        """Probelauf in der sichtbaren Welt, ohne Wertung und ohne Abgabe."""
        aufgabe = state.aufgaben.aufgabe(aufgabe_id)
        if aufgabe is None or aufgabe.task_type != "roboter":
            raise HTTPException(status_code=404, detail="Kein Roboter-Level")
        try:
            return lauf_sichtbar(aufgabe, anfrage.code, state.runner)
        except SandboxFehler as fehler:
            raise HTTPException(status_code=503, detail=str(fehler)) from fehler

    def ampel_level(aufgabe_id: str):
        aufgabe = state.aufgaben.aufgabe(aufgabe_id)
        if aufgabe is None or aufgabe.task_type != "ampel":
            raise HTTPException(status_code=404, detail="Kein Ampel-Level")
        return aufgabe

    @router.get("/ampel/{aufgabe_id}/anlage", response_model=AmpelAnsicht, response_model_exclude={"anlage": {"konflikte"}})
    def ampel_anlage(aufgabe_id: str) -> AmpelAnsicht:
        level = ampel_pruefer.level_von(ampel_level(aufgabe_id))
        return AmpelAnsicht(
            anlage=ampel_pruefer.anlage_von(level),
            ablauf=level.sichtbar[0].name,
            dauer=level.sichtbar[0].dauer,
            arten={art: {"laenge": m["laenge"], "breite": m["breite"]} for art, m in ampel_welt.ARTEN.items()},
            sensoren=list(level.sensoren),
            teilschritte=[TeilschrittText(titel=s.titel, text=s.text) for s in level.teilschritte],
            sterne=level.sterne,
            aufbauend_auf=level.aufbauend_auf,
        )

    @router.post("/ampel/{aufgabe_id}/lauf", response_model=AmpelLaeufe)
    def ampel_lauf(aufgabe_id: str, anfrage: ProgrammProbe) -> AmpelLaeufe:
        """Probelauf in den sichtbaren Abläufen, ohne Wertung und ohne Abgabe."""
        aufgabe = ampel_level(aufgabe_id)
        try:
            return ampel_pruefer.lauf_sichtbar(aufgabe, anfrage.code, state.runner)
        except SandboxFehler as fehler:
            raise HTTPException(status_code=503, detail=str(fehler)) from fehler

    def aufzug_level(aufgabe_id: str):
        aufgabe = state.aufgaben.aufgabe(aufgabe_id)
        if aufgabe is None or aufgabe.task_type != "aufzug":
            raise HTTPException(status_code=404, detail="Kein Aufzug-Level")
        return aufgabe

    @router.get("/aufzug/{aufgabe_id}/haus", response_model=AufzugAnsicht)
    def aufzug_haus(aufgabe_id: str) -> AufzugAnsicht:
        level = aufzug_pruefer.level_von(aufzug_level(aufgabe_id))
        welt = level.haus.fuer_welt()
        return AufzugAnsicht(
            haus=HausBild(etagen=level.haus.etagen, namen=level.haus.namen(), aufzuege=level.haus.aufzuege,
                          plaetze=level.haus.plaetze, last=welt["last"]),
            ablauf=level.sichtbar[0].name,
            dauer=level.sichtbar[0].dauer,
            sensoren=list(level.sensoren),
            teilschritte=[TeilschrittText(titel=s.titel, text=s.text) for s in level.teilschritte],
            sterne=level.sterne,
            aufbauend_auf=level.aufbauend_auf,
        )

    @router.post("/aufzug/{aufgabe_id}/lauf", response_model=AufzugLaeufe)
    def aufzug_lauf(aufgabe_id: str, anfrage: ProgrammProbe) -> AufzugLaeufe:
        """Probelauf in den sichtbaren Abläufen, ohne Wertung und ohne Abgabe."""
        aufgabe = aufzug_level(aufgabe_id)
        try:
            return aufzug_pruefer.lauf_sichtbar(aufgabe, anfrage.code, state.runner)
        except SandboxFehler as fehler:
            raise HTTPException(status_code=503, detail=str(fehler)) from fehler

    def krimi_kapitel(aufgabe_id: str):
        aufgabe = state.aufgaben.aufgabe(aufgabe_id)
        if aufgabe is None or aufgabe.task_type != "sql_krimi":
            raise HTTPException(status_code=404, detail="Kein Krimi-Kapitel")
        return aufgabe

    @router.post("/krimi/{aufgabe_id}/ausfuehren", response_model=KrimiErgebnis)
    def krimi_ausfuehren(aufgabe_id: str, anfrage: KrimiAbfrage) -> KrimiErgebnis:
        """Führt die Abfrage nur auf der Tatort-Datenbank aus; zählt nicht als Versuch."""
        aufgabe = krimi_kapitel(aufgabe_id)
        level = krimi_pruefer.level_von(aufgabe)
        try:
            tabellen, stderr, laufzeit, _ = krimi_pruefer.ausfuehren(aufgabe, [(level.dataset, anfrage.code)], state.runner)
        except SandboxFehler as fehler:
            raise HTTPException(status_code=503, detail=str(fehler)) from fehler
        if tabellen is None:
            return KrimiErgebnis(fehler=stderr, laufzeit_ms=laufzeit)
        return KrimiErgebnis(tabelle=tabellen[0], fehler=tabellen[0].fehler, laufzeit_ms=laufzeit)

    @router.get("/krimi/{aufgabe_id}/pinnwand", response_model=list[Notiz])
    def krimi_pinnwand(aufgabe_id: str) -> list[Notiz]:
        """Notizen der gelösten Kapitel desselben Falls, in der Reihenfolge des Falls."""
        krimi_kapitel(aufgabe_id)
        geloest = {p.aufgabe_id for p in state.progress.hole_alle_progress() if p.status == "geloest"}
        notizen = []
        for pfad_id in state.aufgaben.pfade_von(aufgabe_id):
            pfad = state.aufgaben.pfad(pfad_id)
            for aid in pfad.reihenfolge if pfad else []:
                kapitel = state.aufgaben.aufgabe(aid)
                if kapitel is None or kapitel.task_type != "sql_krimi" or aid not in geloest:
                    continue
                level = krimi_pruefer.level_von(kapitel)
                notizen.append(Notiz(kapitel=level.kapitel, titel=kapitel.titel, text=level.notiz))
        return notizen

    @router.post("/sprint/{aufgabe_id}/runde", response_model=SprintRunde)
    def sprint_runde(aufgabe_id: str) -> SprintRunde:
        aufgabe = state.aufgaben.aufgabe(aufgabe_id)
        if aufgabe is None or aufgabe.task_type != "ausgabe_sprint":
            raise HTTPException(status_code=404, detail="Kein Sprint-Level")
        return state.sprint.neue_runde(aufgabe)

    @router.post("/sprint/runde/{runde_id}/antwort", response_model=SprintRueckmeldung)
    def sprint_antwort(runde_id: str, anfrage: SprintAntwort) -> SprintRueckmeldung:
        with sprint_fehler():
            return state.sprint.antworte(runde_id, anfrage.frage, anfrage.wahl, state.bestand())

    @router.post("/sprint/runde/{runde_id}/abschluss", response_model=SprintAbschluss)
    def sprint_abschluss(runde_id: str) -> SprintAbschluss:
        with sprint_fehler():
            return state.sprint.abschliessen(runde_id, state.bestand())

    return router


@contextmanager
def sprint_fehler() -> Iterator[None]:
    """Fehler der Runde als HTTP-Antwort: unbekannt 404, vorbei 409, unpassend 422."""
    try:
        yield
    except RundeNichtGefunden as fehler:
        raise HTTPException(status_code=404, detail=str(fehler)) from fehler
    except RundeVorbei as fehler:
        raise HTTPException(status_code=409, detail=str(fehler)) from fehler
    except FalscheAntwort as fehler:
        raise HTTPException(status_code=422, detail=str(fehler)) from fehler
