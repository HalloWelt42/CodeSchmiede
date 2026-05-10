"""Pruefer-Registry. Plugin-Pattern fuer Aufgaben-Typen (`task_type`).

Jeder Pruefer registriert sich per `@registriere(typ)`-Decorator. Der
Orchestrator schaut hier nach, welcher Pruefer fuer den `task_type`
einer Aufgabe zustaendig ist. Neue Aufgabentypen (Output-Quiz,
Bug-Finden, ...) brauchen nur eine neue Pruefer-Datei mit Decorator,
keine Aenderung am Orchestrator.
"""

from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models.aufgabe import Aufgabe
    from ..sandbox.runner import Runner
    from .ergebnis import PruefErgebnis


PrueferFn = Callable[["Aufgabe", str, "Runner"], "PruefErgebnis"]

PRUEFER_REGISTRY: dict[str, PrueferFn] = {}


def registriere(typ: str) -> Callable[[PrueferFn], PrueferFn]:
    def deko(fn: PrueferFn) -> PrueferFn:
        PRUEFER_REGISTRY[typ] = fn
        return fn
    return deko


def hole(typ: str) -> PrueferFn | None:
    return PRUEFER_REGISTRY.get(typ)
