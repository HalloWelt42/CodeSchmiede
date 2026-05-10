"""Runner-Interface (Protocol). Erlaubt spaeter weitere Runner ausser Docker."""

from typing import Protocol

from .result import RunLimits, RunResult


class Runner(Protocol):
    """Abstrakter Runner. Fuehrt Code in einer isolierten Umgebung aus."""

    def run_code(self, code: str, limits: RunLimits | None = None) -> RunResult:
        """Fuehrt `code` aus und liefert das Ergebnis. Keine Exceptions
        für Code-Fehler -- das wandert in `RunResult.stderr` / `exit_code`.
        """
        ...
