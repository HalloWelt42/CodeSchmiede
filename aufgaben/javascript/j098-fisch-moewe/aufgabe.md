---
schema_version: 1
id: j098-fisch-moewe
revision: 1
titel: Fisch und Möwe
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 7
tags:
- kurs
- for
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Die Prüfung auf beide (3 und 5) muss vor den einzelnen stehen.
- kosten: 2
  text: Die 7 zuerst prüfen und mit continue überspringen.
tests_sichtbar:
- input:
  - '15'
  expected: 'Bis? 1

    2

    Fisch

    4

    Möwe

    Fisch

    8

    Fisch

    Möwe

    11

    Fisch

    13

    Fischmöwe

    '
tests_versteckt:
- input:
  - '35'
  expected: 'Bis? 1

    2

    Fisch

    4

    Möwe

    Fisch

    8

    Fisch

    Möwe

    11

    Fisch

    13

    Fischmöwe

    16

    17

    Fisch

    19

    Möwe

    22

    23

    Fisch

    Möwe

    26

    Fisch

    29

    Fischmöwe

    31

    32

    Fisch

    34

    '
- input:
  - '2'
  expected: 'Bis? 1

    2

    '
starter_code: ''
---

Zähle von 1 bis zu einer eingelesenen Zahl. Durch 3 teilbare Zahlen heißen `Fisch`, durch 5 teilbare `Möwe`, durch beide teilbare `Fischmöwe`. Alle durch 7 teilbaren überspringst du mit `continue`, die Möwe hat sie gefressen. Bei der Eingabe `15`:

```
Bis? 1
2
Fisch
4
Möwe
Fisch
8
Fisch
Möwe
11
Fisch
13
Fischmöwe
```
