---
schema_version: 1
id: 066-quiz-list-comprehension
revision: 1
titel: Was gibt die Comprehension aus?
sprache: python
task_type: output_quiz
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 4
tags: [quiz, comprehension, output, lesen]
pfade: [python_quiz]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Comprehension-Falle
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
hints: []
quiz:
  code: |
    a = [x*x for x in range(5) if x % 2 == 0]
    print(a)
  optionen:
    - "[0, 4, 16]"
    - "[1, 9, 25]"
    - "[0, 2, 4]"
    - "[0, 1, 4, 9, 16]"
  richtig_index: 0
---

# Was gibt die Comprehension aus?

Lies den Code genau und wähle die richtige Ausgabe.

## Hintergrund

Eine List-Comprehension hat die Form:

```
[ausdruck for variable in iterable if bedingung]
```

Sie wird von links nach rechts ausgewertet:

1. `for x in range(5)` -- nimmt alle x von 0 bis 4
2. `if x % 2 == 0` -- behaelt nur die geraden
3. `x*x` -- quadriert das Ergebnis

## Hinweise

- `range(5)` liefert `0, 1, 2, 3, 4`.
- Davon sind `0, 2, 4` gerade.
- Quadrate: `0, 4, 16`.
