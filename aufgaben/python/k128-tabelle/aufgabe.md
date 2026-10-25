---
schema_version: 1
id: k128-tabelle
revision: 1
titel: Die Fangtabelle
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- aufzaehlen
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Paare als Tupel in einer Liste sammeln.
- kosten: 3
  text: '`for nr, (name, fang) in enumerate(paare, 1):` packt beides aus.'
tests_sichtbar:
- input:
  - Pia
  - '5'
  - Pit
  - '3'
  - ende
  expected: '1 Pia 5

    2 Pit 3

    Summe: 8

    '
tests_versteckt:
- input:
  - ende
  expected: 'Summe: 0

    '
- input:
  - A
  - '1'
  - B
  - '2'
  - C
  - '3'
  - ende
  expected: '1 A 1

    2 B 2

    3 C 3

    Summe: 6

    '
starter_code: ''
---

Lies Paare ein, je Name dann Fang, bis als Name `ende` kommt. Gib danach eine nummerierte Tabelle und die Summe aus. Bei `Pia`, `5`, `Pit`, `3`, `ende`:

```
1 Pia 5
2 Pit 3
Summe: 8
```
