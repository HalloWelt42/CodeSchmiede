"""Härtung der Sandbox gegen das echte Image."""

import subprocess

import pytest

from codeschmiede.sandbox.result import RunLimits
from codeschmiede.sandbox.runner import SandboxFehler

from .conftest import braucht_sandbox

pytestmark = braucht_sandbox
KURZ = RunLimits(timeout_sekunden=2)


def test_normaler_lauf(docker_runner):
    erg = docker_runner.run_code("print(6 * 7)", "python", KURZ)
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
        "import socket\nsocket.create_connection(('1.1.1.1', 80), timeout=1)", "python", KURZ
    )
    assert erg.exit_code != 0 and "unreachable" in erg.stderr.lower()


def test_nur_lesend_ausser_tmp(docker_runner):
    erg = docker_runner.run_code("open('/etc/x', 'w')", "python", KURZ)
    assert "Read-only file system" in erg.stderr
    erg = docker_runner.run_code("open('/tmp/a', 'w').write('ok'); print(open('/tmp/a').read())", "python", KURZ)
    assert erg.stdout.strip() == "ok"


def test_unprivilegiert(docker_runner):
    erg = docker_runner.run_code("import os; print(os.getuid())", "python", KURZ)
    assert erg.stdout.strip() == "65534"


def test_speichergrenze_ist_keine_zeitueberschreitung(docker_runner):
    erg = docker_runner.run_code("x = bytearray(400 * 1024 * 1024)", "python", KURZ)
    assert not erg.timeout
    assert erg.exit_code != 0


def test_javascript(docker_runner):
    erg = docker_runner.run_code("console.log([1, 2].map((x) => x * 2).join(','))", "javascript", KURZ)
    assert erg.stdout.strip() == "2,4"


def test_unbekannte_sprache(docker_runner):
    with pytest.raises(SandboxFehler):
        docker_runner.run_code("x", "cobol", KURZ)


def test_keine_reste(docker_runner):
    docker_runner.run_code("while True: pass", "python", KURZ)
    reste = subprocess.run(
        ["docker", "ps", "-a", "--filter", "name=cs-lauf-", "--format", "{{.Names}}"],
        capture_output=True, text=True,
    ).stdout.strip()
    assert reste == ""
