---
schema_version: 1
id: q079-steckbrief-sortiert
revision: 1
titel: 'Steckbrief: die Ältesten zuerst'
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- projekt
- order_by
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 7
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
- kuerzel
- kolonie
- lieblingsfisch
- jahre
sortierung_egal: false
erwartetes_ergebnis:
- - Paul
  - Pau
  - Nord
  - Hering
  - 9
- - Pit
  - Pit
  - Nord
  - Hering
  - 7
- - Polly
  - Pol
  - Nord
  - Lachs
  - 7
- - Pablo
  - Pab
  - Ost
  - Hering
  - 5
- - Pina
  - Pin
  - Nord
  - unbekannt
  - 4
- - Pünktchen
  - Pün
  - Ost
  - unbekannt
  - 3
hints:
- kosten: 0
  text: '`ORDER BY jahre DESC, name`'
starter_code: 'SELECT name, SUBSTR(name, 1, 3) AS kuerzel, kolonie, COALESCE(lieblingsfisch, ''unbekannt'') AS lieblingsfisch,
  2026 - geburtsjahr AS jahre

  FROM pinguine

  WHERE kolonie IN (''Nord'', ''Ost'');'
---

**Kapitelprojekt Pinguinsteckbrief, Stück 7.** Deine Abfrage aus Stück 6 steht schon da. Auf der Tafel stehen die ältesten Pinguine oben; bei gleichem Alter entscheidet der Name.
