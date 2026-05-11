---
schema_version: 1
id: s010-buecher-dicke
revision: 1
titel: "Lange Buecher (über 500 Seiten)"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [where, order-by, desc]
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
  - ["Tintenherz", 576]
  - ["Die Welt von Gestern", 528]
hints:
  - kosten: 0
    text: |
      `ORDER BY seiten DESC` sortiert absteigend.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Lange Buecher

Titel und Seitenzahl aller Buecher mit mehr als 500 Seiten, dickstes zuerst.
