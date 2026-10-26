---
schema_version: 1
id: q091-je-fisch
revision: 1
titel: Wie oft welcher Fisch?
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 2
schaetz_minuten: 2
tags:
- kurs
- group_by
voraussetzungen: []
quelle:
  notiz: Aufbaukurs SQL, Kapitel 9
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
- fisch
- mal
sortierung_egal: true
erwartetes_ergebnis:
- - Hering
  - 4
- - Lachs
  - 3
- - Makrele
  - 2
- - Sardine
  - 3
hints:
- kosten: 0
  text: Hier musst du nichts ändern, nur prüfen.
starter_code: 'SELECT fisch, COUNT(*) AS mal

  FROM fuetterungen

  GROUP BY fisch;'
---

Die Abfrage steht schon da: sie zählt für jede Fischsorte, wie oft sie verfüttert wurde. Prüfe sie und schau dir im Kurs die Gruppen an.
