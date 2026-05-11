---
schema_version: 1
id: s171-percent-rank-buecher
revision: 1
titel: "PERCENT_RANK der Buecher nach Seiten"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 7
tags: [window-function, percent-rank]
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
erwartete_spalten: ["titel", "seiten", "perc"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Die Verwandlung", 74, 0.0]
  - ["Schachnovelle", 96, 0.053]
  - ["Farm der Tiere", 112, 0.105]
  - ["Karlsson vom Dach", 124, 0.158]
  - ["Siddhartha", 153, 0.211]
  - ["Pippi Langstrumpf", 168, 0.263]
  - ["Erdsee", 224, 0.316]
  - ["Der Steppenwolf", 288, 0.368]
  - ["Naokos Laecheln", 296, 0.421]
  - ["Die linke Hand der Dunkelheit", 304, 0.474]
  - ["Der Process", 312, 0.526]
  - ["1984", 326, 0.579]
  - ["Drachenreiter", 432, 0.632]
  - ["Stolz und Vorurteil", 432, 0.632]
  - ["Emma", 474, 0.737]
  - ["Die Welt von Gestern", 528, 0.789]
  - ["Tintenherz", 576, 0.842]
  - ["Kafka am Strand", 624, 0.895]
  - ["Buddenbrooks", 759, 0.947]
  - ["Der Zauberberg", 992, 1.0]
hints:
  - kosten: 0
    text: |
      PERCENT_RANK liefert 0..1, ROUND auf 3 Stellen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# PERCENT_RANK nach Seiten

Jedes Buch bekommt einen Perzentilrang nach Seitenzahl.
