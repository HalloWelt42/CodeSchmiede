---
schema_version: 1
id: q152-kein-springer-mehr
revision: 1
titel: Kein Springer mehr
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- delete
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 15
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
kontrolle: SELECT * FROM pfleger ORDER BY id
erwartete_spalten:
- id
- name
- kolonie
sortierung_egal: false
erwartetes_ergebnis:
- - 1
  - Greta
  - Nord
- - 2
  - Hannes
  - Süd
- - 3
  - Ida
  - Ost
hints:
- kosten: 0
  text: Löschen aus ...
starter_code: 'DELETE ___ pfleger

  WHERE kolonie IS NULL;'
---

Ergänze die Lücke `___`, damit Pfleger ohne feste Kolonie aus der Tabelle verschwinden.
