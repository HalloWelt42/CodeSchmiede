"""Aufzeichnung eines Laufs: je Zeile des eigenen Codes der Speicher danach, gegen das echte Sandbox-Image."""

from codeschmiede.aufzeichnung import KURS, aufzeichnen
from codeschmiede.sandbox.result import RunLimits

from .conftest import braucht_sandbox

pytestmark = braucht_sandbox
GENUG = RunLimits(timeout_sekunden=15)

PINGUINE = 'kolonie = ["Pit", "Pia", "Paul"]\nfor pinguin in kolonie:\n    print(pinguin, "bekommt einen Fisch")\nprint("Alle satt!")\n'


def _namen(schritt):
    return {k: v.darstellung for r in schritt.rahmen for k, v in r.variablen.items()}


def test_schleife_zeile_fuer_zeile(docker_runner):
    a = aufzeichnen(docker_runner, PINGUINE, GENUG)
    assert a.fehler is None and not a.gekuerzt
    assert [s.zeile for s in a.schritte] == [1, 2, 3, 2, 3, 2, 3, 2, 4]
    assert [_namen(s).get("pinguin") for s in a.schritte[1:7:2]] == ["'Pit'", "'Pia'", "'Paul'"]
    assert a.schritte[2].ausgabe == "Pit bekommt einen Fisch\n" and a.schritte[-1].ausgabe == "Alle satt!\n"
    assert a.ausgabe.endswith("Alle satt!\n")
    liste = a.schritte[0].rahmen[0].variablen["kolonie"]
    assert liste.art == "liste" and [e.darstellung for e in liste.elemente] == ["'Pit'", "'Pia'", "'Paul'"]


def test_funktion_mit_rahmen_und_rueckgabe(docker_runner):
    a = aufzeichnen(docker_runner, "def doppelt(x):\n    y = x * 2\n    return y\n\nz = doppelt(4)\nprint(z)\n", GENUG)
    innen = [s for s in a.schritte if len(s.rahmen) == 2]
    assert innen and all(s.rahmen[1].name == "doppelt" for s in innen)
    assert innen[-1].rueckgabe is not None and innen[-1].rueckgabe.darstellung == "8"
    # nach der Rückkehr ist die Zeile des Aufrufs fertig und z steht im Speicher
    nach = a.schritte[a.schritte.index(innen[-1]) + 1]
    assert nach.zeile == 5 and _namen(nach)["z"] == "8"


def test_verweise_haben_dieselbe_kennung(docker_runner):
    a = aufzeichnen(docker_runner, "a = [1, 2]\nb = a\nb.append(3)\n", GENUG)
    v = a.schritte[-1].rahmen[0].variablen
    assert v["a"].kennung == v["b"].kennung and v["a"].darstellung == "[1, 2, 3]"


def test_laufzeitfehler_mit_zeile(docker_runner):
    a = aufzeichnen(docker_runner, "x = 1\ny = x / 0\n", GENUG)
    assert a.fehler == "ZeroDivisionError: division by zero" and a.fehlerzeile == 2
    assert a.schritte[0].zeile == 1


def test_syntaxfehler_ohne_schritte(docker_runner):
    a = aufzeichnen(docker_runner, "x = (\n", GENUG)
    assert a.fehler.startswith("SyntaxError") and a.fehlerzeile == 1 and a.schritte == []


def test_lange_laeufe_werden_gekuerzt_aber_laufen_zu_ende(docker_runner):
    a = aufzeichnen(docker_runner, "s = 0\nfor i in range(5000):\n    s += i\nprint(s)\n", GENUG)
    assert a.gekuerzt and len(a.schritte) == KURS.schritte and a.ausgabe == "12497500\n"


def test_endlosschleife_bricht_mit_zeit_ab(docker_runner):
    a = aufzeichnen(docker_runner, "while True:\n    pass\n", RunLimits(timeout_sekunden=2))
    assert a.zeitueberschreitung and a.fehler


def test_keine_namen_des_aufzeichners_sichtbar(docker_runner):
    a = aufzeichnen(docker_runner, "import math\nx = math.pi\n", GENUG)
    assert set(a.schritte[-1].rahmen[0].variablen) == {"x"}


def test_eingabe_fuer_input(docker_runner):
    a = aufzeichnen(docker_runner, 'name = input("Name? ")\nalter = int(input())\nprint(name, alter + 1)\n', GENUG, ["Pia", "4"])
    assert a.fehler is None and a.ausgabe == "Name? Pia 5\n"
    assert _namen(a.schritte[1])["alter"] == "4"
