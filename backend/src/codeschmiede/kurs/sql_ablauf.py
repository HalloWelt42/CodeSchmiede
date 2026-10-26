"""Ablauf einer SQL-Abfrage: das Ergebnis und je Klausel die Zwischentabelle, in der Reihenfolge der Abarbeitung.

Die Datenbank arbeitet eine Abfrage anders ab, als man sie schreibt: FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT,
DISTINCT, ORDER BY, LIMIT. Dafür zerlegt der SQL-Parser die Abfrage in Teilabfragen, die nacheinander eine Klausel mehr
enthalten. Alle laufen in der Sandbox auf dem Datensatz wie jede andere Abfrage (sql_pruefer.skript), hier wird nur
verglichen: welche Zeilen ein Filter behält, welche Spalten SELECT fallen lässt, welche Zeilen eine Gruppe bilden.

Zerlegt wird eine einzelne SELECT-Abfrage ohne WITH und ohne UNION. Ein Skript aus mehreren Anweisungen oder mit
Änderungen (INSERT, UPDATE, DELETE, CREATE TABLE ...) läuft Anweisung für Anweisung auf einer Datenbank; je Anweisung
zeigt ein Schritt die betroffene Tabelle davor und danach: neue Zeilen, geänderte Zellen mit ihrem alten Wert,
gelöschte Zeilen. Zeilen werden dabei über ihre rowid wiedererkannt.
"""

from __future__ import annotations

import json
import re
import sqlite3
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Literal

import sqlglot
from pydantic import BaseModel, Field
from sqlglot import exp

from ..pruefung.sql_pruefer import MAX_ZEILEN, anzeigbar, skript
from ..pruefung.testlauf import hinweise, lies_block, neue_marke
from ..sandbox.result import RunLimits
from ..sandbox.runner import Runner

Zeilenzustand = Literal["", "neu", "bleibt", "raus", "geaendert"]
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
    vorher: list[list[Any] | None] = Field(default_factory=list)
    """Je Zeile ihre Werte vor einem UPDATE, falls sie sich geändert hat (sonst None)."""
    spalte_neu: list[bool] = Field(default_factory=list)
    """Je Spalte: kam gerade erst dazu (ALTER TABLE ... ADD COLUMN)."""


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
    skript: bool = False
    """Anweisung für Anweisung statt Klausel für Klausel; das Ergebnis ist das der letzten Abfrage im Skript."""
    fehler: str | None = None
    zeitueberschreitung: bool = False
    laufzeit_ms: float = 0

    @property
    def ausgabe(self) -> str:
        """Das Ergebnis als Text, wie Vorhersagen es schreiben: je Zeile die Werte mit " | " getrennt, ohne Kopf."""
        return als_text(self.zeilen)


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


def _anteil(k: int, n: int) -> str:
    """"2 von 9 Zeilen", "1 von 1 Zeile"."""
    return f"{k} von {n} {'Zeile' if n == 1 else 'Zeilen'}"


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
    zusammengefasst = any(not f.find_ancestor(exp.Subquery) for s in q.expressions for f in s.find_all(exp.AggFunc))
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
        if group is not None:
            return _tabelle(e[i], "neu"), f"SELECT macht aus jeder Gruppe eine Zeile und berechnet {liste}."
        if zusammengefasst:
            return _tabelle(e[i], "neu"), f"SELECT fasst die {_zeilen_wort(len(v['zeilen']))} zu einer zusammen und berechnet {liste}."
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
    """Führt die Abfrage auf einer frischen Datenbank aus dem Datensatz aus und baut die Zwischentabellen; ein Skript
    läuft Anweisung für Anweisung (skript_lauf)."""
    teile_skript = anweisungen(sql)
    if len(teile_skript) > 1 or (teile_skript and teile_skript[0].art != "SELECT"):
        return skript_lauf(runner, datensatz_sql, teile_skript, limits)
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


# ---------- Skripte: Anweisung für Anweisung ----------


@dataclass
class Anweisung:
    sql: str
    zeile: int
    """Zeile im Code, in der die Anweisung beginnt, ab 1."""
    art: str
    """INSERT, UPDATE, DELETE, CREATE TABLE, DROP TABLE, ALTER TABLE, SELECT oder das erste Wort."""
    tabelle: str | None
    """Die Tabelle, die die Anweisung verändert (bei SELECT keine)."""


_ARTEN: dict[type[exp.Expression], str] = {
    exp.Insert: "INSERT", exp.Update: "UPDATE", exp.Delete: "DELETE", exp.Select: "SELECT", exp.Union: "SELECT",
}


def _art_und_tabelle(sql: str) -> tuple[str, str | None]:
    erstes = (re.findall(r"[A-Za-z]+", _ohne_kommentare(sql)) or ["?"])[0].upper()
    try:
        knoten = sqlglot.parse_one(sql, read="sqlite")
    except sqlglot.errors.SqlglotError:
        return erstes, None
    art = _ARTEN.get(type(knoten))
    if art is None and isinstance(knoten, (exp.Create, exp.Drop, exp.Alter)):
        art = f"{erstes} {knoten.args.get('kind') or 'TABLE'}"
    if art is None:
        return erstes, None
    tabelle = knoten.find(exp.Table) if art != "SELECT" else None
    return art, tabelle.name if tabelle is not None else None


