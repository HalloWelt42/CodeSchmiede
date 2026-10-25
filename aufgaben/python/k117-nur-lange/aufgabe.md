---
schema_version: 1
id: k117-nur-lange
revision: 1
titel: Nur lange Wörter
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- abstraktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Ausdruck vorn, Bedingung hinten: `[t.upper() for t in tiere if ...]`.'
tests_sichtbar:
- input: []
  expected: '[''PINGUIN'', ''WALROSS'']

    '
starter_code: 'tiere = ["Wal", "Pinguin", "Robbe", "Walross", "Möwe"]

  '
---

Behalte mit einer Listenabstraktion nur die Wörter mit mehr als 5 Buchstaben, in Großbuchstaben:

```
['PINGUIN', 'WALROSS']
```
