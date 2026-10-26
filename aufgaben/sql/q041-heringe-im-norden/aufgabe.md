---
schema_version: 1
id: q041-heringe-im-norden
revision: 1
titel: Heringsfreunde im Norden
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 2
schaetz_minuten: 2
tags:
- kurs
- logik
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 4
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
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
- - Paul
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
starter_code: 'SELECT name

  FROM pinguine

  WHERE kolonie = ''Nord'' AND lieblingsfisch = ''Hering'';'
---

Die Abfrage steht schon da: sie holt die Pinguine aus dem Norden, die Hering am liebsten mögen. Prüfe sie und schau dir im Kurs an, wie WHERE beide Bedingungen prüft.
