"""Kodierung der Rückgabewerte zwischen Sandbox und Backend.

Die Sandbox schreibt Rückgaben als JSON mit Typmarken, damit Tupel,
Mengen, Wörterbücher mit beliebigen Schlüsseln, nicht endliche Zahlen
und `undefined` erhalten bleiben:

    {"__t": [...]}        Tupel
    {"__s": [...]}        Menge
    {"__d": [[k, v], ...]} Wörterbuch / Objekt / Map
    {"__f": "nan"}        nicht endliche Zahl
    {"__u": 1}            undefined (JavaScript)
    {"__r": "Typ: ..."}   nicht vergleichbarer Wert (eigene Klasse o. ä.)

Dekodiert entstehen nur eingebaute Python-Werte. Verglichen wird im
Backend mit `==`; eigene Klassen des Nutzers kommen nie bis hierher,
ein umgebogenes `__eq__` hat also keine Wirkung.
"""

import math
from typing import Any


class _Undefiniert:
    """`undefined` aus JavaScript. Gleich nur sich selbst, nie `None`."""

    _instanz: "_Undefiniert | None" = None

    def __new__(cls) -> "_Undefiniert":
        if cls._instanz is None:
            cls._instanz = super().__new__(cls)
        return cls._instanz

    def __repr__(self) -> str:
        return "undefined"


UNDEFINIERT = _Undefiniert()


class Unbekannt:
    """Wert, den die Sandbox nicht abbilden konnte. Ist nie gleich etwas."""

    def __init__(self, beschreibung: str):
        self.beschreibung = beschreibung

    def __eq__(self, anderes: object) -> bool:
        return False

    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:
        return self.beschreibung


_NICHT_ENDLICH = {
    "nan": math.nan, "NaN": math.nan,
    "inf": math.inf, "Infinity": math.inf,
    "-inf": -math.inf, "-Infinity": -math.inf,
}


def dekodiere(roh: Any) -> Any:
    if isinstance(roh, list):
        return [dekodiere(x) for x in roh]
    if not isinstance(roh, dict):
        return roh
    if "__t" in roh:
        return tuple(dekodiere(x) for x in roh["__t"])
    if "__s" in roh:
        elemente = [dekodiere(x) for x in roh["__s"]]
        try:
            return set(elemente)
        except TypeError:
            return Unbekannt(f"Menge mit nicht hashbaren Elementen: {elemente!r}"[:200])
    if "__d" in roh:
        paare = [(dekodiere(k), dekodiere(v)) for k, v in roh["__d"]]
        try:
            return dict(paare)
        except TypeError:
            return Unbekannt(f"Wörterbuch mit nicht hashbaren Schlüsseln: {paare!r}"[:200])
    if "__f" in roh:
        return _NICHT_ENDLICH.get(str(roh["__f"]), math.nan)
    if "__u" in roh:
        return UNDEFINIERT
    if "__r" in roh:
        return Unbekannt(str(roh["__r"]))
    return Unbekannt(f"Unbekannte Kodierung: {roh!r}"[:200])


def gleich(ist: Any, soll: Any) -> bool:
    try:
        return bool(ist == soll)
    except Exception:
        return False


def anzeigen(wert: Any) -> Any:
    """Macht einen dekodierten Wert JSON-tauglich für die Anzeige."""
    if isinstance(wert, (_Undefiniert, Unbekannt)):
        return repr(wert)
    if isinstance(wert, float) and not math.isfinite(wert):
        return repr(wert)
    if isinstance(wert, (list, tuple)):
        return [anzeigen(x) for x in wert]
    if isinstance(wert, (set, frozenset)):
        return sorted((anzeigen(x) for x in wert), key=repr)
    if isinstance(wert, dict):
        return {
            (k if isinstance(k, str) else repr(k)): anzeigen(v) for k, v in wert.items()
        }
    return wert
