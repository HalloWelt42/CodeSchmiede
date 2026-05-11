---
schema_version: 1
id: s057-rank-seiten
revision: 1
titel: "Rang nach Seitenzahl"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [window-function, rank]
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
erwartete_spalten: ["titel", "seiten", "rang"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Der Zauberberg", 992, 1]
  - ["Buddenbrooks", 759, 2]
  - ["Kafka am Strand", 624, 3]
  - ["Tintenherz", 576, 4]
  - ["Die Welt von Gestern", 528, 5]
  - ["Emma", 474, 6]
  - ["Drachenreiter", 432, 7]
  - ["Stolz und Vorurteil", 432, 7]
  - ["1984", 326, 9]
  - ["Der Process", 312, 10]
  - ["Die linke Hand der Dunkelheit", 304, 11]
  - ["Naokos Laecheln", 296, 12]
  - ["Der Steppenwolf", 288, 13]
  - ["Erdsee", 224, 14]
  - ["Pippi Langstrumpf", 168, 15]
  - ["Siddhartha", 153, 16]
  - ["Karlsson vom Dach", 124, 17]
  - ["Farm der Tiere", 112, 18]
  - ["Schachnovelle", 96, 19]
  - ["Die Verwandlung", 74, 20]
hints:
  - kosten: 0
    text: |
      `RANK() OVER (ORDER BY ... DESC)` -- gleiche Werte teilen sich Rang.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Rang nach Seitenzahl

Jedes Buch bekommt einen Rang nach Seitenzahl (1 = dickstes).
