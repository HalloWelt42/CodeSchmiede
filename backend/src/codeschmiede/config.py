"""Settings fuer Codeschmiede. Werte aus Umgebungsvariablen oder Defaults."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# backend/src/codeschmiede/config.py -> Projekt-Wurzel ist 4 Ebenen darueber
PROJEKT_WURZEL = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    """Globale Konfiguration. Wird einmalig zur Startzeit gelesen."""

    model_config = SettingsConfigDict(
        env_prefix="CODESCHMIEDE_",
        env_file=".env",
        extra="ignore",
    )

    aufgaben_pfad: Path = PROJEKT_WURZEL / "aufgaben"
    daten_pfad: Path = PROJEKT_WURZEL / "data"
    db_datei: Path = PROJEKT_WURZEL / "data" / "codeschmiede.db"

    sandbox_image: str = "codeschmiede-sandbox:python"

    api_host: str = "127.0.0.1"
    api_port: int = 8200
