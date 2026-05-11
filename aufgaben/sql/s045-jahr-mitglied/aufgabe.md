---
schema_version: 1
id: s045-jahr-mitglied
revision: 1
titel: "Beitrittsjahr der Leser"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: mittel
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [date, strftime]
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
erwartete_spalten: ["name", "jahr"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Hans Wagner", "2008"]
  - ["Eva Schulz", "2010"]
  - ["Karin Koehler", "2012"]
  - ["Ines Becker", "2014"]
  - ["Bernd Mueller", "2015"]
  - ["Maria Klein", "2016"]
  - ["Felix Bauer", "2017"]
  - ["Anna Schmidt", "2018"]
  - ["Olivia Krueger", "2018"]
  - ["Jonas Schaefer", "2019"]
  - ["Clara Weber", "2020"]
  - ["Niklas Wolf", "2020"]
  - ["Greta Hoffmann", "2021"]
  - ["David Fischer", "2022"]
  - ["Lukas Richter", "2023"]
hints:
  - kosten: 0
    text: |
      `strftime('%Y', datum)` extrahiert das Jahr als String.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Beitrittsjahr

Name + Beitrittsjahr aller Leser, nach Jahr und dann Name.
