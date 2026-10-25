---
schema_version: 1
id: k176-alterspruefung
revision: 1
titel: Die Altersprüfung
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 4
tags:
- kurs
- ausnahme
- funktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`raise ValueError("...")` in der Funktion, `except ValueError as fehler:` beim Aufruf.'
tests_sichtbar:
- input:
  - '130'
  expected: 'Fehler: Alter muss zwischen 0 und 120 liegen

    '
- input:
  - '12'
  expected: 'Alter: 12

    '
tests_versteckt:
- input:
  - '-1'
  expected: 'Fehler: Alter muss zwischen 0 und 120 liegen

    '
- input:
  - '0'
  expected: 'Alter: 0

    '
- input:
  - '120'
  expected: 'Alter: 120

    '
starter_code: ''
---

Schreibe eine Funktion `alter_pruefen(alter)`, die bei einem Alter unter 0 oder über 120 einen `ValueError` mit der Meldung `Alter muss zwischen 0 und 120 liegen` auslöst und sonst das Alter zurückgibt. Lies ein Alter ein und gib es aus oder die Meldung mit `Fehler:` davor. Bei `130`:

```
Fehler: Alter muss zwischen 0 und 120 liegen
```

Bei `12`: `Alter: 12`.
