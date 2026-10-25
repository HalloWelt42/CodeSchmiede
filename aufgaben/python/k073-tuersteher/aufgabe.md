---
schema_version: 1
id: k073-tuersteher
revision: 1
titel: Der Türsteher
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- verzweigung
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: if mit `>=`, else für den Rest.
tests_sichtbar:
- input:
  - '5'
  expected: 'Willkommen!

    '
tests_versteckt:
- input:
  - '2'
  expected: 'Leider zu jung.

    '
- input:
  - '3'
  expected: 'Willkommen!

    '
starter_code: ''
---

Am Eisberg-Club darf nur hinein, wer mindestens 3 Jahre alt ist. Lies das Alter ein und gib `Willkommen!` oder `Leider zu jung.` aus. Bei `5`:

```
Willkommen!
```
