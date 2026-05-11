---
schema_version: 1
id: s124-leser-nach-anfang
revision: 1
titel: "Leser gruppieren nach Anfangsbuchstabe"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [group-by, substr]
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
erwartete_spalten: ["buchstabe", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["A", 1]
  - ["B", 1]
  - ["C", 1]
  - ["D", 1]
  - ["E", 1]
  - ["F", 1]
  - ["G", 1]
  - ["H", 1]
  - ["I", 1]
  - ["J", 1]
  - ["K", 1]
  - ["L", 1]
  - ["M", 1]
  - ["N", 1]
  - ["O", 1]
hints:
  - kosten: 0
    text: |
      GROUP BY auf SUBSTR-Ausdruck.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser nach Anfangsbuchstabe

Anfangsbuchstabe + Anzahl Leser, alphabetisch.
