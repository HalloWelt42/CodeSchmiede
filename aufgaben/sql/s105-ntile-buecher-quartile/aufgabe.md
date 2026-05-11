---
schema_version: 1
id: s105-ntile-buecher-quartile
revision: 1
titel: "NTILE: Buecher in Seiten-Quartile"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [window-function, ntile]
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
erwartete_spalten: ["titel", "seiten", "quartil"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Die Verwandlung", 74, 1]
  - ["Schachnovelle", 96, 1]
  - ["Farm der Tiere", 112, 1]
  - ["Karlsson vom Dach", 124, 1]
  - ["Siddhartha", 153, 1]
  - ["Pippi Langstrumpf", 168, 2]
  - ["Erdsee", 224, 2]
  - ["Der Steppenwolf", 288, 2]
  - ["Naokos Laecheln", 296, 2]
  - ["Die linke Hand der Dunkelheit", 304, 2]
  - ["Der Process", 312, 3]
  - ["1984", 326, 3]
  - ["Drachenreiter", 432, 3]
  - ["Stolz und Vorurteil", 432, 3]
  - ["Emma", 474, 3]
  - ["Die Welt von Gestern", 528, 4]
  - ["Tintenherz", 576, 4]
  - ["Kafka am Strand", 624, 4]
  - ["Buddenbrooks", 759, 4]
  - ["Der Zauberberg", 992, 4]
hints:
  - kosten: 0
    text: |
      `NTILE(4) OVER (ORDER BY ...)` teilt Zeilen in 4 gleich große Buckets (1..4).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# NTILE: Quartile nach Seitenzahl

Jedes Buch bekommt sein Seitenzahl-Quartil (1..4) zugewiesen.
