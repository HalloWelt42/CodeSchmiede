---
schema_version: 1
id: s087-autoren-keine-ausleihen
revision: 1
titel: "Autoren, deren Bücher nie ausgeliehen wurden"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [not-exists, correlated-subquery]
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
  []
hints:
  - kosten: 0
    text: |
      `NOT EXISTS (Subquery)` mit Korrelation auf `a.id`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Autoren ohne ausgeliehene Bücher

Alle Autoren, von denen kein Buch jemals ausgeliehen wurde.
