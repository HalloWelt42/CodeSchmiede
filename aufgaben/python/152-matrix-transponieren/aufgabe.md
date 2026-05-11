---
schema_version: 1
id: 152-matrix-transponieren
revision: 1
titel: Matrix transponieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [matrix, listen, zip, 2d]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische 2D-Listen-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: transponieren
hints:
  - kosten: 0
    text: |
      Vertausche Zeilen und Spalten einer Matrix. m[i][j] -> m[j][i].
      Bei [] -> []. Liefere immer Listen-of-Listen, kein Tupel.
  - kosten: 10
    text: |
      zip(*matrix) liefert die transponierte Matrix als Tupel-Generator.
      [list(z) for z in zip(*matrix)] gibt Listen.
tests_sichtbar:
  - input: [[[1, 2, 3], [4, 5, 6]]]
    expected: [[1, 4], [2, 5], [3, 6]]
  - input: [[[1]]]
    expected: [[1]]
  - input: [[]]
    expected: []
  - input: [[[1, 2], [3, 4]]]
    expected: [[1, 3], [2, 4]]
tests_versteckt:
  - input: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
  - input: [[[1], [2], [3]]]
    expected: [[1, 2, 3]]
  - input: [[[1, 2, 3, 4]]]
    expected: [[1], [2], [3], [4]]
  - input: [[["a", "b"], ["c", "d"], ["e", "f"]]]
    expected: [["a", "c", "e"], ["b", "d", "f"]]
  - input: [[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]]
    expected: [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
starter_code: |
  def transponieren(matrix: list[list]) -> list[list]:
      # Deine Lösung hier
      pass
---

# Matrix transponieren

Schreibe eine Funktion `transponieren(matrix)`, die die **Transponierte**
einer 2D-Matrix zurueckgibt -- Zeilen werden Spalten, Spalten werden
Zeilen.

## Beispiele

```
[[1, 2, 3]            [[1, 4]
 [4, 5, 6]]    →       [2, 5]
                       [3, 6]]

[[1, 2]               [[1, 3]
 [3, 4]]      →        [2, 4]]
```

Bei `[]` → `[]`.

## Idee -- zip mit Splat

`zip(*matrix)` ist die idiomatische Loesung -- der Stern entpackt
die Zeilen als Argumente, `zip` faltet sie spaltenweise zusammen.

```python
def transponieren(matrix):
    return [list(z) for z in zip(*matrix)]
```

## Hintergrund

In der linearen Algebra schreibt man $A^T$ -- die Transponierte einer
Matrix. Eigenschaften:

- $(A^T)^T = A$
- $(AB)^T = B^T A^T$
- Symmetrische Matrizen: $A = A^T$

In Bildverarbeitung entspricht das einer **Spiegelung an der
Hauptdiagonalen**. NumPy liefert dasselbe ueber `arr.T`.
