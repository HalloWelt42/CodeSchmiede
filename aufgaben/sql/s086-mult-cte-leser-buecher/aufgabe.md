---
schema_version: 1
id: s086-mult-cte-leser-buecher
revision: 1
titel: "Multi-CTE: Top-Leser + ihre Lieblingsautoren"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 22
schaetz_minuten: 15
tags: [multi-cte, join, group-by]
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
erwartete_spalten: ["leser", "autor", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Clara Weber", "Astrid Lindgren", 2]
  - ["Clara Weber", "Cornelia Funke", 1]
  - ["Eva Schulz", "Stefan Zweig", 2]
  - ["Eva Schulz", "Jane Austen", 1]
hints:
  - kosten: 0
    text: |
      Zwei CTEs verketten: top_leser (3+ Ausleihen), lieblings-Autoren je top-Leser.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Lieblingsautoren der Top-Leser

Für jeden Leser mit 3+ Ausleihen: Name + Autoren + Anzahl Ausleihen dieses Autors.
