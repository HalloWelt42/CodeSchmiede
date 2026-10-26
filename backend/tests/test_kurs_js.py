"""Aufbaukurs JavaScript: Aufzeichnung über den Inspector von Node, Programme mit prompt() und Begriffe über
tree-sitter."""

from codeschmiede.api import app_bauen
from codeschmiede.aufzeichnung import KURS, aufzeichnen
from codeschmiede.kurs.begriffe import merkmale_javascript
from codeschmiede.pruefung.orchestrator import pruefe
from codeschmiede.sandbox.result import RunLimits

from .conftest import braucht_sandbox, schreibe_aufgabe

GENUG = RunLimits(timeout_sekunden=20)

PINGUINE = 'const kolonie = ["Pit", "Pia", "Paul"];\nfor (const pinguin of kolonie) {\n  console.log(pinguin, "bekommt einen Fisch");\n}\nconsole.log("Alle satt!");\n'


def _namen(schritt):
    return {k: v.darstellung for r in schritt.rahmen for k, v in r.variablen.items()}


def _js(runner, code, eingabe=None, limits=GENUG):
    return aufzeichnen(runner, code, limits, eingabe, "javascript")


def test_merkmale_aus_tree_sitter():
    knoten, aufrufe, methoden, eigenschaften = merkmale_javascript(
        "let a = 1;\nconst s = `x${a}`;\nif (a === 1) console.log(Math.round(2.5), [1].push(3), s.length);\nnew Map();\n")
    assert {"let", "const", "template_string", "if_statement", "===", "number"} <= knoten
    assert {"console.log", "Math.round", "Map"} <= aufrufe and {"log", "round", "push"} <= methoden
    assert eigenschaften == {"length"}
    assert merkmale_javascript("let a = ;") is None


@braucht_sandbox
def test_schleife_zeile_fuer_zeile(docker_runner):
    a = _js(docker_runner, PINGUINE)
    assert a.art == "javascript" and a.fehler is None and not a.gekuerzt
    # das Ende der Schleife hält je nach Node-Fassung noch einmal in Zeile 2
    zeilen = [s.zeile for s in a.schritte]
    assert zeilen[:8] == [1, 2, 2, 3, 2, 3, 2, 3] and zeilen[-1] == 5
    assert [_namen(s).get("pinguin") for s in a.schritte[2:8:2]] == ["'Pit'", "'Pia'", "'Paul'"]
    assert a.schritte[3].ausgabe == "Pit bekommt einen Fisch\n" and a.schritte[-1].ausgabe == "Alle satt!\n"
    liste = a.schritte[0].rahmen[0].variablen["kolonie"]
    assert liste.art == "liste" and [e.darstellung for e in liste.elemente] == ["'Pit'", "'Pia'", "'Paul'"]


@braucht_sandbox
def test_funktion_mit_rahmen_und_rueckgabe(docker_runner):
    a = _js(docker_runner, "function doppelt(x) {\n  const y = x * 2;\n  return y;\n}\n\nconst z = doppelt(4);\nconsole.log(z);\n")
    innen = [s for s in a.schritte if len(s.rahmen) == 2]
    assert innen and all(s.rahmen[1].name == "doppelt" for s in innen)
    assert innen[-1].zeile == 3 and innen[-1].rueckgabe is not None and innen[-1].rueckgabe.darstellung == "8"
    nach = a.schritte[a.schritte.index(innen[-1]) + 1]
    assert nach.zeile == 6 and _namen(nach)["z"] == "8"


@braucht_sandbox
def test_werte_objekte_und_verweise(docker_runner):
    a = _js(docker_runner, 'const a = [1, 2];\nconst b = a;\nb.push(3);\nconst o = { name: "Pit", fische: 3 };\nconst m = new Map([["x", 1]]);\nlet nichts = null;\n')
    v = a.schritte[-1].rahmen[0].variablen
    assert v["a"].kennung == v["b"].kennung and v["a"].darstellung == "[ 1, 2, 3 ]"
    assert v["o"].art == "objekt" and v["o"].darstellung == "Objekt" and v["o"].attribute["name"].darstellung == "'Pit'"
    assert v["m"].art == "woerterbuch" and v["nichts"].art == "nichts"


