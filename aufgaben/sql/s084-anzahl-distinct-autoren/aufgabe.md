---
schema_version: 1
id: s084-anzahl-distinct-autoren
revision: 1
titel: "Anzahl verschiedener Autoren mit Büchern"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [count-distinct]
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
erwartete_spalten: ["anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - [10]
hints:
  - kosten: 0
    text: |
      `COUNT(DISTINCT spalte)` zählt verschiedene Werte.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Anzahl verschiedener Autoren

Wieviele verschiedene Autoren tauchen in der Bücher-Tabelle auf?
