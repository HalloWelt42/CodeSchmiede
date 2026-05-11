---
schema_version: 1
id: s158-leser-mit-zwei-ausleihen-am-tag
revision: 1
titel: "Leser mit 2+ Ausleihen am gleichen Tag"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 7
tags: [join, group-by-multi, having]
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
erwartete_spalten: ["name", "ausgeliehen_am", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Greta Hoffmann", "2025-04-12", 2]
hints:
  - kosten: 0
    text: |
      GROUP BY Leser + Datum, HAVING >= 2.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Mehrfach-Ausleihen am Tag

Leser + Datum + Anzahl, wenn jemand am gleichen Tag 2+ Bücher ausgeliehen hat.
