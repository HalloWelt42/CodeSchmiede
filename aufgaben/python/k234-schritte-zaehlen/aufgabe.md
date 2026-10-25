---
schema_version: 1
id: k234-schritte-zaehlen
revision: 1
titel: Schritte zählen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- algorithmus
- suchen
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 23
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`list(range(1, 1001))` sind die Zahlen von 1 bis 1000.'
- kosten: 2
  text: binaer liefert ein Paar, das du entpacken kannst.
tests_sichtbar:
- input:
  - '777'
  expected: '777 nach 8 Schritten

    '
tests_versteckt:
- input:
  - '1'
  expected: '1 nach 9 Schritten

    '
- input:
  - '1000'
  expected: '1000 nach 10 Schritten

    '
starter_code: "def binaer(liste, ziel):\n    links, rechts = 0, len(liste) - 1\n    schritte = 0\n    while links <= rechts:\n\
  \        schritte += 1\n        mitte = (links + rechts) // 2\n        if liste[mitte] == ziel:\n            return mitte,\
  \ schritte\n        if liste[mitte] < ziel:\n            links = mitte + 1\n        else:\n            rechts = mitte -\
  \ 1\n    return -1, schritte\n\n\n"
---

Die binäre Suche steht schon da. Lies eine Zahl von 1 bis 1000 ein und gib aus, in wie vielen Schritten sie in der Liste der Zahlen von 1 bis 1000 gefunden wird. Bei `777`:

```
777 nach 8 Schritten
```
