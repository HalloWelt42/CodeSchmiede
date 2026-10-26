---
schema_version: 1
id: q106-alle-pfleger
revision: 1
titel: Das ganze Pflegeteam
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- left_join
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 10
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
- pfleger
- lage
sortierung_egal: true
erwartetes_ergebnis:
- - Greta
  - Packeis
- - Hannes
  - Felsenküste
- - Ida
  - Sandstrand
- - Jonas
  - null
hints:
- kosten: 0
  text: Bei einem JOIN fiele Jonas heraus.
- kosten: 2
  text: '`FROM pfleger pf LEFT JOIN kolonien k ...`'
starter_code: ''
---

Hole jeden Pfleger (Spalte `pfleger`) mit der Lage seiner Kolonie. Auch Jonas, der überall einspringt, soll dabei sein.
