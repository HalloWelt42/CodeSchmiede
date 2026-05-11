---
schema_version: 1
id: s039-leser-altersgruppen
revision: 1
titel: "Altersgruppen der Leser"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [case-when]
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
erwartete_spalten: ["name", "alter_jahre", "gruppe"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["David Fischer", 19, "jung"]
  - ["Lukas Richter", 22, "jung"]
  - ["Greta Hoffmann", 25, "jung"]
  - ["Niklas Wolf", 27, "jung"]
  - ["Clara Weber", 28, "jung"]
  - ["Jonas Schaefer", 30, "mittel"]
  - ["Olivia Krueger", 33, "mittel"]
  - ["Anna Schmidt", 34, "mittel"]
  - ["Felix Bauer", 37, "mittel"]
  - ["Maria Klein", 39, "mittel"]
  - ["Bernd Mueller", 42, "mittel"]
  - ["Ines Becker", 45, "mittel"]
  - ["Karin Koehler", 52, "reif"]
  - ["Eva Schulz", 56, "reif"]
  - ["Hans Wagner", 61, "reif"]
hints:
  - kosten: 0
    text: |
      CASE WHEN mit drei Klassen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Altersgruppen der Leser

Klassifiziere Leser:
- < 30 -> 'jung'
- 30-49 -> 'mittel'
- ab 50 -> 'reif'
