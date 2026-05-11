---
schema_version: 1
id: s155-autoren-jahre-zwischen
revision: 1
titel: "Autoren des 19. Jahrhunderts"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 3
tags: [where, between]
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
erwartete_spalten: ["name", "geburtsjahr"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Thomas Mann", 1875]
  - ["Hermann Hesse", 1877]
  - ["Stefan Zweig", 1881]
  - ["Franz Kafka", 1883]
hints:
  - kosten: 0
    text: |
      BETWEEN auf Geburtsjahr.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Autoren 19. Jahrhundert

Autoren mit Geburtsjahr 1801-1900.
