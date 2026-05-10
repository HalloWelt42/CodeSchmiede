"""FastAPI-App. Mountet Router und stellt einen Health-Check bereit."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from . import __version__
from .config import Settings
from .routes.aufgaben import baue_aufgaben_router
from .routes.pfade import baue_pfade_router
from .routes.progress import baue_progress_router
from .routes.submissions import baue_submissions_router
from .state import AppState


class HealthAntwort(BaseModel):
    status: str
    version: str
    aufgaben_anzahl: int
    pfade_anzahl: int
    sandbox_image: str


def app_bauen(settings: Settings | None = None) -> FastAPI:
    aktive_settings = settings or Settings()
    state = AppState(aktive_settings)

    app = FastAPI(
        title="Codeschmiede",
        version=__version__,
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
    )

    # Vite-Dev-Server proxied selbst, im Browser direkt aufrufen geht
    # ueber CORS. Im MVP ist die App lokal-only -- CORS bewusst offen.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(baue_aufgaben_router(state))
    app.include_router(baue_pfade_router(state))
    app.include_router(baue_submissions_router(state))
    app.include_router(baue_progress_router(state))

    @app.get("/api/healthz", response_model=HealthAntwort)
    def healthz() -> HealthAntwort:
        return HealthAntwort(
            status="ok",
            version=__version__,
            aufgaben_anzahl=len(state.aufgaben.alle_aufgaben()),
            pfade_anzahl=len(state.aufgaben.alle_pfade()),
            sandbox_image=aktive_settings.sandbox_image,
        )

    return app
