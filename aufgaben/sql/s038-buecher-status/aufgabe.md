---
schema_version: 1
id: s038-buecher-status
revision: 1
titel: "Buchstatus per CASE"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 5
tags: [case-when, expression]
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
erwartete_spalten: ["titel", "status"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Siddhartha", "wenige"]
  - ["Der Steppenwolf", "wenige"]
  - ["Schachnovelle", "wenige"]
  - ["Die Welt von Gestern", "einzeln"]
  - ["Die Verwandlung", "viele"]
  - ["Der Process", "wenige"]
  - ["Buddenbrooks", "einzeln"]
  - ["Der Zauberberg", "einzeln"]
  - ["Pippi Langstrumpf", "viele"]
  - ["Karlsson vom Dach", "wenige"]
  - ["1984", "viele"]
  - ["Farm der Tiere", "wenige"]
  - ["Stolz und Vorurteil", "wenige"]
  - ["Emma", "einzeln"]
  - ["Naokos Laecheln", "wenige"]
  - ["Kafka am Strand", "wenige"]
  - ["Tintenherz", "viele"]
  - ["Drachenreiter", "wenige"]
  - ["Erdsee", "wenige"]
  - ["Die linke Hand der Dunkelheit", "wenige"]
hints:
  - kosten: 0
    text: |
      `CASE WHEN ... THEN ... WHEN ... THEN ... ELSE ... END`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Buchstatus per CASE

Kategorisiere Buecher nach Exemplar-Anzahl:
- 1 -> 'einzeln'
- 2-4 -> 'wenige'
- sonst -> 'viele'
