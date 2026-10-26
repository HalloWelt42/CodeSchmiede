---
schema_version: 1
id: q141-pina-entscheidet-sich
revision: 1
titel: Pina entscheidet sich
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 2
schaetz_minuten: 2
tags:
- kurs
- update
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 14
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
kontrolle: SELECT id, name, lieblingsfisch FROM pinguine ORDER BY id
erwartete_spalten:
- id
- name
- lieblingsfisch
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - Pit
  - Hering
- - 2
  - Pia
  - Lachs
- - 3
  - Paul
  - Hering
- - 4
  - Pina
  - Sardine
- - 5
  - Pepe
  - Makrele
- - 6
  - Polly
  - Lachs
- - 7
  - Pablo
  - Hering
- - 8
  - Pünktchen
  - null
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
starter_code: 'UPDATE pinguine

  SET lieblingsfisch = ''Sardine''

  WHERE id = 4;'
---

Das Skript steht schon da: Pina (Nummer 4) bekommt Sardine als Lieblingsfisch. Prüfe es.