def _ohne_kommentare(sql: str) -> str:
    return re.sub(r"--[^\n]*|/\*.*?\*/", " ", sql, flags=re.S)


def anweisungen(code: str) -> list[Anweisung]:
    """Zerlegt ein Skript an den Semikolons, an denen eine Anweisung vollständig ist; Semikolons in Texten zählen
    nicht (sqlite3.complete_statement). Leere Stücke und reine Kommentare fallen weg."""
    stuecke: list[tuple[int, str]] = []
    puffer, start = "", 0
    for i, zeichen in enumerate(code):
        puffer += zeichen
        if zeichen == ";" and sqlite3.complete_statement(puffer):
            stuecke.append((start, puffer))
            puffer, start = "", i + 1
    stuecke.append((start, puffer))
    liste: list[Anweisung] = []
    for anfang, text in stuecke:
        rumpf = _ohne_kommentare(text).strip().rstrip(";").strip()
        if not rumpf:
            continue
        erste = anfang + text.index(rumpf.split()[0]) if rumpf.split()[0] in text else anfang
        art, tabelle = _art_und_tabelle(text)
        liste.append(Anweisung(sql=text.strip(), zeile=code.count("\n", 0, erste) + 1, art=art, tabelle=tabelle))
    return liste


def _skript_sandbox(datensatz_sql: str, teile: list[Anweisung], marke: str) -> str:
    """Python-Skript für die Sandbox: alle Anweisungen nacheinander auf einer Datenbank; je Anweisung der Stand der
    betroffenen Tabelle davor und danach (mit rowid) und das Ergebnis einer Abfrage."""
    laeufe = [{"sql": t.sql, "tabelle": t.tabelle} for t in teile]
    return (
        "import json, sqlite3, sys\n"
        f"SCHEMA = json.loads({json.dumps(datensatz_sql)!r})\n"
        f"LAEUFE = json.loads({json.dumps(laeufe)!r})\n"
        f"MAX_ZEILEN = {MAX_ZEILEN}\n"
        "conn = sqlite3.connect(':memory:')\n"
        "conn.executescript(SCHEMA)\n"
        "conn.set_authorizer(lambda aktion, *_: sqlite3.SQLITE_DENY if aktion in (sqlite3.SQLITE_ATTACH, sqlite3.SQLITE_DETACH) else sqlite3.SQLITE_OK)\n"
        "def tabelle(cur):\n"
        "    return {'spalten': [d[0] for d in cur.description], 'zeilen': [list(z) for z in cur.fetchmany(MAX_ZEILEN)]}\n"
        "def stand(name):\n"
        "    if not name: return None\n"
        "    try: return tabelle(conn.execute('SELECT rowid AS __zeile, * FROM \"' + name.replace('\"', '\"\"') + '\"'))\n"
        "    except sqlite3.Error: return None\n"
        "aus = []\n"
        "for l in LAEUFE:\n"
        "    vorher = stand(l['tabelle'])\n"
        "    try:\n"
        "        cur = conn.execute(l['sql'])\n"
        "        ergebnis = tabelle(cur) if cur.description else None\n"
        "    except (sqlite3.Error, sqlite3.Warning) as e:\n"
        "        aus.append({'fehler': 'SQL-Fehler: ' + str(e)})\n"
        "        break\n"
        "    aus.append({'vorher': vorher, 'nachher': stand(l['tabelle']), 'ergebnis': ergebnis})\n"
        f"sys.stdout.write({marke!r} + json.dumps(aus, default=repr) + '\\n')\n"
    )


def _ohne_rowid(stand: dict[str, Any] | None) -> tuple[list[str], list[list[Any]], list[Any]]:
    if not stand:
        return [], [], []
    return stand["spalten"][1:], [z[1:] for z in stand["zeilen"]], [z[0] for z in stand["zeilen"]]


