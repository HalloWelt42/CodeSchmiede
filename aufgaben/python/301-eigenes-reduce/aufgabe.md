---
schema_version: 1
id: 301-eigenes-reduce
revision: 1
titel: Eigenes reduce mit Op-String
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [funktional, listen, reduce, dispatch]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 299/300
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: reduce_op
hints:
  - kosten: 0
    text: |
      Falte eine Liste mit einer binaeren Operation:
      "add" (+), "mul" (*), "max", "min".
      start ist der Startwert (neutrales Element für leere Liste).
      Unbekannte Op → start zurück.
  - kosten: 10
    text: |
      from functools import reduce.
      reduce(op, liste, start) macht es. Op via Dispatch-Dict.
tests_sichtbar:
  - input: [[1, 2, 3, 4], "add", 0]
    expected: 10
  - input: [[1, 2, 3, 4], "mul", 1]
    expected: 24
  - input: [[], "add", 0]
    expected: 0
  - input: [[1, 2, 3], "unknown", 5]
    expected: 5
tests_versteckt:
  - input: [[3, 1, 4, 1, 5, 9, 2, 6], "max", 0]
    expected: 9
  - input: [[3, 1, 4, 1, 5, 9, 2, 6], "min", 100]
    expected: 1
  - input: [[5], "add", 0]
    expected: 5
  - input: [[5], "mul", 1]
    expected: 5
  - input: [[10, 20, 30], "add", 100]
    expected: 160
  - input: [[2, 2, 2, 2], "mul", 1]
    expected: 16
starter_code: |
  def reduce_op(liste: list, op: str, start):
      # Tipp: functools.reduce + Dispatch-Dict
      pass
---

# Eigenes reduce mit Op-String

Schreibe `reduce_op(liste, op, start)`, die eine Liste mit einer
binaeren Operation **faltet** (auch "fold" genannt) -- ausgehend
vom Startwert.

## Verfügbare Operationen

| String  | Wirkung           |
|---------|-------------------|
| `"add"` | Akkumulator + x   |
| `"mul"` | Akkumulator * x   |
| `"max"` | max(Akku, x)      |
| `"min"` | min(Akku, x)      |

Unbekannte Op → `start` zurückgeben (kein Fehler).

## Beispiele

| Liste            | Op       | Start | Ergebnis | Bemerkung           |
|------------------|----------|-------|----------|---------------------|
| `[1, 2, 3, 4]`   | `"add"`  | `0`   | `10`     | Summe               |
| `[1, 2, 3, 4]`   | `"mul"`  | `1`   | `24`     | Produkt = Fakultaet |
| `[3, 1, 4, 1, 5]`| `"max"`  | `0`   | `5`      |                    |
| `[3, 1, 4, 1, 5]`| `"min"`  | `100` | `1`      |                    |
| `[]`             | `"add"`  | `0`   | `0`      | Start zurück      |

## Idee

```python
from functools import reduce

OPS = {
    "add": lambda a, x: a + x,
    "mul": lambda a, x: a * x,
    "max": max,
    "min": min,
}


def reduce_op(liste, op, start):
    if op not in OPS:
        return start
    return reduce(OPS[op], liste, start)
```

`functools.reduce` mit Startwert **erlaubt leere Listen** (liefert
dann den Start). Ohne Startwert würde es bei leerer Liste einen
Fehler werfen.

`max` und `min` sind selbst schon **binaere Funktionen** (in dieser
Form) -- kein Lambda nötig.

## Pattern -- Fold

`reduce` heisst in anderen Sprachen `fold`, `foldLeft`, `accumulate`.
Es ist eines der maechtigsten funktionalen Patterns:

- `sum` ist `reduce(+, liste, 0)`.
- `product` ist `reduce(*, liste, 1)`.
- `max` ist `reduce(max, liste, -inf)`.
- `concat` von Listen ist `reduce(+, listen, [])`.
- `flatten` ist auch `reduce(+, ...)`.

## Anwendung

Aggregations-Funktionen in Datenbank-Engines, Stream-Processing
(Kafka, Spark), und überall wo "alle Werte zu einem zusammenfassen".
