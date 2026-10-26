---
schema_version: 1
id: q092-je-tag
revision: 1
titel: Fische je Tag
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- group_by
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 9
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
- tag
- fische
sortierung_egal: true
erwartetes_ergebnis:
- - '2026-10-20'
  - 23
- - '2026-10-21'
  - 18
- - '2026-10-22'
  - 17
hints:
- kosten: 0
  text: Gruppiert wird nach dem Tag.
starter_code: 'SELECT tag, SUM(menge) AS fische

  FROM fuetterungen

  GROUP BY ___;'
---

Ergänze die Lücke `___`, damit für jeden Tag die Summe der Fische herauskommt.
