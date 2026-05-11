---
schema_version: 1
id: 252-ceil-zu-vielfache
revision: 1
titel: Aufrunden zum naechsten Vielfachen von k
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [zahlen, runden, modulo, ceil]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 247 (Standard-Runden)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ceil_vielfache
hints:
  - kosten: 0
    text: |
      Runde n AUFWAERTS zum naechsten Vielfachen von k.
      n = 13, k = 5 → 15. n = 10, k = 5 → 10 (schon Vielfaches).
      k <= 0 → n unveraendert.
      Negative n: -13 mit k=5 → -10 (auf Richtung 0/positiv).
  - kosten: 15
    text: |
      math.ceil(n / k) * k -- aber Achtung bei Floats und negativen.
      Robuster: ((n + k - 1) // k) * k, aber nur fuer positive n/k.
      Standard ist: -(-n // k) * k.
tests_sichtbar:
  - input: [13, 5]
    expected: 15
  - input: [10, 5]
    expected: 10
  - input: [0, 5]
    expected: 0
  - input: [1, 10]
    expected: 10
tests_versteckt:
  - input: [25, 7]
    expected: 28
  - input: [100, 100]
    expected: 100
  - input: [101, 100]
    expected: 200
  - input: [-13, 5]
    expected: -10
  - input: [-10, 5]
    expected: -10
  - input: [-1, 5]
    expected: 0
  - input: [50, 0]
    expected: 50
starter_code: |
  import math

  def ceil_vielfache(n: int, k: int) -> int:
      # Deine Lösung hier -- aufwaerts (Richtung +unendlich)
      pass
---

# Aufrunden zum naechsten Vielfachen von k

Schreibe `ceil_vielfache(n, k)`, die `n` **aufwaerts** zum naechsten
Vielfachen von `k` rundet (Richtung +unendlich).

- Bei `k <= 0` → `n` unveraendert.
- Wenn `n` schon Vielfaches ist → `n` selbst.
- Negative Werte: Richtung 0 (also "aufwaerts" im mathematischen Sinn).

## Beispiele

| `n`  | `k`  | Ergebnis | Bemerkung               |
|------|------|----------|-------------------------|
| 13   | 5    | 15       | 13 → 15                 |
| 10   | 5    | 10       | bereits Vielfaches      |
| 1    | 10   | 10       | aufgerundet auf 10      |
| 25   | 7    | 28       | 25 → 28                 |
| 101  | 100  | 200      | nur knapp drueber       |
| -13  | 5    | -10      | aufwaerts Richtung 0    |
| -1   | 5    | 0        | direkt zu 0             |

## Idee

```python
import math

def ceil_vielfache(n, k):
    if k <= 0:
        return n
    return math.ceil(n / k) * k
```

`math.ceil` liefert die kleinste **ganzzahlige** Obergrenze.
`math.ceil(13/5)` ist `math.ceil(2.6)` = `3`. Mal `5` ergibt `15`.

## Idee -- ohne math

Eleganter Trick:

```python
def ceil_vielfache(n, k):
    if k <= 0:
        return n
    return -(-n // k) * k
```

`-(-n // k)` ist Pythons Idiom fuer "ceil division" -- weil
`//` immer **abwaerts** rundet (auch bei negativen Zahlen), bringt
das doppelte Vorzeichen-Wechseln den Aufwaerts-Effekt.

## Verwandt

| Aufgabe                  | Was?                       |
|--------------------------|----------------------------|
| **247-runden-zu-vielfache** | Standard-Runden (banker's) |
| **252 hier**             | Aufrunden (ceil)           |
| **253-floor-zu-vielfache** | Abrunden (floor)           |
