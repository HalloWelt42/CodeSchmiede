---
schema_version: 1
id: q027-namensschild
revision: 1
titel: Das Namensschild
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- text_verbinden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 2
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
- schild
sortierung_egal: false
erwartetes_ergebnis:
- - Pit (Nord)
- - Pia (Süd)
- - Paul (Nord)
- - Pina (Nord)
- - Pepe (Süd)
- - Polly (Nord)
- - Pablo (Ost)
- - Pünktchen (Ost)
hints:
- kosten: 0
  text: Mit `||` werden Name, Klammern und Kolonie verbunden.
- kosten: 2
  text: '`name || '' ('' || kolonie || '')''`.'
starter_code: ''
---

Baue für jeden Pinguin ein Namensschild wie `Pit (Nord)` in einer Spalte `schild`.
