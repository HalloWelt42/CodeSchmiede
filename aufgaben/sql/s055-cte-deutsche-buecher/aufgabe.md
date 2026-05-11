---
schema_version: 1
id: s055-cte-deutsche-buecher
revision: 1
titel: "CTE: Bücher von deutschen Autoren"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 7
tags: [cte, with, join]
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
erwartete_spalten: ["titel", "name"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Drachenreiter", "Cornelia Funke"]
  - ["Tintenherz", "Cornelia Funke"]
  - ["Der Steppenwolf", "Hermann Hesse"]
  - ["Siddhartha", "Hermann Hesse"]
  - ["Buddenbrooks", "Thomas Mann"]
  - ["Der Zauberberg", "Thomas Mann"]
hints:
  - kosten: 0
    text: |
      `WITH name AS (SELECT ...)` definiert eine Common Table Expression.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# CTE: Bücher von deutschen Autoren

Mit einer CTE die deutschen Autoren vorbereiten und dann Bücher dazu joinen.
