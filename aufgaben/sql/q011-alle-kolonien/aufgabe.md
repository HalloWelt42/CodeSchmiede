---
schema_version: 1
id: q011-alle-kolonien
revision: 1
titel: Alle Kolonien
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 2
schaetz_minuten: 2
tags:
- kurs
- select
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 1
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
- wassertemperatur
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - Packeis
  - -1.5
- - Süd
  - Felsenküste
  - 4.0
- - Ost
  - Sandstrand
  - 9.5
- - West
  - Eishöhle
  - -0.5
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
starter_code: 'SELECT *

  FROM kolonien;'
---

Die Abfrage steht schon da: sie holt alle Spalten der Tabelle `kolonien`. Prüfe sie.
