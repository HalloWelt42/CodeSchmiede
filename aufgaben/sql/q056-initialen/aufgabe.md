---
schema_version: 1
id: q056-initialen
revision: 1
titel: Initialen am Schlüsselbund
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
- initiale
sortierung_egal: false
erwartetes_ergebnis:
- - Greta
  - G
- - Hannes
  - H
- - Ida
  - I
- - Jonas
  - J
hints:
- kosten: 0
  text: '`SUBSTR(text, start, laenge)`, gezählt ab 1.'
starter_code: ''
---

Am Schlüsselbund hängt für jeden Pfleger ein Anhänger mit seinem ersten Buchstaben. Hole Name und ersten Buchstaben (Spalte `initiale`) aller Pfleger.
