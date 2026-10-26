---
schema_version: 1
id: q159-umzug-abschied
revision: 1
titel: 'Umzug in den Westen: ein Abschied'
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- projekt
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
kontrolle: "SELECT kolonie, COUNT(*) AS pinguine,\n       (SELECT COUNT(*) FROM fuetterungen WHERE pinguin_id NOT IN (SELECT\
  \ id FROM pinguine)) AS verwaiste\nFROM pinguine\nGROUP BY kolonie\nORDER BY kolonie"
erwartete_spalten:
- kolonie
- pinguine
- verwaiste
sortierung_egal: false
erwartetes_ergebnis:
- - Nord
  - 4
  - 0
- - Ost
  - 1
  - 0
- - Süd
  - 2
  - 0
- - West
  - 2
  - 0
hints:
- kosten: 0
  text: Erst die Fütterungen mit pinguin_id 7, dann Pablo.
starter_code: "INSERT INTO pinguine (id, name, kolonie, gewicht_kg, geburtsjahr, lieblingsfisch)\nVALUES (9, 'Pelle', 'West',\
  \ 3.1, 2025, NULL),\n       (10, 'Pippa', 'West', 3.6, 2024, 'Hering');\nUPDATE pinguine SET gewicht_kg = 3.4 WHERE id =\
  \ 9;\nUPDATE kolonien SET wassertemperatur = -1.0 WHERE name = 'West';\n"
---

**Kapitelprojekt Umzug in den Westen, Stück 3.** Dein Skript aus Stück 2 steht schon da. Pablo (Nummer 7) zieht dafür in einen anderen Zoo. Hänge zwei DELETE an, die keine verwaisten Fütterungen hinterlassen.
