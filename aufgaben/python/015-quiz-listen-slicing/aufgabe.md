---
schema_version: 1
id: 015-quiz-listen-slicing
revision: 1
titel: Was gibt das Slicing aus?
sprache: python
task_type: output_quiz
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 4
tags: [quiz, slicing, listen, output]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Slicing-Quiz mit negativem Schritt
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
hints: []
quiz:
  code: |
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(a[1:6:2])
  optionen:
    - "[2, 4, 6]"
    - "[1, 3, 5]"
    - "[2, 3, 4, 5]"
    - "[1, 2, 3, 4, 5, 6]"
  richtig_index: 0
---

# Was gibt das Slicing aus?

Lies den Code aufmerksam und wähle die korrekte Ausgabe.

## Hintergrund

Slicing-Notation: `liste[start:stop:schritt]`

- `start` ist inklusiv, `stop` exklusiv.
- `schritt` bestimmt, wie viele Elemente übersprungen werden.
- Negative Indizes zählen von hinten.

## Hinweise

- Index 1 in `[1, 2, 3, 4, 5, 6, 7, 8]` ist die `2`.
- Index 6 ist die `7` -- aber stop ist exklusiv, also wird `7` nicht
  mitgenommen.
- Schritt `2` heisst: jedes zweite Element.
