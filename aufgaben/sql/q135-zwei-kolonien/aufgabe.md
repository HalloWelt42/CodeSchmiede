---
schema_version: 1
id: q135-zwei-kolonien
revision: 1
titel: Zwei neue Kolonien
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
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
kontrolle: SELECT * FROM kolonien ORDER BY name
erwartete_spalten:
- name
- lage
- wassertemperatur
sortierung_egal: false
erwartetes_ergebnis:
- - Insel
  - Vulkanstrand
  - 12.0
- - Mitte
  - Lagune
  - 6.5
- - Nord
  - Packeis
  - -1.5
- - Ost
  - Sandstrand
  - 9.5
- - Süd
  - Felsenküste
  - 4.0
- - West
  - Eishöhle
  - -0.5
hints:
- kosten: 0
  text: Zwei Klammern hinter VALUES, mit Komma getrennt.
starter_code: ''
---

Lege mit einer einzigen Anweisung zwei Kolonien an: Mitte an einer Lagune mit 6,5 Grad und Insel am Vulkanstrand mit 12 Grad.
