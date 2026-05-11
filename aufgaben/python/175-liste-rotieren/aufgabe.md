---
schema_version: 1
id: 175-liste-rotieren
revision: 1
titel: Liste um k Positionen rotieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [listen, slicing, modulo, rotation]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode 189 -- Rotate Array
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: rotieren
hints:
  - kosten: 0
    text: |
      Rotiere die Liste um k Stellen nach RECHTS.
      [1,2,3,4,5] mit k=2 -> [4,5,1,2,3].
      k kann groesser als len(a) sein -> Modulo.
      Negatives k rotiert nach LINKS.
  - kosten: 10
    text: |
      n = len(a). k %= n (vorsicht bei n == 0).
      Slicing-Trick: a[-k:] + a[:-k].
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 2]
    expected: [4, 5, 1, 2, 3]
  - input: [[1, 2, 3, 4, 5], 0]
    expected: [1, 2, 3, 4, 5]
  - input: [[], 3]
    expected: []
  - input: [[1], 100]
    expected: [1]
tests_versteckt:
  - input: [[1, 2, 3, 4, 5], 5]
    expected: [1, 2, 3, 4, 5]
  - input: [[1, 2, 3, 4, 5], 7]
    expected: [4, 5, 1, 2, 3]
  - input: [[1, 2, 3, 4, 5], -1]
    expected: [2, 3, 4, 5, 1]
  - input: [[1, 2, 3, 4, 5], -2]
    expected: [3, 4, 5, 1, 2]
  - input: [["a", "b", "c"], 1]
    expected: ["c", "a", "b"]
  - input: [[1, 2], 3]
    expected: [2, 1]
starter_code: |
  def rotieren(a: list, k: int) -> list:
      # Deine Lösung hier -- nach rechts (k>0), nach links (k<0)
      pass
---

# Liste um k Positionen rotieren

Schreibe eine Funktion `rotieren(a, k)`, die die Liste **um `k`
Positionen nach rechts** rotiert. Negatives `k` rotiert nach links.
`k` kann groesser als `len(a)` sein -- modulo.

## Beispiele

| Liste              | k   | Ergebnis              |
|--------------------|-----|-----------------------|
| `[1, 2, 3, 4, 5]`  | `2` | `[4, 5, 1, 2, 3]`     |
| `[1, 2, 3, 4, 5]`  | `0` | `[1, 2, 3, 4, 5]`     |
| `[1, 2, 3, 4, 5]`  | `5` | `[1, 2, 3, 4, 5]`     |
| `[1, 2, 3, 4, 5]`  | `7` | `[4, 5, 1, 2, 3]`     |
| `[1, 2, 3, 4, 5]`  | `-1`| `[2, 3, 4, 5, 1]`     |
| `[1, 2]`           | `3` | `[2, 1]`              |

## Idee -- Slicing-Trick

```python
def rotieren(a, k):
    n = len(a)
    if n == 0:
        return []
    k %= n
    return a[-k:] + a[:-k] if k else list(a)
```

`a[-k:]` ist der **Schwanz**, der vorne dran soll. `a[:-k]` ist der
**Kopf**, der nach hinten geschoben wird. `k % n` bringt grosse oder
negative `k` in den Bereich `0..n-1`.

**Vorsicht** beim Sonderfall `k == 0`: `a[-0:]` ist die ganze Liste,
nicht die leere -- darum die `if`-Pruefung.

## In-Place-Variante (Reverse-Trick)

Wenn man die Liste **nicht kopieren** darf (z.B. Speicher knapp),
geht das in O(n) und O(1) Extra-Speicher mit drei Reverses:

1. ganze Liste reversen
2. erste k Elemente reversen
3. restliche Elemente reversen

Diesen Trick fragen Bewerbungsgespraeche gerne.
