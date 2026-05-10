"""Globaler Anwendungs-Zustand. Bundle aus Settings, DB, Repositories, Runner.

Wird beim App-Start einmal initialisiert und in die Router injiziert.
Kapselt die Lebensdauer-Abhaengigkeiten: erst DB-Migration, dann Index-
Aufbau aus dem Aufgaben-Verzeichnis, dann ist alles bereit.
"""

from .aufgaben.loader import AufgabenLoader
from .aufgaben.repository import AufgabenRepository
from .config import Settings
from .db.connection import Datenbank
from .sandbox.docker_runner import DockerRunner


class AppState:
    def __init__(self, settings: Settings):
        self.settings = settings

        self.db = Datenbank(settings.db_datei)
        self.db.migriere()

        self.loader = AufgabenLoader(settings.aufgaben_pfad)
        self.aufgaben = AufgabenRepository(self.db, self.loader)
        self.aufgaben.neu_aufbauen()

        self.runner = DockerRunner()
