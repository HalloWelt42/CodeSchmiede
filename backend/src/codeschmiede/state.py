"""Globaler Anwendungs-Zustand. Bundle aus Settings, DB, Repositories, Runner.

Wird beim App-Start einmal initialisiert und in die Router injiziert.
Kapselt die Lebensdauer-Abhängigkeiten: erst DB-Migration, dann Index-
Aufbau aus dem Aufgaben-Verzeichnis, dann ist alles bereit.
"""

from .aufgaben.bestandspruefung import Befund, pruefe_bestand
from .aufgaben.konfig_loader import KonfigLoader
from .aufgaben.loader import AufgabenLoader
from .aufgaben.repository import AufgabenRepository
from .aufgaben.schreiber import AufgabenSchreiber
from .config import Settings
from .kurs.dienst import Kursdienst
from .kurs.fortschritt import KursfortschrittRepository
from .db.connection import Datenbank
from .models.konfig import Konfiguration
from .progress.repository import ProgressRepository
from .progress.submissions import SubmissionRepository
from .pruefung import orchestrator  # noqa: F401  füllt die Pruefer-Registry
from .sandbox.dienst_runner import DienstRunner
from .sandbox.runner import Runner
from .sandbox.schluessel import lade_schluessel
from .spiel.bestand import Bestand
from .spiel.dienst import Spieldienst
from .spiel.gutschriften import GutschriftRepository
from .spiel.sprint import SprintDienst
from .spiel.sprint_runden import SprintRundenRepository


class AppState:
    def __init__(self, settings: Settings, runner: Runner | None = None):
        self.settings = settings

        self.db = Datenbank(settings.db_datei)
        self.db.migriere()

        self.konfig_loader = KonfigLoader(settings.aufgaben_pfad)
        self.konfig: Konfiguration = Konfiguration()
        self.loader = AufgabenLoader(settings.aufgaben_pfad)
        self.aufgaben = AufgabenRepository(self.db, self.loader)
        self.befunde: list[Befund] = []
        self.kurs = Kursdienst(settings.kurs_pfad, KursfortschrittRepository(self.db), lambda: self.runner)
        self.neu_einlesen()

        self.schreiber = AufgabenSchreiber(settings.aufgaben_pfad, self.loader)
        self.progress = ProgressRepository(self.db)
        self.submissions = SubmissionRepository(self.db)
        self.gutschriften = GutschriftRepository(self.db)
        self.spiel = Spieldienst(self.progress, self.submissions, self.gutschriften, self.aufgaben,
                                 kurs=lambda geloest: self.kurs.beitrag({a.id: a for a in self.aufgaben.alle_aufgaben()}, geloest))
        self.sprint = SprintDienst(SprintRundenRepository(self.db), self.spiel)

        self.runner: Runner = runner or DienstRunner(
            settings.sandbox_url,
            lade_schluessel(
                settings.sandbox_schluessel,
                settings.sandbox_schluessel_datei or settings.daten_pfad / "sandbox-schluessel",
            ),
        )

    def bestand(self) -> Bestand:
        return Bestand.aus(self.aufgaben.alle_aufgaben(), self.aufgaben.alle_pfade(), self.konfig)

    def neu_einlesen(self) -> None:
        """Konfiguration, Aufgaben und Pfade neu lesen und den Bestand prüfen.
        Beim Start und vom Watcher bei jeder Änderung im Aufgabenordner."""
        self.konfig = self.konfig_loader.lade()
        self.aufgaben.neu_aufbauen()
        self.befunde = pruefe_bestand(
            self.aufgaben.alle_aufgaben(),
            self.aufgaben.alle_pfade(),
            self.loader.ladefehler,
            self.konfig,
        )
        self.kurs.neu_einlesen({a.id: a for a in self.aufgaben.alle_aufgaben()}, self.loader.lade_musterloesungen)
        self.befunde += self.kurs.befunde
