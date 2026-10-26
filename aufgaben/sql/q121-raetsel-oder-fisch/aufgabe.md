---
schema_version: 1
id: q121-raetsel-oder-fisch
revision: 1
titel: Rätsel oder Fisch
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 2
schaetz_minuten: 2
tags:
- kurs
- case
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 12
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
- fisch
sortierung_egal: false
erwartetes_ergebnis:
- - Pit
  - Hering
- - Pia
  - Lachs
- - Paul
  - Hering
- - Pina
  - Rätsel
- - Pepe
  - Makrele
- - Polly
  - Lachs
- - Pablo
  - Hering
- - Pünktchen
  - Rätsel
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
starter_code: "SELECT name,\n       CASE WHEN lieblingsfisch IS NULL THEN 'Rätsel' ELSE lieblingsfisch END AS fisch\nFROM\
  \ pinguine;"
---

Die Abfrage steht schon da: wo der Lieblingsfisch unbekannt ist, schreibt sie Rätsel. Prüfe sie.
