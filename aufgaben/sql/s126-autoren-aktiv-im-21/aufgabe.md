---
schema_version: 1
id: s126-autoren-aktiv-im-21
revision: 1
titel: "Autoren mit Buch nach 2000"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [join, where, distinct]
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
  - ["Cornelia Funke"]
  - ["Haruki Murakami"]
hints:
  - kosten: 0
    text: |
      JOIN + WHERE jahr >= 2000 + DISTINCT.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Aktive Autoren

Autoren mit mind. einem Buch ab 2000, alphabetisch.
