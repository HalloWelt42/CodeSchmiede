"""FastAPI-App. Mountet Router und stellt einen Health-Check bereit.

Schutz gegen fremde Webseiten im selben Browser:
- CORS nur für ausdrücklich erlaubte Herkünfte (Vorgabe: keine, die
  Oberfläche läuft unter derselben Adresse wie die API).
- Ändernde Anfragen (alles außer GET/HEAD/OPTIONS) aus fremder Herkunft
  werden abgewiesen. Maßgeblich ist `Sec-Fetch-Site` des Browsers, ohne
  diesen Kopf die `Origin` gegen den eigenen Host. Anfragen ohne beides
  kommen nicht aus einem Browser (Skripte, Tests) und sind erlaubt.
"""

import asyncio
from contextlib import asynccontextmanager
from urllib.parse import urlsplit

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from . import _finde_version
from .aufgaben.watcher import AufgabenWatcher
from .config import Settings
from .routes.admin import baue_admin_router
from .routes.aufgaben import baue_aufgaben_router
from .routes.pfade import baue_pfade_router
from .routes.progress import baue_progress_router
from .routes.sql_dataset import baue_sql_dataset_router
from .routes.submissions import baue_submissions_router
from .sandbox.runner import Runner
from .state import AppState

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


def app_bauen(settings: Settings | None = None, runner: Runner | None = None) -> FastAPI:
    aktive_settings = settings or Settings()
    state = AppState(aktive_settings, runner=runner)
    watcher = AufgabenWatcher(state)
    erlaubte = set(aktive_settings.erlaubte_herkuenfte)

    @asynccontextmanager
    async def lifespan(_app: FastAPI):
        if not aktive_settings.aufgaben_beobachten:
            yield
            return
        task = asyncio.create_task(watcher.laufe())
        try:
            yield
        finally:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

    app = FastAPI(
        title="Codeschmiede",
        version=_finde_version(),
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        lifespan=lifespan,
    )
    app.state.codeschmiede = state

    @app.middleware("http")
    async def herkunft_pruefen(request: Request, call_next):
        if request.method not in SICHERE_METHODEN and not herkunft_erlaubt(request, erlaubte):
            return JSONResponse(
                status_code=403, content={"detail": "Anfrage aus fremder Herkunft abgewiesen"}
            )
        return await call_next(request)

    if erlaubte:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=sorted(erlaubte),
            allow_credentials=False,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["X-Total-Count"],
        )

    app.include_router(baue_aufgaben_router(state))
    app.include_router(baue_pfade_router(state))
    app.include_router(baue_submissions_router(state))
    app.include_router(baue_sql_dataset_router(state))
    app.include_router(baue_progress_router(state))
    app.include_router(baue_admin_router(state))

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

    return app
