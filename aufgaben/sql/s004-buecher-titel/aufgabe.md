---
schema_version: 1
id: s004-buecher-titel
revision: 1
titel: "Alle Buchtitel"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags: [select, basics]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- SQL-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
dataset: bibliothek
schema_hinweis: |
  autoren(id, name, geburtsjahr, land)
  buecher(id, titel, autor_id, jahr, seiten, kategorie, exemplare)
  leser(id, name, ort, alter_jahre, mitglied_seit)
  ausleihen(id, leser_id, buch_id, ausgeliehen_am, zurueck_am)
erwartete_spalten: ["titel"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Siddhartha"]
  - ["Der Steppenwolf"]
  - ["Schachnovelle"]
  - ["Die Welt von Gestern"]
  - ["Die Verwandlung"]
  - ["Der Process"]
  - ["Buddenbrooks"]
  - ["Der Zauberberg"]
  - ["Pippi Langstrumpf"]
  - ["Karlsson vom Dach"]
  - ["1984"]
  - ["Farm der Tiere"]
  - ["Stolz und Vorurteil"]
  - ["Emma"]
  - ["Naokos Laecheln"]
  - ["Kafka am Strand"]
  - ["Tintenherz"]
  - ["Drachenreiter"]
  - ["Erdsee"]
  - ["Die linke Hand der Dunkelheit"]
hints:
  - kosten: 0
    text: |
      `SELECT titel FROM buecher;`
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Alle Buchtitel

Liefere nur die `titel`-Spalte aller Bücher.
