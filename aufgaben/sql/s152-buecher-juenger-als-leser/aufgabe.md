---
schema_version: 1
id: s152-buecher-juenger-als-leser
revision: 1
titel: "Buecher juenger als der jüngste Leser"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 7
tags: [subquery, max]
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
erwartete_spalten: ["titel", "jahr"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Erdsee", 1968]
  - ["Die linke Hand der Dunkelheit", 1969]
  - ["Naokos Laecheln", 1987]
  - ["Drachenreiter", 1997]
  - ["Kafka am Strand", 2002]
  - ["Tintenherz", 2003]
hints:
  - kosten: 0
    text: |
      Subquery liefert Geburtsjahr des jüngsten Lesers.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Buecher nach Geburtsjahr des jüngsten Lesers

Bücher erschienen nach dem Geburtsjahr des jüngsten Lesers (in 2026).
