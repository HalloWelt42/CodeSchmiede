"""Sandbox für andere Apps (Nachschlag WIKI-48): nur Apps auf der Erlaubnisliste, Menschen nicht über diesen Weg;
die Aufzeichnung ist die des Debuggers; Code begrenzt."""

from __future__ import annotations

import subprocess
import sys
import time

from appkern.anmeldung import Konto
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.config import Settings
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
    assert app.post("/api/v1/sandbox/aufzeichnen", json={"code": "print(1)", "sprache": "php"}).status_code == 422
