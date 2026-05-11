---
schema_version: 1
id: 173-kartesisches-produkt
revision: 1
titel: Kartesisches Produkt zweier Listen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [listen, kombinatorik, paare]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Mengen-Operation
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: kartesisch
hints:
  - kosten: 0
    text: |
      Liefere alle Paare [a_i, b_j] aus zwei Listen.
      Reihenfolge: erst a fest, dann b durchgehen.
      [1,2] x [3,4] -> [[1,3],[1,4],[2,3],[2,4]].
  - kosten: 10
    text: |
      Listen-Comprehension mit zwei Schleifen:
      [[x, y] for x in a for y in b].
tests_sichtbar:
  - input: [[1, 2], [3, 4]]
    expected: [[1, 3], [1, 4], [2, 3], [2, 4]]
  - input: [[], [1, 2]]
    expected: []
  - input: [[1], [2]]
    expected: [[1, 2]]
  - input: [[1, 2], []]
    expected: []
tests_versteckt:
  - input: [["a", "b"], ["x", "y", "z"]]
    expected: [["a", "x"], ["a", "y"], ["a", "z"], ["b", "x"], ["b", "y"], ["b", "z"]]
  - input: [[1, 2, 3], [4]]
    expected: [[1, 4], [2, 4], [3, 4]]
  - input: [[1, 1], [2, 2]]
    expected: [[1, 2], [1, 2], [1, 2], [1, 2]]
  - input: [[0], [0]]
    expected: [[0, 0]]
  - input: [[1, 2, 3], [4, 5, 6]]
    expected: [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]
starter_code: |
  def kartesisch(a: list, b: list) -> list[list]:
      # Deine Lösung hier -- alle Paare als List-of-Lists
      pass
---

# Kartesisches Produkt zweier Listen

Schreibe eine Funktion `kartesisch(a, b)`, die alle Paare `[a_i, b_j]`
liefert -- die **Mengentheoretische Produktmenge** $A \times B$.

Reihenfolge: erst Element aus `a` fest wählen, dann alle `b`
durchgehen.

## Beispiele

| `a`         | `b`         | Produkt                                   |
|-------------|-------------|-------------------------------------------|
| `[1, 2]`    | `[3, 4]`    | `[[1,3], [1,4], [2,3], [2,4]]`            |
| `[]`        | `[1, 2]`    | `[]`                                      |
| `[1]`       | `[2]`       | `[[1, 2]]`                                |
| `["a","b"]` | `["x","y"]` | `[["a","x"], ["a","y"], ["b","x"], ["b","y"]]` |

## Idee -- Listen-Comprehension

Die zwei Schleifen werden in einer Comprehension verschachtelt -- die
**erste** ist die aeussere, die **zweite** die innere.

## Pythons `itertools.product`

`itertools.product(a, b)` liefert dasselbe als Tupel-Generator und ist
für mehr als zwei Argumente sehr handlich:

## Hintergrund

Das kartesische Produkt ist die Grundlage für **SQL-Joins**
(Cross Join), **Konfigurations-Matrix-Tests** ("alle Kombinationen
Browser × OS × Sprache") und **Dimensions-Aufbau** in
Data-Warehouse-Modellen.
