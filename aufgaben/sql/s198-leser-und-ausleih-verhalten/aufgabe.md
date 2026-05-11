---
schema_version: 1
id: s198-leser-und-ausleih-verhalten
revision: 1
titel: "Leser: Anzahl offen + abgeschlossen"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [left-join, case, group-by]
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
erwartete_spalten: ["name", "abgeschlossen", "offen"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Anna Schmidt", 2, 0]
  - ["Bernd Mueller", 1, 1]
  - ["Clara Weber", 2, 1]
  - ["David Fischer", 1, 0]
  - ["Eva Schulz", 3, 0]
  - ["Felix Bauer", 1, 0]
  - ["Greta Hoffmann", 0, 2]
  - ["Hans Wagner", 2, 0]
  - ["Ines Becker", 1, 1]
  - ["Jonas Schaefer", 2, 0]
  - ["Karin Koehler", 1, 0]
  - ["Lukas Richter", 1, 1]
  - ["Maria Klein", 2, 0]
  - ["Niklas Wolf", 0, 1]
  - ["Olivia Krueger", 0, 1]
hints:
  - kosten: 0
    text: |
      CASE WHEN-Aggregate für offen/abgeschlossen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser-Verhalten

Name + abgeschlossene Ausleihen + offene Ausleihen.
