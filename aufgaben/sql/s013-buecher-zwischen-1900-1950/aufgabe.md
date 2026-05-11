---
schema_version: 1
id: s013-buecher-zwischen-1900-1950
revision: 1
titel: "Bücher 1900-1950"
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
erwartete_spalten: ["titel", "jahr"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Buddenbrooks", 1901]
  - ["Die Verwandlung", 1915]
  - ["Siddhartha", 1922]
  - ["Der Zauberberg", 1924]
  - ["Der Process", 1925]
  - ["Der Steppenwolf", 1927]
  - ["Schachnovelle", 1942]
  - ["Die Welt von Gestern", 1942]
  - ["Pippi Langstrumpf", 1945]
  - ["Farm der Tiere", 1945]
  - ["1984", 1949]
hints:
  - kosten: 0
    text: |
      `BETWEEN 1900 AND 1950` ist inklusiv beidseits.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bücher 1900-1950

Titel und Jahr aller Bücher zwischen 1900 und 1950 (inklusiv).
