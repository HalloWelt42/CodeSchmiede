---
schema_version: 1
id: k155-groessere
revision: 1
titel: Die größere Zahl
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- funktion
- rueckgabe
- verzweigung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein if in der Funktion, in jedem Zweig ein return.
- kosten: 2
  text: Nach einem return endet die Funktion sofort.
tests_sichtbar:
- input:
  - '4'
  - '9'
  expected: 'Größer: 9

    '
tests_versteckt:
- input:
  - '9'
  - '4'
  expected: 'Größer: 9

    '
- input:
  - '-2'
  - '-2'
  expected: 'Größer: -2

    '
starter_code: ''
---

Schreibe ohne `max` eine Funktion `groessere(a, b)`, die die größere der beiden Zahlen zurückgibt. Lies zwei ganze Zahlen ein. Bei `4` und `9`:

```
Größer: 9
```
