"""Pruefer-Registry. Plugin-Pattern für Aufgaben-Typen (`task_type`).

Jeder Pruefer registriert sich per `@registriere(typ)`-Decorator. Dabei
legt er fest,
- welche Felder seines `extra`-Blocks nie an den Browser gehen
  (`verbirgt`, Punktpfade wie "quiz.richtig_index"),
- ob seine Aufgaben im Browser geprüft werden (`im_browser`, etwa
  CSS-Nachbauten, die nur ein Browser rendern kann), und
- wie viele versteckte Tests eine Aufgabe hat (`zaehle_versteckt`,
  Vorgabe: die `tests_versteckt` aus dem Frontmatter).

Neue Aufgabentypen brauchen nur eine neue Pruefer-Datei mit Decorator.
"""

import copy
from collections.abc import Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..models.aufgabe import Aufgabe
    from ..sandbox.runner import Runner
    from .ergebnis import PruefErgebnis


PrueferFn = Callable[["Aufgabe", str, "Runner"], "PruefErgebnis"]
ZaehlFn = Callable[["Aufgabe"], int]


def _versteckte_aus_frontmatter(aufgabe: "Aufgabe") -> int:
    return len(aufgabe.tests_versteckt)


@dataclass(frozen=True)
class Pruefer:
    pruefe: PrueferFn
    verbirgt: tuple[str, ...] = ()
    im_browser: bool = False
    zaehle_versteckt: ZaehlFn = _versteckte_aus_frontmatter


PRUEFER_REGISTRY: dict[str, Pruefer] = {}


def registriere(
    typ: str,
    verbirgt: tuple[str, ...] = (),
    im_browser: bool = False,
    zaehle_versteckt: ZaehlFn = _versteckte_aus_frontmatter,
) -> Callable[[PrueferFn], PrueferFn]:
    def deko(fn: PrueferFn) -> PrueferFn:
        PRUEFER_REGISTRY[typ] = Pruefer(
            pruefe=fn, verbirgt=verbirgt, im_browser=im_browser, zaehle_versteckt=zaehle_versteckt
        )
        return fn
    return deko


def hole(typ: str) -> Pruefer | None:
    return PRUEFER_REGISTRY.get(typ)


def ohne_geheimes(extra: dict[str, Any], verbirgt: tuple[str, ...]) -> dict[str, Any]:
    """Kopie von `extra` ohne die verborgenen Punktpfade."""
    sauber = copy.deepcopy(extra)
    for pfad in verbirgt:
        *eltern, blatt = pfad.split(".")
        knoten: Any = sauber
        for teil in eltern:
            knoten = knoten.get(teil) if isinstance(knoten, dict) else None
        if isinstance(knoten, dict):
            knoten.pop(blatt, None)
    return sauber
