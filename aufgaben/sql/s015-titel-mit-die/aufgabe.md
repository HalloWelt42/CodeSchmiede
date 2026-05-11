---
schema_version: 1
id: s015-titel-mit-die
revision: 1
titel: "Titel beginnt mit Die"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [where, like, pattern]
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
  - ["Die Verwandlung"]
  - ["Die Welt von Gestern"]
  - ["Die linke Hand der Dunkelheit"]
hints:
  - kosten: 0
    text: |
      `LIKE 'Die %'` -- `%` ist Platzhalter für beliebigen Text.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Titel beginnt mit "Die"

Alle Buchtitel, die mit `Die ` (mit Leerzeichen) beginnen.
