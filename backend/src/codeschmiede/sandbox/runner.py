"""Runner-Interface (Protocol) und die Fehler, die ein Runner melden darf."""

from typing import Protocol

from .result import RunLimits, RunResult


class SandboxFehler(RuntimeError):
    """Die Sandbox selbst ist nicht nutzbar (nicht erreichbar, abgewiesen,
    unbekannte Sprache). Fehler im Nutzercode sind KEIN SandboxFehler --
    die landen in `RunResult.stderr` / `exit_code`."""


class Runner(Protocol):
    """Führt Code einer Sprache in einer isolierten Umgebung aus."""

    def run_code(
        self, code: str, sprache: str, limits: RunLimits | None = None
    ) -> RunResult:
        ...
