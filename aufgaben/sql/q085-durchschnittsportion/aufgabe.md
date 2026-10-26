---
schema_version: 1
id: q085-durchschnittsportion
revision: 1
titel: Die durchschnittliche Portion
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- aggregat
- rechnen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 8
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
- schnitt
sortierung_egal: false
erwartetes_ergebnis:
- - 4.8
hints:
- kosten: 0
  text: ROUND kann eine andere Funktion umschließen.
- kosten: 2
  text: '`ROUND(AVG(menge), 1)`'
starter_code: ''
---

Wie viele Fische gibt es im Schnitt pro Fütterung? Runde auf eine Stelle nach dem Komma; die Spalte heißt `schnitt`.
