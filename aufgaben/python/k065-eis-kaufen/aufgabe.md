---
schema_version: 1
id: k065-eis-kaufen
revision: 1
titel: Eis kaufen
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- logik
- eingabe
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: 'Aus der Antwort wird ein Wahrheitswert: `input() == "ja"`.'
- kosten: 2
  text: Beide Bedingungen mit `and` verknüpfen.
tests_sichtbar:
- input:
  - ja
  - '5'
  expected: 'True

    '
tests_versteckt:
- input:
  - nein
  - '9'
  expected: 'False

    '
- input:
  - ja
  - '2'
  expected: 'False

    '
starter_code: ''
---

Pia bekommt ein Eis, wenn die Eisdiele offen hat **und** sie mindestens 3 Taler hat. Lies erst `ja` oder `nein` für offen, dann die Taler ein, und gib aus, ob es klappt. Bei `ja` und `5`:

```
True
```
