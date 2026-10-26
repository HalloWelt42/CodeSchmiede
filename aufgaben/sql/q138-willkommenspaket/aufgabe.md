---
schema_version: 1
id: q138-willkommenspaket
revision: 1
titel: Das Willkommenspaket
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- insert
- kurztest
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
kontrolle: 'SELECT p.name, f.tag, f.fisch, f.menge

  FROM fuetterungen f JOIN pinguine p ON p.id = f.pinguin_id

  WHERE p.kolonie = ''West''

  ORDER BY f.tag'
erwartete_spalten:
- name
- tag
- fisch
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - Pelle
  - '2026-10-23'
  - Sardine
  - 2
- - Pelle
  - '2026-10-24'
  - Hering
  - 3
hints:
- kosten: 0
  text: Erst Pelle, dann seine Fütterungen; die gehören zu pinguin_id 9.
- kosten: 2
  text: Zwei Klammern hinter VALUES in der zweiten Anweisung.
starter_code: ''
---

Pelle zieht ein (Nummer 9, Westkolonie, 3,1 Kilo, geboren 2025, Lieblingsfisch noch unbekannt). Zur Begrüßung bekommt er am 23. Oktober 2026 zwei Sardinen und am 24. Oktober drei Heringe; trage beide Fütterungen mit einer Anweisung ein.
