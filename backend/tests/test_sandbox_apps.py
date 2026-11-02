"""Sandbox für andere Apps (Nachschlag WIKI-48): nur Apps auf der Erlaubnisliste, Menschen nicht über diesen Weg;
die Aufzeichnung ist die des Debuggers; Code begrenzt."""

from __future__ import annotations

import json
import subprocess
import sys
import time

from appkern.anmeldung import Konto
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.config import Settings
from codeschmiede.sandbox.laufzeiten import PHP_FASSUNGEN
from codeschmiede.sandbox.result import RunResult


class LokalerRunner:
    """Führt das Skript mit dem Python der Tests aus, wie die Sandbox es täte (ohne Grenzen)."""

    def run_code(self, code, sprache, limits=None):
        start = time.perf_counter()
        p = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=120)
        return RunResult(stdout=p.stdout, stderr=p.stderr, exit_code=p.returncode, laufzeit_ms=(time.perf_counter() - start) * 1000)


def client(tmp_path, konto: Konto) -> TestClient:
    app = app_bauen(Settings(daten_pfad=tmp_path, anmeldung_pflicht=False), runner=LokalerRunner())
    app.dependency_overrides[app.state.sandbox_pruefen] = lambda: konto
    return TestClient(app)


def test_erlaubte_app_bekommt_die_aufzeichnung(tmp_path):
    # die Kellerwolke nennt die App mit ihrem Namen, die Erlaubnisliste führt die Kennung "nachschlag"
    c = client(tmp_path, Konto(id="1", name="probe", app="Nachschlag"))
    r = c.post("/api/v1/sandbox/aufzeichnen", json={"code": "x = 2\nprint(x * 3)\n", "sprache": "python"})
    assert r.status_code == 200, r.text
    a = r.json()
    assert a["ausgabe"].strip() == "6" and a["fehler"] is None and a["schritte"]


def test_andere_apps_und_menschen_nicht_und_code_begrenzt(tmp_path):
    fremd = client(tmp_path, Konto(id="1", name="probe", app="fremde-app"))
    assert fremd.post("/api/v1/sandbox/aufzeichnen", json={"code": "print(1)", "sprache": "python"}).status_code == 403
    mensch = client(tmp_path, Konto(id="1", name="probe"))
    assert mensch.post("/api/v1/sandbox/aufzeichnen", json={"code": "print(1)", "sprache": "python"}).status_code == 403
    app = client(tmp_path, Konto(id="1", name="probe", app="nachschlag"))
    assert app.post("/api/v1/sandbox/aufzeichnen", json={"code": "x" * 20_001, "sprache": "python"}).status_code == 422
    assert app.post("/api/v1/sandbox/aufzeichnen", json={"code": "print(1)", "sprache": "ruby"}).status_code == 422


class PhpRunner:
    """Antwortet wie die PHP-Abbilder: merkt sich die Laufzeiten; Funktionen je Fassung, 7.4 antwortet nicht."""

    def __init__(self, stdout="", stderr="", exit_code=0):
        self.stdout, self.stderr, self.exit_code, self.laufzeiten = stdout, stderr, exit_code, []

    def run_code(self, code, sprache, limits=None):
        self.laufzeiten.append(sprache)
        if "get_defined_functions" in code:
            if sprache == "php-7.4":
                return RunResult(stderr="kaputt", exit_code=1, laufzeit_ms=1)
            namen = ["strlen", "array_map"] + (["str_contains"] if sprache >= "php-8.0" else ["each"])
            return RunResult(stdout=json.dumps(namen), exit_code=0, laufzeit_ms=1)
        return RunResult(stdout=self.stdout, stderr=self.stderr, exit_code=self.exit_code, laufzeit_ms=12)


def php_client(tmp_path, runner) -> TestClient:
    app = app_bauen(Settings(daten_pfad=tmp_path, anmeldung_pflicht=False), runner=runner)
    app.dependency_overrides[app.state.sandbox_pruefen] = lambda: Konto(id="1", name="probe", app="Nachschlag")
    return TestClient(app)


