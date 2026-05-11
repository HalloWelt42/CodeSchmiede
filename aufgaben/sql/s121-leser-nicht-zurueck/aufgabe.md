---
schema_version: 1
id: s121-leser-nicht-zurueck
revision: 1
titel: "Leser mit offenen Büchern"
sprache: sql
task_type: sql_abfrage
runner_type: sqlite_backend
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 4
tags: [join, is-null, distinct]
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
erwartete_spalten: ["name"]
sortierung_egal: false
erwartetes_ergebnis:
  - ["Bernd Mueller"]
  - ["Clara Weber"]
  - ["Greta Hoffmann"]
  - ["Ines Becker"]
  - ["Lukas Richter"]
  - ["Niklas Wolf"]
  - ["Olivia Krueger"]
hints:
  - kosten: 0
    text: |
      DISTINCT + WHERE IS NULL.
starter_code: |
  SELECT ___
  FROM ___
  WHERE ___;
---

# Leser mit offenen Büchern

Distinkte Leser, die mindestens ein noch nicht zurückgegebenes Buch haben.
