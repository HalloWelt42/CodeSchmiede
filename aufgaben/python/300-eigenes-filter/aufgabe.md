---
schema_version: 1
id: 300-eigenes-filter
revision: 1
titel: Eigenes filter mit Predicate-String
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [funktional, listen, filter, dispatch]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 299
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: filter_pred
hints:
  - kosten: 0
    text: |
      Behalte nur Elemente, die das Predikat erfuellen.
      Predicates: "positive" (>0), "negative" (<0), "even" (gerade),
      "odd" (ungerade), "nonzero" (!= 0).
      Bei UNBEKANNTEM Predicate → Original-Liste.
      Bei [] → [].
  - kosten: 10
    text: |
      Dict {pred_name: lambda x: bool} und [x for x in liste if pred(x)].
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], "even"]
    expected: [2, 4]
  - input: [[-1, 0, 1, 2], "positive"]
    expected: [1, 2]
  - input: [[], "positive"]
    expected: []
  - input: [[1, 2, 3], "unknown"]
    expected: [1, 2, 3]
tests_versteckt:
  - input: [[-1, 0, 1, 2], "negative"]
    expected: [-1]
  - input: [[1, 2, 3, 4, 5], "odd"]
    expected: [1, 3, 5]
  - input: [[-1, 0, 1, 2, 0], "nonzero"]
    expected: [-1, 1, 2]
  - input: [[0, 0, 0], "positive"]
    expected: []
  - input: [[10], "even"]
    expected: [10]
  - input: [[1, 3, 5, 7], "even"]
    expected: []
starter_code: |
  def filter_pred(liste: list, pred: str) -> list:
      # Tipp: Dispatch-Dict mit Lambdas
      pass
---

# Eigenes filter mit Predicate-String

Schreibe `filter_pred(liste, pred)`, die nur Elemente behaelt, die
das Predikat erfuellen.

## Verfuegbare Predicates

| String       | Bedeutung       |
|--------------|------------------|
| `"positive"` | x > 0           |
| `"negative"` | x < 0           |
| `"even"`     | x % 2 == 0      |
| `"odd"`      | x % 2 != 0      |
| `"nonzero"`  | x != 0          |

Unbekanntes Predicate → unveraenderte Liste.

## Beispiele

| Liste                   | Predicate    | Ergebnis    |
|-------------------------|--------------|-------------|
| `[1, 2, 3, 4, 5]`       | `"even"`     | `[2, 4]`    |
| `[-1, 0, 1, 2]`         | `"positive"` | `[1, 2]`    |
| `[-1, 0, 1, 2]`         | `"negative"` | `[-1]`      |
| `[1, 2, 3, 4, 5]`       | `"odd"`      | `[1, 3, 5]` |
| `[-1, 0, 1, 2, 0]`      | `"nonzero"`  | `[-1, 1, 2]`|

## Idee

```python
PREDS = {
    "positive": lambda x: x > 0,
    "negative": lambda x: x < 0,
    "even": lambda x: x % 2 == 0,
    "odd": lambda x: x % 2 != 0,
    "nonzero": lambda x: x != 0,
}


def filter_pred(liste, pred):
    if pred not in PREDS:
        return list(liste)
    fn = PREDS[pred]
    return [x for x in liste if fn(x)]
```

## Lehrziel -- Predicate-Pattern

Predicates (Funktionen `(x) -> bool`) sind das Herzstueck von
**Filter-Operationen**. In Pythons Builtin:

```python
list(filter(lambda x: x > 0, [1, -2, 3]))  # [1, 3]
```

Mit Listen-Comprehension liest sich das aber in Python besser:

```python
[x for x in [1, -2, 3] if x > 0]
```

## Anwendung

Predicates tauchen in **Validierung**, **Suche**, **SQL-WHERE-
Aequivalenten** und **funktionalen Pipelines** ueberall auf.
