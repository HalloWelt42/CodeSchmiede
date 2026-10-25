"""Öffentliche Angaben der App und die erste Einrichtung (ohne Anmeldung erreichbar).

`/api/v1/app` folgt dem Vertrag der Apps im Verbund: Fassung von Server und gebauter Oberfläche, Appkern, laufende
Arbeit (das Ausrollen wartet, bis nichts mehr läuft) und ob die Einrichtung nötig ist. Den Einrichtungscode nennt sie
nie, nur den Ort der Datei.
"""

from collections.abc import Callable

import appkern
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

from .. import _finde_version
from ..zugang.dienst import EinrichtungAbgelehnt, Zugang

LOKAL = {"127.0.0.1", "::1", "localhost"}


class AppInfo(BaseModel):
    name: str = "Codeschmiede"
    kennung: str = "codeschmiede"
    fassung: str
    oberflaeche: str | None
    appkern: str
    auftraege_laufend: int
    anmeldung_pflicht: bool
    einrichtung_noetig: bool
    # solange die Einrichtung nötig ist: wo der Code liegt (nie der Code)
    einrichtungscode: str | None = None
    kellerwolke: str
    app_name: str | None = None
    besitzer: str | None = None


class Einrichtung(BaseModel):
    kellerwolke_adresse: str = Field(min_length=8, max_length=300)
    kellerwolke_schluessel: str = Field(min_length=8, max_length=300)
    einrichtungscode: str = Field("", max_length=64)


def baue_zugangs_router(zugang: Zugang, *, anmeldung_pflicht: bool, oberflaeche: Callable[[], str | None],
                        laufend: Callable[[], int]) -> APIRouter:
    router = APIRouter(prefix="/api/v1", tags=["zugang"])

    def info() -> AppInfo:
        noetig = zugang.einrichtung_noetig
        return AppInfo(
            fassung=_finde_version(),
            oberflaeche=oberflaeche(),
            appkern=appkern.__version__,
            auftraege_laufend=laufend(),
            anmeldung_pflicht=anmeldung_pflicht,
            einrichtung_noetig=noetig,
            einrichtungscode=zugang.einrichtungscode.ort if noetig and zugang.einrichtungscode.aktiv else None,
            kellerwolke=zugang.daten.kellerwolke_adresse,
            app_name=zugang.app_name,
            besitzer=zugang.besitzer,
        )

    @router.get("/app", response_model=AppInfo)
    def app_info() -> AppInfo:
        return info()

    @router.post("/einrichtung", response_model=AppInfo)
    async def einrichten(eingabe: Einrichtung, request: Request) -> AppInfo:
        # Hinter dem Vorschaltdienst sieht jede Anfrage fremd aus; dort gilt immer der Code
        lokal = (request.client.host if request.client else "") in LOKAL and "x-forwarded-for" not in request.headers
        try:
            await zugang.einrichten(eingabe.kellerwolke_adresse, eingabe.kellerwolke_schluessel,
                                    eingabe.einrichtungscode, lokal)
        except EinrichtungAbgelehnt as f:
            raise HTTPException(status_code=f.status, detail=f.meldung)
        return info()

    return router
