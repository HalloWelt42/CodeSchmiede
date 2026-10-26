"""Ablauf einer SQL-Abfrage: das Ergebnis und je Klausel die Zwischentabelle, in der Reihenfolge der Abarbeitung.

Die Datenbank arbeitet eine Abfrage anders ab, als man sie schreibt: FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT,
DISTINCT, ORDER BY, LIMIT. Dafür zerlegt der SQL-Parser die Abfrage in Teilabfragen, die nacheinander eine Klausel mehr
enthalten. Alle laufen in der Sandbox auf dem Datensatz wie jede andere Abfrage (sql_pruefer.skript), hier wird nur
verglichen: welche Zeilen ein Filter behält, welche Spalten SELECT fallen lässt, welche Zeilen eine Gruppe bilden.

Zerlegt wird eine einzelne SELECT-Abfrage ohne WITH und ohne UNION; alles andere liefert nur das Ergebnis.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Literal

import sqlglot
from pydantic import BaseModel, Field
from sqlglot import exp

from ..pruefung.sql_pruefer import skript
from ..pruefung.testlauf import hinweise, lies_block, neue_marke
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner

Zeilenzustand = Literal["", "neu", "bleibt", "raus"]
GRUPPE = "__gruppe"


class Zwischentabelle(BaseModel):
    spalten: list[str]
    zeilen: list[list[Any]]
    zustand: list[Zeilenzustand] = Field(default_factory=list)
    """Je Zeile: neu geholt, bleibt oder fällt heraus (leer: nichts Besonderes)."""
    weg: list[bool] = Field(default_factory=list)
    """Je Spalte: fällt durch SELECT weg."""
    gruppe: list[int] = Field(default_factory=list)
    """Je Zeile die Nummer ihrer Gruppe ab 1 (nur nach GROUP BY)."""


class Klauselschritt(BaseModel):
    klausel: str
    zeile: int | None
    """Zeile der Klausel im Code, ab 1."""
    text: str
    tabelle: Zwischentabelle


class SqlLauf(BaseModel):
    art: Literal["sql"] = "sql"
    spalten: list[str] = Field(default_factory=list)
    zeilen: list[list[Any]] = Field(default_factory=list)
    schritte: list[Klauselschritt] = Field(default_factory=list)
    fehler: str | None = None
    zeitueberschreitung: bool = False
    laufzeit_ms: float = 0

    @property
    def ausgabe(self) -> str:
        """Das Ergebnis als Text, wie Vorhersagen es schreiben: je Zeile die Werte mit " | " getrennt, ohne Kopf."""
        return als_text(self.zeilen)


def anzeigbar(zeilen: list[list[Any]]) -> list[list[Any]]:
    """Kommazahlen als Text, wie die Datenbank sie schreibt (4.0 bleibt 4.0); in JSON würde daraus sonst 4."""
    return [[str(w) if isinstance(w, float) else w for w in z] for z in zeilen]


def als_text(zeilen: list[list[Any]]) -> str:
    return "\n".join(" | ".join("NULL" if w is None else str(w) for w in z) for z in zeilen)


# ---------- Zerlegen ----------


@dataclass
class Teilabfrage:
    klausel: str
    sql: str
    deuten: Callable[[list[dict[str, Any]], int], tuple[Zwischentabelle, str]]
    """Aus allen Ergebnissen und der eigenen Stelle die Zwischentabelle und den Text bauen."""
    stichwort: str
    """Regulärer Ausdruck für die Zeile der Klausel im Code."""
    vorkommen: int = 1


def _ohne(abfrage: exp.Select, *teile: str) -> exp.Select:
    kopie = abfrage.copy()
    for teil in teile:
        kopie.set(teil, None)
    return kopie


def _text(knoten: exp.Expression | None) -> str:
    return knoten.sql(dialect="sqlite") if knoten is not None else ""


def _name(knoten: exp.Expression) -> str:
    """Name einer Tabelle ohne Kürzel (pinguine statt pinguine AS p)."""
    return knoten.name if isinstance(knoten, exp.Table) else _text(knoten)


def _tabelle(ergebnis: dict[str, Any], zustand: Zeilenzustand = "") -> Zwischentabelle:
    zeilen = ergebnis["zeilen"]
    return Zwischentabelle(spalten=ergebnis["spalten"], zeilen=zeilen, zustand=[zustand] * len(zeilen) if zustand else [])


def _gefiltert(vorher: dict[str, Any], nachher: dict[str, Any]) -> tuple[Zwischentabelle, int]:
    """Die Zeilen von vorher, jede als bleibt oder raus, je nachdem ob sie nachher noch da ist (als Vielfachmenge)."""
    uebrig = Counter(tuple(z) for z in nachher["zeilen"])
    zustand: list[Zeilenzustand] = []
    for z in vorher["zeilen"]:
        if uebrig[tuple(z)] > 0:
            uebrig[tuple(z)] -= 1
            zustand.append("bleibt")
        else:
            zustand.append("raus")
    tabelle = Zwischentabelle(spalten=vorher["spalten"], zeilen=vorher["zeilen"], zustand=zustand)
    return tabelle, zustand.count("bleibt")


def _zeilen_wort(n: int) -> str:
    return "eine Zeile" if n == 1 else f"{n} Zeilen"


def zerlege(sql: str) -> list[Teilabfrage] | None:
    """Teilabfragen in der Reihenfolge der Abarbeitung; None, wenn die Abfrage sich nicht zerlegen lässt."""
    try:
        anweisungen = [a for a in sqlglot.parse(sql, read="sqlite") if a is not None]
    except sqlglot.errors.SqlglotError:
        return None
    if len(anweisungen) != 1 or not isinstance(anweisungen[0], exp.Select):
        return None
    q = anweisungen[0]
    if q.args.get("with_") or q.args.get("with") or q.args.get("from_") is None:
        return None

    teile: list[Teilabfrage] = []
    joins = list(q.args.get("joins") or [])
    alle_spalten = _ohne(q, "where", "group", "having", "order", "limit", "offset", "distinct")
    alle_spalten.set("expressions", [exp.Star()])

    # Nach einem JOIN tragen gleichnamige Spalten den Namen ihrer Tabelle davor (p.name, k.name). Welche Spalte zu
    # welcher Tabelle gehört, zeigen die Stufen FROM und JOIN: jede bringt die Spalten einer Tabelle mehr mit.
    quellen = [q.args["from_"].this, *(j.this for j in joins)]
    bezuege = [k.alias_or_name for k in quellen]

    def herkunft(e: list[dict[str, Any]], bis: int = len(joins)) -> tuple[list[str], list[int]]:
        """Die Spalten nach dem JOIN Nummer bis (0: nur FROM) und je Spalte die Nummer ihrer Tabelle."""
        grenzen = [len(e[k]["spalten"]) for k in range(bis + 1)]
        return e[bis]["spalten"], [next(k for k, g in enumerate(grenzen) if j < g) for j in range(grenzen[-1])]

    def beschriftet(e: list[dict[str, Any]], tabelle: Zwischentabelle, bis: int = len(joins)) -> Zwischentabelle:
        if joins:
            alle, tabelle_je = herkunft(e, bis)
            kopf = [f"{bezuege[tabelle_je[j]]}.{n}" if alle.count(n) > 1 else n for j, n in enumerate(alle)]
            tabelle.spalten = kopf + tabelle.spalten[len(alle):]
        return tabelle

    # FROM und je JOIN eine Stufe mehr
    von = alle_spalten.copy()
    von.set("joins", None)
    erste = quellen[0]
    woher = ("rechnet die Datenbank die Unterabfrage hinter FROM aus" if isinstance(erste, exp.Subquery)
             else f"holt die Datenbank die Tabelle {_name(erste)}")
    teile.append(Teilabfrage("FROM", _text(von), lambda e, i, w=woher: (
        _tabelle(e[i], "neu"), f"Zuerst {w}: {_zeilen_wort(len(e[i]['zeilen']))}."), r"\bFROM\b"))
    for n, join in enumerate(joins, 1):
        stufe = alle_spalten.copy()
        stufe.set("joins", [j.copy() for j in joins[:n]])
        name = _name(join.this)
        art = "LEFT JOIN" if join.side else "JOIN"
        ohne_partner = " Zeilen ohne Partner bleiben, ihre neuen Spalten sind leer (NULL)." if join.side else ""
        teile.append(Teilabfrage(art, _text(stufe), lambda e, i, t=name, a=art, o=ohne_partner: (
            beschriftet(e, _tabelle(e[i], "neu"), i),
            f"{a} verbindet mit {t}: je passendes Paar eine Zeile, zusammen {_zeilen_wort(len(e[i]['zeilen']))}.{o}"),
            r"\bJOIN\b", n))
    vorher = len(teile) - 1

    where = q.args.get("where")
    gefiltert = alle_spalten.copy()
    if where is not None:
        gefiltert.set("where", where.copy())

        def deute_where(e: list[dict[str, Any]], i: int, v: int = vorher) -> tuple[Zwischentabelle, str]:
            t, bleiben = _gefiltert(e[v], e[i])
            return beschriftet(e, t), f"WHERE prüft jede Zeile: {bleiben} von {len(e[v]['zeilen'])} bleiben, die anderen fallen durchs Sieb."
        teile.append(Teilabfrage("WHERE", _text(gefiltert), deute_where, r"\bWHERE\b"))

    group = q.args.get("group")
    if group is not None:
        schluessel = [k.copy() for k in group.expressions]
        gruppen = gefiltert.copy()
        rang = exp.alias_(exp.Window(this=exp.Anonymous(this="DENSE_RANK"), order=exp.Order(expressions=[k.copy() for k in schluessel])), GRUPPE)
        gruppen.set("expressions", [exp.Star(), rang])
        gruppen.set("order", exp.Order(expressions=[k.copy() for k in schluessel]))
        nach = ", ".join(_text(k) for k in schluessel)

        def deute_group(e: list[dict[str, Any]], i: int, nach: str = nach) -> tuple[Zwischentabelle, str]:
            spalten = e[i]["spalten"]
            stelle = spalten.index(GRUPPE)
            zeilen = [z[:stelle] + z[stelle + 1:] for z in e[i]["zeilen"]]
            gruppe = [int(z[stelle]) for z in e[i]["zeilen"]]
            t = beschriftet(e, Zwischentabelle(spalten=spalten[:stelle] + spalten[stelle + 1:], zeilen=zeilen, gruppe=gruppe))
            anzahl = max(gruppe, default=0)
            wort = "eine Gruppe" if anzahl == 1 else f"{anzahl} Gruppen"
            return t, f"GROUP BY legt Zeilen mit gleichem Wert in {nach} zusammen: {wort}. Jede Gruppe wird nachher zu einer Zeile."
        teile.append(Teilabfrage("GROUP BY", _text(gruppen), deute_group, r"\bGROUP\s+BY\b"))

    having = q.args.get("having")
    if having is not None:
        ohne_having = _ohne(q, "having", "order", "limit", "offset", "distinct")
        teile.append(Teilabfrage("HAVING", _text(ohne_having), lambda e, i: (_tabelle(e[i]), ""), r"\bHAVING\b"))
        mit_having = _ohne(q, "order", "limit", "offset", "distinct")

        def deute_having(e: list[dict[str, Any]], i: int) -> tuple[Zwischentabelle, str]:
            t, bleiben = _gefiltert(e[i - 1], e[i])
            return t, f"HAVING prüft jede Gruppe (gezeigt mit den Spalten aus SELECT): {bleiben} von {len(e[i - 1]['zeilen'])} bleiben."
        teile.append(Teilabfrage("HAVING", _text(mit_having), deute_having, r"\bHAVING\b"))

    # SELECT: bei reinen Spalten ohne Gruppen die Zeilen von vorher, nicht gewählte Spalten durchgestrichen
    auswahl = _ohne(q, "order", "limit", "offset", "distinct")
    gewaehlt = [(s.table, s.name) if isinstance(s, exp.Column) else ("", s.alias_or_name) for s in q.expressions]
    schlicht = (group is None and not q.find(exp.AggFunc) and q.expressions
                and all(isinstance(s, exp.Column) and not isinstance(s.this, exp.Star) for s in q.expressions))
    quelle = len(teile) - 1
    liste = ", ".join(_text(s) for s in q.expressions)

    def stelle_von(e: list[dict[str, Any]], tabelle: str, name: str) -> int | None:
        """Stelle einer gewählten Spalte in der Tabelle vor SELECT; mit Tabellenname davor nur in dieser Tabelle."""
        alle, tabelle_je = herkunft(e)
        return next((j for j, n in enumerate(alle) if n == name and (not tabelle or bezuege[tabelle_je[j]] == tabelle)), None)

    def deute_select(e: list[dict[str, Any]], i: int, quelle: int = quelle) -> tuple[Zwischentabelle, str]:
        v = e[quelle]
        stellen = [stelle_von(e, t, n) for t, n in gewaehlt] if schlicht else [None]
        if None not in stellen:
            t = Zwischentabelle(spalten=v["spalten"], zeilen=v["zeilen"], weg=[j not in stellen for j in range(len(v["spalten"]))])
            return beschriftet(e, t), f"Jetzt erst wählt SELECT die Spalten {liste}; die übrigen fallen weg."
        return _tabelle(e[i], "neu"), f"SELECT berechnet die Spalten {liste}: {_zeilen_wort(len(e[i]['zeilen']))}."
    teile.append(Teilabfrage("SELECT", _text(auswahl), deute_select, r"\bSELECT\b"))

    if q.args.get("distinct"):
        mit_distinct = _ohne(q, "order", "limit", "offset")

        def deute_distinct(e: list[dict[str, Any]], i: int) -> tuple[Zwischentabelle, str]:
            gesehen: set[tuple[Any, ...]] = set()
            zustand: list[Zeilenzustand] = []
            for z in e[i - 1]["zeilen"]:
                zustand.append("raus" if tuple(z) in gesehen else "bleibt")
                gesehen.add(tuple(z))
            t = Zwischentabelle(spalten=e[i - 1]["spalten"], zeilen=e[i - 1]["zeilen"], zustand=zustand)
            return t, f"DISTINCT streicht doppelte Zeilen: {zustand.count('bleibt')} von {len(zustand)} bleiben."
        teile.append(Teilabfrage("DISTINCT", _text(mit_distinct), deute_distinct, r"\bDISTINCT\b"))

    order = q.args.get("order")
    if order is not None:
        sortiert = _ohne(q, "limit", "offset")
        reihenfolge = ", ".join(_text(o) for o in order.expressions)
        absteigend = "; DESC heißt absteigend" if any(o.args.get("desc") for o in order.expressions) else ""
        teile.append(Teilabfrage("ORDER BY", _text(sortiert), lambda e, i, r=reihenfolge, a=absteigend: (
            _tabelle(e[i]), f"ORDER BY sortiert nach {r}{a}."), r"\bORDER\s+BY\b"))

    if q.args.get("limit") is not None:
        def deute_limit(e: list[dict[str, Any]], i: int) -> tuple[Zwischentabelle, str]:
            alle, behalten = e[i - 1]["zeilen"], e[i]["zeilen"]
            start = next((s for s in range(len(alle) - len(behalten) + 1) if alle[s:s + len(behalten)] == behalten), 0)
            zustand: list[Zeilenzustand] = ["bleibt" if start <= n < start + len(behalten) else "raus" for n in range(len(alle))]
            t = Zwischentabelle(spalten=e[i - 1]["spalten"], zeilen=alle, zustand=zustand)
            return t, f"LIMIT behält nur {_zeilen_wort(len(behalten))} der {len(alle)}."
        teile.append(Teilabfrage("LIMIT", _text(q), deute_limit, r"\bLIMIT\b"))
    return teile


def _zeile(code: str, stichwort: str, vorkommen: int) -> int | None:
    """Zeile (ab 1) des n-ten Vorkommens eines Stichworts außerhalb von Texten in Hochkommas."""
    gefunden = 0
    for nr, zeile in enumerate(code.split("\n"), 1):
        ohne_texte = re.sub(r"'[^']*'", "''", zeile)
        for _ in re.finditer(stichwort, ohne_texte, re.IGNORECASE):
            gefunden += 1
            if gefunden == vorkommen:
                return nr
    return None


# ---------- Ausführen ----------


def sql_lauf(runner: Runner, datensatz_sql: str, sql: str, limits: RunLimits | None = None) -> SqlLauf:
    """Führt die Abfrage auf einer frischen Datenbank aus dem Datensatz aus und baut die Zwischentabellen."""
    teile = zerlege(sql) or []
    abfragen = [sql, *(t.sql for t in teile)]
    marke = neue_marke()
    erg = runner.run_code(skript(datensatz_sql, [{"sql": a, "ausduennen": None} for a in abfragen], marke), "python",
                          limits or RunLimits())
    _, block = lies_block(erg, marke)
    if not isinstance(block, list) or len(block) != len(abfragen):
        return SqlLauf(fehler="Zeitgrenze überschritten" if erg.timeout else (hinweise(erg).strip() or "Die Abfrage lief nicht zu Ende."),
                       zeitueberschreitung=erg.timeout, laufzeit_ms=erg.laufzeit_ms)
    haupt = block[0]
    if "fehler" in haupt:
        return SqlLauf(fehler=haupt["fehler"], laufzeit_ms=erg.laufzeit_ms)
    lauf = SqlLauf(spalten=haupt["spalten"], zeilen=haupt["zeilen"], laufzeit_ms=erg.laufzeit_ms)
    ergebnisse = block[1:]
    if teile and not any("fehler" in e for e in ergebnisse):
        for i, t in enumerate(teile):
            tabelle, text = t.deuten(ergebnisse, i)
            if t.klausel == "HAVING" and not text:
                continue  # Vorstufe ohne HAVING: nur Vergleichsgrundlage
            tabelle.zeilen = anzeigbar(tabelle.zeilen)
            lauf.schritte.append(Klauselschritt(klausel=t.klausel, zeile=_zeile(sql, t.stichwort, t.vorkommen), text=text, tabelle=tabelle))
    lauf.zeilen = anzeigbar(lauf.zeilen)
    return lauf
