"""Lecksuche -- findet versteckte Tests, die der Aufgabentext verrät.

Ein versteckter Test gilt als verraten, wenn eine Zeile aus Beschreibung
oder Hinweisen (Beispieltabelle, Aufzählung) alle seine Eingaben und
seine Erwartung zeigt. Dann ließe sich das Ergebnis abschreiben statt
berechnen. Kleine Zahlen, leere Werte und Wahrheitswerte allein zählen
nicht, die stehen in jedem Text.
"""

import json
import re
from typing import Any

from ..models.aufgabe import Aufgabe, TestFall


def _schreibweisen(wert: Any) -> set[str]:
    formen = {json.dumps(wert, ensure_ascii=False), repr(wert)}
    if isinstance(wert, str):
        formen |= {wert, f'"{wert}"', f"'{wert}'"}
    if isinstance(wert, bool):
        formen |= {"True" if wert else "False", "true" if wert else "false"}
    if isinstance(wert, list):
        formen.add(json.dumps(wert, ensure_ascii=False, separators=(",", ":")))
    return formen


def _steht_in(wert: Any, zeile: str) -> bool:
    if isinstance(wert, (int, float)) and not isinstance(wert, bool):
        # Zahlen nur als ganzes Wort, sonst steckt 12 in 120
        return any(
            re.search(rf"(?<![\w.]){re.escape(f)}(?![\w.]|\.\d)", zeile) for f in _schreibweisen(wert)
        )
    if isinstance(wert, str) and len(wert) < 4:
        return any(f in zeile for f in (f'"{wert}"', f"'{wert}'", f"`{wert}`"))
    return any(f in zeile for f in _schreibweisen(wert))


def _belanglos(wert: Any) -> bool:
    if isinstance(wert, bool) or wert is None:
        return True
    if isinstance(wert, (int, float)) and abs(wert) < 10:
        return True
    if isinstance(wert, (str, list, dict)) and len(wert) <= (1 if isinstance(wert, str) else 0):
        return True
    return False


def ist_verraten(test: TestFall, text: str) -> bool:
    if all(_belanglos(a) for a in test.input) and _belanglos(test.expected):
        return False
    return any(
        all(_steht_in(a, zeile) for a in test.input) and _steht_in(test.expected, zeile)
        for zeile in text.splitlines()
        if zeile.strip()
    )


def aufgabentext(aufgabe: Aufgabe) -> str:
    return aufgabe.beschreibung_md + "\n" + "\n".join(h.text for h in aufgabe.hints)


def verratene_tests(aufgabe: Aufgabe) -> list[int]:
    """Indizes der verratenen Tests in `tests_versteckt`."""
    text = aufgabentext(aufgabe)
    return [i for i, t in enumerate(aufgabe.tests_versteckt) if ist_verraten(t, text)]
