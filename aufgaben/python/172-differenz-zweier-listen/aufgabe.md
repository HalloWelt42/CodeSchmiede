---
schema_version: 1
id: 172-differenz-zweier-listen
revision: 1
titel: Differenz zweier Listen
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
funktion: differenz
hints:
  - kosten: 0
    text: |
      Liefere die Elemente, die in a aber NICHT in b vorkommen --
      eindeutig und aufsteigend sortiert.
  - kosten: 8
    text: |
      sorted(set(a) - set(b)) erledigt es in einem Ausdruck.
tests_sichtbar:
  - input: [[1, 2, 3], [2, 3, 4]]
    expected: [1]
  - input: [[1, 2, 3], []]
    expected: [1, 2, 3]
  - input: [[], [1, 2]]
    expected: []
  - input: [[1, 2, 3], [1, 2, 3]]
    expected: []
tests_versteckt:
  - input: [[5, 5, 5], [5]]
    expected: []
  - input: [[1, 2, 3, 4, 5], [3]]
    expected: [1, 2, 4, 5]
  - input: [[-3, -2, -1, 0], [0]]
    expected: [-3, -2, -1]
  - input: [[10, 20, 30], [40, 50, 60]]
    expected: [10, 20, 30]
  - input: [[1, 1, 2, 2, 3, 3], [2]]
    expected: [1, 3]
starter_code: |
  def differenz(a: list, b: list) -> list:
      # Deine Lösung hier -- a \ b, eindeutig sortiert
      pass
---

# Differenz zweier Listen

Schreibe eine Funktion `differenz(a, b)`, die die Elemente aus `a`
liefert, die **nicht** in `b` vorkommen -- als **aufsteigend
sortierte, eindeutige** Liste.

## Beispiele

| `a`               | `b`           | Differenz `a \ b` |
|-------------------|---------------|-------------------|
| `[1, 2, 3]`       | `[2, 3, 4]`   | `[1]`             |
| `[1, 2, 3]`       | `[]`          | `[1, 2, 3]`       |
| `[]`              | `[1, 2]`      | `[]`              |
| `[1, 1, 2, 2, 3]` | `[2]`         | `[1, 3]`          |

Doppelte Werte in `a` werden zu einem Eintrag verdichtet.

## Set-Differenz vs. Symmetrische Differenz

| Operator      | Bedeutung                                     |
|---------------|-----------------------------------------------|
| `set(a) - b`  | nur in a, nicht in b                          |
| `a ^ b`       | in a oder b, aber nicht in beiden             |
| `b - a`       | nur in b, nicht in a                          |

Die symmetrische Differenz ist die Vereinigung von `a - b` und `b - a`
-- praktisch, wenn man "Was ist anders?" beantworten will.

## Anwendung

In Versionierungs-Tools (Git diff, dbt audit) ist Set-Differenz ein
Standard-Schritt: "Welche Schlüssel sind im neuen Dump dazugekommen?"
→ `set(neu) - set(alt)`.
