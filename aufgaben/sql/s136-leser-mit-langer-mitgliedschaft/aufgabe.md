---
schema_version: 1
id: s136-leser-mit-langer-mitgliedschaft
revision: 1
titel: "Mitglieder ueber 5 Jahre"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: fortgeschritten
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [date, julianday]
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
erwartete_spalten: ["name", "mitglied_seit"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Hans Wagner", "2008-02-22"]
  - ["Eva Schulz", "2010-05-04"]
  - ["Karin Koehler", "2012-10-09"]
  - ["Ines Becker", "2014-04-18"]
  - ["Bernd Mueller", "2015-07-01"]
  - ["Maria Klein", "2016-03-03"]
  - ["Felix Bauer", "2017-11-30"]
  - ["Anna Schmidt", "2018-03-15"]
  - ["Olivia Krueger", "2018-06-20"]
  - ["Jonas Schaefer", "2019-08-25"]
  - ["Clara Weber", "2020-01-20"]
  - ["Niklas Wolf", "2020-12-07"]
hints:
  - kosten: 0
    text: |
      5 Jahre ~ 1825 Tage. julianday-Diff verwenden.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Mitglieder ueber 5 Jahre

Name + Beitritt fuer alle, die schon ueber 5 Jahre dabei sind (Stand 2026-05-11).
