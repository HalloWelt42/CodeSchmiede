---
schema_version: 1
id: s106-first-value-leser
revision: 1
titel: "Erstes ausgeliehenes Buch pro Leser"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 20
schaetz_minuten: 12
tags: [window-function, first-value, partition-by]
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
erwartete_spalten: ["name", "erstes_buch"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Anna Schmidt", "Siddhartha"]
  - ["Bernd Mueller", "Buddenbrooks"]
  - ["Clara Weber", "Pippi Langstrumpf"]
  - ["David Fischer", "1984"]
  - ["Eva Schulz", "Schachnovelle"]
  - ["Felix Bauer", "Kafka am Strand"]
  - ["Greta Hoffmann", "Pippi Langstrumpf"]
  - ["Hans Wagner", "Der Process"]
  - ["Ines Becker", "Siddhartha"]
  - ["Jonas Schaefer", "Erdsee"]
  - ["Karin Koehler", "1984"]
  - ["Lukas Richter", "Die Verwandlung"]
  - ["Maria Klein", "Naokos Laecheln"]
  - ["Niklas Wolf", "Der Process"]
  - ["Olivia Krueger", "Der Zauberberg"]
hints:
  - kosten: 0
    text: |
      `FIRST_VALUE(...) OVER (PARTITION BY ... ORDER BY ...)`. DISTINCT, damit jede Person nur einmal.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Erstes ausgeliehenes Buch pro Leser

Leser-Name + Titel seiner ersten Ausleihe (alphabetisch nach Leser).
