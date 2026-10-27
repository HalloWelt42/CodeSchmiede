"""YAML lesen, für Aufgaben, Pfade, Konfiguration und Kurs an einer Stelle.

Mit libyaml (in den Wheels von PyYAML enthalten) liest der C-Leser, sonst der aus reinem Python; beide liefern
dasselbe (am ganzen Bestand verglichen), der C-Leser etwa achtmal schneller. Das zählt beim Start, der rund 2700
Dateien liest.
"""

from typing import Any

import yaml

_LESER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def lies_yaml(text: str) -> Any:
    return yaml.load(text, Loader=_LESER)
