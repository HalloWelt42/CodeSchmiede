"""Begriffe im Code erkennen: welche Bausteine einer Sprache ein Stück Code benutzt.

Grundlage der Prüfung "nichts vorausgesetzt": der Begriffskatalog einer Sprache sagt je Begriff, woran man ihn
erkennt; ein Erkenner je Sprache liefert die benutzten Begriffe. Python liest den Syntaxbaum, SQL den Baum des
SQL-Parsers, JavaScript den Baum von tree-sitter, CSS die Regeln von tinycss2 und das Markup der Beispiele und
Aufgaben über html.parser.
"""

from __future__ import annotations

import ast
from collections.abc import Callable
from dataclasses import dataclass, field
from html.parser import HTMLParser

import sqlglot
import tinycss2
import tree_sitter_javascript
from sqlglot import exp
from tree_sitter import Language, Node, Parser

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


_JS = Parser(Language(tree_sitter_javascript.language()))


def merkmale_javascript(code: str) -> tuple[set[str], set[str], set[str], set[str]] | None:
    """Knotenarten von tree-sitter, benannte (if_statement, template_string, arrow_function ...) wie unbenannte
    (Operatoren und Schlüsselwörter: ===, %, let, const, new ...), aufgerufene Namen (prompt, Number, dazu
    console.log und Math.round als Name mit Punkt), Methoden (push, toUpperCase ...) und gelesene Eigenschaften
    (length ...); None, wenn der Code nicht parst."""
    baum = _JS.parse(code.encode())
    if baum.root_node.has_error:
        return None
    knoten: set[str] = set()
    aufrufe: set[str] = set()
    methoden: set[str] = set()
    eigenschaften: set[str] = set()
    offen: list[Node] = [baum.root_node]
    while offen:
        k = offen.pop()
        knoten.add(k.type)
        offen.extend(k.children)
        if k.type == "member_expression" and (e := k.child_by_field_name("property")) is not None and e.text:
            ist_aufruf = k.parent is not None and k.parent.type == "call_expression" and k.parent.child_by_field_name("function") == k
            if not ist_aufruf:
                eigenschaften.add(e.text.decode())
        if k.type not in ("call_expression", "new_expression"):
            continue
        ziel = k.child_by_field_name("function" if k.type == "call_expression" else "constructor")
        if ziel is None or ziel.text is None:
            continue
        if ziel.type == "identifier":
            aufrufe.add(ziel.text.decode())
        elif ziel.type == "member_expression" and (eigenschaft := ziel.child_by_field_name("property")) is not None and eigenschaft.text:
            methoden.add(eigenschaft.text.decode())
            objekt = ziel.child_by_field_name("object")
            if objekt is not None and objekt.type == "identifier" and objekt.text:
                aufrufe.add(f"{objekt.text.decode()}.{eigenschaft.text.decode()}")
    return knoten, aufrufe, methoden, eigenschaften


def erkenne_javascript(katalog: Begriffskatalog, code: str) -> set[str] | None:
    merkmale = merkmale_javascript(code)
    if merkmale is None:
        return None
    knoten, aufrufe, methoden, eigenschaften = merkmale
    gefunden: set[str] = set()
    for b in katalog.begriffe:
        e = b.erkennung
        if (set(e.knoten) & knoten or set(e.operatoren) & knoten or set(e.literale) & knoten
                or set(e.aufrufe) & aufrufe or set(e.methoden) & methoden or set(e.eigenschaften) & eigenschaften):
            gefunden.add(b.id)
    return gefunden


@dataclass
class MerkmaleCss:
    """Was ein Stück CSS oder Markup benutzt (Felder wie in Erkennung)."""

    knoten: set[str] = field(default_factory=set)
    aufrufe: set[str] = field(default_factory=set)
    literale: set[str] = field(default_factory=set)
    eigenschaften: set[str] = field(default_factory=set)
    werte: set[str] = field(default_factory=set)
    elemente: set[str] = field(default_factory=set)
    attribute: set[str] = field(default_factory=set)


class _Markup(HTMLParser):
    def __init__(self, merkmale: MerkmaleCss):
        super().__init__()
        self.merkmale = merkmale

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.merkmale.elemente.add(tag)
        self.merkmale.attribute.update(name for name, _ in attrs)
        if any(name == "style" for name, _ in attrs):
            for name, wert in attrs:
                if name == "style" and wert:
                    _werte_lesen(self.merkmale, tinycss2.parse_blocks_contents(wert))

    def handle_comment(self, data: str) -> None:
        self.merkmale.knoten.add("kommentar")


