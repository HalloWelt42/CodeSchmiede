---
schema_version: 1
id: j095-rueckwaerts
revision: 1
titel: Rückwärts
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
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
  text: Start bei `wort.length - 1`, Bedingung `i >= 0`, Schritt `i--`.
tests_sichtbar:
- input:
  - Hering
  expected: 'Wort? gnireH

    '
tests_versteckt:
- input:
  - Otto
  expected: 'Wort? ottO

    '
- input:
  - a
  expected: 'Wort? a

    '
starter_code: ''
---

Gib ein eingelesenes Wort rückwärts aus, mit einer for-Schleife, die beim letzten Index beginnt und bis 0 herunterzählt. Bei der Eingabe `Hering`:

```
Wort? gnireH
```
