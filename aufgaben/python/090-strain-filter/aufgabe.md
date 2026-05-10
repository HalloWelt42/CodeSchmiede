---
schema_version: 1
id: 090-strain-filter
revision: 1
titel: Eigene filter-Funktion
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [listen, funktional, schleifen]
pfade: [python_funktional]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (strain), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: behalte
hints:
  - kosten: 0
    text: |
      Die Aufgabe: schreibe filter() selbst nach. Für jedes Element
      `x` aus der Liste: ist `funktion(x)` truthy, behalte es.
  - kosten: 10
    text: |
      List-Comprehension ist ein schöner One-Liner:
      `[x for x in liste if funktion(x)]`. Aber bewusst NICHT die
      eingebaute `filter()` verwenden -- die wäre Cheating.
tests_sichtbar:
  - input: [[1, 2, 3], "lambda x: x > 1"]
    expected: [2, 3]
  - input: [[], "lambda x: True"]
    expected: []
  - input: [[1, 2, 3, 4, 5], "lambda x: x % 2 == 0"]
    expected: [2, 4]
  - input: [["apple", "banana", "cherry"], "lambda x: 'a' in x"]
    expected: ["apple", "banana"]
tests_versteckt:
  - input: [[1, 2, 3, 4, 5], "lambda x: False"]
    expected: []
  - input: [[1, 2, 3, 4, 5], "lambda x: True"]
    expected: [1, 2, 3, 4, 5]
  - input: [[0, 1, 2, 3, 0, 0, 4], "lambda x: x"]
    expected: [1, 2, 3, 4]
  - input: [[-3, -2, -1, 0, 1, 2, 3], "lambda x: x < 0"]
    expected: [-3, -2, -1]
starter_code: |
  def behalte(liste, funktion_text):
      # `funktion_text` ist ein lambda-Ausdruck als String, etwa
      # "lambda x: x > 0". Mit `eval(funktion_text)` machst du daraus
      # eine Funktion. Dann filter selbst nachbauen -- ohne filter() zu
      # nutzen.
      pass
---

# Eigene filter-Funktion

Schreibe eine Funktion `behalte(liste, funktion_text)`, die eine
**neue Liste** zurückgibt mit allen Elementen, für die die Test-Funktion
`True` (oder truthy) liefert. **Ohne** das eingebaute `filter()` zu
verwenden.

`funktion_text` kommt als String -- du machst daraus mit `eval()` eine
echte Funktion.

## Beispiele

| Liste              | Funktion              | Ergebnis        |
|--------------------|-----------------------|-----------------|
| `[1,2,3]`          | `x > 1`               | `[2,3]`         |
| `[]`               | beliebig              | `[]`            |
| `[1,2,3,4,5]`      | `x % 2 == 0`          | `[2,4]`         |
| `[1,2,3,4,5]`      | `False` (alle weg)    | `[]`            |
| `[0,1,2,3,0,0,4]`  | `x` (truthy-Check)    | `[1,2,3,4]`     |

## Idee

```python
def behalte(liste, funktion_text):
    f = eval(funktion_text)
    return [x for x in liste if f(x)]
```

## Hintergrund

Die eingebaute `filter()`-Funktion ist nur ein dünner Wrapper um
genau diese Logik. Selbst-Reimplementierung trainiert das Pattern
und macht klar, was unter der Haube passiert -- der Pfad zu
`map`, `reduce` und Higher-Order-Functions öffnet sich.
