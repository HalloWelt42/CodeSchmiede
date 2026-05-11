---
schema_version: 1
id: s053-buecher-anzahl-autoren-mehr-als-1
revision: 1
titel: "Autoren mit mehr als einem Buch"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [join, group-by, having]
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
erwartete_spalten: ["name", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Astrid Lindgren", 2]
  - ["Cornelia Funke", 2]
  - ["Franz Kafka", 2]
  - ["George Orwell", 2]
  - ["Haruki Murakami", 2]
  - ["Hermann Hesse", 2]
  - ["Jane Austen", 2]
  - ["Stefan Zweig", 2]
  - ["Thomas Mann", 2]
  - ["Ursula K. Le Guin", 2]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY + HAVING.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Autoren mit mehr als einem Buch

Autoren mit Buchanzahl > 1, viele zuerst.
