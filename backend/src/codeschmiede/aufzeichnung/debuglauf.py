"""Debugger einer Aufgabe: ihr Code läuft mit der Eingabe des Probelaufs als Aufzeichnung.

Programme bekommen die Zeilen für input() oder prompt(). Bei Funktionsaufgaben hängt eine Zeile den Aufruf mit den
Argumenten an den Code; ihre Schritte gehören nicht zum eigenen Code und fallen weg, die Rückgabe des Aufrufs steht
für sich. Vor- und Zurückspulen, Haltepunkte und Schritte über Aufrufe hinweg macht die Oberfläche auf den Schritten.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any

from ..pruefung.testlauf import FUNKTIONSNAME
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner
from .lauf import Aufzeichnung, Grenzen, Schritt, Sprache, Wert, aufzeichnen

DEBUGGER = Grenzen(schritte=2000)
"""Eigener Code mit Schleifen braucht mehr Schritte als ein Beispiel im Kurs; die Bytes bleiben die Grenze."""
MIN_SEKUNDEN = 10
"""Die Aufzeichnung bremst den Lauf, darum mindestens so viel Zeit, auch wenn die Aufgabe weniger erlaubt."""

AUFRUFE: dict[str, Callable[[str, str], str]] = {
    "python": lambda funktion, argumente: f"{funktion}(*__import__('json').loads({argumente!r}))\n",
    "javascript": lambda funktion, argumente: f";{funktion}(...JSON.parse({json.dumps(argumente)}));\n",
}


class Debuglauf(Aufzeichnung):
    rueckgabe: Wert | None = None
    """Bei Funktionsaufgaben: was der Aufruf zurückgab."""


def limits(zeitlimit_sekunden: int) -> RunLimits:
    return RunLimits(timeout_sekunden=max(zeitlimit_sekunden, MIN_SEKUNDEN))


def debuggen(runner: Runner, sprache: Sprache, code: str, limits: RunLimits, *, funktion: str | None = None,
             argumente: list[Any] | None = None, eingabe: list[str] | None = None) -> Debuglauf:
    """Zeichnet ein Programm mit den Eingabezeilen auf oder, mit `funktion`, deren Aufruf mit den Argumenten."""
    if funktion is None:
        return Debuglauf(**dict(aufzeichnen(runner, code, limits, eingabe, sprache, DEBUGGER)))
    if not FUNKTIONSNAME.match(funktion):
        raise ValueError(f"Ungültiger Funktionsname '{funktion}'")
    eigener = code.rstrip("\n")
    zeilen = eigener.count("\n") + 1
    quelltext = eigener + "\n" + AUFRUFE[sprache](funktion, json.dumps(argumente or []))
    return _ohne_aufruf(aufzeichnen(runner, quelltext, limits, None, sprache, DEBUGGER), zeilen, funktion)


def _ohne_aufruf(a: Aufzeichnung, zeilen: int, funktion: str) -> Debuglauf:
    """Schritte der angehängten Aufrufzeile fallen weg, ihre Ausgabe wandert zum nächsten eigenen Schritt."""
    schritte: list[Schritt] = []
    uebrig = ""
    for s in a.schritte:
        if s.zeile > zeilen:
            uebrig += s.ausgabe
            continue
        schritte.append(s.model_copy(update={"ausgabe": uebrig + s.ausgabe}) if uebrig else s)
        uebrig = ""
    if uebrig and schritte:
        schritte[-1] = schritte[-1].model_copy(update={"ausgabe": schritte[-1].ausgabe + uebrig})
    # Rückgabe des Aufrufs: die letzte der Funktion direkt unter dem Hauptprogramm (bei Rekursion die äußerste)
    rueckgabe = None if a.fehler else next(
        (s.rueckgabe for s in reversed(schritte) if s.rueckgabe is not None and [r.name for r in s.rahmen][1:] == [funktion]), None)
    fehlerzeile = a.fehlerzeile if a.fehlerzeile is not None and a.fehlerzeile <= zeilen else None
    return Debuglauf(**{**dict(a), "schritte": schritte, "fehlerzeile": fehlerzeile, "rueckgabe": rueckgabe})
