---
schema_version: 1
id: k127-eingaben-paare
revision: 1
titel: Paare einlesen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- tupel
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei Listenabstraktionen mit input, dann `list(zip(...))`.
- kosten: 2
  text: zip liefert die Paare erst, wenn man mit list(...) eine Liste daraus macht.
tests_sichtbar:
- input:
  - Pia
  - Pit
  - Paul
  - '5'
  - '3'
  - '2'
  expected: '[(''Pia'', 5), (''Pit'', 3), (''Paul'', 2)]

    '
tests_versteckt:
- input:
  - A
  - B
  - C
  - '1'
  - '2'
  - '3'
  expected: '[(''A'', 1), (''B'', 2), (''C'', 3)]

    '
starter_code: ''
---

Lies drei Namen und drei Fänge ein (erst alle Namen, dann alle Fänge), bilde mit zip eine Liste von Paaren und gib sie aus. Bei `Pia`, `Pit`, `Paul`, `5`, `3`, `2`:

```
[('Pia', 5), ('Pit', 3), ('Paul', 2)]
```
