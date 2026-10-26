---
schema_version: 1
id: q077-groesste-portionen
revision: 1
titel: Die größten Portionen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- order_by
- limit
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
- tag
- fisch
- menge
sortierung_egal: false
erwartetes_ergebnis:
- - '2026-10-20'
  - Hering
  - 8
- - '2026-10-22'
  - Makrele
  - 7
- - '2026-10-20'
  - Hering
  - 6
hints:
- kosten: 0
  text: Zwei Fütterungen haben sechs Fische; die zweite Sortierspalte entscheidet.
- kosten: 2
  text: '`ORDER BY menge DESC, tag`'
starter_code: ''
---

Hole Tag, Fisch und Menge der drei größten Fütterungen. Bei gleicher Menge kommt der frühere Tag zuerst.
