---
schema_version: 1
id: 206-matrix-mal-matrix
revision: 1
titel: Matrix mal Matrix
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 35
schaetz_minuten: 15
tags: [matrix, mathematik, comprehension, lineare-algebra]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Lineare-Algebra-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: matmul
hints:
  - kosten: 0
    text: |
      Multipliziere zwei Matrizen A (m x n) und B (n x p)
      zu einer Matrix C (m x p).
      Wenn die Spalten von A nicht zur Zeilen-Anzahl von B passen
      → []. Wenn A oder B leer → [].
  - kosten: 24
    text: |
      C[i][j] = sum(A[i][k] * B[k][j] for k in range(n)).
      Drei verschachtelte Schleifen oder Comprehensions.
tests_sichtbar:
  - input: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    expected: [[19, 22], [43, 50]]
  - input: [[[1, 0], [0, 1]], [[5, 6], [7, 8]]]
    expected: [[5, 6], [7, 8]]
  - input: [[], [[1, 2]]]
    expected: []
  - input: [[[1, 2]], [[1, 2], [3, 4]]]
    expected: [[7, 10]]
tests_versteckt:
  - input: [[[1, 2, 3]], [[4], [5], [6]]]
    expected: [[32]]
  - input: [[[1], [2], [3]], [[4, 5, 6]]]
    expected: [[4, 5, 6], [8, 10, 12], [12, 15, 18]]
  - input: [[[1, 2], [3, 4], [5, 6]], [[1, 0, 0], [0, 1, 0]]]
    expected: [[1, 2, 0], [3, 4, 0], [5, 6, 0]]
  - input: [[[2, 0], [0, 2]], [[1, 2], [3, 4]]]
    expected: [[2, 4], [6, 8]]
  - input: [[[1, 2]], [[1], [2], [3]]]
    expected: []
starter_code: |
  def matmul(a: list[list], b: list[list]) -> list[list]:
      # Deine Lösung hier -- Standard-Matrix-Multiplikation
      pass
---

# Matrix mal Matrix

Schreibe `matmul(a, b)`, die zwei Matrizen multipliziert. Wenn `A`
die Form `(m, n)` hat und `B` die Form `(n, p)`, dann hat das
Ergebnis die Form `(m, p)`.

Wenn die **Spaltenanzahl von A** nicht der **Zeilenanzahl von B**
entspricht → `[]`. Bei leeren Matrizen → `[]`.

## Beispiel

```
[[1, 2],   *   [[5, 6],   =   [[19, 22],
 [3, 4]]        [7, 8]]        [43, 50]]
```

Berechnung: `C[0][0] = 1*5 + 2*7 = 19`, `C[0][1] = 1*6 + 2*8 = 22`,
usw.

## Idee

Drei Schleifen → `O(m * n * p)`. Effizientere Algorithmen
(Straßen, Coppersmith-Winograd) kommen erst bei sehr großen
Matrizen ins Spiel.

## Identitaets-Matrix

Die **Einheitsmatrix** `I` mit Einsen auf der Diagonale wirkt wie
"1" bei der Multiplikation -- `A * I = A`. Test im Beispiel:

```
[[1, 0],   *   [[5, 6],   =   [[5, 6],
 [0, 1]]        [7, 8]]        [7, 8]]
```

## Hintergrund

Matrix-Multiplikation ist die zentrale Operation in **Computer-Grafik**
(3D-Transformation), **neuronalen Netzen** (Layer-Berechnung) und
**Statistik** (lineare Modelle). Numpy oder PyTorch nutzen hochoptimierte
BLAS-Bibliotheken -- aber das Schul-Schema steckt drunter.
