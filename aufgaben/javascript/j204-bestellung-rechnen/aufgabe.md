---
schema_version: 1
id: j204-bestellung-rechnen
revision: 1
titel: Eine Bestellung als JSON
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- json
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 20
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Nach dem parse ist es ein ganz normales Array aus Objekten.
tests_sichtbar:
- input:
  - '[{"ware":"Hering","anzahl":3,"preis":2.5},{"ware":"Suppe","anzahl":1,"preis":4.5}]'
  expected: 'Bestellung? 3 x Hering: 7.50

    1 x Suppe: 4.50

    Summe: 12.00

    '
tests_versteckt:
- input:
  - '[]'
  expected: 'Bestellung? Summe: 0.00

    '
- input:
  - '[{"ware":"Aal","anzahl":2,"preis":5}]'
  expected: 'Bestellung? 2 x Aal: 10.00

    Summe: 10.00

    '
starter_code: ''
---

Die Bestellung kommt als JSON-Array von Posten mit `ware`, `anzahl` und `preis`. Lies sie, gib jeden Posten aus und die Summe. Bei der Eingabe `[{"ware":"Hering","anzahl":3,"preis":2.5},{"ware":"Suppe","anzahl":1,"preis":4.5}]`:

```
Bestellung? 3 x Hering: 7.50
1 x Suppe: 4.50
Summe: 12.00
```
