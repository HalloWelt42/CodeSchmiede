---
schema_version: 1
id: 156-diagonal-summen
revision: 1
titel: Diagonal-Summen einer Matrix
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [matrix, summe, listen, 2d]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische 2D-Indexierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: diagonal_summen
hints:
  - kosten: 0
    text: |
      Liefere [haupt, neben] fuer eine quadratische NxN-Matrix.
      Bei []  ->  [0, 0]. Mittelelement bei ungerader Groesse zaehlt
      einmal in jede Diagonale.
  - kosten: 10
    text: |
      Hauptdiagonale: m[i][i].
      Nebendiagonale: m[i][n - 1 - i].
      Beide Summen unabhaengig berechnen.
tests_sichtbar:
  - input: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    expected: [15, 15]
  - input: [[[1]]]
    expected: [1, 1]
  - input: [[]]
    expected: [0, 0]
  - input: [[[1, 2], [3, 4]]]
    expected: [5, 5]
tests_versteckt:
  - input: [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]
    expected: [34, 34]
  - input: [[[5, 0, 0], [0, 5, 0], [0, 0, 5]]]
    expected: [15, 5]
  - input: [[[1, 0], [0, 1]]]
    expected: [2, 0]
  - input: [[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]]
    expected: [0, 0]
  - input: [[[2, 0, 0, 0, 0], [0, 2, 0, 0, 0], [0, 0, 2, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 2]]]
    expected: [10, 2]
starter_code: |
  def diagonal_summen(matrix: list[list[int]]) -> list[int]:
      # Deine Lösung hier -- [haupt, neben]; bei nicht-quadratisch -> [0, 0]
      pass
---

# Diagonal-Summen einer Matrix

Schreibe eine Funktion `diagonal_summen(matrix)`, die fuer eine
**quadratische** NxN-Matrix die Summe der **Hauptdiagonalen** und die
Summe der **Nebendiagonalen** zurueckgibt -- als Liste `[haupt, neben]`.

Bei nicht-quadratischen Matrizen oder leerer Matrix → `[0, 0]`.

## Beispiel

```
1 2 3       Hauptdiagonale: 1 + 5 + 9 = 15
4 5 6       Nebendiagonale: 3 + 5 + 7 = 15
7 8 9
```

Bei ungerader Groesse `N` schneiden sich beide Diagonalen am
**Mittelelement** -- es wird in beiden Summen einmal gezaehlt.

## Beispiel 2x2

```
1 2         Haupt: 1 + 4 = 5
3 4         Neben: 2 + 3 = 5
```

## Idee

```python
def diagonal_summen(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return [0, 0]
    n = len(matrix)
    haupt = sum(matrix[i][i] for i in range(n))
    neben = sum(matrix[i][n - 1 - i] for i in range(n))
    return [haupt, neben]
```

## Anwendung

In linearer Algebra ist die Hauptdiagonal-Summe die **Spur** (trace)
einer Matrix -- gleich der Summe der Eigenwerte. Die Nebendiagonale
spielt z.B. in der Bestimmung von **Determinanten** kleiner Matrizen
eine Rolle (Sarrus-Regel).
