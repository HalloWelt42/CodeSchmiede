---
schema_version: 1
id: s183-autor-mit-buch-und-leser
revision: 1
titel: "Autor mit Buch- und Leser-Anzahl"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [join, left-join, count-distinct]
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
erwartete_spalten: ["name", "buecher", "leser"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Astrid Lindgren", 2, 2]
  - ["Cornelia Funke", 2, 2]
  - ["Franz Kafka", 2, 3]
  - ["George Orwell", 2, 4]
  - ["Haruki Murakami", 2, 2]
  - ["Hermann Hesse", 2, 3]
  - ["Jane Austen", 2, 2]
  - ["Stefan Zweig", 2, 1]
  - ["Thomas Mann", 2, 2]
  - ["Ursula K. Le Guin", 2, 1]
hints:
  - kosten: 0
    text: |
      JOIN buecher, LEFT JOIN ausleihen, COUNT DISTINCT.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Autor: Buecher und Leser

Für jeden Autor: Anzahl Bücher + Anzahl unterschiedlicher Leser.
