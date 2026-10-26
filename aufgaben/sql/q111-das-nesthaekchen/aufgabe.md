---
schema_version: 1
id: q111-das-nesthaekchen
revision: 1
titel: Das Nesthäkchen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 2
schaetz_minuten: 2
tags:
- kurs
- unterabfrage
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 11
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
- geburtsjahr
sortierung_egal: false
erwartetes_ergebnis:
- - Pünktchen
  - 2023
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
starter_code: 'SELECT name, geburtsjahr

  FROM pinguine

  WHERE geburtsjahr = (SELECT MAX(geburtsjahr) FROM pinguine);'
---

Die Abfrage steht schon da: sie findet den jüngsten Pinguin. Prüfe sie.
