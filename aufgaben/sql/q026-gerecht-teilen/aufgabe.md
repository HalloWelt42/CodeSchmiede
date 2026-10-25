---
schema_version: 1
id: q026-gerecht-teilen
revision: 1
titel: Gerecht teilen
sprache: sql
task_type: sql_abfrage
runner_type: docker_sqlite
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- rechnen
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
- fisch
- menge
- je_pinguin
sortierung_egal: false
erwartetes_ergebnis:
- - Hering
  - 6
  - 3.0
- - Lachs
  - 4
  - 2.0
- - Hering
  - 8
  - 4.0
- - Makrele
  - 5
  - 2.5
- - Hering
  - 5
  - 2.5
- - Sardine
  - 3
  - 1.5
- - Lachs
  - 6
  - 3.0
- - Hering
  - 4
  - 2.0
- - Makrele
  - 7
  - 3.5
- - Sardine
  - 2
  - 1.0
- - Lachs
  - 5
  - 2.5
- - Sardine
  - 3
  - 1.5
hints:
- kosten: 0
  text: Ganze durch ganze Zahl bleibt ganz.
- kosten: 1
  text: Teile durch `2.0`.
starter_code: 'SELECT fisch, menge, menge / 2 AS je_pinguin

  FROM fuetterungen;'
---

Jede Fütterung soll gerecht auf zwei Pinguine verteilt werden. Hole Fisch, Menge und die Fische je Pinguin als Spalte `je_pinguin`, mit Kommastelle (bei 5 Fischen also 2.5).
