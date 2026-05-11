---
schema_version: 1
id: s005-autoren-namen
revision: 1
titel: "Alle Autoren-Namen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
tags: [select, basics]
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
  - ["Hermann Hesse"]
  - ["Stefan Zweig"]
  - ["Franz Kafka"]
  - ["Thomas Mann"]
  - ["Astrid Lindgren"]
  - ["George Orwell"]
  - ["Jane Austen"]
  - ["Haruki Murakami"]
  - ["Cornelia Funke"]
  - ["Ursula K. Le Guin"]
hints:
  - kosten: 0
    text: |
      `SELECT name FROM autoren;`
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Alle Autoren-Namen

Nur die Spalte `name` aus `autoren`.