def _deute_anweisung(a: Anweisung, lauf: dict[str, Any]) -> tuple[Zwischentabelle, str]:
    """Zwischentabelle und Erklärung einer Anweisung aus dem Stand davor und danach."""
    t = a.tabelle or ""
    v_spalten, v_zeilen, v_ids = _ohne_rowid(lauf.get("vorher"))
    n_spalten, n_zeilen, n_ids = _ohne_rowid(lauf.get("nachher"))
    if a.art == "SELECT" or lauf.get("ergebnis"):
        e = lauf.get("ergebnis") or {"spalten": [], "zeilen": []}
        return Zwischentabelle(spalten=e["spalten"], zeilen=e["zeilen"]), f"SELECT liefert {_zeilen_wort(len(e['zeilen']))}."
    if a.art == "INSERT":
        alt = set(v_ids)
        zustand: list[Zeilenzustand] = ["neu" if i not in alt else "" for i in n_ids]
        neu = zustand.count("neu")
        return (Zwischentabelle(spalten=n_spalten, zeilen=n_zeilen, zustand=zustand),
                f"INSERT fügt {_zeilen_wort(neu)} in {t} ein; jetzt hat {t} {_zeilen_wort(len(n_zeilen))}.")
    if a.art == "UPDATE":
        alt_je_id = dict(zip(v_ids, v_zeilen))
        vorher = [alt_je_id.get(i) if alt_je_id.get(i) != z else None for i, z in zip(n_ids, n_zeilen)]
        zustand = ["geaendert" if w is not None else "" for w in vorher]
        geaendert = zustand.count("geaendert")
        alle = " Ohne WHERE trifft es jede Zeile." if geaendert == len(n_zeilen) and geaendert > 1 and "WHERE" not in a.sql.upper() else ""
        return (Zwischentabelle(spalten=n_spalten, zeilen=n_zeilen, zustand=zustand, vorher=vorher),
                f"UPDATE ändert {_anteil(geaendert, len(n_zeilen))} in {t}; die alten Werte sind durchgestrichen.{alle}")
    if a.art == "DELETE":
        bleiben = set(n_ids)
        zustand = ["bleibt" if i in bleiben else "raus" for i in v_ids]
        weg = zustand.count("raus")
        leer = (" Ohne WHERE trifft es jede Zeile; die Tabelle bleibt, nur leer."
                if weg == len(v_zeilen) and weg > 1 and "WHERE" not in a.sql.upper() else "")
        return (Zwischentabelle(spalten=v_spalten, zeilen=v_zeilen, zustand=zustand),
                f"DELETE löscht {_anteil(weg, len(v_zeilen))} aus {t}; {len(v_zeilen) - weg} bleiben.{leer}")
    if a.art.startswith("CREATE"):
        zustand = ["neu"] * len(n_zeilen)
        inhalt = f"gleich mit {_zeilen_wort(len(n_zeilen))}" if n_zeilen else "noch ohne Zeilen"
        return (Zwischentabelle(spalten=n_spalten, zeilen=n_zeilen, zustand=zustand, spalte_neu=[True] * len(n_spalten)),
                f"CREATE TABLE legt die Tabelle {t} an, mit den Spalten {', '.join(n_spalten)}, {inhalt}.")
    if a.art.startswith("DROP"):
        return (Zwischentabelle(spalten=v_spalten, zeilen=v_zeilen, zustand=["raus"] * len(v_zeilen)),
                f"DROP TABLE löscht die Tabelle {t} samt ihren {_zeilen_wort(len(v_zeilen))}.")
    if a.art.startswith("ALTER"):
        neue = [sp not in v_spalten for sp in n_spalten]
        dazu = [sp for sp, n in zip(n_spalten, neue) if n]
        text = (f"ALTER TABLE gibt {t} die neue Spalte {', '.join(dazu)}; in den vorhandenen Zeilen steht dort NULL."
                if dazu else f"ALTER TABLE ändert den Aufbau von {t}.")
        return Zwischentabelle(spalten=n_spalten, zeilen=n_zeilen, spalte_neu=neue), text
    return Zwischentabelle(spalten=n_spalten, zeilen=n_zeilen), f"{a.art} ist ausgeführt."


def skript_lauf(runner: Runner, datensatz_sql: str, teile: list[Anweisung], limits: RunLimits | None = None) -> SqlLauf:
    """Führt ein Skript Anweisung für Anweisung auf einer frischen Datenbank aus dem Datensatz aus."""
    marke = neue_marke()
    erg = runner.run_code(_skript_sandbox(datensatz_sql, teile, marke), "python", limits or RunLimits())
    _, block = lies_block(erg, marke)
    if not isinstance(block, list):
        return SqlLauf(skript=True, fehler="Zeitgrenze überschritten" if erg.timeout else (hinweise(erg).strip() or "Das Skript lief nicht zu Ende."),
                       zeitueberschreitung=erg.timeout, laufzeit_ms=erg.laufzeit_ms)
    lauf = SqlLauf(skript=True, laufzeit_ms=erg.laufzeit_ms)
    for a, ergebnis in zip(teile, block):
        if "fehler" in ergebnis:
            lauf.fehler = f"Anweisung {teile.index(a) + 1} (Zeile {a.zeile}): {ergebnis['fehler']}"
            break
        tabelle, text = _deute_anweisung(a, ergebnis)
        tabelle.zeilen = anzeigbar(tabelle.zeilen)
        tabelle.vorher = [anzeigbar([w])[0] if w is not None else None for w in tabelle.vorher]
        lauf.schritte.append(Klauselschritt(klausel=a.art, zeile=a.zeile, text=text, tabelle=tabelle))
        if ergebnis.get("ergebnis"):
            lauf.spalten, lauf.zeilen = ergebnis["ergebnis"]["spalten"], anzeigbar(ergebnis["ergebnis"]["zeilen"])
    return lauf
