---
schema_version: 1
id: j154-summe-reduce
revision: 1
titel: Summe mit reduce
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- rueckrufmethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Beim Malnehmen fängt man mit 1 an, nicht mit 0.
tests_sichtbar:
- input: []
  expected: 'Summe: 15

    Produkt: 120

    '
starter_code: 'const zahlen = [1, 2, 3, 4, 5];

  '
---

Rechne die Summe und das Produkt der Zahlen mit `reduce` aus, jeweils mit passendem Startwert:

```
Summe: 15
Produkt: 120
```
