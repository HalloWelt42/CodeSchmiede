---
schema_version: 1
id: k096-umgedreht
revision: 1
titel: Rückwärts lesen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- for
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Beginne mit einem leeren Text und setze jedes Zeichen vorn davor.
tests_sichtbar:
- input:
  - Eis
  expected: 'siE

    '
tests_versteckt:
- input:
  - Pinguin
  expected: 'niugniP

    '
- input:
  - a
  expected: 'a

    '
starter_code: ''
---

Lies ein Wort ein und baue es mit einer for-Schleife rückwärts zusammen, ohne Ausschnitt mit `[::-1]`. Bei `Eis`:

```
siE
```
