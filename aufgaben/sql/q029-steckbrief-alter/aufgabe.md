---
schema_version: 1
id: q029-steckbrief-alter
revision: 1
titel: 'Steckbrief: das Alter'
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- projekt
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
- name
- kolonie
- lieblingsfisch
- jahre
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - Nord
  - Hering
  - 7
- - Pia
  - Süd
  - Lachs
  - 6
- - Paul
  - Nord
  - Hering
  - 9
- - Pina
  - Nord
  - null
  - 4
- - Pepe
  - Süd
  - Makrele
  - 8
- - Polly
  - Nord
  - Lachs
  - 7
- - Pablo
  - Ost
  - Hering
  - 5
- - Pünktchen
  - Ost
  - null
  - 3
hints:
- kosten: 0
  text: '`2026 - geburtsjahr AS jahre` als vierte Spalte.'
starter_code: 'SELECT name, kolonie, lieblingsfisch

  FROM pinguine;'
---

**Kapitelprojekt Pinguinsteckbrief, Stück 2.** Deine Abfrage aus Stück 1 steht schon da. Ergänze am Ende eine Spalte `jahre` mit dem Alter im Jahr 2026.
