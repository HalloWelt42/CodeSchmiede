---
schema_version: 1
id: 171-schnitt-zweier-listen
revision: 1
titel: Schnitt zweier Listen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [listen, set, mengen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Set-Operation
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: schnitt
hints:
  - kosten: 0
    text: |
      Liefere die Elemente, die in beiden Listen vorkommen --
      eindeutig und aufsteigend sortiert.
      Bei [] und/oder Disjunktion → [].
  - kosten: 10
    text: |
      sorted(set(a) & set(b)) erledigt alles in einem Ausdruck.
tests_sichtbar:
  - input: [[1, 2, 3], [2, 3, 4]]
    expected: [2, 3]
  - input: [[], [1, 2]]
    expected: []
  - input: [[1, 2, 3], [4, 5]]
    expected: []
  - input: [[1, 1, 2, 2], [2, 2, 3, 3]]
    expected: [2]
tests_versteckt:
  - input: [[1, 2, 3, 4, 5], [3, 4, 5, 6, 7]]
    expected: [3, 4, 5]
  - input: [[5, 5, 5], [5]]
    expected: [5]
  - input: [[-3, -2, -1], [-1, 0, 1]]
    expected: [-1]
  - input: [[10, 20, 30, 40, 50], [50, 40, 30, 20, 10]]
    expected: [10, 20, 30, 40, 50]
  - input: [[1], [1]]
    expected: [1]
starter_code: |
  def schnitt(a: list, b: list) -> list:
      # Deine Lösung hier -- aufsteigend sortiert, eindeutig
      pass
---

# Schnitt zweier Listen

Schreibe eine Funktion `schnitt(a, b)`, die die **gemeinsamen Elemente**
zweier Listen als **aufsteigend sortierte, eindeutige** Liste
zurückgibt.

## Beispiele

| `a`              | `b`              | Schnitt        |
|------------------|------------------|----------------|
| `[1, 2, 3]`      | `[2, 3, 4]`      | `[2, 3]`       |
| `[1, 2, 3]`      | `[4, 5]`         | `[]`           |
| `[1, 1, 2, 2]`   | `[2, 2, 3, 3]`   | `[2]`          |
| `[]`             | `[1, 2]`         | `[]`           |

Doppelte Werte in den Eingaben werden zu einem Eintrag verdichtet.

## Idee -- Set-Operation

```python
def schnitt(a, b):
    return sorted(set(a) & set(b))
```

Effizient (`O(n + m)` Hash-Vergleiche) und **lesbar**.

## Verwandte Operationen

| Operator | Bedeutung           |
|----------|---------------------|
| `&`      | Schnitt             |
| `\|`     | Vereinigung         |
| `-`      | Differenz           |
| `^`      | Symmetrische Diff.  |

Alle vier sind in der Mengenlehre Standard und in Python direkt
verfügbar -- siehe Aufgaben **172-differenz-zweier-listen** und
spaeter **vereinigung** / **symmetrische Differenz**.
