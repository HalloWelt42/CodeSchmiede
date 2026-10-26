---
schema_version: 1
id: q049-steckbrief-nord-ost
revision: 1
titel: 'Steckbrief: Nord und Ost'
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- projekt
- in_between
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
- kolonie
- lieblingsfisch
- jahre
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - Nord
  - Hering
  - 7
- - Paul
  - Nord
  - Hering
  - 9
- - Pina
  - Nord
  - null
  - 4
- - Polly
  - Nord
  - Lachs
  - 7
- - Pablo
  - Ost
  - Hering
  - 5
- - Pünktchen
  - Ost
  - null
  - 3
hints:
- kosten: 0
  text: '`WHERE kolonie IN (''Nord'', ''Ost'')`'
starter_code: 'SELECT name, kolonie, lieblingsfisch, 2026 - geburtsjahr AS jahre

  FROM pinguine

  WHERE kolonie = ''Nord'';'
---

**Kapitelprojekt Pinguinsteckbrief, Stück 4.** Deine Abfrage aus Stück 3 steht schon da. Die Tafel zieht um: sie hängt jetzt zwischen Nord- und Ostgehege. Zeige die Pinguine aus beiden Kolonien.
