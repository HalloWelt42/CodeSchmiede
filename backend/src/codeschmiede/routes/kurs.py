"""HTTP-Routen des Aufbaukurses: Übersicht, Einführung, Antworten, Beispiele, Kurztest, Merkblatt, Bilder."""

from collections.abc import Iterator
from contextlib import contextmanager

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from ..kurs.aufzeichnung import Aufzeichnung
from ..kurs.dienst import NichtErlaubt, NichtGefunden
from ..kurs.sicht import (Antwort, AusfuehrenAnfrage, EinfuehrungSicht, KursSicht, KurztestSicht, MerkblattSicht,
                          Urteil)
from ..sandbox.runner import SandboxFehler
from ..state import AppState


@contextmanager
def _fehler() -> Iterator[None]:
    try:
        yield
    except NichtGefunden as f:
        raise HTTPException(status_code=404, detail=str(f)) from f
    except NichtErlaubt as f:
        raise HTTPException(status_code=409, detail=str(f)) from f
    except SandboxFehler as f:
        raise HTTPException(status_code=503, detail=str(f)) from f


def baue_kurs_router(state: AppState) -> APIRouter:
    router = APIRouter(prefix="/api/kurs", tags=["kurs"])

    def aufgaben():
        return {a.id: a for a in state.aufgaben.alle_aufgaben()}

    def geloest() -> set[str]:
        return {p.aufgabe_id for p in state.progress.hole_alle_progress() if p.status == "geloest"}

    def offen(eid: str) -> None:
        state.kurs.pruefe_offen(eid, aufgaben(), geloest())

    @router.get("", response_model=list[KursSicht])
    def uebersicht() -> list[KursSicht]:
        return state.kurs.uebersicht(aufgaben(), geloest())

    @router.get("/einfuehrung/{eid}", response_model=EinfuehrungSicht)
    def einfuehrung(eid: str) -> EinfuehrungSicht:
        with _fehler():
            offen(eid)
            return state.kurs.einfuehrung(eid)

    @router.post("/einfuehrung/{eid}/antwort", response_model=Urteil)
    def antwort(eid: str, a: Antwort) -> Urteil:
        with _fehler():
            offen(eid)
            return state.kurs.antworten(eid, a)

    @router.post("/einfuehrung/{eid}/abschnitt/{nummer}/fertig", response_model=EinfuehrungSicht)
    def abschnitt_fertig(eid: str, nummer: int) -> EinfuehrungSicht:
        with _fehler():
            offen(eid)
            state.kurs.abschnitt_fertig(eid, nummer)
            return state.kurs.einfuehrung(eid)

    @router.post("/einfuehrung/{eid}/beispiel/{bid}/ausfuehren", response_model=Aufzeichnung)
    def ausfuehren(eid: str, bid: str, anfrage: AusfuehrenAnfrage) -> Aufzeichnung:
        with _fehler():
            offen(eid)
            return state.kurs.ausfuehren(eid, bid, anfrage.code)

    @router.get("/kurztest/{eid}", response_model=KurztestSicht)
    def kurztest(eid: str) -> KurztestSicht:
        with _fehler():
            g = geloest()
            state.kurs.kurztest_abschliessen(eid, g)
            return state.kurs.kurztest(eid, aufgaben(), g)

    @router.post("/kurztest/{eid}/antwort", response_model=Urteil)
    def kurztest_antwort(eid: str, a: Antwort) -> Urteil:
        with _fehler():
            return state.kurs.kurztest_antworten(eid, a, geloest())

    @router.get("/merkblatt/{eid}", response_model=MerkblattSicht)
    def merkblatt(eid: str) -> MerkblattSicht:
        with _fehler():
            return state.kurs.merkblatt(eid)

    @router.get("/bilder/{schluessel}.webp")
    def bild(schluessel: str) -> FileResponse:
        datei = state.kurs.bilddatei(schluessel)
        if datei is None:
            raise HTTPException(status_code=404, detail="Bild gibt es nicht")
        return FileResponse(datei, media_type="image/webp", headers={"Cache-Control": "public, max-age=86400"})

    @router.get("/zeichnungen/{eid}/{name}.svg")
    def zeichnung(eid: str, name: str) -> FileResponse:
        datei = state.kurs.zeichnungsdatei(eid, name)
        if datei is None:
            raise HTTPException(status_code=404, detail="Zeichnung gibt es nicht")
        return FileResponse(datei, media_type="image/svg+xml", headers={"Cache-Control": "public, max-age=3600"})

    @router.get("/diagramme/{pruefsumme}.svg")
    def diagramm(pruefsumme: str) -> FileResponse:
        datei = state.kurs.diagrammdatei(pruefsumme)
        if datei is None:
            raise HTTPException(status_code=404, detail="Diagramm gibt es nicht")
        return FileResponse(datei, media_type="image/svg+xml", headers={"Cache-Control": "public, max-age=86400"})

    return router
