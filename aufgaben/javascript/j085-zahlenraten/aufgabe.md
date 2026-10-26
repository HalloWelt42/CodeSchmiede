---
schema_version: 1
id: j085-zahlenraten
revision: 1
titel: Zahlenraten
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 5
tags:
- kurs
- while
- break
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Jeder Versuch zählt, auch der richtige.
- kosten: 2
  text: Beim richtigen Tipp steigt `break` aus, die Erfolgsmeldung steht hinter der Schleife.
tests_sichtbar:
- input:
  - '50'
  - '30'
  - '42'
  expected: 'Tipp? zu groß

    Tipp? zu klein

    Tipp? Richtig nach 3 Versuchen!

    '
tests_versteckt:
- input:
  - '42'
  expected: 'Tipp? Richtig nach 1 Versuchen!

    '
- input:
  - '1'
  - '99'
  - '41'
  - '43'
  - '42'
  expected: 'Tipp? zu klein

    Tipp? zu groß

    Tipp? zu klein

    Tipp? zu groß

    Tipp? Richtig nach 5 Versuchen!

    '
starter_code: ''
---

Die geheime Zahl ist 42. Lies Tipps, bis der richtige kommt, und hilf mit `zu klein` oder `zu groß`. Bei den Eingaben `50`, `30` und `42`:

```
Tipp? zu groß
Tipp? zu klein
Tipp? Richtig nach 3 Versuchen!
```
