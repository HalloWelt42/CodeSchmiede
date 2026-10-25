"""Pruefer-Registry. Plugin-Pattern für Aufgaben-Typen (`task_type`).

Jeder Pruefer registriert sich per `@registriere(typ)`-Decorator. Dabei
legt er fest,
- welche Felder seines `extra`-Blocks nie an den Browser gehen
  (`verbirgt`, Punktpfade wie "quiz.richtig_index"),
- auf welchem Weg Abgaben kommen (`abgabe`): "server" prüft hier,
  "browser" schickt eine Messung (CSS-Nachbauten, die nur ein Browser
  rendern kann), aus der `werte` das Ergebnis macht; "runde" gibt über
  eine Spielrunde ab (Sprint),
- ob die Abgabe selbst geschriebener Code ist, dessen Zeichen sich mit
  Musterlösung und früheren Versuchen vergleichen lassen
  (`vergleicht_zeichen`; nicht bei gewählten Antworten), und
- wie viele versteckte Tests eine Aufgabe hat (`zaehle_versteckt`,
  Vorgabe: die `tests_versteckt` aus dem Frontmatter), und
- was an seinem `extra`-Block nicht stimmt (`pruefe_aufbau`, für die
  Bestandsprüfung; Vorgabe: nichts).

Neue Aufgabentypen brauchen nur eine neue Pruefer-Datei mit Decorator.
"""

import copy
from collections.abc import Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from ..models.aufgabe import Aufgabe
    from ..sandbox.runner import Runner
    from .ergebnis import Messung, PruefErgebnis


Abgabeweg = Literal["server", "browser", "runde"]
PrueferFn = Callable[["Aufgabe", str, "Runner"], "PruefErgebnis"]
# Aufgabe, Code, Messung des Browsers, Zeichen der kürzesten Musterlösung
WerteFn = Callable[["Aufgabe", str, "Messung", int | None], "PruefErgebnis"]
ZaehlFn = Callable[["Aufgabe"], int]
AufbauFn = Callable[["Aufgabe"], list[str]]


def _versteckte_aus_frontmatter(aufgabe: "Aufgabe") -> int:
    return len(aufgabe.tests_versteckt)


def _kein_befund(aufgabe: "Aufgabe") -> list[str]:
    return []


@dataclass(frozen=True)
class Pruefer:
    pruefe: PrueferFn
    verbirgt: tuple[str, ...] = ()
    abgabe: Abgabeweg = "server"
    zaehle_versteckt: ZaehlFn = _versteckte_aus_frontmatter
    vergleicht_zeichen: bool = True
    pruefe_aufbau: AufbauFn = _kein_befund
    # nur bei abgabe "browser": macht aus der Messung das Ergebnis
    werte: WerteFn | None = None


PRUEFER_REGISTRY: dict[str, Pruefer] = {}


def registriere(
    typ: str,
    verbirgt: tuple[str, ...] = (),
    abgabe: Abgabeweg = "server",
    zaehle_versteckt: ZaehlFn = _versteckte_aus_frontmatter,
    vergleicht_zeichen: bool = True,
    pruefe_aufbau: AufbauFn = _kein_befund,
    werte: WerteFn | None = None,
) -> Callable[[PrueferFn], PrueferFn]:
    if (abgabe == "browser") != (werte is not None):
        raise ValueError(f"{typ}: genau die Abgabe 'browser' braucht eine Wertung der Messung")

    def deko(fn: PrueferFn) -> PrueferFn:
        PRUEFER_REGISTRY[typ] = Pruefer(
            pruefe=fn,
            verbirgt=verbirgt,
            abgabe=abgabe,
            zaehle_versteckt=zaehle_versteckt,
            vergleicht_zeichen=vergleicht_zeichen,
            pruefe_aufbau=pruefe_aufbau,
            werte=werte,
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
