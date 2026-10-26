---
schema_version: 1
id: q088-heringsbericht
revision: 1
titel: Der Heringsbericht
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- aggregat
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 8
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
- fuetterungen
- fische
- groesste
- schnitt
sortierung_egal: false
erwartetes_ergebnis:
- - 4
  - 23
  - 8
  - 5.8
hints:
- kosten: 0
  text: Vier Funktionen nebeneinander, vorher WHERE.
- kosten: 2
  text: '`ROUND(AVG(menge), 1) AS schnitt`'
starter_code: ''
---

Für den Bericht an den Fischhändler: hole für alle Fütterungen mit Hering die Zahl der Fütterungen (`fuetterungen`), die Fische insgesamt (`fische`), die größte Portion (`groesste`) und die durchschnittliche Portion auf eine Stelle gerundet (`schnitt`).
