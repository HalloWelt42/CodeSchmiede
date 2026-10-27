"""Loader für die zentrale `_konfig.yml`.

Liest die Datei beim Start und bei Watcher-Reload neu. Falls sie nicht
existiert, wird eine leere Default-Konfiguration zurückgegeben -- die
App läuft dann mit harten Defaults im Frontend (oder leerer Liste).
"""

from pathlib import Path

from ..models.konfig import Konfiguration
from ..yaml_lesen import lies_yaml


KONFIG_DATEINAME = "_konfig.yml"


class KonfigLoader:
    def __init__(self, aufgaben_pfad: Path):
        self.datei = aufgaben_pfad / KONFIG_DATEINAME

    def lade(self) -> Konfiguration:
        if not self.datei.exists():
            return Konfiguration()
        with self.datei.open(encoding="utf-8") as f:
            daten = lies_yaml(f.read()) or {}
        return Konfiguration.model_validate(daten)
