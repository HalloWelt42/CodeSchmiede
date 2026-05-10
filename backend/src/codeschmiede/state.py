"""Globaler Anwendungs-Zustand. Bundle aus Settings, DB, Repositories, Runner.

Wird beim App-Start einmal initialisiert und in die Router injiziert.
Kapselt die Lebensdauer-Abhängigkeiten: erst DB-Migration, dann Index-
Aufbau aus dem Aufgaben-Verzeichnis, dann ist alles bereit.
"""

from .aufgaben.konfig_loader import KonfigLoader
from .aufgaben.loader import AufgabenLoader
from .aufgaben.repository import AufgabenRepository
from .config import Settings
from .db.connection import Datenbank
from .models.konfig import Konfiguration
from .progress.repository import ProgressRepository
from .sandbox.docker_runner import DockerRunner


class AppState:
    def __init__(self, settings: Settings):
        self.settings = settings

        self.db = Datenbank(settings.db_datei)
        self.db.migriere()

        self.konfig_loader = KonfigLoader(settings.aufgaben_pfad)
        self.konfig: Konfiguration = self.konfig_loader.lade()

        self.loader = AufgabenLoader(settings.aufgaben_pfad)
        self.aufgaben = AufgabenRepository(self.db, self.loader)
        self.aufgaben.neu_aufbauen()

        self.progress = ProgressRepository(self.db)

        self.runner = DockerRunner()

    def konfig_neu_laden(self) -> None:
        """Wird vom Watcher aufgerufen, wenn `_konfig.yml` sich aendert."""
        self.konfig = self.konfig_loader.lade()
