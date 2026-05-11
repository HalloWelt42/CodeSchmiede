---
schema_version: 1
id: 025-set-schnitt
revision: 1
titel: Schnittmenge zweier Listen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [listen, sets, schleifen]
pfade: [python_sets]
voraussetzungen: []
quelle:
  url: null
  notiz: Standard-Set-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: schnittmenge
hints:
  - kosten: 0
    text: |
      Die Schnittmenge enthält nur Elemente, die in beiden Listen
      vorkommen. Reihenfolge: nach Position in `a`. Doppelte vermeiden.
  - kosten: 7
    text: |
      Mit Sets:

      ```
      gemeinsam = set(a) & set(b)
      return [x for x in a if x in gemeinsam]
      ```

      Aber pass auf Doppelte in `a` auf -- jedes Element nur einmal
      ins Ergebnis aufnehmen.
tests_sichtbar:
  - input: [[1, 2, 3, 4], [3, 4, 5, 6]]
    expected: [3, 4]
  - input: [[], [1, 2]]
    expected: []
  - input: [[1, 1, 2, 2], [2]]
    expected: [2]
  - input: [["a", "b", "c"], ["c", "d", "e"]]
    expected: ["c"]
tests_versteckt:
  - input: [[1, 2, 3], [4, 5, 6]]
    expected: []
  - input: [[1, 2, 3, 4, 5], [3, 1, 4]]
    expected: [1, 3, 4]
  - input: [[1, 2, 2, 3, 3, 3], [3, 2]]
    expected: [2, 3]
starter_code: |
  def schnittmenge(a: list, b: list) -> list:
      # Deine Lösung hier -- Reihenfolge nach a, ohne Doppelte.
      pass
---

# Schnittmenge zweier Listen

Schreibe eine Funktion `schnittmenge(a, b)`, die alle Elemente
zurückgibt, die in **beiden Listen** vorkommen.

Reihenfolge: nach erstem Auftreten in `a`. Jedes Element kommt im
Ergebnis nur **einmal** vor.

## Beispiele

| `a`             | `b`             | Ergebnis  |
|-----------------|-----------------|-----------|
| `[1,2,3,4]`     | `[3,4,5,6]`     | `[3,4]`   |
| `[]`            | `[1,2]`         | `[]`      |
| `[1,1,2,2]`     | `[2]`           | `[2]`     |
| `["a","b","c"]` | `["c","d","e"]` | `["c"]`   |

## Idee

Sets sind hier dein Freund: `set(b)` macht den `in`-Test sehr schnell.
Über `a` iterieren, jedes Element prüfen, ob es in `set(b)` ist und
noch nicht im Ergebnis steht.

## Hintergrund

In Python ist `x in set` ein O(1)-Test (Hash-Lookup), während `x in
list` linear in der Listenlaenge ist. Bei großen Datenmengen macht
diese Wahl einen riesigen Unterschied.
