---
schema_version: 1
id: s159-buecher-pro-monat-ausleihen
revision: 1
titel: "Top-Buecher in 2025 nach Ausleihen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join, group-by, limit, date]
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
erwartete_spalten: ["titel", "ausleihen"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["1984", 3]
  - ["Der Zauberberg", 2]
  - ["Kafka am Strand", 2]
  - ["Pippi Langstrumpf", 2]
  - ["Siddhartha", 2]
hints:
  - kosten: 0
    text: |
      JOIN + WHERE Jahr + GROUP BY + ORDER + LIMIT.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Top-5 Bücher 2025

Die 5 am häufigsten ausgeliehenen Bücher in 2025.
