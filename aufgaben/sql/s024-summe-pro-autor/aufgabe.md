---
schema_version: 1
id: s024-summe-pro-autor
revision: 1
titel: "Anzahl Buecher pro Autor"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [group-by, count]
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
erwartete_spalten: ["autor_id", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - [1, 2]
  - [2, 2]
  - [3, 2]
  - [4, 2]
  - [5, 2]
  - [6, 2]
  - [7, 2]
  - [8, 2]
  - [9, 2]
  - [10, 2]
hints:
  - kosten: 0
    text: |
      `GROUP BY autor_id` plus `COUNT(*)`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Anzahl Buecher pro Autor

Autor-ID und wieviele Buecher der Autor hat, sortiert nach Autor-ID.
