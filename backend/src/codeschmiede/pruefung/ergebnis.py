"""Ergebnis-Modelle einer Pruefung.

`TestErgebnis` ist ein einzelner sichtbarer Test. `PruefErgebnis` ist
die Antwort an das Frontend: aggregiert + Nutzerausgabe + Laufzeit.
Versteckte Tests werden nur als Anzahl durchgereicht (Anti-Hardcoding).
"""

from typing import Any

from pydantic import BaseModel


class TestErgebnis(BaseModel):
    index: int
    bestanden: bool
    eingabe: list[Any] = []
    erwartet: Any = None
    tatsaechlich: Any = None
    fehler: str | None = None


class PruefErgebnis(BaseModel):
    bestanden: bool
    sichtbar: list[TestErgebnis]
    versteckt_pass: int
    versteckt_fail: int
    laufzeit_ms: float
    stdout: str = ""
    stderr: str = ""
    timeout: bool = False
