"""Begriffe im Code erkennen: welche Bausteine einer Sprache ein Stück Code benutzt.

Grundlage der Prüfung "nichts vorausgesetzt": der Begriffskatalog einer Sprache sagt je Begriff, woran man ihn
erkennt; ein Erkenner je Sprache liefert die benutzten Begriffe. Python liest den Syntaxbaum, SQL den Baum des
SQL-Parsers; für die übrigen Sprachen kommt der Erkenner mit ihrem Kurs (bis dahin liefern sie keine Begriffe und
werden nicht geprüft).
"""

from __future__ import annotations

import ast
from collections.abc import Callable

import sqlglot
from sqlglot import exp

from .modelle import Begriffskatalog


def merkmale_python(code: str) -> tuple[set[str], set[str], set[str], set[str]] | None:
    """Knotennamen (einschließlich Operatoren), aufgerufene Namen, Methoden und Typen fester Werte; None, wenn der
    Code nicht parst."""
    try:
        baum = ast.parse(code)
    except SyntaxError:
        return None
    knoten: set[str] = set()
    aufrufe: set[str] = set()
    methoden: set[str] = set()
    literale: set[str] = set()
    for k in ast.walk(baum):
        knoten.add(type(k).__name__)
        if isinstance(k, ast.Constant):
            literale.add(type(k.value).__name__)
        if isinstance(k, ast.Call):
            if isinstance(k.func, ast.Name):
                aufrufe.add(k.func.id)
            elif isinstance(k.func, ast.Attribute):
                methoden.add(k.func.attr)
    return knoten, aufrufe, methoden, literale


def erkenne_python(katalog: Begriffskatalog, code: str) -> set[str] | None:
    merkmale = merkmale_python(code)
    if merkmale is None:
        return None
    knoten, aufrufe, methoden, literale = merkmale
    gefunden: set[str] = set()
    for b in katalog.begriffe:
        e = b.erkennung
        if (set(e.knoten) & knoten or set(e.aufrufe) & aufrufe or set(e.methoden) & methoden
                or set(e.operatoren) & knoten or set(e.literale) & literale):
            gefunden.add(b.id)
    return gefunden


def merkmale_sql(code: str) -> tuple[set[str], set[str]] | None:
    """Ausdrucksarten des SQL-Parsers (dazu LeftJoin und RightJoin für äußere Verbindungen) und aufgerufene Funktionen
    in Großbuchstaben; None, wenn der Code nicht parst."""
    try:
        anweisungen = [a for a in sqlglot.parse(code, read="sqlite") if a is not None]
    except sqlglot.errors.SqlglotError:
        return None
    knoten: set[str] = set()
    aufrufe: set[str] = set()
    for a in anweisungen:
        for k in a.walk():
            knoten.add(type(k).__name__)
            if isinstance(k, exp.Join) and k.side:
                knoten.add(k.side.capitalize() + "Join")  # LEFT JOIN als LeftJoin
            if isinstance(k, exp.Func):
                aufrufe.add(k.name.upper() if isinstance(k, exp.Anonymous) else k.sql_name())
    return knoten, aufrufe


def erkenne_sql(katalog: Begriffskatalog, code: str) -> set[str] | None:
    merkmale = merkmale_sql(code)
    if merkmale is None:
        return None
    knoten, aufrufe = merkmale
    return {b.id for b in katalog.begriffe if set(b.erkennung.knoten) & knoten or set(b.erkennung.aufrufe) & aufrufe}


ERKENNER: dict[str, Callable[[Begriffskatalog, str], set[str] | None]] = {"python": erkenne_python, "sql": erkenne_sql}


def erkenne(katalog: Begriffskatalog, code: str) -> set[str] | None:
    """Benutzte Begriffe; None, wenn die Sprache noch keinen Erkenner hat oder der Code nicht lesbar ist."""
    erkenner = ERKENNER.get(katalog.sprache)
    return erkenner(katalog, code) if erkenner else None
