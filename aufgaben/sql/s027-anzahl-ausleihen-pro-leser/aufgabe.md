---
schema_version: 1
id: s027-anzahl-ausleihen-pro-leser
revision: 1
titel: "Anzahl Ausleihen pro Leser"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 7
tags: [join, group-by, count]
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
erwartete_spalten: ["name", "anzahl"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Clara Weber", 3]
  - ["Eva Schulz", 3]
  - ["Anna Schmidt", 2]
  - ["Bernd Mueller", 2]
  - ["Greta Hoffmann", 2]
  - ["Hans Wagner", 2]
  - ["Ines Becker", 2]
  - ["Jonas Schaefer", 2]
  - ["Lukas Richter", 2]
  - ["Maria Klein", 2]
  - ["David Fischer", 1]
  - ["Felix Bauer", 1]
  - ["Karin Koehler", 1]
  - ["Niklas Wolf", 1]
  - ["Olivia Krueger", 1]
hints:
  - kosten: 0
    text: |
      JOIN + GROUP BY auf Leser, COUNT der Ausleihen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Anzahl Ausleihen pro Leser

Leser-Name + wieviel Bücher er ausgeliehen hat (gesamt), absteigend.
