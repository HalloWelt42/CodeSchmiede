---
schema_version: 1
id: k148-zwei-tage
revision: 1
titel: Zwei Tage am Eisloch
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 9
schaetz_minuten: 6
tags:
- kurs
- menge
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Zwei Schleifen, je eine Menge.
- kosten: 3
  text: '`&` für beide Tage, `-` für nur Montag, `|` für alle.'
tests_sichtbar:
- input:
  - Pia
  - Pit
  - Pia
  - ende
  - Pit
  - Paul
  - ende
  expected: 'Beide Tage: [''Pit'']

    Nur Montag: [''Pia'']

    Insgesamt: 3

    '
tests_versteckt:
- input:
  - ende
  - Paul
  - ende
  expected: 'Beide Tage: []

    Nur Montag: []

    Insgesamt: 1

    '
- input:
  - A
  - B
  - C
  - ende
  - C
  - B
  - ende
  expected: 'Beide Tage: [''B'', ''C'']

    Nur Montag: [''A'']

    Insgesamt: 3

    '
starter_code: ''
---

Lies die Besucher vom Montag ein, bis `ende` kommt, dann die vom Dienstag, wieder bis `ende`. Gib aus, wer an beiden Tagen da war, wer nur am Montag kam (beides sortiert) und wie viele verschiedene Besucher es insgesamt waren. Bei `Pia`, `Pit`, `Pia`, `ende`, `Pit`, `Paul`, `ende`:

```
Beide Tage: ['Pit']
Nur Montag: ['Pia']
Insgesamt: 3
```
