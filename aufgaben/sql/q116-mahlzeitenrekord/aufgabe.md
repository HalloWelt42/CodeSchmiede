---
schema_version: 1
id: q116-mahlzeitenrekord
revision: 1
titel: Der Mahlzeitenrekord
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- unterabfrage
- group_by
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
- rekord
sortierung_egal: false
erwartetes_ergebnis:
- - 3
hints:
- kosten: 0
  text: 'Innen: GROUP BY pinguin_id mit COUNT(*) AS mahlzeiten.'
- kosten: 2
  text: 'Außen: `SELECT MAX(mahlzeiten) AS rekord FROM (...)`'
starter_code: ''
---

Wie oft wurde der am häufigsten gefütterte Pinguin gefüttert? Zähle erst je Pinguin in einer Unterabfrage hinter FROM und nimm dann das Größte (Spalte `rekord`).
