---
schema_version: 1
id: s051-autoren-mit-roman
revision: 1
titel: "Autoren mit mindestens einem Roman"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [subquery, in]
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
erwartete_spalten: ["name"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Franz Kafka"]
  - ["George Orwell"]
  - ["Haruki Murakami"]
  - ["Hermann Hesse"]
  - ["Jane Austen"]
  - ["Thomas Mann"]
hints:
  - kosten: 0
    text: |
      WHERE id IN (Subquery).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Autoren mit Roman

Alle Autoren, die mindestens einen Roman geschrieben haben, alphabetisch.
