---
schema_version: 1
id: s197-buecher-und-kategorien-uebersicht
revision: 1
titel: "Kategorien-Übersicht: Anzahl + Schnitt-Seiten"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [group-by, count, avg, sum]
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
erwartete_spalten: ["kategorie", "anzahl", "schnitt_seiten", "exemplare"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Roman", 11, 433.5, 26]
  - ["Kinderbuch", 4, 325.0, 19]
  - ["Erzählung", 2, 85.0, 9]
  - ["Biographie", 1, 528.0, 1]
  - ["Fantasy", 1, 224.0, 2]
  - ["Sci-Fi", 1, 304.0, 2]
hints:
  - kosten: 0
    text: |
      GROUP BY kategorie + drei Aggregate.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Kategorien-Übersicht

Kategorie + Buchanzahl + Durchschnitt Seiten + Exemplare-Summe.
