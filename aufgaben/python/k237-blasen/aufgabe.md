---
schema_version: 1
id: k237-blasen
revision: 1
titel: Blasen steigen auf
sprache: python
task_type: programm
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 5
tags:
- kurs
- algorithmus
- sortieren
voraussetzungen: []
quelle:
  notiz: Aufbaukurs Python, Kapitel 23
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-25'
zeitlimit_sekunden: 5
hints:
- kosten: 0
  text: Eine while-Schleife, die läuft, solange im letzten Durchgang getauscht wurde.
- kosten: 3
  text: Nachbarn sind `zahlen[i]` und `zahlen[i + 1]`, darum läuft i nur bis `len(zahlen) - 1`.
tests_sichtbar:
- input:
  - '3'
  - '1'
  - '2'
  - ende
  expected: '[1, 2, 3]

    Tauschvorgänge: 2

    '
tests_versteckt:
- input:
  - '1'
  - '2'
  - '3'
  - ende
  expected: '[1, 2, 3]

    Tauschvorgänge: 0

    '
- input:
  - '4'
  - '3'
  - '2'
  - '1'
  - ende
  expected: '[1, 2, 3, 4]

    Tauschvorgänge: 6

    '
starter_code: ''
---

Ein anderes Verfahren: Beim Blasensortieren geht man die Liste immer wieder durch und tauscht zwei Nachbarn, wenn der linke größer ist, bis ein Durchgang ohne Tausch bleibt. Lies Zahlen ein, bis `ende` kommt, sortiere so und gib die Liste und die Zahl der Tauschvorgänge aus. Bei `3`, `1`, `2`, `ende`:

```
[1, 2, 3]
Tauschvorgänge: 2
```
