---
schema_version: 1
id: s017-top-3-dickste
revision: 1
titel: "Top 3 dickste Buecher"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [order-by, limit]
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
erwartete_spalten: ["titel", "seiten"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Der Zauberberg", 992]
  - ["Buddenbrooks", 759]
  - ["Kafka am Strand", 624]
hints:
  - kosten: 0
    text: |
      `ORDER BY seiten DESC LIMIT 3` -- die ersten 3 nach Sortierung.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Top 3 dickste Buecher

Die drei Buecher mit den meisten Seiten.
