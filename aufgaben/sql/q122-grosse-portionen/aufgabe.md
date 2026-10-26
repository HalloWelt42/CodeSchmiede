---
schema_version: 1
id: q122-grosse-portionen
revision: 1
titel: Groß oder normal
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- case
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 12
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
- menge
- portion
sortierung_egal: false
erwartetes_ergebnis:
- - '2026-10-20'
  - 6
  - groß
- - '2026-10-20'
  - 4
  - normal
- - '2026-10-20'
  - 8
  - groß
- - '2026-10-20'
  - 5
  - normal
- - '2026-10-21'
  - 5
  - normal
- - '2026-10-21'
  - 3
  - normal
- - '2026-10-21'
  - 6
  - groß
- - '2026-10-21'
  - 4
  - normal
- - '2026-10-22'
  - 7
  - groß
- - '2026-10-22'
  - 2
  - normal
- - '2026-10-22'
  - 5
  - normal
- - '2026-10-22'
  - 3
  - normal
hints:
- kosten: 0
  text: Der Wert für alle übrigen Fälle.
starter_code: "SELECT tag, menge,\n       CASE WHEN menge >= 6 THEN 'groß' ___ 'normal' END AS portion\nFROM fuetterungen;"
---

Ergänze die Lücke `___`, damit jede Fütterung mit weniger als sechs Fischen als normal gilt.
