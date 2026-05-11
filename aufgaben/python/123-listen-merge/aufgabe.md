---
schema_version: 1
id: 123-listen-merge
revision: 1
titel: Zwei sortierte Listen mergen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [listen, schleifen, vergleich, merge-sort]
pfade: [python_listen3]
voraussetzungen: []
quelle:
  url: null
  notiz: Standard-Schritt von Merge-Sort, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: merge
hints:
  - kosten: 0
    text: |
      Eingabe sind zwei bereits sortierte Listen. Zwei Zeiger,
      pro Schritt das kleinere vordere Element nehmen.
  - kosten: 8
    text: |
      Verboten: `sorted(a + b)`. Eigene Schleife.
tests_sichtbar:
  - input: [[1, 3, 5], [2, 4, 6]]
    expected: [1, 2, 3, 4, 5, 6]
  - input: [[], [1, 2, 3]]
    expected: [1, 2, 3]
  - input: [[1, 2, 3], []]
    expected: [1, 2, 3]
  - input: [[], []]
    expected: []
tests_versteckt:
  - input: [[1, 1, 1], [1, 1, 1]]
    expected: [1, 1, 1, 1, 1, 1]
  - input: [[5], [1, 2, 3, 4]]
    expected: [1, 2, 3, 4, 5]
  - input: [[-3, -1, 0], [-2, 1, 2]]
    expected: [-3, -2, -1, 0, 1, 2]
  - input: [[1, 5, 9], [2, 6, 10, 11, 12]]
    expected: [1, 2, 5, 6, 9, 10, 11, 12]
starter_code: |
  def merge(a: list[int], b: list[int]) -> list[int]:
      # Deine Lösung hier -- ohne sorted(). Zwei Zeiger.
      pass
---

# Zwei sortierte Listen mergen

Schreibe eine Funktion `merge(a, b)`, die zwei bereits **aufsteigend
sortierte** Listen zu einer sortierten Liste zusammenführt.

**Verboten**: `sorted(a + b)`. Eigene Schleife.

## Idee

Zwei Zeiger `i`, `j`. Pro Schritt vergleichen `a[i]` und `b[j]`,
das kleinere ans Ergebnis anhängen, Zeiger weiter. Am Ende den
Rest der nicht-leeren Liste anhängen.

## Beispiele

| `a`        | `b`        | Ergebnis        |
|------------|------------|-----------------|
| `[1,3,5]`  | `[2,4,6]`  | `[1,2,3,4,5,6]` |
| `[]`       | `[1,2,3]`  | `[1,2,3]`       |
| `[5]`      | `[1,2,3,4]`| `[1,2,3,4,5]`   |

## Hintergrund

Der **Merge-Schritt** in Merge-Sort. $O(n + m)$. Diese kleine
Routine ist die Eintrittskarte zu allen Sortier- und
Mengen-Algorithmen.
