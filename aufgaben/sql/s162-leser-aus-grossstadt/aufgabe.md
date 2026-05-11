---
schema_version: 1
id: s162-leser-aus-grossstadt
revision: 1
titel: "Leser aus den Top-Drei-Staedten"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [subquery, in, limit]
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
erwartete_spalten: ["name", "ort"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Anna Schmidt", "Berlin"]
  - ["David Fischer", "Berlin"]
  - ["Ines Becker", "Berlin"]
  - ["Niklas Wolf", "Berlin"]
  - ["Bernd Mueller", "Hamburg"]
  - ["Greta Hoffmann", "Hamburg"]
  - ["Maria Klein", "Hamburg"]
  - ["Clara Weber", "München"]
  - ["Jonas Schaefer", "München"]
  - ["Olivia Krueger", "München"]
hints:
  - kosten: 0
    text: |
      Subquery: die 3 häufigsten Orte. Hauptquery: WHERE ort IN (...).
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser aus Top-3-Staedten

Name + Ort der Leser aus den 3 Orten mit den meisten Lesern.
