---
schema_version: 1
id: q146-pablo-zieht-um
revision: 1
titel: Pablo zieht um
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
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
kontrolle: SELECT name, kolonie FROM pinguine ORDER BY id
erwartete_spalten:
- name
- kolonie
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - Nord
- - Pia
  - Süd
- - Paul
  - Nord
- - Pina
  - Nord
- - Pepe
  - Süd
- - Polly
  - Nord
- - Pablo
  - Süd
- - Pünktchen
  - Ost
hints:
- kosten: 0
  text: Dem UPDATE fehlt sein WHERE.
starter_code: 'UPDATE pinguine

  SET kolonie = ''Süd'';'
---

Das Skript soll Pablo in die Südkolonie schicken, schickt aber alle dorthin. Repariere es.
