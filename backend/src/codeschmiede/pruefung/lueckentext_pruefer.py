"""Pruefer für `task_type: lueckentext`.

Eine Lueckentext-Aufgabe definiert **Code mit Platzhaltern** der Form
`___1___`, `___2___`, ... Der Nutzer reicht eine Zuordnung
`{platzhalter: ersetzung}` als JSON ein, der Pruefer setzt sie ein,
laesst die Tests laufen.

Im Frontmatter (`extra` Block):
  - `lueckentext.template`: Code mit `___N___`-Platzhaltern
  - `lueckentext.luecken`: Liste `[{nummer, hinweis?}]` -- nur fuer UI

Wie bei `code_schreiben`:
  - `funktion`, `tests_sichtbar`, `tests_versteckt`, `zeitlimit_sekunden`

Submission-Format:
  Der Nutzer schickt entweder:
  - JSON-String `{"1": "ersetzung", "2": "ersetzung"}` ODER
  - direkt den fertig-gefuellten Code (wenn die UI das Ersetzen macht).

  Wir versuchen erst JSON zu parsen; wenn das gelingt und keys "1",
  "2", ... entdeckt werden, machen wir das Replace selbst. Sonst
  verwenden wir den Code direkt.
"""

from __future__ import annotations

import json
import re

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis
from .registry import registriere
from .yaml_pruefer import pruefe as pruefe_code_schreiben


PLATZHALTER_MUSTER = re.compile(r"___(\d+)___")


def _setze_ein(template: str, ersetzungen: dict[str, str]) -> str:
    return PLATZHALTER_MUSTER.sub(
        lambda m: ersetzungen.get(m.group(1), m.group(0)),
        template,
    )


@registriere("lueckentext")
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    extra = getattr(aufgabe, "model_extra", {}) or {}
    lueckentext = extra.get("lueckentext", {}) or {}
    template = lueckentext.get("template", "")

    # Versuche JSON-Map zu parsen
    finaler_code = code
    if template:
        try:
            ersetzungen_roh = json.loads(code)
            if isinstance(ersetzungen_roh, dict):
                # Alle Werte zu Strings normalisieren
                ersetzungen = {str(k): str(v) for k, v in ersetzungen_roh.items()}
                finaler_code = _setze_ein(template, ersetzungen)
        except (json.JSONDecodeError, ValueError):
            # War kein JSON -- nimm Code wie er ist
            pass

    return pruefe_code_schreiben(aufgabe, finaler_code, runner)
