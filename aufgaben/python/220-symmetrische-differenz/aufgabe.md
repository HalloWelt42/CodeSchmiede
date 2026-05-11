---
schema_version: 1
id: 220-symmetrische-differenz
revision: 1
titel: Symmetrische Differenz zweier Listen
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
funktion: symdiff
hints:
  - kosten: 0
    text: |
      Liefere die Elemente, die in genau EINER der beiden Listen
      vorkommen (in a oder b, aber NICHT in beiden).
      Eindeutig, aufsteigend sortiert.
  - kosten: 10
    text: |
      sorted(set(a) ^ set(b)) -- der ^-Operator ist die symmetrische
      Differenz auf Sets.
tests_sichtbar:
  - input: [[1, 2, 3], [3, 4, 5]]
    expected: [1, 2, 4, 5]
  - input: [[1, 2, 3], [1, 2, 3]]
    expected: []
  - input: [[], [1, 2]]
    expected: [1, 2]
  - input: [[], []]
    expected: []
tests_versteckt:
  - input: [[1, 1, 2, 2], [2, 2, 3, 3]]
    expected: [1, 3]
  - input: [[10, 20, 30], [20, 30, 40]]
    expected: [10, 40]
  - input: [[-1, 0, 1], [0]]
    expected: [-1, 1]
  - input: [[5, 5, 5], [5]]
    expected: []
  - input: [[1, 2, 3], [4, 5, 6]]
    expected: [1, 2, 3, 4, 5, 6]
starter_code: |
  def symdiff(a: list, b: list) -> list:
      # Deine Lösung hier
      pass
---

# Symmetrische Differenz zweier Listen

Schreibe `symdiff(a, b)`, die die **symmetrische Differenz** als
sortierte, eindeutige Liste zurückgibt: alle Elemente, die in
**genau einer** der beiden Listen vorkommen.

$$A \triangle B = (A \cup B) \setminus (A \cap B)$$

## Beispiele

| `a`              | `b`              | $A \triangle B$  |
|------------------|------------------|-------------------|
| `[1, 2, 3]`      | `[3, 4, 5]`      | `[1, 2, 4, 5]`    |
| `[1, 2, 3]`      | `[1, 2, 3]`      | `[]`              |
| `[10, 20, 30]`   | `[20, 30, 40]`   | `[10, 40]`        |
| `[]`             | `[1, 2]`         | `[1, 2]`          |
| `[5, 5, 5]`      | `[5]`            | `[]`              |

## Idee

```python
def symdiff(a, b):
    return sorted(set(a) ^ set(b))
```

Der `^`-Operator (XOR) auf Sets ist die symmetrische Differenz --
"in genau einem von beiden".

## Wann braucht man das?

- **Diff-Tools**: was hat sich zwischen zwei Sammlungen verändert?
- **Set-Updates**: in Spielen (Inventar A vs. B → was wurde gewechselt?).
- **Symmetric-Difference-Index** in Versionskontrollen.

## Verwandte Operationen (Aufgaben)

| Operator | Aufgabe |
|----------|---------|
| `&`      | 171 (Schnitt)            |
| `\|`     | 219 (Vereinigung)         |
| `-`      | 172 (Differenz)           |
| `^`      | hier                       |

Vier Set-Operationen, vier Aufgaben -- danach ist die Mengenlehre
in Python solide.
