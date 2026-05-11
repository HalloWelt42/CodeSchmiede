---
schema_version: 1
id: 225-produkt-elemente
revision: 1
titel: Produkt aller Listen-Elemente
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [listen, mathematik, reduce, math]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu sum
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: produkt
hints:
  - kosten: 0
    text: |
      Multipliziere alle Zahlen in der Liste miteinander.
      Bei leerer Liste → 1 (neutrales Element der Multiplikation).
  - kosten: 4
    text: |
      math.prod(liste) macht es in einem Aufruf.
      Alternativ: functools.reduce(operator.mul, liste, 1).
tests_sichtbar:
  - input: [[1, 2, 3, 4]]
    expected: 24
  - input: [[]]
    expected: 1
  - input: [[5]]
    expected: 5
  - input: [[2, 0, 3]]
    expected: 0
tests_versteckt:
  - input: [[1, 1, 1, 1]]
    expected: 1
  - input: [[10, 10]]
    expected: 100
  - input: [[-2, -3]]
    expected: 6
  - input: [[-1, 2, -3]]
    expected: 6
  - input: [[1, 2, 3, 4, 5, 6, 7]]
    expected: 5040
  - input: [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
    expected: 1024
starter_code: |
  def produkt(liste: list) -> int:
      # Deine Lösung hier -- math.prod oder reduce
      pass
---

# Produkt aller Listen-Elemente

Schreibe `produkt(liste)`, die **alle Zahlen** in der Liste
miteinander multipliziert.

Bei leerer Liste → `1` (neutrales Element der Multiplikation, wie
`sum([]) == 0`).

## Beispiele

| Liste                  | Produkt |
|------------------------|---------|
| `[1, 2, 3, 4]`         | `24`    |
| `[]`                   | `1`     |
| `[5]`                  | `5`     |
| `[2, 0, 3]`            | `0`     |
| `[-2, -3]`             | `6`     |
| `[1, 2, 3, 4, 5, 6, 7]`| `5040`  |
| `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]` | `1024` (= 2^10) |

## Idee 1 -- math.prod (seit Python 3.8)

Eine Zeile -- standardisiert, getestet, schnell.

## Idee 2 -- reduce

Allgemeineres Pattern -- `reduce` faltet jede binaere Operation
über eine Liste.

## Idee 3 -- Schleife

Klar lesbar, jede Sprache versteht das.

## Anwendung

`math.prod` braucht man für:
- Fakultaet: `math.prod(range(1, n+1))`
- Volumen einer Box: `math.prod([breite, höhe, tiefe])`
- Wahrscheinlichkeit unabhängiger Ereignisse: $P(A \cap B) = P(A) \cdot P(B)$
- Geometrisches Mittel (Aufgabe 217).
