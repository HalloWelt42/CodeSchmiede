"""Härtung der Sandbox gegen das echte Image."""

import subprocess
import time
import uuid

import pytest

from codeschmiede.sandbox.result import RunLimits
from codeschmiede.sandbox.runner import SandboxFehler

from .conftest import braucht_sandbox

pytestmark = braucht_sandbox
# für die Zeitgrenze selbst: kurz, damit der Test nicht wartet
KURZ = RunLimits(timeout_sekunden=2)
# für Sicherheitseigenschaften: großzügig, denn unter hoher Last des Rechners braucht schon der Start von Python
# im Container mehr als 2 s, und dann prüfte der Test die Zeitgrenze statt der Eigenschaft
GENUG = RunLimits(timeout_sekunden=15)


def test_normaler_lauf(docker_runner):
    erg = docker_runner.run_code("print(6 * 7)", "python", GENUG)
    assert erg.exit_code == 0 and erg.stdout == "42\n" and not erg.timeout


def test_endlosschleife_bricht_ab(docker_runner):
    erg = docker_runner.run_code("while True: pass", "python", KURZ)
    assert erg.timeout


def test_ausgabeflut_wird_gekuerzt(docker_runner):
    erg = docker_runner.run_code("while True: print('x' * 1000)", "python", KURZ)
    assert erg.gekuerzt
    assert len(erg.stdout) <= 200_000


def test_kein_netz(docker_runner):
    erg = docker_runner.run_code(
        "import socket\nsocket.create_connection(('1.1.1.1', 80), timeout=1)", "python", GENUG
    )
    assert erg.exit_code != 0 and "unreachable" in erg.stderr.lower()


def test_nur_lesend_ausser_tmp(docker_runner):
    erg = docker_runner.run_code("open('/etc/x', 'w')", "python", GENUG)
    assert "Read-only file system" in erg.stderr
    erg = docker_runner.run_code("open('/tmp/a', 'w').write('ok'); print(open('/tmp/a').read())", "python", GENUG)
    assert erg.stdout.strip() == "ok"


def test_unprivilegiert(docker_runner):
    erg = docker_runner.run_code("import os; print(os.getuid())", "python", GENUG)
    assert erg.stdout.strip() == "65534"


def test_speichergrenze_ist_keine_zeitueberschreitung(docker_runner):
    erg = docker_runner.run_code("x = bytearray(400 * 1024 * 1024)", "python", GENUG)
    assert not erg.timeout
    assert erg.exit_code != 0


def test_javascript(docker_runner):
    erg = docker_runner.run_code("console.log([1, 2].map((x) => x * 2).join(','))", "javascript", GENUG)
    assert erg.stdout.strip() == "2,4"


def test_unbekannte_sprache(docker_runner):
    with pytest.raises(SandboxFehler):
        docker_runner.run_code("x", "cobol", KURZ)


def test_keine_reste(docker_runner, monkeypatch):
    # fester Name, damit nur dieser Lauf zählt und nicht Läufe anderer Nutzer derselben Sandbox
    kennung = uuid.uuid4()
    monkeypatch.setattr(uuid, "uuid4", lambda: kennung)
    docker_runner.run_code("while True: pass", "python", KURZ)
    name = f"cs-lauf-{kennung.hex[:16]}"
    # --rm räumt im Docker-Dienst nach, unter Last mit Verzögerung
    frist = time.monotonic() + 30
    while True:
        reste = subprocess.run(
            ["docker", "ps", "-a", "--filter", f"name=^{name}$", "--format", "{{.Names}}"],
            capture_output=True, text=True,
        ).stdout.strip()
        if reste == "" or time.monotonic() > frist:
            break
        time.sleep(1)
    assert reste == ""


def test_ohne_speicher_cgroup_nur_datengrenze():
    from codeschmiede.sandbox.docker_runner import DockerRunner, Sprachbild

    runner = DockerRunner({"python": "bild-py", "javascript": "bild-js"})
    runner._speicher_cgroup = False
    befehl = runner._befehl_bauen("lauf", runner.bilder["python"], KURZ)
    assert not any(a.startswith("--memory") for a in befehl)
    assert "data=134217728:134217728" in befehl
    # Node braucht beim Start mehr beschreibbaren Adressraum
    assert "data=536870912:536870912" in runner._befehl_bauen("lauf", runner.bilder["javascript"], KURZ)
    runner._speicher_cgroup = True
    befehl = runner._befehl_bauen("lauf", Sprachbild("x", ("python", "-")), KURZ)
    assert "--memory=128m" in befehl and "--memory-swap=128m" in befehl


def test_langsames_aufraeumen_kippt_keine_pruefung(monkeypatch):
    from codeschmiede.sandbox.docker_runner import DockerRunner

    def zu_langsam(*args, **kwargs):
        raise subprocess.TimeoutExpired(args[0], kwargs.get("timeout", 15))

    monkeypatch.setattr(subprocess, "run", zu_langsam)
    DockerRunner({"python": "bild-py"})._beende("lauf")  # wirft nicht


def test_datengrenze_wirkt(docker_runner):
    erg = docker_runner.run_code("x = bytearray(400 * 1024 * 1024)", "python", GENUG)
    assert erg.exit_code != 0 and not erg.timeout
