"""Aufzeichnung eines PHP-Laufs (Nachschlag WIKI-48): Xdebug im Abbild der Fassung, der Aufzeichner steuert den Lauf
über DBGp. Ohne Docker nur das Skript; mit den Abbildern php-8.5 und php-5.6 gegen das echte PHP."""

from __future__ import annotations

import base64
import shutil
import subprocess

import pytest

from codeschmiede.aufzeichnung import aufzeichnen
from codeschmiede.aufzeichnung.debuglauf import DEBUGGER
from codeschmiede.aufzeichnung.lauf import skript_php
from codeschmiede.sandbox.docker_runner import DockerRunner
from codeschmiede.sandbox.laufzeiten import abbild
from codeschmiede.sandbox.result import RunLimits, RunResult

FASSUNGEN = ("8.5", "5.6")
WUERFEL = """<?php
function cube($n)
{
    return ($n * $n * $n);
}

$a = [1, 2, 3];
$b = array_map('cube', $a);
print_r($b);
"""


def _bilder_da() -> bool:
    if shutil.which("docker") is None:
        return False
    return all(subprocess.run(["docker", "image", "inspect", abbild(f"php-{f}")], capture_output=True).returncode == 0
               for f in FASSUNGEN)


braucht_php = pytest.mark.skipif(not _bilder_da(), reason="PHP-Abbilder fehlen (scripts/build-sandbox.sh)")


class Merker:
    """Merkt sich Laufzeit und Skript; antwortet mit einer leeren Aufzeichnung hinter der Marke."""

    def run_code(self, code, sprache, limits=None):
        self.code, self.sprache, self.limits = code, sprache, limits
        marke = base64.b64decode(code.split("$MARKE = base64_decode('")[1].split("'")[0]).decode()
        return RunResult(stdout=f"\n{marke}\n" + '{"schritte": [], "ausgabe": "", "gekuerzt": false, "fehler": null, '
                                                 '"fehlerzeile": null, "hinweise": "Deprecated: x"}\n', exit_code=0, laufzeit_ms=5)


def test_skript_mit_code_und_grenzen_in_der_fassung():
    runner = Merker()
    a = aufzeichnen(runner, "<?php echo '\\'$x';", RunLimits(timeout_sekunden=10), ["Zeile"], "php", DEBUGGER, "7.4")
    assert runner.sprache == "php-7.4" and a.art == "php" and a.hinweise == "Deprecated: x" and not a.fehler
    assert base64.b64decode(runner.code.split("$CODE = base64_decode('")[1].split("'")[0]).decode() == "<?php echo '\\'$x';"
    assert "$FRIST = microtime(true) + 8.5;" in runner.code
    assert not any(p in runner.code for p in ("__GRENZEN__", "__CODE__", "__EINGABE__", "__MARKE__", "__SEKUNDEN__"))
    assert "__SEKUNDEN__" not in skript_php("x", "m", None, DEBUGGER, 0.2) and "+ 1.0;" in skript_php("x", "m", None, DEBUGGER, 0.2)


@pytest.fixture
def php_runner() -> DockerRunner:
    return DockerRunner({f"php-{f}": abbild(f"php-{f}") for f in FASSUNGEN}, max_ausgabe_bytes=1_000_000)


def _namen(schritt):
    return [(r.name, {k: v.darstellung for k, v in r.variablen.items()}) for r in schritt.rahmen]


@braucht_php
@pytest.mark.parametrize("fassung", FASSUNGEN)
def test_aufruf_rueckkehr_und_ausgabe(php_runner, fassung):
    a = aufzeichnen(php_runner, WUERFEL, RunLimits(timeout_sekunden=15), None, "php", DEBUGGER, fassung)
    assert a.fehler is None and "[2] => 27" in a.ausgabe
    zeilen = [s.zeile for s in a.schritte]
    # Zeile 8 ruft cube auf (eingebautes array_map bleibt unsichtbar), je Aufruf ein neuer Rahmen mit $n
    eintritte = [s for s in a.schritte if s.zeile == 8 and len(s.rahmen) == 2]
    assert [_namen(s)[1] for s in eintritte] == [("cube", {"$n": "1"}), ("cube", {"$n": "2"}), ("cube", {"$n": "3"})]
    assert zeilen.count(4) == 3 and _namen(a.schritte[-1]) == [("Modul", {"$a": "[1, 2, 3]", "$b": "[1, 8, 27]"})]
    assert "Array" in "".join(s.ausgabe for s in a.schritte if s.zeile == 9)
    rueckgaben = [s.rueckgabe.darstellung for s in a.schritte if s.rueckgabe]
    assert rueckgaben == (["1", "8", "27"] if fassung.startswith("8") else [])     # erst Xdebug 3 nennt sie


@braucht_php
def test_woerterbuch_objekt_und_fehler_mit_zeile(php_runner):
    code = "<?php\nclass P { public $name = 'Ada'; }\n$p = new P();\n$w = ['a' => 1];\nthrow new Exception('Absicht');\n"
    a = aufzeichnen(php_runner, code, RunLimits(timeout_sekunden=15), None, "php", DEBUGGER, "8.5")
    werte = {k: v for r in a.schritte[-1].rahmen for k, v in r.variablen.items()}
    assert werte["$w"].art == "woerterbuch" and werte["$p"].art == "objekt" and werte["$p"].attribute["name"].darstellung == "'Ada'"
    assert a.fehlerzeile == 5 and "Absicht" in a.fehler and "beispiel.php" in a.fehler


@braucht_php
def test_syntaxfehler_ohne_schritte(php_runner):
    a = aufzeichnen(php_runner, "<?php\n$x = ;\n", RunLimits(timeout_sekunden=15), None, "php", DEBUGGER, "5.6")
    assert not a.schritte and a.fehlerzeile == 2 and "Parse error" in a.fehler
