---
schema_version: 1
id: s156-leser-im-alter
revision: 1
titel: "Leser in den 30ern"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [where, between]
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
erwartete_spalten: ["name", "alter_jahre"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Jonas Schaefer", 30]
  - ["Olivia Krueger", 33]
  - ["Anna Schmidt", 34]
  - ["Felix Bauer", 37]
  - ["Maria Klein", 39]
hints:
  - kosten: 0
    text: |
      BETWEEN 30 AND 39.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser in den 30ern

Name + Alter aller Leser zwischen 30 und 39.
