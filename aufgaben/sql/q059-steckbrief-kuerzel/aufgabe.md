---
schema_version: 1
id: q059-steckbrief-kuerzel
revision: 1
titel: 'Steckbrief: das Kürzel'
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- projekt
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
- kuerzel
- kolonie
- lieblingsfisch
- jahre
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - Pit
  - Nord
  - Hering
  - 7
- - Paul
  - Pau
  - Nord
  - Hering
  - 9
- - Pina
  - Pin
  - Nord
  - null
  - 4
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
- - Pünktchen
  - Pün
  - Ost
  - null
  - 3
hints:
- kosten: 0
  text: '`SUBSTR(name, 1, 3) AS kuerzel`'
starter_code: 'SELECT name, kolonie, lieblingsfisch, 2026 - geburtsjahr AS jahre

  FROM pinguine

  WHERE kolonie IN (''Nord'', ''Ost'');'
---

**Kapitelprojekt Pinguinsteckbrief, Stück 5.** Deine Abfrage aus Stück 4 steht schon da. Für die Futtereimer bekommt jeder Pinguin ein Kürzel aus den ersten drei Buchstaben seines Namens. Füge direkt nach name die Spalte `kuerzel` ein.
