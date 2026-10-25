---
schema_version: 1
id: k245-umdrehen
revision: 1
titel: Rückwärts gelesen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 3
tags:
- kurs
- rekursion
- text
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 24
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Ein leerer Text bleibt leer.
- kosten: 2
  text: Der Rest umgedreht, dann der erste Buchstabe hinten dran.
tests_sichtbar:
- input:
  - Pinguin
  expected: 'niugniP

    '
tests_versteckt:
- input:
  - a
  expected: 'a

    '
- input:
  - Otto
  expected: 'ottO

    '
starter_code: ''
---

Schreibe ohne Schleife und ohne `[::-1]` eine rekursive Funktion `umdrehen(text)`. Lies ein Wort ein. Bei `Pinguin`:

```
niugniP
```
