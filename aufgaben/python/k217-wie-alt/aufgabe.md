---
schema_version: 1
id: k217-wie-alt
revision: 1
titel: Wie alt?
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- datum
- verzweigung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst die Jahre abziehen.
- kosten: 2
  text: 'Tupel vergleichen der Reihe nach: `(monat, tag) < (monat, tag)`.'
tests_sichtbar:
- input:
  - '2014-11-03'
  - '2026-10-25'
  expected: 'Alter: 11

    '
tests_versteckt:
- input:
  - '2014-10-25'
  - '2026-10-25'
  expected: 'Alter: 12

    '
- input:
  - '2014-10-26'
  - '2026-10-25'
  expected: 'Alter: 11

    '
- input:
  - '2014-01-01'
  - '2026-10-25'
  expected: 'Alter: 12

    '
starter_code: ''
---

Lies einen Geburtstag und einen Stichtag ein (beide `2026-10-25`) und gib das Alter in ganzen Jahren aus. Wer am Stichtag noch nicht Geburtstag hatte, ist ein Jahr jünger. Bei `2014-11-03` und `2026-10-25`:

```
Alter: 11
```
