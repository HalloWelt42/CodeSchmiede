---
schema_version: 1
id: s012-buecher-kindelreihe
revision: 1
titel: "Kinderbuecher mit mehr als 4 Exemplaren"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [where, and, filter]
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
erwartete_spalten: ["titel", "exemplare"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Pippi Langstrumpf", 6]
  - ["Tintenherz", 5]
hints:
  - kosten: 0
    text: |
      Zwei Bedingungen mit `AND` verknuepft.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Kinderbuecher mit mehr als 4 Exemplaren

Titel + Exemplare aller Kinderbuecher mit > 4 Exemplaren.
