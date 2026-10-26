---
schema_version: 1
id: j082-summe-bis
revision: 1
titel: Alles zusammen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- while
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zähler `i` ab 1 und Sammler `summe` ab 0, beide vor der Schleife.
- kosten: 2
  text: 'Im Block: `summe += i;` und `i++;`'
tests_sichtbar:
- input:
  - '4'
  expected: 'Bis? Summe 1 bis 4: 10

    '
tests_versteckt:
- input:
  - '100'
  expected: 'Bis? Summe 1 bis 100: 5050

    '
- input:
  - '1'
  expected: 'Bis? Summe 1 bis 1: 1

    '
starter_code: ''
---

Lies eine Zahl n und zähle alle Zahlen von 1 bis n zusammen, mit einem Zähler und einem Sammler. Bei der Eingabe `4`:

```
Bis? Summe 1 bis 4: 10
```
