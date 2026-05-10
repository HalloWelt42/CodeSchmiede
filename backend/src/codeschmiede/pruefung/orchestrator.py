"""Pruefungs-Orchestrator -- waehlt den Pruefer nach `task_type` aus.

Wichtig: importiert die einzelnen Pruefer-Module, damit ihre Decorator
ausgeführt werden und sich in der Registry eintragen. Wer einen neuen
`task_type` ergaenzt, fuegt hier einfach einen weiteren `from . import
xxx_pruefer  # noqa: F401` hinzu -- mehr nicht.
"""

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from . import yaml_pruefer  # noqa: F401  registriert "code_schreiben"
from .ergebnis import PruefErgebnis
from .registry import hole


def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    pruefer = hole(aufgabe.task_type)
    if pruefer is None:
        raise ValueError(
            f"Kein Pruefer für task_type '{aufgabe.task_type}' registriert"
        )
    return pruefer(aufgabe, code, runner)
