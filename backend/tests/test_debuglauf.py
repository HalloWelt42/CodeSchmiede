"""Debugger einer Aufgabe: Aufzeichnung mit Aufruf oder Eingabezeilen, gegen das echte Sandbox-Image."""

import json

from codeschmiede.aufzeichnung.debuglauf import DEBUGGER, debuggen
from codeschmiede.sandbox.docker_runner import DockerRunner
from codeschmiede.sandbox.result import RunLimits

from .conftest import BILDER, braucht_sandbox

pytestmark = braucht_sandbox
GENUG = RunLimits(timeout_sekunden=20)

GERADE = '''def ist_gerade(x):
    return x % 2 == 0

def nur_gerade(zahlen):
    ergebnis = []
    for x in zahlen:
        if ist_gerade(x):
            ergebnis.append(x)
    print("gefunden:", len(ergebnis))
    return ergebnis
'''


def test_funktion_ohne_die_aufrufzeile(docker_runner):
    a = debuggen(docker_runner, "python", GERADE, GENUG, funktion="nur_gerade", argumente=[[1, 2, 3, 4]])
    assert a.fehler is None and not a.gekuerzt
    assert all(s.zeile <= 10 for s in a.schritte)
    assert a.rueckgabe is not None and a.rueckgabe.darstellung == "[2, 4]"
    assert "".join(s.ausgabe for s in a.schritte) == "gefunden: 2\n"
    # in ist_gerade steht der Aufrufstapel mit beiden Funktionen
    assert ["Modul", "nur_gerade", "ist_gerade"] in [[r.name for r in s.rahmen] for s in a.schritte]


def test_rekursion_gibt_die_aeusserste_rueckgabe(docker_runner):
    code = "def fak(n):\n    if n <= 1:\n        return 1\n    return n * fak(n - 1)\n"
    a = debuggen(docker_runner, "python", code, GENUG, funktion="fak", argumente=[4])
    assert a.rueckgabe is not None and a.rueckgabe.darstellung == "24"
    assert max(len(s.rahmen) for s in a.schritte) == 5


def test_fehler_im_eigenen_code_mit_zeile(docker_runner):
    a = debuggen(docker_runner, "python", "def teile(a, b):\n    return a / b\n", GENUG, funktion="teile", argumente=[1, 0])
    assert a.fehler and a.fehler.startswith("ZeroDivisionError") and a.fehlerzeile == 2 and a.rueckgabe is None


def test_fehlende_funktion_ohne_fremde_zeile(docker_runner):
    a = debuggen(docker_runner, "python", "x = 1\n", GENUG, funktion="f", argumente=[])
    assert a.fehler and a.fehler.startswith("NameError") and a.fehlerzeile is None
    assert [s.zeile for s in a.schritte] == [1]


def test_programm_mit_eingabezeilen(docker_runner):
    code = "name = input()\nprint('Hallo', name)\n"
    a = debuggen(docker_runner, "python", code, GENUG, eingabe=["Pit"])
    assert a.ausgabe == "Hallo Pit\n" and [s.zeile for s in a.schritte] == [1, 2] and a.rueckgabe is None


def test_javascript_funktion(docker_runner):
    code = "function summe(xs) {\n  let s = 0;\n  for (const x of xs) s += x;\n  return s;\n}\n"
    a = debuggen(docker_runner, "javascript", code, GENUG, funktion="summe", argumente=[[1, 2, 3]])
    assert a.fehler is None and a.rueckgabe is not None and a.rueckgabe.darstellung == "6"
    assert all(s.zeile <= 5 for s in a.schritte) and a.schritte


def test_grosse_werte_kuerzen_nach_bytes_statt_den_lauf_zu_verlieren():
    # mit der Ausgabegrenze des Sandbox-Dienstes (1 MB), nicht der knappen der übrigen Tests
    docker_runner = DockerRunner(BILDER)
    code = "def f():\n    tabelle = [[i * j for j in range(20)] for i in range(20)]\n    for k in range(1500):\n        tabelle[0][0] = k\n    return k\n"
    a = debuggen(docker_runner, "python", code, GENUG, funktion="f", argumente=[])
    assert a.fehler is None and a.gekuerzt and 0 < len(a.schritte) < DEBUGGER.schritte
    assert len(json.dumps([s.model_dump(exclude_defaults=True) for s in a.schritte])) <= DEBUGGER.bytes * 1.05
