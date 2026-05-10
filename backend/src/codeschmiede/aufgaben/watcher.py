"""DateiWatcher -- beobachtet das Aufgaben-Verzeichnis und triggert
einen Repository-Reindex bei Änderungen.

Im Dev-Modus heisst das: neue Aufgabe anlegen oder eine bestehende
editieren, und das Frontend sieht die Änderung beim nächsten Request,
ohne dass das Backend neu gestartet werden muss.
"""

import asyncio
from pathlib import Path

from watchfiles import awatch

from .repository import AufgabenRepository


class AufgabenWatcher:
    def __init__(
        self,
        aufgaben_pfad: Path,
        repository: AufgabenRepository,
        debounce_ms: int = 250,
    ):
        self.aufgaben_pfad = aufgaben_pfad
        self.repository = repository
        self.debounce_ms = debounce_ms

    async def laufe(self) -> None:
        """Endlosschleife. Bricht ab, wenn die Task gecanceled wird."""
        if not self.aufgaben_pfad.exists():
            return
        try:
            async for changes in awatch(
                str(self.aufgaben_pfad), debounce=self.debounce_ms
            ):
                try:
                    self.repository.neu_aufbauen()
                    print(f"[watcher] {len(changes)} Änderung(en), reindexed", flush=True)
                except Exception as e:
                    # Reindex darf den Watcher nicht killen.
                    print(f"[watcher] Reindex-Fehler: {e}", flush=True)
        except asyncio.CancelledError:
            raise
