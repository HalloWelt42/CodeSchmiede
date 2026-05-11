---
schema_version: 1
id: s034-summe-seiten-kafka
revision: 1
titel: "Summe Seiten von Kafka"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [join, sum, where]
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
erwartete_spalten: ["gesamt_seiten"]
sortierung_egal: false
erwartetes_ergebnis:
  - [386]
hints:
  - kosten: 0
    text: |
      JOIN + SUM + WHERE. Spalte `gesamt_seiten`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Summe Seiten von Kafka

Gesamtseitenzahl aller Bücher von Franz Kafka.
