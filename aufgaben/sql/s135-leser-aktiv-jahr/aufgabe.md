---
schema_version: 1
id: s135-leser-aktiv-jahr
revision: 1
titel: "Aktive Leser im Jahr 2025"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [join, where, date]
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
erwartete_spalten: ["name"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Anna Schmidt"]
  - ["Bernd Mueller"]
  - ["Clara Weber"]
  - ["David Fischer"]
  - ["Eva Schulz"]
  - ["Felix Bauer"]
  - ["Greta Hoffmann"]
  - ["Hans Wagner"]
  - ["Ines Becker"]
  - ["Jonas Schaefer"]
  - ["Karin Koehler"]
  - ["Lukas Richter"]
  - ["Maria Klein"]
  - ["Niklas Wolf"]
  - ["Olivia Krueger"]
hints:
  - kosten: 0
    text: |
      JOIN + WHERE auf Jahr aus ausgeliehen_am.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Aktive Leser 2025

Distinkte Leser mit mind. einer Ausleihe in 2025.
