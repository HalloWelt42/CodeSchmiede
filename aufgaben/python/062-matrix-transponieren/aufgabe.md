---
schema_version: 1
id: 062-matrix-transponieren
revision: 1
titel: Matrix transponieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [matrix, listen, comprehension, zip]
pfade: [python_logik]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Transponierte_Matrix
  notiz: Klassische Matrix-Operation
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: transponieren
hints:
  - kosten: 0
    text: |
      Aus Spalten werden Zeilen. Bei einer m x n Matrix wird das
      Ergebnis n x m.
  - kosten: 8
    text: |
      Mit zip(*matrix) und List-Comprehension geht es in einer Zeile:
      `[list(zeile) for zeile in zip(*matrix)]`.
tests_sichtbar:
  - input: [[[1, 2, 3], [4, 5, 6]]]
    expected: [[1, 4], [2, 5], [3, 6]]
  - input: [[[1, 2], [3, 4]]]
    expected: [[1, 3], [2, 4]]
  - input: [[[1]]]
    expected: [[1]]
  - input: [[[1, 2, 3]]]
    expected: [[1], [2], [3]]
tests_versteckt:
  - input: [[[1], [2], [3]]]
    expected: [[1, 2, 3]]
  - input: [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
    expected: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
starter_code: |
  def transponieren(matrix: list[list]) -> list[list]:
      # Deine Lösung hier -- m x n -> n x m
      pass
---

# Matrix transponieren

Schreibe eine Funktion `transponieren(matrix)`, die eine Matrix
**transponiert** -- aus Zeilen werden Spalten und umgekehrt.

Eine `m x n` Matrix wird zu `n x m`.

## Beispiele

| Eingabe                          | Ergebnis                       |
|----------------------------------|--------------------------------|
| `[[1,2,3],[4,5,6]]`              | `[[1,4],[2,5],[3,6]]`          |
| `[[1,2],[3,4]]`                  | `[[1,3],[2,4]]`                |
| `[[1]]`                          | `[[1]]`                        |
| `[[1,2,3]]`                      | `[[1],[2],[3]]`                |

## Idee

Element `matrix[i][j]` landet im Ergebnis bei `result[j][i]`.

## Idiomatic

`list(zip(*matrix))` macht das in einer Zeile -- `zip` mit Unpacking
liefert Tupel der Spalten. `list(...)` und ggf. `list(zeile) for ...`
für reine Listen.
