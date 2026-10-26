---
schema_version: 1
id: q149-umzug-erste-woche
revision: 1
titel: 'Umzug in den Westen: die erste Woche'
sprache: sql
task_type: sql_aenderung
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- projekt
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
kontrolle: 'SELECT p.name, p.gewicht_kg, k.wassertemperatur

  FROM pinguine p JOIN kolonien k ON k.name = p.kolonie

  WHERE p.kolonie = ''West''

  ORDER BY p.id'
erwartete_spalten:
- name
- gewicht_kg
- wassertemperatur
sortierung_egal: false
erwartetes_ergebnis:
- - Pelle
  - 3.4
  - -1.0
- - Pippa
  - 3.6
  - -1.0
hints:
- kosten: 0
  text: Ein UPDATE für pinguine, eins für kolonien.
- kosten: 2
  text: '`UPDATE kolonien SET wassertemperatur = -1.0 WHERE name = ''West'';`'
starter_code: "INSERT INTO pinguine (id, name, kolonie, gewicht_kg, geburtsjahr, lieblingsfisch)\nVALUES (9, 'Pelle', 'West',\
  \ 3.1, 2025, NULL),\n       (10, 'Pippa', 'West', 3.6, 2024, 'Hering');\n"
---

**Kapitelprojekt Umzug in den Westen, Stück 2.** Dein Skript aus Stück 1 steht schon da. Nach der ersten Woche wiegt Pelle 3,4 Kilo, und weil die Neuen frieren sollen wie zu Hause, wird das Wasser der Westkolonie auf -1,0 Grad gekühlt. Hänge zwei UPDATE an.
