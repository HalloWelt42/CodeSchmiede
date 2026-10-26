---
schema_version: 1
id: q158-pepe-zieht-aus
revision: 1
titel: Pepe zieht aus
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- delete
- unterabfrage
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 15
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
kontrolle: "SELECT p.name,\n       (SELECT COUNT(*) FROM fuetterungen f WHERE f.pinguin_id = p.id) AS fuetterungen,\n    \
  \   (SELECT COUNT(*) FROM fuetterungen WHERE pinguin_id NOT IN (SELECT id FROM pinguine)) AS verwaist\nFROM pinguine p\n\
  ORDER BY p.id"
erwartete_spalten:
- name
- fuetterungen
- verwaist
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - 3
  - 0
- - Pia
  - 2
  - 0
- - Paul
  - 2
  - 0
- - Pina
  - 1
  - 0
- - Polly
  - 1
  - 0
- - Pablo
  - 1
  - 0
- - Pünktchen
  - 1
  - 0
hints:
- kosten: 0
  text: Die Fütterungen findest du über eine Unterabfrage auf pinguine.
- kosten: 1
  text: Erst fuetterungen, dann pinguine.
starter_code: ''
---

Pepe zieht in einen anderen Zoo. Lösche erst seine Fütterungen, dann ihn selbst. Benutze dabei seinen Namen, nicht seine Nummer.
