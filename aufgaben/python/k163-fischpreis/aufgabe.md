---
schema_version: 1
id: k163-fischpreis
revision: 1
titel: Der Fischpreis
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 3
tags:
- kurs
- sichtbarkeit
- funktion
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 16
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Lesen von außen klappt ohne global.
tests_sichtbar:
- input:
  - '4'
  expected: 'Kosten: 12

    '
tests_versteckt:
- input:
  - '0'
  expected: 'Kosten: 0

    '
- input:
  - '10'
  expected: 'Kosten: 30

    '
starter_code: 'PREIS = 3

  '
---

Der Preis je Fisch steht draußen in `PREIS`. Schreibe eine Funktion `kosten(anzahl)`, die ihn liest und die Kosten zurückgibt. Lies die Anzahl ein. Bei `4`:

```
Kosten: 12
```
