"""DockerRunner -- fuehrt Python-Code in einem isolierten Container aus.

Implementiert das Runner-Protocol. Pro Aufruf wird ein frischer Container
via `docker run --rm` gestartet, mit Memory-, CPU-, Netz-, Filesystem-,
Process- und FD-Limits. Der zu pruefende Code wird per read-only Bind-Mount
ins Container-Filesystem gehaengt; das Working-Dir liegt auf einem
schreibbaren tmpfs.
"""

import subprocess
import tempfile
import time
from pathlib import Path

from .result import RunLimits, RunResult


class DockerRunner:
    """Fuehrt Code in `codeschmiede-sandbox:python` aus."""

    IMAGE = "codeschmiede-sandbox:python"
    DOCKER_OVERHEAD_SEKUNDEN = 3

    def run_code(self, code: str, limits: RunLimits | None = None) -> RunResult:
        limits = limits or RunLimits()

        with tempfile.TemporaryDirectory(prefix="codeschmiede_") as tmpdir:
            code_pfad = Path(tmpdir) / "code.py"
            code_pfad.write_text(code, encoding="utf-8")

            befehl = self._befehl_bauen(tmpdir, limits)

            start = time.perf_counter()
            try:
                proc = subprocess.run(
                    befehl,
                    capture_output=True,
                    text=True,
                    timeout=limits.timeout_sekunden + self.DOCKER_OVERHEAD_SEKUNDEN,
                )
            except subprocess.TimeoutExpired as fehler:
                laufzeit_ms = (time.perf_counter() - start) * 1000
                return RunResult(
                    stdout=self._dekodiere(fehler.stdout),
                    stderr=self._dekodiere(fehler.stderr),
                    exit_code=-1,
                    laufzeit_ms=laufzeit_ms,
                    timeout=True,
                )

            laufzeit_ms = (time.perf_counter() - start) * 1000
            return RunResult(
                stdout=proc.stdout,
                stderr=proc.stderr,
                exit_code=proc.returncode,
                laufzeit_ms=laufzeit_ms,
                timeout=False,
            )

    def _befehl_bauen(self, code_dir: str, limits: RunLimits) -> list[str]:
        return [
            "docker", "run", "--rm",
            f"--memory={limits.memory_mb}m",
            f"--cpus={limits.cpus}",
            "--network=none",
            "--read-only",
            "--tmpfs", "/tmp:size=16m,mode=1777",
            "--pids-limit=64",
            "--ulimit", "nofile=64",
            "-v", f"{code_dir}:/sandbox/code:ro",
            "--workdir", "/tmp",
            "-e", "PYTHONDONTWRITEBYTECODE=1",
            self.IMAGE,
            "python", "/sandbox/code/code.py",
        ]

    @staticmethod
    def _dekodiere(daten: bytes | str | None) -> str:
        if daten is None:
            return ""
        if isinstance(daten, bytes):
            return daten.decode("utf-8", errors="replace")
        return daten
