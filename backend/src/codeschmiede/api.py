"""FastAPI-App. Mountet Router und stellt einen Health-Check bereit.

Im Tag-1-Stand bietet die App nur `GET /api/healthz`. Spaetere Router
fuer Aufgaben, Submissions, Pfade und Progress werden hier eingehaengt.
"""

from fastapi import FastAPI

from . import __version__
from .config import Settings


def app_bauen(settings: Settings | None = None) -> FastAPI:
    """Baut die FastAPI-App mit der gegebenen Konfiguration."""
    aktive_settings = settings or Settings()

    app = FastAPI(
        title="Codeschmiede",
        version=__version__,
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
    )

    @app.get("/api/healthz")
    def healthz() -> dict[str, str]:
        return {
            "status": "ok",
            "version": __version__,
            "aufgaben_pfad": str(aktive_settings.aufgaben_pfad),
            "sandbox_image": aktive_settings.sandbox_image,
        }

    return app
