---
schema_version: 1
id: q117-abweichung
revision: 1
titel: Schwerer als die Nachbarn?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- unterabfrage
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 11
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
- name
- gewicht_kg
- abweichung
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - 4.2
  - -0.15
- - Paul
  - 5.1
  - 0.75
- - Pina
  - 3.5
  - -0.85
- - Polly
  - 4.6
  - 0.25
hints:
- kosten: 0
  text: Die Unterabfrage rechnet den Schnitt der Kolonie der äußeren Zeile.
- kosten: 2
  text: '`gewicht_kg - (SELECT AVG(gewicht_kg) FROM pinguine WHERE kolonie = p.kolonie)`'
starter_code: ''
---

Hole für jeden Pinguin der Nordkolonie Name, Gewicht und wie weit er vom Durchschnittsgewicht seiner eigenen Kolonie entfernt ist, auf zwei Stellen gerundet (Spalte `abweichung`, positiv heißt schwerer).
