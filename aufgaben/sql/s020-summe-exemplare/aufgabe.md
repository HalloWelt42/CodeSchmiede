---
schema_version: 1
id: s020-summe-exemplare
revision: 1
titel: "Summe aller Exemplare"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags: [sum, aggregat]
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
erwartete_spalten: ["gesamt"]
sortierung_egal: false
erwartetes_ergebnis:
  - [59]
hints:
  - kosten: 0
    text: |
      `SUM(exemplare)` summiert die Spalte ueber alle Zeilen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Summe aller Exemplare

Gesamtzahl aller Buchexemplare. Spalte `gesamt`.
