---
schema_version: 1
id: j054-was-ist-das
revision: 1
titel: Was ist das?
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- eingabe
- typeof
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`typeof wert` liefert den Typ als Text.'
- kosten: 2
  text: Auch NaN hat den Typ number, das prüft ein versteckter Fall.
tests_sichtbar:
- input:
  - '12'
  expected: 'Eingabe? Vorher: string

    Nachher: number

    '
tests_versteckt:
- input:
  - drei
  expected: 'Eingabe? Vorher: string

    Nachher: number

    '
starter_code: ''
---

Lies eine Eingabe, wandle sie mit `Number` um und gib beide Typen aus. Bei der Eingabe `12`:

```
Eingabe? Vorher: string
Nachher: number
```
