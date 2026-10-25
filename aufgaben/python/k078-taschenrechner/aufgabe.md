---
schema_version: 1
id: k078-taschenrechner
revision: 1
titel: Der kleine Taschenrechner
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- verzweigung
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Je Zeichen ein elif; beim Teilen ein if im Block für die Null.
- kosten: 3
  text: 'Verschachtelt: `elif zeichen == "/":` und darin `if b == 0:`.'
tests_sichtbar:
- input:
  - '6'
  - '*'
  - '7'
  expected: '42

    '
tests_versteckt:
- input:
  - '9'
  - /
  - '2'
  expected: '4.5

    '
- input:
  - '5'
  - /
  - '0'
  expected: 'Teilen durch 0 geht nicht.

    '
- input:
  - '3'
  - '-'
  - '8'
  expected: '-5

    '
- input:
  - '1'
  - '%'
  - '1'
  expected: 'Unbekanntes Zeichen.

    '
- input:
  - '2'
  - +
  - '2'
  expected: '4

    '
starter_code: ''
---

Lies eine Zahl, ein Rechenzeichen (`+`, `-`, `*` oder `/`) und eine zweite Zahl ein (ganze Zahlen) und gib das Ergebnis aus. Bei Teilen durch 0 erscheint `Teilen durch 0 geht nicht.`, bei einem unbekannten Zeichen `Unbekanntes Zeichen.`. Bei `6`, `*`, `7`:

```
42
```
