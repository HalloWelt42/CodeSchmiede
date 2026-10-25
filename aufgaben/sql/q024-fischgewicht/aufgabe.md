---
schema_version: 1
id: q024-fischgewicht
revision: 1
titel: Wie schwer war das Futter?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
dataset: pinguinzoo
schema_hinweis: 'kolonien(name, lage, wassertemperatur)

  pinguine(id, name, kolonie, gewicht_kg, geburtsjahr, lieblingsfisch)

  pfleger(id, name, kolonie)

  fuetterungen(id, pinguin_id, tag, fisch, menge)

  '
erwartete_spalten:
- fisch
- gramm
sortierung_egal: false
erwartetes_ergebnis:
- - Hering
  - 720
- - Lachs
  - 480
- - Hering
  - 960
- - Makrele
  - 600
- - Hering
  - 600
- - Sardine
  - 360
- - Lachs
  - 720
- - Hering
  - 480
- - Makrele
  - 840
- - Sardine
  - 240
- - Lachs
  - 600
- - Sardine
  - 360
hints:
- kosten: 0
  text: Tabelle `fuetterungen`, die Menge mal 120.
starter_code: ''
---

Ein Fisch wiegt im Schnitt 120 Gramm. Hole für jede Fütterung den Fisch und das Gewicht des Futters als Spalte `gramm`.
