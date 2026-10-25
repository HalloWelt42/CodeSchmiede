---
schema_version: 1
id: k087-zahlenraten
revision: 1
titel: Zahlenraten
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags:
- kurs
- while
- verzweigung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zähler für die Versuche, while True und break bei Treffer.
tests_sichtbar:
- input:
  - '3'
  - '9'
  - '7'
  expected: 'zu klein

    zu groß

    getroffen!

    Versuche: 3

    '
tests_versteckt:
- input:
  - '7'
  expected: 'getroffen!

    Versuche: 1

    '
- input:
  - '1'
  - '2'
  - '8'
  - '7'
  expected: 'zu klein

    zu klein

    zu groß

    getroffen!

    Versuche: 4

    '
starter_code: 'geheim = 7

  '
---

Pit denkt sich die Zahl 7. Lies so lange Tipps ein, bis 7 getroffen ist. Zu jedem Tipp erscheint `zu klein`, `zu groß` oder `getroffen!`; danach die Zahl der Versuche. Bei `3`, `9`, `7`:

```
zu klein
zu groß
getroffen!
Versuche: 3
```
