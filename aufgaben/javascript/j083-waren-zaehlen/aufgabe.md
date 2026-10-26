---
schema_version: 1
id: j083-waren-zaehlen
revision: 1
titel: Waren zählen
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 4
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
  text: '`while (true)` mit einem `break`, wenn die Eingabe null oder fertig ist.'
- kosten: 2
  text: Ein versteckter Fall endet ohne fertig, dann liefert prompt null.
tests_sichtbar:
- input:
  - Hering
  - Gurke
  - fertig
  expected: 'Ware? Ware? Ware? 2 Waren

    '
tests_versteckt:
- input:
  - fertig
  expected: 'Ware? 0 Waren

    '
- input:
  - A
  - B
  - C
  - D
  expected: 'Ware? Ware? Ware? Ware? Ware? 4 Waren

    '
starter_code: ''
---

Lies Waren, bis `fertig` kommt oder gar nichts mehr, und gib aus, wie viele es waren. Bei den Eingaben `Hering`, `Gurke` und `fertig`:

```
Ware? Ware? Ware? 2 Waren
```
