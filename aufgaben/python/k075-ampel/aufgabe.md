---
schema_version: 1
id: k075-ampel
revision: 1
titel: Die Ampel
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
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
  text: if, zweimal elif und ein else.
tests_sichtbar:
- input:
  - gelb
  expected: 'Warten

    '
tests_versteckt:
- input:
  - rot
  expected: 'Stehen

    '
- input:
  - gruen
  expected: 'Gehen

    '
- input:
  - blau
  expected: 'Ampel kaputt?

    '
starter_code: ''
---

Lies eine Ampelfarbe ein und gib aus, was der Pinguin tun soll: bei `rot` `Stehen`, bei `gelb` `Warten`, bei `gruen` `Gehen`, bei allem anderen `Ampel kaputt?`. Bei `gelb`:

```
Warten
```
