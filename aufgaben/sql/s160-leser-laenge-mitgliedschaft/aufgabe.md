---
schema_version: 1
id: s160-leser-laenge-mitgliedschaft
revision: 1
titel: "Mitgliedschaftsjahre pro Leser"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [date, julianday, cast]
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
erwartete_spalten: ["name", "jahre"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Hans Wagner", 18]
  - ["Eva Schulz", 16]
  - ["Karin Koehler", 13]
  - ["Ines Becker", 12]
  - ["Bernd Mueller", 10]
  - ["Maria Klein", 10]
  - ["Anna Schmidt", 8]
  - ["Felix Bauer", 8]
  - ["Olivia Krueger", 7]
  - ["Clara Weber", 6]
  - ["Jonas Schaefer", 6]
  - ["Niklas Wolf", 5]
  - ["Greta Hoffmann", 4]
  - ["David Fischer", 3]
  - ["Lukas Richter", 3]
hints:
  - kosten: 0
    text: |
      (julianday-Diff) / 365 als ganze Jahre.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Mitgliedsjahre

Name + ganze Jahre Mitgliedschaft (Stand 2026-05-11), längste zuerst.
