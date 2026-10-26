---
schema_version: 1
id: q127-portionsgroessen
revision: 1
titel: Riesige Portionen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
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
- pinguin_id
- menge
- portion
sortierung_egal: false
erwartetes_ergebnis:
- - '2026-10-20'
  - 1
  - 6
  - ordentlich
- - '2026-10-20'
  - 2
  - 4
  - ordentlich
- - '2026-10-20'
  - 3
  - 8
  - riesig
- - '2026-10-20'
  - 5
  - 5
  - ordentlich
- - '2026-10-21'
  - 1
  - 5
  - ordentlich
- - '2026-10-21'
  - 4
  - 3
  - klein
- - '2026-10-21'
  - 6
  - 6
  - ordentlich
- - '2026-10-21'
  - 7
  - 4
  - ordentlich
- - '2026-10-22'
  - 3
  - 7
  - riesig
- - '2026-10-22'
  - 8
  - 2
  - klein
- - '2026-10-22'
  - 2
  - 5
  - ordentlich
- - '2026-10-22'
  - 1
  - 3
  - klein
hints:
- kosten: 0
  text: Die erste zutreffende Bedingung gewinnt.
- kosten: 2
  text: Die Bedingung für riesig muss vor die für ordentlich.
starter_code: "SELECT tag, pinguin_id, menge,\n       CASE WHEN menge >= 4 THEN 'ordentlich'\n            WHEN menge >= 7\
  \ THEN 'riesig'\n            ELSE 'klein'\n       END AS portion\nFROM fuetterungen;"
---

Die Abfrage soll Fütterungen ab sieben Fischen riesig nennen, ab vier ordentlich, sonst klein. Riesig kommt aber nie vor. Repariere sie.