def test_angebot_nennt_php_fassungen_mit_aufzeichnung(tmp_path):
    c = php_client(tmp_path, PhpRunner())
    angebot = {a["sprache"]: a for a in c.get("/api/v1/sandbox/sprachen").json()}
    assert angebot["python"]["aufzeichnen"] and not angebot["python"]["fassungen"]
    assert angebot["php"]["fassungen"] == list(PHP_FASSUNGEN) and angebot["php"]["aufzeichnen"]
    assert PHP_FASSUNGEN[0] == "8.5" and "5.6" in PHP_FASSUNGEN


def test_php_ausfuehren_in_der_gewaehlten_fassung(tmp_path):
    runner = PhpRunner(stdout="Array\n", stderr="Warning: Achtung in Standard input code on line 1")
    c = php_client(tmp_path, runner)
    gut = c.post("/api/v1/sandbox/ausfuehren", json={"code": "<?php print_r([]);", "sprache": "php", "fassung": "7.4"}).json()
    assert runner.laufzeiten[-1] == "php-7.4"
    assert (gut["ausgabe"], gut["fehler"], gut["hinweise"]) == ("Array\n", None, "Warning: Achtung in beispiel.php on line 1")
    c.post("/api/v1/sandbox/ausfuehren", json={"code": "<?php echo 1;", "sprache": "php"})
    assert runner.laufzeiten[-1] == "php-8.5"                        # ohne Fassung die neueste
    runner.stderr, runner.exit_code = ("Fatal error: Uncaught Error: Call to undefined function x() in Standard input code:2\n"
                                       "  thrown in Standard input code on line 2"), 255
    kaputt = c.post("/api/v1/sandbox/ausfuehren", json={"code": "<?php\nx();", "sprache": "php", "fassung": "8.3"}).json()
    assert kaputt["fehlerzeile"] == 2 and "beispiel.php" in kaputt["fehler"] and not kaputt["hinweise"]
    runner.stderr = "Parse error: syntax error, unexpected ':' in - on line 2"   # PHP 5.6 nennt stdin "-"
    alt = c.post("/api/v1/sandbox/ausfuehren", json={"code": "<?php\nx();", "sprache": "php", "fassung": "5.6"}).json()
    assert alt["fehler"] == "Parse error: syntax error, unexpected ':' in beispiel.php on line 2" and alt["fehlerzeile"] == 2
    assert c.post("/api/v1/sandbox/ausfuehren", json={"code": "1", "sprache": "php", "fassung": "4.4"}).status_code == 422
    assert c.post("/api/v1/sandbox/ausfuehren", json={"code": "1", "sprache": "python", "fassung": "3.12"}).status_code == 422


def test_php_aufzeichnen_in_der_gewaehlten_fassung(tmp_path):
    runner = PhpRunner()
    c = php_client(tmp_path, runner)
    assert c.post("/api/v1/sandbox/aufzeichnen", json={"code": "<?php echo 1;", "sprache": "php", "fassung": "5.6"}).status_code == 200
    assert runner.laufzeiten[-1] == "php-5.6"
    assert c.post("/api/v1/sandbox/aufzeichnen", json={"code": "1", "sprache": "php", "fassung": "4.4"}).status_code == 422


def test_php_funktionen_je_fassung_einmal_gefragt(tmp_path):
    runner = PhpRunner()
    c = php_client(tmp_path, runner)
    bestand = c.get("/api/v1/sandbox/funktionen/php").json()
    assert "7.4" not in bestand and "str_contains" in bestand["8.0"] and "each" in bestand["5.6"]
    gefragt = len(runner.laufzeiten)
    c.get("/api/v1/sandbox/funktionen/php")
    assert len(runner.laufzeiten) == gefragt + 1                      # nur die Fassung, die nicht geantwortet hatte


def test_laufzeiten_mit_ihren_abbildern_und_befehlen():
    from codeschmiede.sandbox.docker_runner import DockerRunner
    from codeschmiede.sandbox.laufzeiten import bilder
    r = DockerRunner(bilder())
    assert r.bilder["php-5.6"].image == "codeschmiede-sandbox:php-5.6" and r.bilder["php-5.6"].befehl[0] == "php"
    assert r.bilder["python"].befehl == ("python", "-") and len(r.sprachen) == 2 + len(PHP_FASSUNGEN)
