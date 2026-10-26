"""Pruefungs-Orchestrator -- wählt den Pruefer nach `task_type` aus.

Wichtig: importiert die einzelnen Pruefer-Module, damit ihre Decorator
ausgeführt werden und sich in der Registry eintragen. Wer einen neuen
`task_type` ergänzt, fügt hier einen weiteren Import hinzu.
"""

from typing import Any

from ..models.aufgabe import Aufgabe
from ..sandbox.runner import Runner
from . import code_pruefer  # noqa: F401  registriert "code_schreiben"
from . import output_quiz_pruefer  # noqa: F401  registriert "output_quiz"
from . import bug_finden_pruefer  # noqa: F401  registriert "bug_finden"
from . import lueckentext_pruefer  # noqa: F401  registriert "lueckentext"
from . import sql_pruefer  # noqa: F401  registriert "sql_abfrage" und "sql_aenderung"
from . import css_klon_pruefer  # noqa: F401  registriert "css_klon"
from . import muster_pruefer  # noqa: F401  registriert "muster_jagd"
from . import sprint_pruefer  # noqa: F401  registriert "ausgabe_sprint"
from . import roboter_pruefer  # noqa: F401  registriert "roboter"
from . import krimi_pruefer  # noqa: F401  registriert "sql_krimi"
from . import programm_pruefer  # noqa: F401  registriert "programm"
from .ergebnis import PruefErgebnis
from .registry import Pruefer, hole, ohne_geheimes


class UnbekannterAufgabentyp(ValueError):
    pass


def pruefer_fuer(aufgabe: Aufgabe) -> Pruefer:
    pruefer = hole(aufgabe.task_type)
    if pruefer is None:
        raise UnbekannterAufgabentyp(
            f"Kein Pruefer für task_type '{aufgabe.task_type}' registriert"
        )
    return pruefer


def pruefe(aufgabe: Aufgabe, code: str, runner: Runner) -> PruefErgebnis:
    return pruefer_fuer(aufgabe).pruefe(aufgabe, code, runner)


def oeffentliches_extra(aufgabe: Aufgabe) -> dict[str, Any]:
    """Die typ-eigenen Frontmatter-Felder ohne das, was der Pruefer verbirgt."""
    extra = getattr(aufgabe, "model_extra", {}) or {}
    pruefer = hole(aufgabe.task_type)
    return ohne_geheimes(extra, pruefer.verbirgt) if pruefer else dict(extra)


def anzahl_versteckt(aufgabe: Aufgabe) -> int:
    pruefer = hole(aufgabe.task_type)
    return pruefer.zaehle_versteckt(aufgabe) if pruefer else len(aufgabe.tests_versteckt)
