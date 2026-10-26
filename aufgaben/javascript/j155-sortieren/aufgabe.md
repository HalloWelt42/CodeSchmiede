---
schema_version: 1
id: j155-sortieren
revision: 1
titel: Richtig sortiert
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- rueckrufmethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`sort((a, b) => a - b)` aufsteigend, `b - a` absteigend.'
- kosten: 2
  text: Vor dem Sortieren mit `slice()` kopieren.
tests_sichtbar:
- input:
  - 10,9,1,25
  expected: 'Preise? Auf: 1, 9, 10, 25

    Ab: 25, 10, 9, 1

    Original: 10, 9, 1, 25

    '
tests_versteckt:
- input:
  - '3'
  expected: 'Preise? Auf: 3

    Ab: 3

    Original: 3

    '
- input:
  - 2.5,100,30,4
  expected: 'Preise? Auf: 2.5, 4, 30, 100

    Ab: 100, 30, 4, 2.5

    Original: 2.5, 100, 30, 4

    '
starter_code: ''
---

Lies Preise mit Kommas ein und gib sie aufsteigend und absteigend sortiert aus, ohne das Original zu ändern, das danach auch noch kommt. Bei der Eingabe `10,9,1,25`:

```
Preise? Auf: 1, 9, 10, 25
Ab: 25, 10, 9, 1
Original: 10, 9, 1, 25
```
