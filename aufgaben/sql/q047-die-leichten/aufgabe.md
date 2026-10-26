---
schema_version: 1
id: q047-die-leichten
revision: 1
titel: Die Leichtgewichte
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- logik
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
- gewicht_kg
sortierung_egal: false
erwartetes_ergebnis:
- - Pina
  - 3.5
- - Pünktchen
  - 2.9
hints:
- kosten: 0
  text: AND bindet stärker als OR.
- kosten: 2
  text: Klammern um die beiden Kolonien.
starter_code: 'SELECT name, gewicht_kg

  FROM pinguine

  WHERE kolonie = ''Nord'' OR kolonie = ''Ost'' AND gewicht_kg < 4;'
---

Die Abfrage soll die Pinguine aus Nord und Ost holen, die weniger als vier Kilo wiegen. Sie liefert aber auch schwere. Repariere sie.
