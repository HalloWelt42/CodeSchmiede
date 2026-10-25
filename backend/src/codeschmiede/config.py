"""Settings für Codeschmiede. Werte aus Umgebungsvariablen oder Defaults."""

from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# backend/src/codeschmiede/config.py -> Projekt-Wurzel ist 4 Ebenen darüber
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
    # Dürfen Verwaltung und Editor Aufgabendateien schreiben? Auf dem Pi
    # nein: dort kommen die Aufgaben aus dem Repo (Bearbeiten am Mac).
    aufgaben_schreibbar: bool = True
    # Aufgabenordner beobachten und Änderungen sofort einlesen (Entwicklung).
    # Ohne Nutzen, wenn die Aufgaben mit dem Ausrollen kommen; das Einrichten
    # dauert auf eingehängten Ordnern lange.
    aufgaben_beobachten: bool = True

    # Sandbox-Dienst (einziger Teil mit Docker-Zugang). Ohne gesetzten
    # Schlüssel teilen sich Backend und Dienst eine Schlüsseldatei
    # (Vorgabe `<daten_pfad>/sandbox-schluessel`).
    sandbox_url: str = "http://127.0.0.1:8203"
    sandbox_schluessel: SecretStr = SecretStr("")
    sandbox_schluessel_datei: Path | None = None

    # Fremde Herkünfte, die die API aus dem Browser nutzen dürfen. Leer:
    # nur die eigene Herkunft (Oberfläche und API unter derselben Adresse).
    erlaubte_herkuenfte: list[str] = []

    # Anmeldung mit dem Kellerwolke-Konto. Aus nur für Tests und eine
    # Entwicklung ohne Kellerwolke; im Betrieb immer an.
    anmeldung_pflicht: bool = True
    # Vorgabe für die Einrichtung; gespeichert wird, was dort eingetragen wird.
    kellerwolke_adresse: str = ""
    # Zusätzliche Zertifikatsstelle für HTTPS im Heimnetz (Hausstelle).
    # Leer: die mkcert-Stelle dieses Rechners, wenn es eine gibt.
    ca_datei: Path | None = None

    # Nächtliche Sicherung der Datenbank in diesen Ordner (Betrieb).
    # Leer: keine; vor jedem Ausrollen sichert zusätzlich das Ausrollen.
    sicherungen_pfad: Path | None = None
    sicherung_stunde: int = 3
    sicherungen_behalten: int = 14

    # Gebaute Oberfläche, die das Backend selbst ausliefert (Betrieb).
    # Leer: keine; in der Entwicklung liefert Vite die Oberfläche.
    oberflaeche_pfad: Path | None = None

    api_host: str = "127.0.0.1"
    api_port: int = 8200
