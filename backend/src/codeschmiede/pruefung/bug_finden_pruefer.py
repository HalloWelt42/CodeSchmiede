"""Pruefer für `task_type: bug_finden`.

Eine Bug-Finden-Aufgabe gibt **gebrochenen Code** als Starter und
laesst den Nutzer den Bug fixen. Tests laufen wie bei `code_schreiben`.

Im Frontmatter:
  - `funktion`: Name der zu testenden Funktion
  - `tests_sichtbar` + `tests_versteckt`: wie gewohnt
  - `starter_code`: enthaelt den **gebuggten** Code (NICHT leer!)
  - optional `bug_hinweis`: kurze Beschreibung was kaputt ist (im
    `extra`-Block)

Pruefer-Logik ist identisch zu `code_schreiben` -- der Unterschied
liegt nur in der Aufgaben-Setup. Wir leihen uns die Skript-Bauerei
direkt vom yaml_pruefer.
"""

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis
from .registry import registriere
from .yaml_pruefer import pruefe as pruefe_code_schreiben


@registriere("bug_finden")
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    return pruefe_code_schreiben(aufgabe, code, runner)
