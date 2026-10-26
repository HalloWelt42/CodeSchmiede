---
schema_version: 1
id: q065-kein-lachs
revision: 1
titel: Bloß kein Lachs
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- null_werte
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 6
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
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
- - Paul
- - Pina
- - Pepe
- - Pablo
- - Pünktchen
hints:
- kosten: 0
  text: Ein Vergleich allein lässt die Unbekannten herausfallen.
- kosten: 2
  text: '`OR lieblingsfisch IS NULL`'
starter_code: ''
---

Hole die Namen aller Pinguine, deren Lieblingsfisch nicht Lachs ist. Diesmal sollen auch die Pinguine mit unbekanntem Lieblingsfisch dabei sein.
