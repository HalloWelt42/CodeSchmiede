"""Entry-Point für den Codeschmiede-Backend-Server.

Aufruf:
    python -m codeschmiede.main
oder als Skript:
    python backend/src/codeschmiede/main.py
"""

import uvicorn

from .api import app_bauen
from .config import Settings


def starte() -> None:
    settings = Settings()
    app = app_bauen(settings)
    uvicorn.run(app, host=settings.api_host, port=settings.api_port)


if __name__ == "__main__":
    starte()
