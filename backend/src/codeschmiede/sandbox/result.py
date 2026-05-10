"""Datenmodelle fuer den Sandbox-Lauf -- Eingabe-Limits und Ausgabe-Ergebnis."""

from pydantic import BaseModel, Field


class RunLimits(BaseModel):
    """Ressourcen-Grenzen fuer einen einzelnen Sandbox-Lauf."""

    timeout_sekunden: int = Field(default=5, ge=1, le=60)
    memory_mb: int = Field(default=128, ge=32, le=1024)
    cpus: float = Field(default=0.5, gt=0.0, le=2.0)


class RunResult(BaseModel):
    """Ergebnis eines Sandbox-Laufs. Wird unabhaengig vom Erfolg befuellt."""

    stdout: str = ""
    stderr: str = ""
    exit_code: int
    laufzeit_ms: float
    timeout: bool = False

    @property
    def erfolgreich(self) -> bool:
        return self.exit_code == 0 and not self.timeout
