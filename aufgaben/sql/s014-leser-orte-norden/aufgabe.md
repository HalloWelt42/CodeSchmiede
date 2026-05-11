---
schema_version: 1
id: s014-leser-orte-norden
revision: 1
titel: "Leser aus Norddeutschland"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [where, in]
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
  - ["Bernd Mueller", "Hamburg"]
  - ["David Fischer", "Berlin"]
  - ["Greta Hoffmann", "Hamburg"]
  - ["Ines Becker", "Berlin"]
  - ["Karin Koehler", "Leipzig"]
  - ["Lukas Richter", "Dresden"]
  - ["Maria Klein", "Hamburg"]
  - ["Niklas Wolf", "Berlin"]
hints:
  - kosten: 0
    text: |
      `WHERE ort IN ('Hamburg','Berlin', ...)`.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser aus Norddeutschland

Namen + Ort aller Leser aus Hamburg, Berlin, Leipzig oder Dresden.
