---
schema_version: 1
id: k175-sicher-teilen
revision: 1
titel: Sicher teilen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- ausnahme
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 17
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei except hintereinander, je eines je Fehlerart.
tests_sichtbar:
- input:
  - '10'
  - '4'
  expected: 'Ergebnis: 2.5

    '
- input:
  - '10'
  - '0'
  expected: 'Durch null geht nicht

    '
- input:
  - zehn
  - '4'
  expected: 'Bitte nur Zahlen

    '
tests_versteckt:
- input:
  - '9'
  - x
  expected: 'Bitte nur Zahlen

    '
- input:
  - '0'
  - '5'
  expected: 'Ergebnis: 0.0

    '
starter_code: ''
---

Lies zwei Eingaben ein und teile die erste durch die zweite. Fange beide möglichen Fehler getrennt ab. Bei `10` und `4`:

```
Ergebnis: 2.5
```

Bei `10` und `0`: `Durch null geht nicht`. Bei `zehn` und `4`: `Bitte nur Zahlen`.
