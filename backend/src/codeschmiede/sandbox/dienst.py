"""Sandbox-Dienst -- der einzige Teil der Codeschmiede mit Docker-Zugang.

Nimmt Läufe vom Backend entgegen (nur mit gemeinsamem Schlüssel), führt
sie über den DockerRunner aus und liefert das Ergebnis. Er kennt nur
die eingetragenen Sprach-Images und die festen Härtungen; beliebige
Docker-Befehle gibt es nicht. Wie viele Läufe gleichzeitig laufen
dürfen, ist einstellbar (auf dem Pi klein halten).

Aufruf:
    python -m codeschmiede.sandbox.dienst
"""

import secrets
import threading
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from ..config import PROJEKT_WURZEL
from .docker_runner import DockerRunner
from .result import RunLimits, RunResult
from .runner import SandboxFehler
from .schluessel import lade_schluessel

SCHLUESSEL_HEADER = "X-Sandbox-Schluessel"


class DienstEinstellungen(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CODESCHMIEDE_SANDBOX_", env_file=".env", extra="ignore"
    )

    host: str = "127.0.0.1"
    port: int = 8203
    daten_pfad: Path = PROJEKT_WURZEL / "data"
    schluessel: SecretStr = SecretStr("")
    # Gemeinsame Schlüsseldatei mit dem Backend (Vorgabe `<daten_pfad>/sandbox-schluessel`).
    schluessel_datei: Path | None = None
    bilder: dict[str, str] = {
        "python": "codeschmiede-sandbox:python",
        "javascript": "codeschmiede-sandbox:javascript",
    }
    max_parallel: int = Field(default=2, ge=1, le=16)
    # Wie lange ein Lauf auf einen freien Platz wartet, bevor er abgewiesen wird.
    warte_sekunden: float = Field(default=30, gt=0)
    max_ausgabe_bytes: int = Field(default=1_000_000, ge=10_000)
    # Reserve für den Containerstart über die Laufzeitgrenze hinaus.
    startzeit_sekunden: float = Field(default=20, gt=0)


class LaufAnfrage(BaseModel):
    code: str = Field(max_length=200_000)
    sprache: str
    limits: RunLimits = Field(default_factory=RunLimits)


class Gesundheit(BaseModel):
    status: str
    sprachen: list[str]
    max_parallel: int


def dienst_bauen(
    einstellungen: DienstEinstellungen | None = None,
    runner: DockerRunner | None = None,
) -> FastAPI:
    e = einstellungen or DienstEinstellungen()
    schluessel = lade_schluessel(
        e.schluessel, e.schluessel_datei or e.daten_pfad / "sandbox-schluessel"
    )
    runner = runner or DockerRunner(
        e.bilder, max_ausgabe_bytes=e.max_ausgabe_bytes, startzeit_sekunden=e.startzeit_sekunden
    )
    plaetze = threading.BoundedSemaphore(e.max_parallel)

    app = FastAPI(title="Codeschmiede Sandbox", docs_url=None, openapi_url=None)

    def pruefe_schluessel(wert: str | None) -> None:
        if not wert or not secrets.compare_digest(wert, schluessel):
            raise HTTPException(status_code=401, detail="Schlüssel fehlt oder stimmt nicht")

    @app.get("/gesund", response_model=Gesundheit)
    def gesund() -> Gesundheit:
        return Gesundheit(status="ok", sprachen=runner.sprachen, max_parallel=e.max_parallel)

    @app.post("/laeufe", response_model=RunResult)
    def lauf(
        anfrage: LaufAnfrage,
        x_sandbox_schluessel: str | None = Header(default=None),
    ) -> RunResult:
        pruefe_schluessel(x_sandbox_schluessel)
        if not plaetze.acquire(timeout=e.warte_sekunden):
            raise HTTPException(status_code=503, detail="Alle Sandbox-Plätze sind belegt")
        try:
            return runner.run_code(anfrage.code, anfrage.sprache, anfrage.limits)
        except SandboxFehler as fehler:
            raise HTTPException(status_code=400, detail=str(fehler)) from fehler
        finally:
            plaetze.release()

    return app


def starte() -> None:
    e = DienstEinstellungen()
    uvicorn.run(dienst_bauen(e), host=e.host, port=e.port)


if __name__ == "__main__":
    starte()
