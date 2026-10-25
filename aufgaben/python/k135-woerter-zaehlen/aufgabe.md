---
schema_version: 1
id: k135-woerter-zaehlen
revision: 1
titel: Wörter zählen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- woerterbuch
- textmethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`satz.split()` liefert die Wörter als Liste.'
- kosten: 2
  text: '`anzahl[w] = anzahl.get(w, 0) + 1`'
tests_sichtbar:
- input:
  - fisch eis fisch
  expected: '{''fisch'': 2, ''eis'': 1}

    '
tests_versteckt:
- input:
  - a b c a b a
  expected: '{''a'': 3, ''b'': 2, ''c'': 1}

    '
- input:
  - eis
  expected: '{''eis'': 1}

    '
starter_code: ''
---

Lies einen Satz ein, zerlege ihn mit `split()` in Wörter und zähle, wie oft jedes vorkommt. Gib das Wörterbuch aus. Bei `fisch eis fisch`:

```
{'fisch': 2, 'eis': 1}
```
