---
schema_version: 1
id: j077-groesste
revision: 1
titel: Die größte von dreien
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- verzweigung
- logik
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ist a mindestens so groß wie b und wie c, ist a der größte.
- kosten: 2
  text: 'Sonst bleibt der größere von b und c: noch ein `else if`.'
tests_sichtbar:
- input:
  - '4'
  - '9'
  - '7'
  expected: 'Pia? Paul? Pit? Größter Fang: 9

    '
tests_versteckt:
- input:
  - '8'
  - '2'
  - '5'
  expected: 'Pia? Paul? Pit? Größter Fang: 8

    '
- input:
  - '1'
  - '3'
  - '6'
  expected: 'Pia? Paul? Pit? Größter Fang: 6

    '
- input:
  - '5'
  - '5'
  - '2'
  expected: 'Pia? Paul? Pit? Größter Fang: 5

    '
starter_code: ''
---

Lies drei Fänge ein und gib den größten aus, **ohne** `Math.max`, nur mit if und else. Bei den Eingaben `4`, `9` und `7`:

```
Pia? Paul? Pit? Größter Fang: 9
```
