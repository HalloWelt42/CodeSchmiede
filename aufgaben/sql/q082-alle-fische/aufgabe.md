---
schema_version: 1
id: q082-alle-fische
revision: 1
titel: Alle Fische zusammen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- aggregat
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
- fische
sortierung_egal: false
erwartetes_ergebnis:
- - 58
hints:
- kosten: 0
  text: Gesucht ist die Summe.
starter_code: 'SELECT ___(menge) AS fische

  FROM fuetterungen;'
---

Ergänze die Lücke `___`, damit herauskommt, wie viele Fische insgesamt verfüttert wurden.
