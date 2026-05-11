---
schema_version: 1
id: 315-itertools-combinations
revision: 1
titel: Alle k-er Kombinationen aus Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 25
schaetz_minuten: 10
tags: [itertools, kombinatorik, listen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: itertools.combinations als Wrapper
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: kombis
hints:
  - kosten: 0
    text: |
      Liefere alle k-elementigen Kombinationen aus der Liste -- als
      Liste von Listen, lexikographisch geordnet.
      [1,2,3] mit k=2 → [[1,2], [1,3], [2,3]].
      k <= 0 oder k > len → [].
  - kosten: 10
    text: |
      itertools.combinations(liste, k) liefert Tupel-Generator,
      [list(t) for t in ...] zur Konvertierung.
tests_sichtbar:
  - input: [[1, 2, 3], 2]
    expected: [[1, 2], [1, 3], [2, 3]]
  - input: [[1, 2, 3, 4], 1]
    expected: [[1], [2], [3], [4]]
  - input: [[1, 2, 3], 0]
    expected: []
  - input: [[1, 2], 3]
    expected: []
tests_versteckt:
  - input: [[1, 2, 3, 4], 2]
    expected: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
  - input: [[1, 2, 3, 4], 3]
    expected: [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
  - input: [[1, 2, 3, 4, 5], 4]
    expected: [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]]
  - input: [["a", "b", "c"], 2]
    expected: [["a", "b"], ["a", "c"], ["b", "c"]]
  - input: [[], 2]
    expected: []
  - input: [[42], 1]
    expected: [[42]]
starter_code: |
  from itertools import combinations

  def kombis(liste: list, k: int) -> list[list]:
      # Tipp: itertools.combinations liefert Tupel, in Listen wandeln
      pass
---

# Alle k-er Kombinationen aus Liste

Schreibe `kombis(liste, k)`, die alle **k-elementigen Kombinationen**
aus der Liste liefert -- lexikographisch geordnet.

`k <= 0` oder `k > len(liste)` → `[]`.

## Beispiele

| Liste            | k | Ergebnis                                  |
|------------------|---|--------------------------------------------|
| `[1, 2, 3]`      | 2 | `[[1,2], [1,3], [2,3]]`                   |
| `[1, 2, 3, 4]`   | 2 | `[[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]` |
| `[1, 2, 3, 4]`   | 3 | `[[1,2,3], [1,2,4], [1,3,4], [2,3,4]]`    |
| `[1, 2, 3, 4]`   | 1 | `[[1], [2], [3], [4]]`                    |
| `[1, 2]`         | 3 | `[]` (k > len)                            |

Anzahl der Kombinationen: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.
Bei `[1,2,3,4]` mit `k=2`: $\binom{4}{2} = 6$.

## Idee

```python
from itertools import combinations

def kombis(liste, k):
    if k <= 0 or k > len(liste):
        return []
    return [list(t) for t in combinations(liste, k)]
```

`itertools.combinations` ist hochoptimiert (C-Implementierung) und
liefert die Reihenfolge **lexikographisch** -- also genau wie in
unseren Tests erwartet.

## Verwandt

- **108-permutationen** (alle Permutationen)
- **132-binomialkoeffizient** (Anzahl der Kombinationen)
- **315 hier** (die Kombinationen selbst)

## Anwendung

- **Lotto-Tippen**: alle moeglichen 6-aus-49 Ziehungen.
- **Team-Aufstellung**: alle Spieler-Kombinationen.
- **Subset-Probleme** in der Algorithmik.
