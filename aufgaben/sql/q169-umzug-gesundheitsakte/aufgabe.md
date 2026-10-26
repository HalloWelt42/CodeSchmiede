---
schema_version: 1
id: q169-umzug-gesundheitsakte
revision: 1
titel: 'Umzug in den Westen: die Gesundheitsakte'
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- projekt
- create_table
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 16
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
kontrolle: 'SELECT p.name, g.tag, g.befund

  FROM gesundheit g JOIN pinguine p ON p.id = g.pinguin_id

  ORDER BY p.name'
erwartete_spalten:
- name
- tag
- befund
sortierung_egal: false
erwartetes_ergebnis:
- - Pelle
  - '2026-10-24'
  - gesund
- - Pippa
  - '2026-10-24'
  - leichter Schnupfen
hints:
- kosten: 0
  text: Erst CREATE TABLE, dann ein INSERT mit zwei Klammern.
- kosten: 2
  text: '`VALUES (9, ''2026-10-24'', ''gesund''), (10, ''2026-10-24'', ''leichter Schnupfen'')`'
starter_code: "INSERT INTO pinguine (id, name, kolonie, gewicht_kg, geburtsjahr, lieblingsfisch)\nVALUES (9, 'Pelle', 'West',\
  \ 3.1, 2025, NULL),\n       (10, 'Pippa', 'West', 3.6, 2024, 'Hering');\nUPDATE pinguine SET gewicht_kg = 3.4 WHERE id =\
  \ 9;\nUPDATE kolonien SET wassertemperatur = -1.0 WHERE name = 'West';\nDELETE FROM fuetterungen WHERE pinguin_id = 7;\n\
  DELETE FROM pinguine WHERE id = 7;\n"
---

**Kapitelprojekt Umzug in den Westen, letztes Stück.** Dein Skript aus Stück 3 steht schon da. Die Neuen bekommen eine Gesundheitsakte. Lege die Tabelle gesundheit an mit id (INTEGER PRIMARY KEY), pinguin_id (INTEGER, Pflicht, zeigt auf pinguine(id)), tag (TEXT, Pflicht) und befund (TEXT, Pflicht). Trage für den 24. Oktober 2026 ein: Pelle ist gesund, Pippa hat einen leichten Schnupfen. Dann ist der Umzug geschafft.
