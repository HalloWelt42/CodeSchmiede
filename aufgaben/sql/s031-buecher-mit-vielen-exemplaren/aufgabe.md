---
schema_version: 1
id: s031-buecher-mit-vielen-exemplaren
revision: 1
titel: "Bücher mit überdurchschnittlich vielen Exemplaren"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [subquery, avg, vergleich]
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
erwartete_spalten: ["titel", "exemplare"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Pippi Langstrumpf", 6]
  - ["1984", 5]
  - ["Die Verwandlung", 5]
  - ["Tintenherz", 5]
  - ["Drachenreiter", 4]
  - ["Farm der Tiere", 4]
  - ["Karlsson vom Dach", 4]
  - ["Schachnovelle", 4]
  - ["Kafka am Strand", 3]
  - ["Siddhartha", 3]
hints:
  - kosten: 0
    text: |
      Subquery in WHERE: `> (SELECT AVG(exemplare) FROM bücher)`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Überdurchschnittlich viele Exemplare

Bücher mit mehr Exemplaren als der Durchschnitt.
