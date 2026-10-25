---
schema_version: 1
id: k088-ziffernsumme
revision: 1
titel: Die Quersumme
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- while
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: zahl % 10 ist die letzte Ziffer, zahl // 10 schneidet sie ab.
- kosten: 3
  text: 'In der Schleife: `summe += zahl % 10`, dann `zahl //= 10`.'
tests_sichtbar:
- input:
  - '472'
  expected: '13

    '
tests_versteckt:
- input:
  - '9'
  expected: '9

    '
- input:
  - '1000'
  expected: '1

    '
- input:
  - '98765'
  expected: '35

    '
starter_code: ''
---

Lies eine positive ganze Zahl ein und gib ihre Quersumme aus, also die Summe ihrer Ziffern. Rechne mit `% 10` und `// 10`, nicht mit Text. Bei `472`:

```
13
```
