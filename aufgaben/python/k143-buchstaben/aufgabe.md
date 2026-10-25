---
schema_version: 1
id: k143-buchstaben
revision: 1
titel: Verschiedene Buchstaben
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- menge
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein Text ist auch eine Folge, `set(wort)` liefert seine Buchstaben je einmal.
tests_sichtbar:
- input:
  - Banane
  expected: 'Verschiedene Buchstaben: 4

    '
tests_versteckt:
- input:
  - aaaa
  expected: 'Verschiedene Buchstaben: 1

    '
- input:
  - Pinguin
  expected: 'Verschiedene Buchstaben: 5

    '
starter_code: ''
---

Lies ein Wort ein und gib aus, aus wie vielen verschiedenen Buchstaben es besteht. Bei `Banane`:

```
Verschiedene Buchstaben: 4
```
