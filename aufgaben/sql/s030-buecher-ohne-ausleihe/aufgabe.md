---
schema_version: 1
id: s030-buecher-ohne-ausleihe
revision: 1
titel: "Bücher ohne jemals ausgeliehen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [subquery, not-in]
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
  []
hints:
  - kosten: 0
    text: |
      Subquery: `WHERE id NOT IN (SELECT DISTINCT buch_id FROM ausleihen)`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bücher ohne Ausleihe

Titel aller Bücher, die nie ausgeliehen wurden.
