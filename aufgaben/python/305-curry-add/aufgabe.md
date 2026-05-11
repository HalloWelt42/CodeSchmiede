---
schema_version: 1
id: 305-curry-add
revision: 1
titel: Curry-artige partielle Anwendung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 35
schaetz_minuten: 12
tags: [funktional, curry, closures]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Funktionales Curry-Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: addiere_zu_allen
hints:
  - kosten: 0
    text: |
      Erzeuge intern einen "Adder" mit fester Konstante c und wende
      ihn auf jedes Element der Liste an.
      Beispiel: addiere_zu_allen(10, [1, 2, 3]) → [11, 12, 13].
      Bei [] → [].
  - kosten: 15
    text: |
      Innerer Helper macher = lambda x: x + c. Dann [macher(x) for x in liste].
      ODER per functools.partial(operator.add, c).
tests_sichtbar:
  - input: [10, [1, 2, 3]]
    expected: [11, 12, 13]
  - input: [0, [1, 2, 3]]
    expected: [1, 2, 3]
  - input: [5, []]
    expected: []
  - input: [-1, [10, 20, 30]]
    expected: [9, 19, 29]
tests_versteckt:
  - input: [100, [1, 2, 3, 4, 5]]
    expected: [101, 102, 103, 104, 105]
  - input: [0, []]
    expected: []
  - input: [3, [3]]
    expected: [6]
  - input: [-100, [100, 200, 300]]
    expected: [0, 100, 200]
  - input: [1, [-1, 0, 1]]
    expected: [0, 1, 2]
  - input: [1000, [1000000]]
    expected: [1001000]
starter_code: |
  def addiere_zu_allen(c: int, liste: list[int]) -> list[int]:
      # Tipp: einen Adder als Lambda/closure erzeugen
      pass
---

# Curry-artige partielle Anwendung

Schreibe `addiere_zu_allen(c, liste)`, die einen **Addierer** mit
fester Konstante `c` baut und auf jedes Element der Liste anwendet.

## Beispiele

| `c`   | Liste            | Ergebnis             |
|-------|------------------|----------------------|
| 10    | `[1, 2, 3]`      | `[11, 12, 13]`       |
| 0     | `[1, 2, 3]`      | `[1, 2, 3]`          |
| -1    | `[10, 20, 30]`   | `[9, 19, 29]`        |
| 100   | `[1, 2, 3, 4, 5]`| `[101,102,103,104,105]`|
| 5     | `[]`             | `[]`                 |

## Idee 1 -- Closure mit Lambda

```python
def addiere_zu_allen(c, liste):
    add_c = lambda x: x + c
    return [add_c(x) for x in liste]
```

Das Lambda **fängt** den aktuellen Wert von `c` aus dem
umschließenden Scope ein -- das ist eine **Closure**.

## Idee 2 -- functools.partial

```python
from functools import partial
from operator import add

def addiere_zu_allen(c, liste):
    add_c = partial(add, c)
    return [add_c(x) for x in liste]
```

`partial(add, c)` erzeugt eine neue Funktion, die `add(c, x)`
ausführt -- das ist **partielle Anwendung**: aus einer 2-stelligen
Funktion machen wir eine 1-stellige.

## Curry vs. Partial

In **Haskell** ist jede Funktion implizit curried -- `add 3 5` ist
das Gleiche wie `(add 3) 5`. In Python muss man explizit `partial`
oder Lambdas nutzen.

**Curry**: `f(a, b, c)` → `f(a)(b)(c)` (eine Stelle nach der anderen).
**Partial**: `f(a, b, c)` → `g(b, c)` mit `g = partial(f, a)`.

Im Alltag sind die Begriffe oft austauschbar -- gemeint ist meist
"Funktion mit fixierten Argumenten".

## Anwendung

- **Event-Handler**: `button.on_click(partial(handler, "X"))`.
- **Map-Operationen** mit Konfiguration: `map(partial(format, fmt="json"), items)`.
- **Sort-Keys**: `sorted(items, key=partial(getattr, "name"))`.
