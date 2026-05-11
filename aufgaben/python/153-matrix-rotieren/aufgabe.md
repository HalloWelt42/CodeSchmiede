---
schema_version: 1
id: 153-matrix-rotieren
revision: 1
titel: Matrix 90 Grad rotieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [matrix, listen, zip, 2d, rotation]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode-Klassiker 48
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: rotieren
hints:
  - kosten: 0
    text: |
      Drehe die NxN-Matrix um 90 Grad im Uhrzeigersinn.
      [[1,2,3],[4,5,6],[7,8,9]] →
      [[7,4,1],[8,5,2],[9,6,3]]
      Bei [] → [].
  - kosten: 15
    text: |
      Rotation 90 Grad CW = Transponieren + jede Zeile umdrehen
      ODER: list(zip(*matrix[::-1])).
      Aussere Liste, innere Listen.
tests_sichtbar:
  - input: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
  - input: [[[1, 2], [3, 4]]]
    expected: [[3, 1], [4, 2]]
  - input: [[[1]]]
    expected: [[1]]
  - input: [[]]
    expected: []
tests_versteckt:
  - input: [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]
    expected: [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
  - input: [[["a", "b"], ["c", "d"]]]
    expected: [["c", "a"], ["d", "b"]]
  - input: [[[1, 2], [3, 4], [5, 6]]]
    expected: [[5, 3, 1], [6, 4, 2]]
  - input: [[[0, 0], [0, 1]]]
    expected: [[0, 0], [1, 0]]
starter_code: |
  def rotieren(matrix: list[list]) -> list[list]:
      # Deine Lösung hier -- 90 Grad im Uhrzeigersinn
      pass
---

# Matrix 90 Grad rotieren

Schreibe eine Funktion `rotieren(matrix)`, die eine 2D-Matrix um
**90 Grad im Uhrzeigersinn** dreht.

## Beispiel 3x3

```
1 2 3       7 4 1
4 5 6   →   8 5 2
7 8 9       9 6 3
```

Die linke Spalte wird zur oberen Zeile (von rechts nach links gelesen).
Bei `[]` → `[]`.

## Idee -- Zwei Tricks

**Trick 1**: Erst **Zeilen umdrehen**, dann **transponieren**:

**Trick 2**: Direkt mit Index-Math:

```
neu[j][n - 1 - i] = matrix[i][j]
```

## Andere Drehungen

| Winkel        | Trick                              |
|---------------|------------------------------------|
| 90 CW         | `zip(*matrix[::-1])`               |
| 90 CCW        | `zip(*matrix)` und Zeilen umdrehen |
| 180           | `[zeile[::-1] for zeile in matrix[::-1]]` |
| 270 CW        | wie 90 CCW                         |

## Wozu?

In Spielen wie Tetris oder Sudoku-Generatoren rotiert man Bloecke
oder Felder. In der Bildverarbeitung sind 90-Grad-Rotationen die
einzigen, die **ohne Interpolation** verlustfrei moeglich sind.
