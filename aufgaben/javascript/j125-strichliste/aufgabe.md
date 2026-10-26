---
schema_version: 1
id: j125-strichliste
revision: 1
titel: Strichliste
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- objekt
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein leeres Objekt als Zähler; beim ersten Mal 1, danach hochzählen.
tests_sichtbar:
- input:
  - Hering Aal Hering Limonade Hering
  expected: 'Bestellung? Hering: 3

    Aal: 1

    Limonade: 1

    '
tests_versteckt:
- input:
  - Aal
  expected: 'Bestellung? Aal: 1

    '
- input:
  - b a b a c
  expected: 'Bestellung? b: 2

    a: 2

    c: 1

    '
starter_code: ''
---

Lies eine Bestellung als Wörter mit Leerzeichen und zähle mit einem Objekt, wie oft jedes Wort vorkommt, in der Reihenfolge des ersten Auftretens. Bei der Eingabe `Hering Aal Hering Limonade Hering`:

```
Bestellung? Hering: 3
Aal: 1
Limonade: 1
```
