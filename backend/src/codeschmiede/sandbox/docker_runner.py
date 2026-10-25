"""DockerRunner -- startet je Lauf einen frischen, abgeschotteten Container.

Läuft ausschließlich im Sandbox-Dienst; das Backend hat keinen
Docker-Zugang. Der Code kommt über stdin in den Container, es gibt
keinen Mount. Das funktioniert auch dann, wenn der Dienst selbst in
einem Container mit dem Docker-Socket des Hosts läuft.

Härtung je Lauf:
- kein Netz
- nur-lesendes Dateisystem mit kleinem tmpfs
- alle Capabilities entzogen, keine Rechteerhöhung
- unprivilegierter Nutzer
- Speicher ohne Swap, Grenzen für CPU, Prozesse und offene Dateien

Die Laufzeitgrenze setzt `timeout` im Container. Hält der Container
trotzdem länger (Startzeit eingerechnet), beendet der Dienst ihn über
seinen Namen. Die Ausgabe ist auf eine Höchstmenge begrenzt; wer mehr
schreibt, wird abgebrochen.
"""

import logging
import subprocess
import threading
import time
import uuid
from dataclasses import dataclass
from typing import IO

from .result import RunLimits, RunResult
from .runner import SandboxFehler

logger = logging.getLogger("codeschmiede.sandbox")


# Wie jede Sprache ihr Programm von stdin liest.
SPRACHBEFEHLE: dict[str, tuple[str, ...]] = {
    "python": ("python", "-"),
    "javascript": ("node", "-"),
}

# Datengrenze je Prozess (RLIMIT_DATA): wirkt auch ohne Speicher-cgroup (Raspberry Pi OS startet mit
# cgroup_disable=memory, dann verwirft Docker --memory). Node reserviert beim Start rund 400 MB beschreibbaren
# Adressraum für seinen Code und braucht darum mindestens 512 MB; die übrigen Sprachen bekommen die Speichergrenze.
MINDEST_DATEN_MB: dict[str, int] = {"javascript": 512}

# Exit-Code von `timeout`, wenn die Laufzeitgrenze griff. 137 (SIGKILL) heißt
# fast immer Speichergrenze; die gemessene Laufzeit enthält die Startzeit des
# Containers und taugt nicht zur Unterscheidung.
TIMEOUT_EXIT = 124
KILL_EXIT = 137
NOBODY = "65534:65534"


@dataclass(frozen=True)
class Sprachbild:
    image: str
    befehl: tuple[str, ...]
    mindest_daten_mb: int = 0


class _BegrenzterLeser(threading.Thread):
    """Liest einen Datenstrom bis zur Höchstmenge und verwirft den Rest,
    damit der Container nie an einer vollen Pipe hängt."""

    def __init__(self, strom: IO[bytes], max_bytes: int):
        super().__init__(daemon=True)
        self.strom = strom
        self.max_bytes = max_bytes
        self.teile: list[bytes] = []
        self.gelesen = 0
        self.ueberlauf = False

    def run(self) -> None:
        while chunk := self.strom.read(65536):
            frei = self.max_bytes - self.gelesen
            if frei > 0:
                self.teile.append(chunk[:frei])
            self.gelesen += len(chunk)
            if self.gelesen > self.max_bytes:
                self.ueberlauf = True

    def text(self) -> str:
        return b"".join(self.teile).decode("utf-8", errors="replace")


