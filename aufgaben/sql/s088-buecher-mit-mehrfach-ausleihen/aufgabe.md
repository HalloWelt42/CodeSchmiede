---
schema_version: 1
id: s088-buecher-mit-mehrfach-ausleihen
revision: 1
titel: "Bücher, die mehr als 2x ausgeliehen wurden"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join, group-by, having]
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
erwartete_spalten: ["titel", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["1984", 3]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY + HAVING COUNT(*) > 2.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Beliebte Bücher

Bücher mit mehr als 2 Ausleihen + Anzahl, hauefigste zuerst.
