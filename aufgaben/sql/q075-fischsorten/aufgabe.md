---
schema_version: 1
id: q075-fischsorten
revision: 1
titel: Welche Fische gibt es?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- distinct
- order_by
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
- fisch
sortierung_egal: false
erwartetes_ergebnis:
- - Hering
- - Lachs
- - Makrele
- - Sardine
hints:
- kosten: 0
  text: DISTINCT für jeden nur einmal, ORDER BY für das Alphabet.
starter_code: ''
---

Hole jede Fischsorte, die in der Tabelle `fuetterungen` vorkommt, genau einmal, nach dem Alphabet sortiert.
