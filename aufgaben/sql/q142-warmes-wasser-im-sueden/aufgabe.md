---
schema_version: 1
id: q142-warmes-wasser-im-sueden
revision: 1
titel: Warmes Wasser im Süden
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- update
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 14
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
kontrolle: SELECT * FROM kolonien ORDER BY name
erwartete_spalten:
- name
- lage
- wassertemperatur
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - Packeis
  - -1.5
- - Ost
  - Sandstrand
  - 9.5
- - Süd
  - Felsenküste
  - 5.0
- - West
  - Eishöhle
  - -0.5
hints:
- kosten: 0
  text: Das Wort vor den neuen Werten.
starter_code: 'UPDATE kolonien

  ___ wassertemperatur = 5.0

  WHERE name = ''Süd'';'
---

Ergänze die Lücke `___`, damit das Wasser der Südkolonie 5 Grad warm ist.
