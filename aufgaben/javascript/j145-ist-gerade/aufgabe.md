---
schema_version: 1
id: j145-ist-gerade
revision: 1
titel: Ist es gerade?
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- funktion
- return
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Der Vergleich selbst ist schon true oder false: `return zahl % 2 === 0;`'
tests_sichtbar:
- input:
  - '7'
  expected: 'Bis? Gerade: 2, 4, 6

    Ungerade: 1, 3, 5, 7

    '
tests_versteckt:
- input:
  - '1'
  expected: "Bis? Gerade: \nUngerade: 1\n"
- input:
  - '4'
  expected: 'Bis? Gerade: 2, 4

    Ungerade: 1, 3

    '
starter_code: ''
---

Schreib `istGerade(zahl)`, die true oder false liefert, und benutze sie, um die Zahlen von 1 bis zu einer eingelesenen Grenze in gerade und ungerade zu sortieren. Bei der Eingabe `7`:

```
Bis? Gerade: 2, 4, 6
Ungerade: 1, 3, 5, 7
```
