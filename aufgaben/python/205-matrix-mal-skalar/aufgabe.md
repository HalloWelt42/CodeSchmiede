---
schema_version: 1
id: 205-matrix-mal-skalar
revision: 1
titel: Matrix mal Skalar
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [matrix, mathematik, comprehension]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Lineare Algebra Grundlagen
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: skalar_mal
hints:
  - kosten: 0
    text: |
      Multipliziere jedes Element einer Matrix mit einer Zahl.
      Bei [] -> [].
  - kosten: 7
    text: |
      Doppelte Listen-Comprehension:
      [[c * x for x in zeile] for zeile in matrix].
tests_sichtbar:
  - input: [[[1, 2], [3, 4]], 2]
    expected: [[2, 4], [6, 8]]
  - input: [[[1, 2, 3]], 0]
    expected: [[0, 0, 0]]
  - input: [[], 5]
    expected: []
  - input: [[[1]], 7]
    expected: [[7]]
tests_versteckt:
  - input: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3]
    expected: [[3, 6, 9], [12, 15, 18], [21, 24, 27]]
  - input: [[[1, -2], [-3, 4]], -1]
    expected: [[-1, 2], [3, -4]]
  - input: [[[1.5, 2.5]], 2]
    expected: [[3.0, 5.0]]
  - input: [[[10, 20], [30, 40]], 0]
    expected: [[0, 0], [0, 0]]
  - input: [[[100]], 100]
    expected: [[10000]]
starter_code: |
  def skalar_mal(matrix: list[list], c) -> list[list]:
      # Deine Lösung hier
      pass
---

# Matrix mal Skalar

Schreibe `skalar_mal(matrix, c)`, die jedes Element einer Matrix
mit einer Zahl `c` multipliziert.

Bei leerer Matrix → `[]`.

## Beispiele

```
3 *                 [[3, 6, 9],
[[1, 2, 3],   →      [12, 15, 18],
 [4, 5, 6],          [21, 24, 27]]
 [7, 8, 9]]
```

| Matrix         | `c` | Ergebnis              |
|----------------|-----|-----------------------|
| `[[1,2],[3,4]]`| `2` | `[[2,4],[6,8]]`       |
| `[[1,2,3]]`    | `0` | `[[0,0,0]]`           |
| `[[1.5,2.5]]`  | `2` | `[[3.0,5.0]]`         |
| `[[1,-2],[-3,4]]` | `-1` | `[[-1,2],[3,-4]]`  |

## Idee

Verschachtelte Listen-Comprehension -- aussere Schleife durch
Zeilen, innere durch Elemente.

## Hintergrund

Skalare Multiplikation ist die simpelste Matrix-Operation. Sie
**bewahrt die Form** (gleiche Dimensionen) und ist die Vorstufe
zur **Matrix-Matrix-Multiplikation** (siehe Aufgabe 206).
