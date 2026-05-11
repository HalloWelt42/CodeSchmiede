---
schema_version: 1
id: s177-buecher-mit-ausleihzahlen
revision: 1
titel: "Buecher mit Ausleihzahl"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [left-join, group-by, count]
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
erwartete_spalten: ["titel", "ausleihen"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["1984", 3]
  - ["Der Process", 2]
  - ["Der Zauberberg", 2]
  - ["Kafka am Strand", 2]
  - ["Pippi Langstrumpf", 2]
  - ["Siddhartha", 2]
  - ["Buddenbrooks", 1]
  - ["Der Steppenwolf", 1]
  - ["Die Verwandlung", 1]
  - ["Die Welt von Gestern", 1]
  - ["Die linke Hand der Dunkelheit", 1]
  - ["Drachenreiter", 1]
  - ["Emma", 1]
  - ["Erdsee", 1]
  - ["Farm der Tiere", 1]
  - ["Karlsson vom Dach", 1]
  - ["Naokos Laecheln", 1]
  - ["Schachnovelle", 1]
  - ["Stolz und Vorurteil", 1]
  - ["Tintenherz", 1]
hints:
  - kosten: 0
    text: |
      LEFT JOIN damit auch nie-ausgeliehene Bücher mit COUNT 0 erscheinen.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Bücher mit Ausleihzahl

Jedes Buch + Anzahl Ausleihen (0 wenn nie), häufigste zuerst.
