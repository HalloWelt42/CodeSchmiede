---
schema_version: 1
id: k095-vokale
revision: 1
titel: Vokale zählen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- for
- enthalten
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Erst klein machen, dann je Zeichen prüfen, ob es in "aeiou" steckt.
tests_sichtbar:
- input:
  - Pinguin
  expected: '3

    '
tests_versteckt:
- input:
  - EISBAER
  expected: '4

    '
- input:
  - Rhythm
  expected: '0

    '
starter_code: ''
---

Lies ein Wort ein und zähle seine Vokale (a, e, i, o, u, groß oder klein). Bei `Pinguin`:

```
3
```
