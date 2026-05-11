---
schema_version: 1
id: s001-alle-buecher
revision: 1
titel: "SELECT alle Bücher: Titel und Jahr"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [select, basics]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- SELECT-Basics.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
dataset: bibliothek
schema_hinweis: |
  buecher(id, titel, autor_id, jahr, seiten, kategorie, exemplare)
  autoren(id, name, geburtsjahr, land)
  leser(id, name, ort, alter_jahre, mitglied_seit)
  ausleihen(id, leser_id, buch_id, ausgeliehen_am, zurueck_am)
erwartete_spalten: ["titel", "jahr"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Siddhartha", 1922]
  - ["Der Steppenwolf", 1927]
  - ["Schachnovelle", 1942]
  - ["Die Welt von Gestern", 1942]
  - ["Die Verwandlung", 1915]
  - ["Der Process", 1925]
  - ["Buddenbrooks", 1901]
  - ["Der Zauberberg", 1924]
  - ["Pippi Langstrumpf", 1945]
  - ["Karlsson vom Dach", 1955]
  - ["1984", 1949]
  - ["Farm der Tiere", 1945]
  - ["Stolz und Vorurteil", 1813]
  - ["Emma", 1815]
  - ["Naokos Laecheln", 1987]
  - ["Kafka am Strand", 2002]
  - ["Tintenherz", 2003]
  - ["Drachenreiter", 1997]
  - ["Erdsee", 1968]
  - ["Die linke Hand der Dunkelheit", 1969]
hints:
  - kosten: 0
    text: |
      `SELECT spalte1, spalte2 FROM tabelle` -- ohne WHERE liefert
      es alle Zeilen, in der Reihenfolge wie sie eingefügt wurden.
  - kosten: 2
    text: |
      `SELECT titel, jahr FROM bücher;`
starter_code: |
  SELECT ___ FROM buecher;
---

# SELECT alle Bücher: Titel und Jahr

Schreibe eine Abfrage, die für **alle Bücher** den `titel` und das
`jahr` liefert -- in der Reihenfolge, wie sie in der Tabelle stehen.

## Spalten

| titel | jahr |
|-------|------|
| ...   | ...  |

20 Zeilen werden erwartet.
