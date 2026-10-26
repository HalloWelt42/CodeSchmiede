---
schema_version: 1
id: q114-raetselkolonien
revision: 1
titel: Kolonien mit Rätseln
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
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
- lage
sortierung_egal: true
erwartetes_ergebnis:
- - Nord
  - Packeis
- - Ost
  - Sandstrand
hints:
- kosten: 0
  text: Die Unterabfrage liefert Kolonien aus der Tabelle pinguine.
- kosten: 2
  text: '`WHERE name IN (SELECT kolonie ...)`'
starter_code: ''
---

Hole Name und Lage aller Kolonien, in denen mindestens ein Pinguin mit unbekanntem Lieblingsfisch wohnt.
