"""Programm-Prüfer: ein ganzes Programm läuft mit vorgegebener Eingabe, verglichen wird seine Ausgabe.

Für den Aufbaukurs, der mit `print` beginnt und Funktionen erst spät einführt. Ein Testfall ist
`{input: [Zeilen der Eingabe], expected: "erwartete Ausgabe"}`; `input()` in Python und `prompt()` in JavaScript
lesen diese Zeilen der Reihe nach (der Rahmen für JavaScript steht in programm_rahmen.js).

Die Sandbox bekommt den Code über die Standardeingabe; darum liest das Programm nicht von dort, sondern ein kleiner
Rahmen setzt je Fall eine eigene Eingabe ein, führt den Code mit frischen Namen aus und fängt die Ausgabe auf. Alle
Fälle laufen in einem Lauf. Die erwarteten Ausgaben verlassen das Backend nie; verglichen wird hier, Zeile für Zeile
ohne Leerzeichen am Zeilenende und ohne Leerzeilen am Schluss.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from ..models.aufgabe import Aufgabe
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis, TestErgebnis
from .registry import registriere
from .testlauf import hinweise, lies_block, neue_marke

PROGRAMM = "<programm>"
PROGRAMM_JS = "programm.js"
RAHMEN_JS = Path(__file__).with_name("programm_rahmen.js")
SPRACHEN = ("python", "javascript")

_RAHMEN = r'''
import io as _io, json as _j, sys as _s
_code = _j.loads(__CODE__)
_faelle = _j.loads(__FAELLE__)
_ergebnisse = []
_echt = _s.stdout
try:
    _uebersetzt = compile(_code, __DATEI__, "exec")
except SyntaxError as e:
    _uebersetzt = None
    _syntax = "SyntaxError: " + str(e.msg) + " (Zeile " + str(e.lineno) + ")"
for _eingabe in _faelle:
    if _uebersetzt is None:
        _ergebnisse.append({"ausgabe": "", "fehler": _syntax})
        continue
    _aus = _io.StringIO()
    _s.stdin = _io.StringIO("".join(z + "\n" for z in _eingabe))
    _s.stdout = _aus
    _fehler = None
    try:
        exec(_uebersetzt, {"__name__": "__main__"})
    except SystemExit:
        pass
    except BaseException as e:
        _fehler = type(e).__name__ + (": " + str(e) if str(e) else "")
    finally:
        _s.stdout = _echt
    _ergebnisse.append({"ausgabe": _aus.getvalue(), "fehler": _fehler})
print(__MARKE__)
print(_j.dumps(_ergebnisse))
'''


@dataclass
class Programmlauf:
    ergebnisse: list[dict] | None
    """Je Fall Ausgabe und Fehler; None, wenn der Lauf nicht bis zum Ende kam."""
    stderr: str
    laufzeit_ms: float
    timeout: bool


def skript(code: str, eingaben: list[list[str]], marke: str) -> str:
    return (_RAHMEN.replace("__CODE__", repr(json.dumps(code))).replace("__FAELLE__", repr(json.dumps(eingaben)))
            .replace("__DATEI__", repr(PROGRAMM)).replace("__MARKE__", repr(marke)))


def skript_javascript(code: str, eingaben: list[list[str]], marke: str) -> str:
    text = RAHMEN_JS.read_text(encoding="utf-8")
    for platzhalter, wert in {"__FAELLE__": eingaben, "__DATEI__": PROGRAMM_JS, "__MARKE__": marke, "__CODE__": code}.items():
        text = text.replace(platzhalter, json.dumps(wert))
    return text


SKRIPTE = {"python": skript, "javascript": skript_javascript}


def fuehre_programm_aus(runner: Runner, code: str, eingaben: list[list[str]], limits: RunLimits,
                        sprache: str = "python") -> Programmlauf:
    marke = neue_marke()
    erg = runner.run_code(SKRIPTE[sprache](code, eingaben, marke), sprache, limits)
    _, block = lies_block(erg, marke)
    return Programmlauf(ergebnisse=block if isinstance(block, list) else None, stderr=hinweise(erg),
                        laufzeit_ms=erg.laufzeit_ms, timeout=erg.timeout)


def normalisiert(ausgabe: str) -> str:
    return "\n".join(z.rstrip() for z in ausgabe.rstrip().split("\n"))


def _zeilen(eingabe: list) -> list[str]:
    return [str(z) for z in eingabe]


def _aufbau(aufgabe: Aufgabe) -> list[str]:
    befunde = []
    if aufgabe.sprache not in SPRACHEN:
        befunde.append(f"Programm-Aufgaben gibt es nur für {' und '.join(SPRACHEN)}")
    for i, t in enumerate(aufgabe.tests_sichtbar + aufgabe.tests_versteckt):
        if not isinstance(t.expected, str):
            befunde.append(f"Test {i + 1}: expected muss die erwartete Ausgabe als Text sein")
    if not aufgabe.tests_sichtbar:
        befunde.append("mindestens ein sichtbarer Test nötig")
    return befunde


@registriere("programm", pruefe_aufbau=_aufbau)
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    if aufgabe.sprache not in SPRACHEN:
        raise ValueError(f"Aufgabe {aufgabe.id}: Programm-Aufgaben gibt es nur für {' und '.join(SPRACHEN)}")
    tests = aufgabe.tests_sichtbar + aufgabe.tests_versteckt
    lauf = fuehre_programm_aus(runner, code, [_zeilen(t.input) for t in tests], RunLimits(timeout_sekunden=aufgabe.zeitlimit_sekunden),
                               aufgabe.sprache)
    if lauf.ergebnisse is None:
        return PruefErgebnis(
            bestanden=False,
            sichtbar=[TestErgebnis(index=i, bestanden=False, eingabe=t.input, erwartet=t.expected, fehler="Programm lief nicht bis zum Ende")
                      for i, t in enumerate(aufgabe.tests_sichtbar)],
            versteckt_pass=0, versteckt_fail=len(aufgabe.tests_versteckt), laufzeit_ms=lauf.laufzeit_ms,
            stderr=lauf.stderr, timeout=lauf.timeout,
        )
    sichtbar: list[TestErgebnis] = []
    versteckt_pass = versteckt_fail = 0
    for i, (test, e) in enumerate(zip(tests, lauf.ergebnisse)):
        ok = e["fehler"] is None and normalisiert(e["ausgabe"]) == normalisiert(str(test.expected))
        if i < len(aufgabe.tests_sichtbar):
            sichtbar.append(TestErgebnis(index=i, bestanden=ok, eingabe=test.input, erwartet=test.expected,
                                         tatsaechlich=e["ausgabe"], fehler=e["fehler"]))
        elif ok:
            versteckt_pass += 1
        else:
            versteckt_fail += 1
    erste = lauf.ergebnisse[0] if lauf.ergebnisse else {"ausgabe": "", "fehler": None}
    return PruefErgebnis(
        bestanden=all(t.bestanden for t in sichtbar) and versteckt_fail == 0,
        sichtbar=sichtbar, versteckt_pass=versteckt_pass, versteckt_fail=versteckt_fail, laufzeit_ms=lauf.laufzeit_ms,
        stdout=erste["ausgabe"], stderr=(erste["fehler"] or "") + lauf.stderr, timeout=lauf.timeout,
    )
