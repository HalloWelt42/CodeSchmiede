---
schema_version: 1
id: s022-min-max-jahr
revision: 1
titel: "Aelteste und neueste Veröffentlichung"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [min, max, aggregat]
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
erwartete_spalten: ["aeltestes", "neuestes"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1813, 2003]
hints:
  - kosten: 0
    text: |
      `MIN()` und `MAX()` können in einer Zeile kombiniert werden.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Aelteste und neueste Veröffentlichung

Früheste und spaeteste `jahr`-Spalte als `ältestes` und `neuestes`.
