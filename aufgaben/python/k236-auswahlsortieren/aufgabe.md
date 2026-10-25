---
schema_version: 1
id: k236-auswahlsortieren
revision: 1
titel: Auswahlsortieren
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 5
tags:
- kurs
- algorithmus
- sortieren
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 23
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Außen eine Schleife über alle Plätze, innen die Suche nach dem Kleinsten im Rest.
- kosten: 3
  text: 'Tauschen in einer Zeile: `a[i], a[k] = a[k], a[i]`.'
tests_sichtbar:
- input:
  - '5'
  - '2'
  - '8'
  - '1'
  - ende
  expected: '[1, 2, 5, 8]

    '
tests_versteckt:
- input:
  - ende
  expected: '[]

    '
- input:
  - '3'
  - '3'
  - '-1'
  - '0'
  - ende
  expected: '[-1, 0, 3, 3]

    '
starter_code: ''
---

Lies Zahlen ein, bis `ende` kommt, und sortiere sie ohne `sorted` und `sort` mit Auswahlsortieren. Gib die Liste zum Schluss aus. Bei `5`, `2`, `8`, `1`, `ende`:

```
[1, 2, 5, 8]
```