def _selektor_lesen(m: MerkmaleCss, teile: list) -> None:
    """Selektorarten: typ, klasse, id, universal, attribut, gruppe, nachfahre, kind, nachbar, geschwister, dazu
    Pseudoklassen (:first-child) und Pseudoelemente (::before) mit Namen."""
    vorher = None  # letztes Zeichen ohne Leerraum
    leer = False
    i = 0
    while i < len(teile):
        t = teile[i]
        if t.type == "whitespace":
            leer = True
            i += 1
            continue
        if t.type == "literal" and t.value == ":":
            doppelt = i + 1 < len(teile) and teile[i + 1].type == "literal" and teile[i + 1].value == ":"
            if doppelt:
                i += 1
            name = teile[i + 1] if i + 1 < len(teile) else None
            if name is not None and name.type in ("ident", "function"):
                m.knoten.add(("::" if doppelt else ":") + name.lower_value if name.type == "ident" else
                             ("::" if doppelt else ":") + name.lower_name)
                if name.type == "function":
                    _werte_lesen(m, name.arguments)
                i += 1
            m.knoten.add("pseudoelement" if doppelt else "pseudoklasse")
            vorher, leer = "zusatz", False
            i += 1
            continue
        verbinder = t.type == "literal" and t.value in (",", ">", "+", "~")
        if leer and vorher not in (None, "verbinder") and not verbinder:
            m.knoten.add("nachfahre")
        leer = False
        if verbinder:
            m.knoten.add({",": "gruppe", ">": "kind", "+": "nachbar", "~": "geschwister"}[t.value])
            vorher = "verbinder"
        elif t.type == "ident":
            m.knoten.add("typ")
            m.elemente.add(t.lower_value)
            vorher = "teil"
        elif t.type == "literal" and t.value == "." and i + 1 < len(teile) and teile[i + 1].type == "ident":
            m.knoten.add("klasse")
            i += 1
            vorher = "teil"
        elif t.type == "hash":
            m.knoten.add("id")
            vorher = "teil"
        elif t.type == "literal" and t.value == "*":
            m.knoten.add("universal")
            vorher = "teil"
        elif t.type == "[] block":
            m.knoten.add("attribut")
            vorher = "teil"
        else:
            vorher = "teil"
        i += 1


def _werte_lesen(m: MerkmaleCss, teile: list, eigenschaft: str | None = None) -> None:
    for t in teile:
        if t.type == "declaration":
            name = t.lower_name
            if name.startswith("--"):
                m.knoten.add("eigene_eigenschaft")
            else:
                m.eigenschaften.add(name)
            if t.important:
                m.knoten.add("!important")
            _werte_lesen(m, t.value, name)
        elif t.type == "dimension":
            m.literale.add(t.lower_unit)
        elif t.type == "percentage":
            m.literale.add("%")
        elif t.type == "number":
            m.literale.add("zahl")
        elif t.type == "hash":
            m.literale.add("hex")
        elif t.type == "string":
            m.literale.add("text")
        elif t.type == "ident" and eigenschaft:
            m.werte.update((f"{eigenschaft}:{t.lower_value}", f"*:{t.lower_value}"))
        elif t.type == "function":
            m.aufrufe.add(t.lower_name)
            _werte_lesen(m, t.arguments, eigenschaft)
        elif t.type in ("() block", "[] block", "{} block"):
            _werte_lesen(m, t.content, eigenschaft)
        elif t.type == "comment":
            m.knoten.add("kommentar")


def _regeln_lesen(m: MerkmaleCss, regeln: list) -> bool:
    for r in regeln:
        if r.type == "error":
            return False
        if r.type == "comment":
            m.knoten.add("kommentar")
        elif r.type == "at-rule":
            m.knoten.add("@" + r.lower_at_keyword)
            _werte_lesen(m, r.prelude)
            if r.content is not None:
                innen = tinycss2.parse_rule_list(r.content, skip_comments=False, skip_whitespace=True)
                if r.lower_at_keyword == "keyframes":
                    for schritt in innen:
                        if schritt.type == "qualified-rule":
                            _werte_lesen(m, tinycss2.parse_blocks_contents(schritt.content, skip_comments=False))
                elif not _regeln_lesen(m, innen):
                    return False
        elif r.type == "qualified-rule":
            m.knoten.add("regel")
            _selektor_lesen(m, r.prelude)
            inhalt = tinycss2.parse_blocks_contents(r.content, skip_comments=False, skip_whitespace=True)
            if any(t.type == "error" for t in inhalt):
                return False
            _werte_lesen(m, inhalt)
    return True


def merkmale_css(code: str) -> MerkmaleCss | None:
    """Merkmale eines Stücks CSS (Selektorarten, Pseudoklassen und at-Regeln als Knoten, Funktionen wie rgb und calc
    als Aufrufe, Einheiten, hex, zahl und text als Literale, Eigenschaften, Schlüsselwörter als eigenschaft:wert) oder,
    wenn es mit < beginnt, eines Stücks Markup (Elemente und Attribute); None, wenn das CSS nicht lesbar ist."""
    m = MerkmaleCss()
    if code.lstrip().startswith("<"):
        _Markup(m).feed(code)
        return m
    regeln = tinycss2.parse_stylesheet(code, skip_comments=False, skip_whitespace=True)
    return m if _regeln_lesen(m, regeln) else None


def erkenne_css(katalog: Begriffskatalog, code: str) -> set[str] | None:
    m = merkmale_css(code)
    if m is None:
        return None
    gefunden: set[str] = set()
    for b in katalog.begriffe:
        e = b.erkennung
        if (set(e.knoten) & m.knoten or set(e.aufrufe) & m.aufrufe or set(e.literale) & m.literale
                or set(e.eigenschaften) & m.eigenschaften or set(e.werte) & m.werte
                or set(e.elemente) & m.elemente or set(e.attribute) & m.attribute):
            gefunden.add(b.id)
    return gefunden


ERKENNER: dict[str, Callable[[Begriffskatalog, str], set[str] | None]] = {"python": erkenne_python, "sql": erkenne_sql,
                                                                            "javascript": erkenne_javascript, "css": erkenne_css}


def erkenne(katalog: Begriffskatalog, code: str) -> set[str] | None:
    """Benutzte Begriffe; None, wenn die Sprache noch keinen Erkenner hat oder der Code nicht lesbar ist."""
    erkenner = ERKENNER.get(katalog.sprache)
    return erkenner(katalog, code) if erkenner else None
