---
schema_version: 1
id: q071-zum-wiegen
revision: 1
titel: Aufstellung zum Wiegen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 2
schaetz_minuten: 2
tags:
- kurs
- order_by
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 7
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
sortierung_egal: false
erwartetes_ergebnis:
- - Pünktchen
  - 2.9
- - Pina
  - 3.5
- - Pia
  - 3.8
- - Pablo
  - 4.0
- - Pit
  - 4.2
- - Polly
  - 4.6
- - Pepe
  - 4.9
- - Paul
  - 5.1
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
starter_code: 'SELECT name, gewicht_kg

  FROM pinguine

  ORDER BY gewicht_kg;'
---

Die Abfrage steht schon da: sie stellt die Pinguine vom leichtesten bis zum schwersten auf. Prüfe sie.
