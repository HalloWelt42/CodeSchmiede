---
schema_version: 1
id: j087-mindestens-einmal
revision: 1
titel: Mindestens einmal fragen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
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
  text: Bei do ... while steht die Bedingung am Ende, der Block läuft mindestens einmal.
- kosten: 2
  text: Wiederholen, solange der Wurf kleiner als 1 oder größer als 6 ist.
tests_sichtbar:
- input:
  - '9'
  - '0'
  - '4'
  expected: 'Würfel? Nur 1 bis 6!

    Würfel? Nur 1 bis 6!

    Würfel? Gewürfelt: 4

    '
tests_versteckt:
- input:
  - '6'
  expected: 'Würfel? Gewürfelt: 6

    '
- input:
  - '7'
  - '1'
  expected: 'Würfel? Nur 1 bis 6!

    Würfel? Gewürfelt: 1

    '
starter_code: ''
---

Frag mit `do ... while` so lange nach einer Zahl zwischen 1 und 6, bis eine passende kommt, und gib sie dann aus. Für falsche Zahlen erscheint `Nur 1 bis 6!`. Bei den Eingaben `9`, `0` und `4`:

```
Würfel? Nur 1 bis 6!
Würfel? Nur 1 bis 6!
Würfel? Gewürfelt: 4
```
