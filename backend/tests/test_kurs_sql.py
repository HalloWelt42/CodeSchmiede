"""Aufbaukurs SQL: Datensatz je Einführung, Begriffe über den SQL-Parser, Beispiele mit Zwischentabellen je Klausel
und Vorhersagen über die Zahl der Ergebniszeilen."""

import textwrap
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from codeschmiede.api import app_bauen
from codeschmiede.config import Settings
from codeschmiede.kurs.begriffe import merkmale_sql
from codeschmiede.kurs.einlesen import lade
from codeschmiede.kurs.sql_ablauf import sql_lauf, zerlege
from codeschmiede.state import AppState

from .conftest import braucht_sandbox, schreibe_aufgabe

BEGRIFFE = """\
sprache: sql
begriffe:
  - {id: select, titel: SELECT und FROM, erkennung: {knoten: [Select]}}
  - {id: where, titel: Zeilen filtern, erkennung: {knoten: [Where]}}
  - {id: order_by, titel: Sortieren, erkennung: {knoten: [Order]}}
"""

DATENSATZ = """\
CREATE TABLE tiere (id INTEGER PRIMARY KEY, name TEXT, art TEXT, gewicht REAL);
INSERT INTO tiere VALUES (1, 'Pit', 'Pinguin', 4.2), (2, 'Rosa', 'Robbe', 80.0), (3, 'Paul', 'Pinguin', 5.1);
"""

EINFUEHRUNG = '''\
---
id: sql-filtern
sprache: sql
titel: Zeilen filtern
kurz: Nur passende Zeilen.
fuehrt_ein: [select, where]
lernziele: [mit WHERE filtern]
karte: Ich siebe Zeilen
datensatz: mini
---

## Nur die Pinguine

Text.

```beispiel
id: pinguine
code: |
  SELECT name
  FROM tiere
  WHERE art = 'Pinguin'
vorhersage:
  art: auswahl
  frage: Wie viele Zeilen hat das Ergebnis?
  vergleich: zeilen
  optionen:
    - {text: 2 Zeilen, richtig: true, erklaerung: Genau.}
    - {text: 3 Zeilen, erklaerung: Die Robbe fällt heraus.}
```

```beispiel
id: zaehlen
code: SELECT name FROM tiere
vorhersage:
  art: eintippen
  vergleich: zeilen
  erklaerung: Alle drei Tiere.
```
'''


def baue_sql_kurs(kurs: Path, aufgaben: Path, einfuehrung: str = EINFUEHRUNG, uebung: str = "SELECT name FROM tiere WHERE art = 'Robbe'") -> None:
    (kurs / "begriffe").mkdir(parents=True)
    (kurs / "begriffe" / "sql.yml").write_text(BEGRIFFE, encoding="utf-8")
    ordner = kurs / "einfuehrungen" / "sql" / "filtern"
    ordner.mkdir(parents=True)
    (ordner / "einfuehrung.md").write_text(einfuehrung, encoding="utf-8")
    (kurs / "sql.yml").write_text(textwrap.dedent("""\
        sprache: sql
        titel: SQL
        bloecke:
          - titel: Abfragen
            kapitel:
              - {einfuehrung: sql-filtern, uebungen: [q011-robbe]}
        """), encoding="utf-8")
    (aufgaben / "sql" / "datasets").mkdir(parents=True, exist_ok=True)
    (aufgaben / "sql" / "datasets" / "mini.sql").write_text(DATENSATZ, encoding="utf-8")
    ordner = schreibe_aufgabe(aufgaben, "sql", "q011-robbe", "sql_abfrage", """\
        dataset: mini
        erwartete_spalten: [name]
        erwartetes_ergebnis: [[Rosa]]
        """)
    (ordner / "solution_idiomatic.sql").write_text(uebung + "\n")


@pytest.fixture
def sql_settings(settings: Settings) -> Settings:
    baue_sql_kurs(settings.kurs_pfad, settings.aufgaben_pfad)
    return settings


def test_merkmale_aus_dem_sql_parser():
    knoten, aufrufe = merkmale_sql("SELECT COUNT(*) FROM t LEFT JOIN u ON t.id = u.id WHERE name LIKE 'P%' ORDER BY 1")
    assert {"Select", "Where", "Like", "Order", "Join", "LeftJoin"} <= knoten
    assert aufrufe == {"COUNT"}
    assert merkmale_sql("SELEKT was") is None or "Select" not in merkmale_sql("SELEKT was")[0]


def test_zerlegen_in_der_reihenfolge_der_abarbeitung():
    teile = zerlege("SELECT DISTINCT art, COUNT(*) AS n FROM tiere t JOIN zoo z ON t.zoo = z.id WHERE gewicht > 1 "
                    "GROUP BY art HAVING COUNT(*) > 1 ORDER BY n DESC LIMIT 2")
    assert [t.klausel for t in teile] == ["FROM", "JOIN", "WHERE", "GROUP BY", "HAVING", "HAVING", "SELECT", "DISTINCT", "ORDER BY", "LIMIT"]
    assert zerlege("SELECT 1 UNION SELECT 2") is None
    assert zerlege("INSERT INTO t VALUES (1)") is None


