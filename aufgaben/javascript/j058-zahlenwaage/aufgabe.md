---
schema_version: 1
id: j058-zahlenwaage
revision: 1
titel: Die Zahlenwaage
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 6
tags:
- kurs
- eingabe
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Beide Eingaben mit `Number(...)` umwandeln.
- kosten: 2
  text: '`(a + b).toFixed(1)` rundet auf eine Stelle.'
tests_sichtbar:
- input:
  - '1.25'
  - '2'
  expected: 'Erstes? Zweites? Summe: 3.3

    Erstes keine Zahl: false

    kg: 2

    '
tests_versteckt:
- input:
  - viel
  - '4.5'
  expected: 'Erstes? Zweites? Summe: NaN

    Erstes keine Zahl: true

    kg: 4.5

    '
- input:
  - '0.5'
  - '0.25'
  expected: 'Erstes? Zweites? Summe: 0.8

    Erstes keine Zahl: false

    kg: 0.25

    '
starter_code: ''
---

Lies zwei Gewichte ein. Gib ihre Summe mit einer Nachkommastelle aus, prüfe mit `Number.isNaN`, ob die erste Eingabe keine Zahl war, und gib die zweite als Text aus, der mit `String` gebaut und mit `+` an `"kg: "` geklebt wird. Bei den Eingaben `1.25` und `2`:

```
Erstes? Zweites? Summe: 3.3
Erstes keine Zahl: false
kg: 2
```
