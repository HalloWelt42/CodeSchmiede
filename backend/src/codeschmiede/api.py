"""FastAPI-App. Mountet Router und stellt einen Health-Check bereit.

Schutz gegen fremde Webseiten im selben Browser:
- CORS nur für ausdrücklich erlaubte Herkünfte (Vorgabe: keine, die
  Oberfläche läuft unter derselben Adresse wie die API).
- Ändernde Anfragen (alles außer GET/HEAD/OPTIONS) aus fremder Herkunft
  werden abgewiesen. Maßgeblich ist `Sec-Fetch-Site` des Browsers, ohne
  diesen Kopf die `Origin` gegen den eigenen Host. Anfragen ohne beides
  kommen nicht aus einem Browser (Skripte, Tests) und sind erlaubt.

Anmeldung: alle Endpunkte außer Gesundheit, App-Angaben, Einrichtung und
Anmeldung selbst verlangen ein Kellerwolke-Konto, das die App nutzen darf
(zugang/). Im Betrieb liefert das Backend auch die gebaute Oberfläche aus.
"""

import asyncio
from contextlib import asynccontextmanager
from urllib.parse import urlsplit

import httpx
from appkern.anmeldung.api import angemeldet, anmeldungs_router
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from . import _finde_version
from .aufgaben.watcher import AufgabenWatcher
from .config import Settings
from .oberflaeche import fassung_der_oberflaeche, oberflaeche_einhaengen
from .sicherung import nachts_sichern
from .routes.admin import baue_admin_router
from .routes.aufgaben import baue_aufgaben_router
from .routes.pfade import baue_pfade_router
from .routes.progress import baue_progress_router
from .routes.sql_dataset import baue_sql_dataset_router
from .routes.submissions import baue_submissions_router
from .routes.zugang import baue_zugangs_router
from .sandbox.runner import Runner
from .state import AppState
from .zugang import Zugang

SICHERE_METHODEN = {"GET", "HEAD", "OPTIONS"}
FREMD = {"cross-site", "same-site"}


class HealthAntwort(BaseModel):
    status: str
    version: str
    aufgaben_anzahl: int
    pfade_anzahl: int
    befunde_anzahl: int
    aufgaben_schreibbar: bool


def herkunft_erlaubt(request: Request, erlaubte: set[str]) -> bool:
    origin = request.headers.get("origin")
    if origin and origin in erlaubte:
        return True
    fetch_site = request.headers.get("sec-fetch-site")
    if fetch_site is not None:
        return fetch_site not in FREMD
    if origin:
        return urlsplit(origin).netloc == request.headers.get("host", "")
    return True


def app_bauen(
    settings: Settings | None = None,
    runner: Runner | None = None,
    kellerwolke_transport: httpx.AsyncBaseTransport | None = None,
) -> FastAPI:
    aktive_settings = settings or Settings()
    state = AppState(aktive_settings, runner=runner)
    zugang = Zugang(aktive_settings, state.db, transport=kellerwolke_transport)
    watcher = AufgabenWatcher(state)
    erlaubte = set(aktive_settings.erlaubte_herkuenfte)
    oberflaeche = aktive_settings.oberflaeche_pfad
    # ändernde Anfragen in Arbeit (Prüfungen, Probeläufe): das Ausrollen wartet darauf
    laufend = 0

    @asynccontextmanager
    async def lifespan(_app: FastAPI):
        await zugang.starten()
        aufgaben = []
        if aktive_settings.aufgaben_beobachten:
            aufgaben.append(asyncio.create_task(watcher.laufe()))
        if aktive_settings.sicherungen_pfad is not None:
            aufgaben.append(asyncio.create_task(nachts_sichern(
                aktive_settings.db_datei, aktive_settings.sicherungen_pfad,
                aktive_settings.sicherung_stunde, aktive_settings.sicherungen_behalten,
            )))
        try:
            yield
        finally:
            for aufgabe in aufgaben:
                aufgabe.cancel()
            await asyncio.gather(*aufgaben, return_exceptions=True)
            await zugang.schliessen()

    app = FastAPI(
        title="Codeschmiede",
        version=_finde_version(),
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        lifespan=lifespan,
    )
    app.state.codeschmiede = state
    app.state.zugang = zugang

    @app.middleware("http")
    async def herkunft_pruefen(request: Request, call_next):
        nonlocal laufend
        if request.method in SICHERE_METHODEN:
            return await call_next(request)
        if not herkunft_erlaubt(request, erlaubte):
            return JSONResponse(
                status_code=403, content={"detail": "Anfrage aus fremder Herkunft abgewiesen"}
            )
        laufend += 1
        try:
            return await call_next(request)
        finally:
            laufend -= 1

    if erlaubte:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=sorted(erlaubte),
            allow_credentials=False,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["X-Total-Count"],
        )

    schutz = [Depends(angemeldet(zugang.anmeldung))] if aktive_settings.anmeldung_pflicht else []
    app.include_router(baue_aufgaben_router(state), dependencies=schutz)
    app.include_router(baue_pfade_router(state), dependencies=schutz)
    app.include_router(baue_submissions_router(state), dependencies=schutz)
    app.include_router(baue_sql_dataset_router(state), dependencies=schutz)
    app.include_router(baue_progress_router(state), dependencies=schutz)
    app.include_router(baue_admin_router(state), dependencies=schutz)
    app.include_router(anmeldungs_router(zugang.anmeldung))
    app.include_router(baue_zugangs_router(
        zugang,
        anmeldung_pflicht=aktive_settings.anmeldung_pflicht,
        oberflaeche=lambda: fassung_der_oberflaeche(oberflaeche),
        laufend=lambda: laufend,
    ))

    @app.get("/api/healthz", response_model=HealthAntwort)
    def healthz() -> HealthAntwort:
        # Version je Aufruf frisch aus der VERSION-Datei, sonst zeigt der
        # Endpunkt nach einem Sprung bis zum Neustart die alte Zahl.
        return HealthAntwort(
            status="ok",
            version=_finde_version(),
            aufgaben_anzahl=len(state.aufgaben.alle_aufgaben()),
            pfade_anzahl=len(state.aufgaben.alle_pfade()),
            befunde_anzahl=len(state.befunde),
            aufgaben_schreibbar=aktive_settings.aufgaben_schreibbar,
        )

    # zuletzt: fängt alle übrigen Orte für die Oberfläche
    if oberflaeche is not None and (oberflaeche / "index.html").is_file():
        oberflaeche_einhaengen(app, oberflaeche)

    return app
