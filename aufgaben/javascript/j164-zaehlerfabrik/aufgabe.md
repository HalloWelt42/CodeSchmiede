---
schema_version: 1
id: j164-zaehlerfabrik
revision: 1
titel: Die Zählerfabrik
sprache: javascript
task_type: programm
runner_type: docker_javascript
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- sichtbarkeit
- closure
voraussetzungen: []
quelle:
  notiz: Aufbaukurs JavaScript, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Der Zähler merkt sich den aktuellen Wert in der Fabrik.
- kosten: 2
  text: 'Ein Trick: mit `start - schritt` beginnen und vor dem Liefern addieren.'
tests_sichtbar:
- input: []
  expected: '10 15 20

    0 -2 -4 -6

    '
starter_code: ''
---

Schreib `zaehlerBauen(start, schritt)`, die einen Zähler liefert: Der erste Aufruf liefert start, jeder weitere den vorigen Wert plus schritt. Gib damit aus:

```
10 15 20
0 -2 -4 -6
```
