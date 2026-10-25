---
schema_version: 1
id: k174-nochmal-bitte
revision: 1
titel: Nochmal bitte
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- ausnahme
- while
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Eine Endlosschleife mit try darin; break direkt hinter dem int.
- kosten: 2
  text: Das except gehört noch in die Schleife.
tests_sichtbar:
- input:
  - zwei
  - '2.5'
  - '2'
  expected: 'Bitte eine ganze Zahl

    Bitte eine ganze Zahl

    Danke: 2 Fische

    '
tests_versteckt:
- input:
  - '7'
  expected: 'Danke: 7 Fische

    '
- input:
  - ''
  - x
  - '0'
  expected: 'Bitte eine ganze Zahl

    Bitte eine ganze Zahl

    Danke: 0 Fische

    '
starter_code: ''
---

Frage so lange nach der Zahl der Fische, bis eine ganze Zahl kommt. Bei jeder falschen Eingabe erscheint `Bitte eine ganze Zahl`. Bei `zwei`, `2.5`, `2`:

```
Bitte eine ganze Zahl
Bitte eine ganze Zahl
Danke: 2 Fische
```
