"""Ausführen ohne Aufzeichnung, für Sprachen ohne Debugger (heute PHP; Nachschlag WIKI-48): Ausgabe, Hinweise und
Fehler mit Zeile, so wie die Ebene Ausprobieren sie zeigt. PHP nennt seinen Code "Standard input code"; in Meldungen
heißt er wie im Editor. Dazu die Funktionen, die eine PHP-Fassung kennt: der Editor markiert damit Aufrufe, die es in
der gewählten Fassung nicht gibt (WIKI-52, Wahl des Nutzers: die Wahrheit ist die Sandbox selbst)."""

from __future__ import annotations

import json
import re

from pydantic import BaseModel

from .laufzeiten import laufzeit
from .result import RunLimits
from .runner import Runner, SandboxFehler

#: wie der Code in Meldungen heißt (wie die Datei im Editor)
DATEINAMEN = {"php": "beispiel.php", "python": "beispiel.py", "javascript": "beispiel.js"}
#: so nennt PHP Code, der über stdin kam
PHP_EINGABE = "Standard input code"
#: Zeile in einer Meldung: "on line 3" oder "beispiel.php:3" (Stapel)
ZEILE = re.compile(r"on line (\d+)|\.php:(\d+)")

FUNKTIONEN_CODE = "<?php echo json_encode(get_defined_functions()['internal']);"


class Ausfuehrung(BaseModel):
    art: str
    ausgabe: str = ""
    hinweise: str = ""                  # Warnungen eines Laufs, der trotzdem zu Ende kam
    fehler: str | None = None
    fehlerzeile: int | None = None
    gekuerzt: bool = False
    zeitueberschreitung: bool = False
    laufzeit_ms: float = 0


def ausfuehren(runner: Runner, code: str, sprache: str, fassung: str, limits: RunLimits) -> Ausfuehrung:
    ergebnis = runner.run_code(code, laufzeit(sprache, fassung), limits)
    meldungen = ergebnis.stderr.replace(PHP_EINGABE, DATEINAMEN.get(sprache, "beispiel")).strip()
    gescheitert = ergebnis.exit_code != 0 or ergebnis.timeout or ergebnis.gekuerzt
    fehler = None
    if ergebnis.timeout:
        fehler = f"Zeit überschritten: nach {limits.timeout_sekunden} s abgebrochen"
    elif ergebnis.gekuerzt:
        fehler = "Zu viel Ausgabe: der Lauf wurde abgebrochen"
    elif gescheitert:
        fehler = meldungen or f"Abgebrochen mit Code {ergebnis.exit_code}"
    zeile = ZEILE.search(meldungen) if gescheitert else None
    return Ausfuehrung(art=sprache, ausgabe=ergebnis.stdout, hinweise="" if gescheitert else meldungen, fehler=fehler,
                       fehlerzeile=int(zeile.group(1) or zeile.group(2)) if zeile else None, gekuerzt=ergebnis.gekuerzt,
                       zeitueberschreitung=ergebnis.timeout, laufzeit_ms=ergebnis.laufzeit_ms)


def php_funktionen(runner: Runner, fassung: str, limits: RunLimits) -> list[str]:
    """Die eingebauten Funktionen einer PHP-Fassung (klein geschrieben, sortiert), gefragt beim Abbild selbst."""
    ergebnis = runner.run_code(FUNKTIONEN_CODE, laufzeit("php", fassung), limits)
    if ergebnis.exit_code != 0:
        raise SandboxFehler(f"PHP {fassung} nennt seine Funktionen nicht: {ergebnis.stderr.strip()[:200]}")
    return sorted(json.loads(ergebnis.stdout))
