---
schema_version: 1
id: k248-kistenlager
revision: 1
titel: Das Kistenlager
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- rekursion
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 24
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`isinstance(ding, list)` sagt, ob ding eine innere Kiste ist.'
- kosten: 3
  text: 'Tiefe: 1 plus die größte Tiefe der inneren Kisten (0, wenn es keine gibt).'
tests_sichtbar:
- input: []
  expected: 'lager_a: 21 Fische, Tiefe 3

    lager_b: 8 Fische, Tiefe 4

    '
starter_code: 'lager_a = [3, [2, [1, 4]], 5, [[6]]]

  lager_b = [[[[7]]], 1]

  '
---

Im Lager stecken Kisten in Kisten, und in den Kisten liegen Zahlen für Fische. Schreibe zwei rekursive Funktionen: `fische(kiste)` zählt alle Fische, `tiefe(kiste)` liefert, wie tief die Kisten ineinanderstecken (eine Kiste ohne innere Kisten hat Tiefe 1). Gib für beide Lager eine Zeile aus:

```
lager_a: 21 Fische, Tiefe 3
lager_b: 8 Fische, Tiefe 4
```
