---
schema_version: 1
id: k232-mitte
revision: 1
titel: Die Mitte
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 2
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
  text: Die Mitte ist die ganzzahlige Hälfte von links plus rechts.
tests_sichtbar:
- input: []
  expected: '(5, 3)

    '
starter_code: "def binaer(liste, ziel):\n    links, rechts = 0, len(liste) - 1\n    schritte = 0\n    while links <= rechts:\n\
  \        schritte += 1\n        mitte = (links + rechts) // ___\n        if liste[mitte] == ziel:\n            return mitte,\
  \ schritte\n        if liste[mitte] < ziel:\n            links = mitte + 1\n        else:\n            rechts = mitte -\
  \ 1\n    return -1, schritte\n\n\nprint(binaer([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23))\n"
---

Ergänze die Lücke `___` in der binären Suche, damit die 23 gefunden wird:

```
(5, 3)
```
