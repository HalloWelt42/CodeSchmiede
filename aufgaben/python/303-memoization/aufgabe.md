---
schema_version: 1
id: 303-memoization
revision: 1
titel: Memoization-Demo mit Cache-Verlauf
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 25
schaetz_minuten: 10
tags: [funktional, cache, optimierung, dict]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Funktionales Caching-Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: memoize_lauf
hints:
  - kosten: 0
    text: |
      Simuliere eine teure Funktion (square: x → x²) mit Cache.
      Liefere PRO Eingabe ein Tupel [wert, war_im_cache] zurück.
      Reihenfolge wie in der Eingabe.
      Beispiel: [3, 5, 3] → [[9, false], [25, false], [9, true]].
  - kosten: 15
    text: |
      Dict cache. Pro x: if x in cache → True, sonst rechnen + cachen.
tests_sichtbar:
  - input: [[3, 5, 3]]
    expected: [[9, false], [25, false], [9, true]]
  - input: [[]]
    expected: []
  - input: [[2]]
    expected: [[4, false]]
  - input: [[2, 2, 2]]
    expected: [[4, false], [4, true], [4, true]]
tests_versteckt:
  - input: [[1, 2, 3, 1, 2, 3]]
    expected: [[1, false], [4, false], [9, false], [1, true], [4, true], [9, true]]
  - input: [[5, 5, 5, 5, 5]]
    expected: [[25, false], [25, true], [25, true], [25, true], [25, true]]
  - input: [[10, 20, 30]]
    expected: [[100, false], [400, false], [900, false]]
  - input: [[0]]
    expected: [[0, false]]
  - input: [[-3, 3]]
    expected: [[9, false], [9, false]]
  - input: [[7, 8, 7, 8, 7]]
    expected: [[49, false], [64, false], [49, true], [64, true], [49, true]]
starter_code: |
  def memoize_lauf(eingaben: list[int]) -> list:
      # Tipp: Dict-Cache, pro Eingabe pruefen + ggf. eintragen
      pass
---

# Memoization-Demo mit Cache-Verlauf

Schreibe `memoize_lauf(eingaben)`, die eine "teure" Funktion
(`square: x → x²`) auf eine Liste von Eingaben anwendet -- mit
**Cache** -- und pro Eingabe zurückgibt:

`[wert, war_im_cache]`

`war_im_cache` ist `True`, wenn der Wert vor dieser Berechnung
schon im Cache war (also wir nicht wirklich neu rechnen mussten).

## Beispiele

| Eingaben       | Ergebnis                                                |
|----------------|---------------------------------------------------------|
| `[3, 5, 3]`    | `[[9, False], [25, False], [9, True]]`                  |
| `[2, 2, 2]`    | `[[4, False], [4, True], [4, True]]`                    |
| `[5, 5, 5, 5]` | `[[25, False], [25, True], [25, True], [25, True]]`     |
| `[1, 2, 3, 1, 2, 3]` | `[[1,F], [4,F], [9,F], [1,T], [4,T], [9,T]]`     |

**Achtung**: `-3` und `3` sind verschiedene Schlüssel -- der Cache
unterscheidet das nicht aufgrund vom Quadrat, sondern vom rohen
Eingabe-Wert.

## Idee

```python
def memoize_lauf(eingaben):
    cache = {}
    out = []
    for x in eingaben:
        if x in cache:
            out.append([cache[x], True])
        else:
            wert = x * x
            cache[x] = wert
            out.append([wert, False])
    return out
```

## Pattern -- Memoization

In echtem Code nutzt man oft `functools.lru_cache` oder
`functools.cache` als **Decorator**:

```python
from functools import cache

@cache
def square(x):
    return x * x
```

Damit wird jeder Aufruf automatisch gecached. Der **Hash-Lookup**
ist `O(1)` -- bei teuren Funktionen massiv schneller als
Neuberechnung.

## Anwendung

- **Rekursive DP-Lösungen** (Fibonacci, LCS, Coin-Change).
- **API-Caches** (HTTP-GET-Anfragen mit gleichen Argumenten).
- **Datenbank-Query-Caches**.
- **Render-Memoization** in React-ähnlichen Frameworks.

## Stolperstein -- Mutable Args

`@cache` braucht **hashbare** Argumente. Listen/Dicts gehen nicht
direkt -- man müsste sie zu Tupeln konvertieren oder einen eigenen
Hash-Schlüssel berechnen.
