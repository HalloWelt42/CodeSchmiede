---
schema_version: 1
id: k224-postleitzahl
revision: 1
titel: Die Postleitzahl
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- regex
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 22
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: '`re.fullmatch(r"\d{5}", plz)` prüft den ganzen Text.'
tests_sichtbar:
- input:
  - '48143'
  expected: '48143 ist gültig

    '
- input:
  - 4814a
  expected: '4814a ist ungültig

    '
tests_versteckt:
- input:
  - '481430'
  expected: '481430 ist ungültig

    '
- input:
  - '1234'
  expected: '1234 ist ungültig

    '
- input:
  - '01067'
  expected: '01067 ist gültig

    '
starter_code: ''
---

Lies eine Postleitzahl ein und prüfe, ob sie aus genau fünf Ziffern besteht. Bei `48143`:

```
48143 ist gültig
```

Bei `4814a`: `4814a ist ungültig`.
