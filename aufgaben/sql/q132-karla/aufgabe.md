---
schema_version: 1
id: q132-karla
revision: 1
titel: Karla fängt an
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- insert
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 13
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
kontrolle: SELECT * FROM pfleger ORDER BY id
erwartete_spalten:
- id
- name
- kolonie
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - Greta
  - Nord
- - 2
  - Hannes
  - Süd
- - 3
  - Ida
  - Ost
- - 4
  - Jonas
  - null
- - 5
  - Karla
  - West
hints:
- kosten: 0
  text: Das Wort vor den Werten.
starter_code: 'INSERT INTO pfleger (id, name, kolonie)

  ___ (5, ''Karla'', ''West'');'
---

Ergänze die Lücke `___`, damit Pflegerin Karla mit der Nummer 5 für die Westkolonie eingetragen wird.