class DockerRunner:
    def __init__(
        self,
        bilder: dict[str, str],
        max_ausgabe_bytes: int = 1_000_000,
        startzeit_sekunden: float = 20,
        docker: str = "docker",
    ):
        self.bilder = {
            sprache: Sprachbild(image=image, befehl=SPRACHBEFEHLE[sprache],
                                mindest_daten_mb=MINDEST_DATEN_MB.get(sprache, 0))
            for sprache, image in bilder.items()
            if sprache in SPRACHBEFEHLE
        }
        self.max_ausgabe_bytes = max_ausgabe_bytes
        # Zeit für den Containerstart, die über die Laufzeitgrenze hinaus
        # erlaubt ist, bevor der Dienst hart beendet (Host-abhängig).
        self.startzeit_sekunden = startzeit_sekunden
        self.docker = docker
        self._speicher_cgroup: bool | None = None

    @property
    def speicher_cgroup(self) -> bool:
        """Ob der Docker-Daemon Speichergrenzen per cgroup durchsetzt (einmal gefragt). Ohne sie verwirft er --memory
        mit einer Warnung, die sonst in jeder Fehlerausgabe stünde; dann bleibt die Datengrenze je Prozess."""
        if self._speicher_cgroup is None:
            try:
                antwort = subprocess.run([self.docker, "info", "--format", "{{.MemoryLimit}}"],
                                         capture_output=True, text=True, timeout=15, check=False)
                self._speicher_cgroup = antwort.stdout.strip() == "true"
            except (OSError, subprocess.TimeoutExpired):
                self._speicher_cgroup = True   # unbekannt: wie bisher übergeben, Docker meldet es selbst
            if not self._speicher_cgroup:
                logger.warning("Docker setzt keine Speichergrenzen durch (Speicher-cgroup aus); es gilt nur die "
                               "Datengrenze je Prozess")
        return self._speicher_cgroup

    @property
    def sprachen(self) -> list[str]:
        return sorted(self.bilder)

    def run_code(
        self, code: str, sprache: str, limits: RunLimits | None = None
    ) -> RunResult:
        limits = limits or RunLimits()
        bild = self.bilder.get(sprache)
        if bild is None:
            raise SandboxFehler(f"Für die Sprache '{sprache}' gibt es kein Sandbox-Image")

        name = f"cs-lauf-{uuid.uuid4().hex[:16]}"
        start = time.perf_counter()
        try:
            proc = subprocess.Popen(
                self._befehl_bauen(name, bild, limits),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except OSError as fehler:
            raise SandboxFehler(f"Docker lässt sich nicht starten ({self.docker}): {fehler}") from fehler
        assert proc.stdin and proc.stdout and proc.stderr
        aus = _BegrenzterLeser(proc.stdout, self.max_ausgabe_bytes)
        err = _BegrenzterLeser(proc.stderr, self.max_ausgabe_bytes)
        aus.start()
        err.start()
        try:
            proc.stdin.write(code.encode("utf-8"))
            proc.stdin.close()
        except BrokenPipeError:
            pass

        frist = time.monotonic() + limits.timeout_sekunden + self.startzeit_sekunden
        hart_beendet = False
        while True:
            try:
                proc.wait(timeout=0.05)
                break
            except subprocess.TimeoutExpired:
                if aus.ueberlauf or err.ueberlauf or time.monotonic() > frist:
                    hart_beendet = time.monotonic() > frist
                    self._beende(name)
                    proc.kill()
                    proc.wait()
                    break
        aus.join(timeout=5)
        err.join(timeout=5)
        laufzeit_ms = (time.perf_counter() - start) * 1000

        exit_code = proc.returncode
        gekuerzt = aus.ueberlauf or err.ueberlauf
        stderr = err.text()
        if exit_code == KILL_EXIT and not gekuerzt and not hart_beendet:
            stderr += (
                f"\nAbgebrochen: Speichergrenze von {limits.memory_mb} MB "
                "überschritten oder Prozess hart beendet."
            )
        return RunResult(
            stdout=aus.text(),
            stderr=stderr,
            exit_code=exit_code,
            laufzeit_ms=laufzeit_ms,
            timeout=hart_beendet or exit_code == TIMEOUT_EXIT,
            gekuerzt=gekuerzt,
        )

    def _befehl_bauen(self, name: str, bild: Sprachbild, limits: RunLimits) -> list[str]:
        daten = max(limits.memory_mb, bild.mindest_daten_mb) * 1024 * 1024
        return [
            self.docker, "run", "--rm", "-i",
            "--name", name,
            "--network=none",
            "--read-only",
            "--tmpfs", "/tmp:rw,nosuid,nodev,size=16m,mode=1777",
            "--cap-drop=ALL",
            "--security-opt=no-new-privileges",
            "--user", NOBODY,
            *([f"--memory={limits.memory_mb}m", f"--memory-swap={limits.memory_mb}m"] if self.speicher_cgroup else []),
            "--ulimit", f"data={daten}:{daten}",
            f"--cpus={limits.cpus}",
            "--pids-limit=64",
            "--ulimit", "nofile=64:64",
            "--workdir", "/tmp",
            "--env", "HOME=/tmp",
            bild.image,
            "timeout", "-k", "1", f"{limits.timeout_sekunden}s",
            *bild.befehl,
        ]

    def _beende(self, name: str) -> None:
        subprocess.run(
            [self.docker, "rm", "-f", name],
            capture_output=True,
            timeout=15,
            check=False,
        )
