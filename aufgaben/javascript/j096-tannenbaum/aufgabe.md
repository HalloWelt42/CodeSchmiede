---
schema_version: 1
id: j096-tannenbaum
revision: 1
titel: Der Tannenbaum
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 6
tags:
- kurs
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Außen eine Schleife für die Zeilen, darin eine für die Leerzeichen und eine für die Sternchen.
- kosten: 2
  text: '`" ".repeat(...)` ginge auch, aber probier es hier mit Schleifen.'
tests_sichtbar:
- input:
  - '3'
  expected: "Höhe?   *\n ***\n*****\n"
tests_versteckt:
- input:
  - '1'
  expected: 'Höhe? *

    '
- input:
  - '5'
  expected: "Höhe?     *\n   ***\n  *****\n *******\n*********\n"
starter_code: ''
---

Zeichne einen Tannenbaum aus Sternchen mit einer eingelesenen Höhe. In Zeile z stehen 2·z−1 Sternchen, davor so viele Leerzeichen, dass alles mittig steht (Höhe minus z). Bei der Eingabe `3`:

```
Höhe?   *
 ***
*****
```
