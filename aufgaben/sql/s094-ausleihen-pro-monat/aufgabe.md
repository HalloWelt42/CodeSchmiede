---
schema_version: 1
id: s094-ausleihen-pro-monat
revision: 1
titel: "Ausleihen pro Monat"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [date, strftime, group-by]
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
erwartete_spalten: ["monat", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["2024-11", 1]
  - ["2024-12", 1]
  - ["2025-01", 6]
  - ["2025-02", 6]
  - ["2025-03", 7]
  - ["2025-04", 6]
hints:
  - kosten: 0
    text: |
      Wie bei Bestellungen-pro-Monat -- nur auf ausleihen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Ausleihen pro Monat

Monat (YYYY-MM) + Anzahl Ausleihen, chronologisch.
