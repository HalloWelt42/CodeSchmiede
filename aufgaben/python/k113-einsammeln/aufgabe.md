---
schema_version: 1
id: k113-einsammeln
revision: 1
titel: Wörter einsammeln
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- listenmethoden
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Eine leere Liste, while True, break bei fertig, sonst append.
tests_sichtbar:
- input:
  - Eis
  - Fisch
  - fertig
  expected: '[''Eis'', ''Fisch'']

    '
tests_versteckt:
- input:
  - fertig
  expected: '[]

    '
- input:
  - a
  - b
  - c
  - fertig
  expected: '[''a'', ''b'', ''c'']

    '
starter_code: ''
---

Lies Wörter ein, bis `fertig` kommt, sammle sie mit `append` und gib am Ende die Liste aus. Bei `Eis`, `Fisch`, `fertig`:

```
['Eis', 'Fisch']
```