@braucht_sandbox
def test_laufzeitfehler_behaelt_die_schritte(docker_runner):
    a = _js(docker_runner, 'function laut(x) {\n  return x.toUpperCase();\n}\nconsole.log("vorher");\nlaut(5);\n')
    assert a.fehler == "TypeError: x.toUpperCase is not a function" and a.fehlerzeile == 2
    assert [s.zeile for s in a.schritte] == [4, 5, 2] and a.ausgabe == "vorher\n"


@braucht_sandbox
def test_syntaxfehler_ohne_schritte(docker_runner):
    a = _js(docker_runner, "let x = 1 +* 2;\n")
    assert a.fehler.startswith("SyntaxError") and a.fehlerzeile == 1 and a.schritte == []


@braucht_sandbox
def test_lange_laeufe_werden_gekuerzt_aber_laufen_zu_ende(docker_runner):
    a = _js(docker_runner, "let s = 0;\nfor (let i = 0; i < 5000; i++) {\n  s += i;\n}\nconsole.log(s);\n", limits=RunLimits(timeout_sekunden=40))
    assert a.gekuerzt and len(a.schritte) == KURS.schritte and a.ausgabe == "12497500\n"


@braucht_sandbox
def test_eingabe_und_rueckrufe(docker_runner):
    a = _js(docker_runner, 'const name = prompt("Name? ");\nsetTimeout(() => {\n  console.log("später", name);\n}, 5);\nconsole.log("Hallo", name);\n', ["Pia"])
    assert a.fehler is None and a.ausgabe == "Name? Hallo Pia\nspäter Pia\n"
    assert set(a.schritte[0].rahmen[0].variablen) == {"name"}
    assert a.schritte[-1].rahmen[-1].name == "(anonym)"


@braucht_sandbox
def test_zeitgeber_laufen_auf_eigener_uhr(docker_runner):
    """Die Halte des Verfolgers kosten echte Zeit; die eigene Uhr hält die Reihenfolge trotzdem nach den Wartezeiten."""
    code = ('const kochen = (g, ms) => new Promise((ok) => setTimeout(() => { console.log(g); ok(g); }, ms));\n'
            'async function kueche() {\n  const t = await Promise.all([kochen("Suppe", 30), kochen("Brot", 10), kochen("Limo", 5)]);\n'
            '  console.log(t.join(","));\n}\nkueche();\n')
    a = _js(docker_runner, code)
    assert a.fehler is None and a.ausgabe == "Limo\nBrot\nSuppe\nSuppe,Brot,Limo\n"


@braucht_sandbox
def test_programm_mit_prompt(settings, docker_runner):
    state = app_bauen(settings, runner=docker_runner).state.codeschmiede
    schreibe_aufgabe(settings.aufgaben_pfad, "javascript", "j901-gruss", "programm", """\
        tests_sichtbar:
          - {input: [Anna], expected: "Wie heißt du? Hallo Anna!"}
        tests_versteckt:
          - {input: [Bo], expected: "Wie heißt du? Hallo Bo!"}
        """)
    state.neu_einlesen()
    aufgabe = state.aufgaben.aufgabe("j901-gruss")
    gut = pruefe(aufgabe, 'const name = prompt("Wie heißt du? ");\nconsole.log(`Hallo ${name}!`);\n', docker_runner)
    assert gut.bestanden and gut.versteckt_pass == 1
    schlecht = pruefe(aufgabe, 'console.log("Hallo Anna!");\n', docker_runner)
    assert not schlecht.bestanden and schlecht.versteckt_fail == 1
    kaputt = pruefe(aufgabe, 'console.log("Hallo"\n', docker_runner)
    assert not kaputt.bestanden and "SyntaxError" in (kaputt.sichtbar[0].fehler or "")
