---
schema_version: 1
id: q057-winterlage
revision: 1
titel: Winterlage
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- textfunktionen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 5
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
- winterlage
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - Packeis
- - Süd
  - Felsenküste
- - Ost
  - Sandstrand
- - West
  - Schneehöhle
hints:
- kosten: 0
  text: '`REPLACE(text, alt, neu)`'
starter_code: ''
---

Im Winter heißt alles mit Eis bei den Pflegern Schnee. Hole Name und Lage jeder Kolonie, in der Lage `'Eis'` durch `'Schnee'` ersetzt (Spalte `winterlage`). REPLACE achtet dabei genau auf die Schreibweise.
