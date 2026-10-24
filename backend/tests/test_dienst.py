"""Sandbox-Dienst: nur mit Schlüssel, Backend spricht ihn über den DienstRunner an."""

import pytest
from fastapi.testclient import TestClient
from pydantic import SecretStr

from codeschmiede.sandbox.dienst import DienstEinstellungen, dienst_bauen
from codeschmiede.sandbox.dienst_runner import DienstRunner
from codeschmiede.sandbox.result import RunLimits
from codeschmiede.sandbox.runner import SandboxFehler

from .conftest import braucht_sandbox

# Der DienstRunner gibt jedem Aufruf eine Zeitgrenze mit; der TestClient ignoriert sie.
pytestmark = pytest.mark.filterwarnings("ignore:You should not use the .timeout. argument")


@pytest.fixture
def dienst(tmp_path, docker_runner):
    e = DienstEinstellungen(daten_pfad=tmp_path, schluessel=SecretStr("geheim"))
    return TestClient(dienst_bauen(e, runner=docker_runner))


def test_ohne_schluessel_abgewiesen(dienst):
    antwort = dienst.post("/laeufe", json={"code": "print(1)", "sprache": "python"})
    assert antwort.status_code == 401


def test_falscher_schluessel_abgewiesen(dienst):
    antwort = dienst.post(
        "/laeufe",
        json={"code": "print(1)", "sprache": "python"},
        headers={"X-Sandbox-Schluessel": "falsch"},
    )
    assert antwort.status_code == 401


@braucht_sandbox
def test_lauf_ueber_dienst_runner(dienst):
    runner = DienstRunner("http://testserver", "geheim", client=dienst)
    erg = runner.run_code("print('hallo')", "python", RunLimits(timeout_sekunden=2))
    assert erg.stdout == "hallo\n"


def test_unbekannte_sprache_ist_sandboxfehler(dienst):
    runner = DienstRunner("http://testserver", "geheim", client=dienst)
    with pytest.raises(SandboxFehler):
        runner.run_code("x", "cobol")


def test_schluesseldatei_wird_geteilt(tmp_path, docker_runner):
    e = DienstEinstellungen(daten_pfad=tmp_path)
    dienst_bauen(e, runner=docker_runner)
    from codeschmiede.sandbox.schluessel import lade_schluessel

    datei = tmp_path / "sandbox-schluessel"
    assert datei.exists() and oct(datei.stat().st_mode)[-3:] == "600"
    assert lade_schluessel(SecretStr(""), datei) == datei.read_text().strip()


def test_dienst_nicht_erreichbar():
    runner = DienstRunner("http://127.0.0.1:9", "x")
    with pytest.raises(SandboxFehler):
        runner.run_code("print(1)", "python")


def test_fehlendes_docker_ist_sandboxfehler():
    from codeschmiede.sandbox.docker_runner import DockerRunner

    runner = DockerRunner({"python": "x"}, docker="/gibt/es/nicht/docker")
    with pytest.raises(SandboxFehler, match="Docker lässt sich nicht starten"):
        runner.run_code("print(1)", "python")
