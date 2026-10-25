---
schema_version: 1
id: q028-besuchertafel
revision: 1
titel: Die Besuchertafel
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 5
tags:
- kurs
- rechnen
- kurztest
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
- tafel
- jahre
sortierung_egal: false
erwartetes_ergebnis:
- - Pit wiegt 4200.0 Gramm
  - 7
- - Pia wiegt 3800.0 Gramm
  - 6
- - Paul wiegt 5100.0 Gramm
  - 9
- - Pina wiegt 3500.0 Gramm
  - 4
- - Pepe wiegt 4900.0 Gramm
  - 8
- - Polly wiegt 4600.0 Gramm
  - 7
- - Pablo wiegt 4000.0 Gramm
  - 5
- - Pünktchen wiegt 2900.0 Gramm
  - 3
hints:
- kosten: 0
  text: 'Zwei Spalten: ein verbundener Text und eine Rechnung.'
- kosten: 2
  text: 'Die Rechnung gehört in Klammern: `(gewicht_kg * 1000)`.'
starter_code: ''
---

Für die Besuchertafel: je Pinguin eine Spalte `tafel` mit einem Satz wie `Pit wiegt 4200.0 Gramm` und eine Spalte `jahre` mit dem Alter im Jahr 2026. Vorsicht: `||` klebt stärker als `*` rechnet.
