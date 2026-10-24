"""Gemeinsame Vorrichtungen: ein kleiner Aufgabenbestand im Temp-Ordner,
eigene Datenbank, echte Sandbox über den DockerRunner (ohne Dienst).

Die echten Daten unter data/ werden nie berührt.
"""

import shutil
import subprocess
import textwrap
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.config import Settings
from codeschmiede.sandbox.docker_runner import DockerRunner

BILDER = {
    "python": "codeschmiede-sandbox:python",
    "javascript": "codeschmiede-sandbox:javascript",
}


def _bilder_da() -> bool:
    if shutil.which("docker") is None:
        return False
    for image in BILDER.values():
        if subprocess.run(["docker", "image", "inspect", image], capture_output=True).returncode != 0:
            return False
    return True


braucht_sandbox = pytest.mark.skipif(
    not _bilder_da(), reason="Sandbox-Images fehlen (scripts/build-sandbox.sh)"
)

KONFIG = """
schwierigkeiten:
  - {id: anfaenger, titel: Anfänger, farbe: green, score_max: 25}
sprachen:
  - {id: python, titel: Python, editor_lang: python, endung: py, runner_type: docker_python}
  - {id: javascript, titel: JavaScript, editor_lang: javascript, endung: js, runner_type: docker_javascript}
  - {id: css, titel: CSS, editor_lang: css, endung: css, runner_type: iframe_css}
  - {id: sql, titel: SQL, editor_lang: sql, endung: sql, runner_type: docker_sqlite}
aufgabentypen:
  - {id: code_schreiben, titel: Code schreiben, view: code_aufgabe}
  - {id: output_quiz, titel: Quiz, view: output_quiz}
  - {id: css_klon, titel: CSS, view: css_klon}
  - {id: sql_abfrage, titel: SQL, view: sql_abfrage}
"""

KOPF = """schema_version: 1
id: {id}
revision: 1
titel: {titel}
sprache: {sprache}
task_type: {typ}
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 3
"""


def schreibe_aufgabe(wurzel: Path, sprache: str, aid: str, typ: str, rest: str, text: str = "Text") -> Path:
    ordner = wurzel / sprache / aid
    ordner.mkdir(parents=True, exist_ok=True)
    kopf = KOPF.format(id=aid, titel=aid, sprache=sprache, typ=typ)
    (ordner / "aufgabe.md").write_text(f"---\n{kopf}{textwrap.dedent(rest)}---\n\n{text}\n", encoding="utf-8")
    return ordner


def baue_bestand(wurzel: Path) -> None:
    (wurzel / "_konfig.yml").write_text(KONFIG, encoding="utf-8")
    ordner = schreibe_aufgabe(wurzel, "python", "001-verdoppeln", "code_schreiben", """\
        funktion: verdoppeln
        hints:
          - {kosten: 3, text: "Mal zwei"}
        tests_sichtbar:
          - {input: [2], expected: 4}
        tests_versteckt:
          - {input: [21], expected: 42}
          - {input: [-3], expected: -6}
        starter_code: "def verdoppeln(x):\\n    pass\\n"
        """)
    (ordner / "solution_idiomatic.py").write_text("def verdoppeln(x):\n    return 2 * x\n")
    schreibe_aufgabe(wurzel, "python", "002-paar", "code_schreiben", """\
        funktion: paar
        tests_sichtbar:
          - {input: [1, 2], expected: [1, 2]}
        """)
    schreibe_aufgabe(wurzel, "javascript", "003-js-summe", "code_schreiben", """\
        funktion: summe
        tests_sichtbar:
          - {input: [[1, 2, 3]], expected: 6}
        tests_versteckt:
          - {input: [[]], expected: 0}
          - {input: [[10, -5]], expected: 5}
        """)
    schreibe_aufgabe(wurzel, "python", "004-quiz", "output_quiz", """\
        quiz:
          code: "print(1)"
          optionen: ["0", "1"]
          richtig_index: 1
        """)
    schreibe_aufgabe(wurzel, "css", "c005-knopf", "css_klon", """\
        ziel_html: "<b>x</b>"
        ziel_css: "b { color: red; }"
        asserts: []
        """)
    datasets = wurzel / "sql" / "datasets"
    datasets.mkdir(parents=True)
    (datasets / "zahlen.sql").write_text(
        "CREATE TABLE z (id INTEGER PRIMARY KEY, wert INTEGER);\n"
        + "".join(f"INSERT INTO z (wert) VALUES ({i * 10});\n" for i in range(1, 7))
    )
    ordner = schreibe_aufgabe(wurzel, "sql", "s006-werte", "sql_abfrage", """\
        dataset: zahlen
        erwartete_spalten: [wert]
        sortierung_egal: false
        erwartetes_ergebnis: [[10], [20], [30], [40], [50], [60]]
        """)
    (ordner / "solution_idiomatic.sql").write_text("SELECT wert FROM z ORDER BY id;\n")
    pfade = wurzel / "pfade"
    pfade.mkdir()
    (pfade / "start.yml").write_text(
        "id: start\ntitel: Start\nreihenfolge: [001-verdoppeln, 002-paar]\n", encoding="utf-8"
    )


@pytest.fixture
def bestand(tmp_path: Path) -> Path:
    wurzel = tmp_path / "aufgaben"
    wurzel.mkdir()
    baue_bestand(wurzel)
    return wurzel


@pytest.fixture
def settings(tmp_path: Path, bestand: Path) -> Settings:
    return Settings(
        aufgaben_pfad=bestand,
        daten_pfad=tmp_path / "data",
        db_datei=tmp_path / "data" / "test.db",
    )


@pytest.fixture(scope="session")
def docker_runner() -> DockerRunner:
    return DockerRunner(BILDER, max_ausgabe_bytes=200_000)


@pytest.fixture
def client(settings: Settings, docker_runner: DockerRunner) -> TestClient:
    return TestClient(app_bauen(settings, runner=docker_runner))
