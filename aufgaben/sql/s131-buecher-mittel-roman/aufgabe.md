---
schema_version: 1
id: s131-buecher-mittel-roman
revision: 1
titel: "Romane mittlerer Laenge"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [where, and, between]
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
erwartete_spalten: ["titel", "seiten"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Der Steppenwolf", 288]
  - ["Naokos Laecheln", 296]
  - ["Der Process", 312]
  - ["1984", 326]
  - ["Stolz und Vorurteil", 432]
  - ["Emma", 474]
hints:
  - kosten: 0
    text: |
      Zwei Bedingungen via AND.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Romane mittlerer Laenge

Romane mit 200-500 Seiten, sortiert nach Seitenzahl.
