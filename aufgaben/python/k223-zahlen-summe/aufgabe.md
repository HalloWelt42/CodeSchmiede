---
schema_version: 1
id: k223-zahlen-summe
revision: 1
titel: Zahlen im Satz
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
  text: '`re.findall(r"\d+", satz)` liefert die Zahlen als Text, int macht Zahlen daraus.'
tests_sichtbar:
- input:
  - Pia fing 3 Heringe und 12 Lachse
  expected: 'Summe: 15

    '
tests_versteckt:
- input:
  - keine Fische heute
  expected: 'Summe: 0

    '
- input:
  - 100 und 20 und 3
  expected: 'Summe: 123

    '
starter_code: ''
---

Lies einen Satz ein und gib die Summe aller Zahlen darin aus. Bei `Pia fing 3 Heringe und 12 Lachse`:

```
Summe: 15
```
