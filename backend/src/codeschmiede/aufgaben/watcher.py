"""DateiWatcher -- beobachtet das Aufgaben-Verzeichnis und triggert
einen Repository-Reindex plus Konfig-Reload bei Änderungen.

Im Dev-Modus heisst das: neue Aufgabe anlegen oder eine bestehende
editieren, und das Frontend sieht die Änderung beim nächsten Request,
ohne dass das Backend neu gestartet werden muss. Dasselbe gilt für
Änderungen an `_konfig.yml`.
"""

import asyncio
from typing import TYPE_CHECKING

from watchfiles import awatch

if TYPE_CHECKING:
    from ..state import AppState


class AufgabenWatcher:
    def __init__(self, state: "AppState", debounce_ms: int = 250):
        self.state = state
        self.aufgaben_pfad = state.settings.aufgaben_pfad
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
                    self.state.konfig_neu_laden()
                    self.state.aufgaben.neu_aufbauen()
                    print(f"[watcher] {len(changes)} Änderung(en), reindexed", flush=True)
                except Exception as e:
                    # Reindex darf den Watcher nicht killen.
                    print(f"[watcher] Reindex-Fehler: {e}", flush=True)
        except asyncio.CancelledError:
            raise