def test_sql_einfuehrung_braucht_datensatz(tmp_path):
    baue_sql_kurs(tmp_path / "kurs", tmp_path / "aufgaben", EINFUEHRUNG.replace("datensatz: mini\n", ""))
    inhalt = lade(tmp_path / "kurs")
    assert "sql-filtern" not in inhalt.einfuehrungen
    assert any("Datensatz" in f.meldung for f in inhalt.ladefehler)


def test_vorgriff_in_sql_uebung_und_fehlender_datensatz(settings: Settings, docker_runner):
    baue_sql_kurs(settings.kurs_pfad, settings.aufgaben_pfad, EINFUEHRUNG.replace("datensatz: mini", "datensatz: weg"),
                  uebung="SELECT name FROM tiere ORDER BY name")
    befunde = [b.meldung for b in AppState(settings, runner=docker_runner).befunde]
    assert any("order_by" in m for m in befunde), befunde
    assert any("Datensatz weg fehlt" in m for m in befunde), befunde


def test_vorhersage_zeigt_frage_ohne_antwort(settings: Settings, docker_runner):
    baue_sql_kurs(settings.kurs_pfad, settings.aufgaben_pfad)
    client = TestClient(app_bauen(settings, runner=docker_runner))
    e = client.get("/api/kurs/einfuehrung/sql-filtern").json()
    assert e["datensatz"] == "mini"
    beispiel = e["abschnitte"][0]["teile"][1]
    assert beispiel["ablauf"] and beispiel["vorhersage"]["frage"] == "Wie viele Zeilen hat das Ergebnis?"
    assert "richtig" not in str(beispiel["vorhersage"]["optionen"])


@braucht_sandbox
def test_sql_beispiel_mit_zwischentabellen(settings: Settings, docker_runner):
    baue_sql_kurs(settings.kurs_pfad, settings.aufgaben_pfad)
    client = TestClient(app_bauen(settings, runner=docker_runner))
    weg = "/api/kurs/einfuehrung/sql-filtern/beispiel/pinguine/ausfuehren"
    assert client.post(weg, json={}).status_code == 409
    assert client.post("/api/kurs/einfuehrung/sql-filtern/antwort", json={"element": "pinguine", "wahl": [0]}).json()["richtig"]
    lauf = client.post(weg, json={}).json()
    assert lauf["art"] == "sql" and lauf["zeilen"] == [["Pit"], ["Paul"]]
    schritte = {s["klausel"]: s for s in lauf["schritte"]}
    assert list(schritte) == ["FROM", "WHERE", "SELECT"]
    assert schritte["WHERE"]["zeile"] == 3 and schritte["WHERE"]["tabelle"]["zustand"] == ["bleibt", "raus", "bleibt"]
    assert schritte["SELECT"]["tabelle"]["weg"] == [True, False, True, True]
    kaputt = client.post(weg, json={"code": "SELECT nam FROM tiere"}).json()
    assert kaputt["fehler"].startswith("SQL-Fehler")


@braucht_sandbox
def test_eintippen_vergleicht_die_zahl_der_zeilen(settings: Settings, docker_runner):
    baue_sql_kurs(settings.kurs_pfad, settings.aufgaben_pfad)
    client = TestClient(app_bauen(settings, runner=docker_runner))
    antwort = "/api/kurs/einfuehrung/sql-filtern/antwort"
    assert not client.post(antwort, json={"element": "zaehlen", "eingetippt": "2"}).json()["richtig"]
    assert client.post(antwort, json={"element": "zaehlen", "eingetippt": " 3 "}).json()["richtig"]


@braucht_sandbox
def test_join_zeigt_gleichnamige_spalten_mit_tabelle(docker_runner):
    daten = DATENSATZ + "CREATE TABLE arten (name TEXT, futter TEXT);\nINSERT INTO arten VALUES ('Pinguin', 'Fisch'), ('Wal', 'Krill');\n"
    lauf = sql_lauf(docker_runner, daten, "SELECT a.name, t.name\nFROM arten a\nLEFT JOIN tiere t ON t.art = a.name")
    schritte = {s.klausel: s for s in lauf.schritte}
    assert list(schritte) == ["FROM", "LEFT JOIN", "SELECT"]
    assert schritte["LEFT JOIN"].zeile == 3 and "ohne Partner" in schritte["LEFT JOIN"].text
    kopf = ["a.name", "futter", "id", "t.name", "art", "gewicht"]
    assert schritte["LEFT JOIN"].tabelle.spalten == kopf == schritte["SELECT"].tabelle.spalten
    assert schritte["SELECT"].tabelle.weg == [False, True, True, False, True, True]
    assert sorted(lauf.zeilen, key=str) == sorted([["Pinguin", "Pit"], ["Pinguin", "Paul"], ["Wal", None]], key=str)
