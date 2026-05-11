---
schema_version: 1
id: s113-leser-mehr-als-schnitt
revision: 1
titel: "Leser mit mehr Ausleihen als Schnitt"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [cte, subquery, avg]
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
erwartete_spalten: ["name", "anz"]
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
hints:
  - kosten: 0
    text: |
      CTE mit Pro-Leser-Anzahl, dann WHERE > AVG aus CTE.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Vielleser ueber dem Schnitt

Leser, die mehr Ausleihen haben als der Leser-Durchschnitt.
