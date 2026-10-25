"""Pruefer für `task_type: css_klon`.

CSS-Nachbauten kann nur ein Browser rendern; geprüft wird dort (iframe
mit den `asserts`), das Backend speichert nur das Ergebnis. Ziel und
Asserts sind von Natur aus sichtbar: Wer das Ziel sieht, sieht auch
seine Stile. Ein Lauf über die Sandbox gibt es für diesen Typ nicht.
"""

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from .ergebnis import PruefErgebnis
from .registry import registriere


@registriere("css_klon", abgabe="browser")
def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    raise ValueError(f"Aufgabe {aufgabe.id} wird im Browser geprüft")
