---
schema_version: 1
id: q101-wo-wohnt-wer
revision: 1
titel: Wo wohnt wer?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 2
schaetz_minuten: 2
tags:
- kurs
- join
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 10
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
- lage
sortierung_egal: true
erwartetes_ergebnis:
- - Pit
  - Packeis
- - Pia
  - Felsenküste
- - Paul
  - Packeis
- - Pina
  - Packeis
- - Pepe
  - Felsenküste
- - Polly
  - Packeis
- - Pablo
  - Sandstrand
- - Pünktchen
  - Sandstrand
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
starter_code: 'SELECT p.name, k.lage

  FROM pinguine p

  JOIN kolonien k ON k.name = p.kolonie;'
---

Die Abfrage steht schon da: sie holt zu jedem Pinguin die Lage seiner Kolonie. Prüfe sie und schau dir im Kurs an, wie JOIN die beiden Tabellen nebeneinanderlegt.
