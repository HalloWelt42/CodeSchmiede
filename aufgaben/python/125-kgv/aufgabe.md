---
schema_version: 1
id: 125-kgv
revision: 1
titel: Kleinstes gemeinsames Vielfaches
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [zahlen, listen, ggt, kgv]
pfade: [python_mathe2]
voraussetzungen: [124-ggt-multi]
quelle:
  url: https://de.wikipedia.org/wiki/Kleinstes_gemeinsames_Vielfaches
  notiz: Klassische Mathe-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: kgv_liste
hints:
  - kosten: 0
    text: |
      kgV von zwei Zahlen: a*b // ggt(a,b). Auch fuer Listen
      assoziativ -- reduce ueber Paare.
  - kosten: 10
    text: |
      `from math import lcm; from functools import reduce`.
      `reduce(lcm, zahlen, 1)`. Bei leerer Liste 0 als Konvention.
tests_sichtbar:
  - input: [[4, 6]]
    expected: 12
  - input: [[2, 3, 4]]
    expected: 12
  - input: [[7]]
    expected: 7
  - input: [[]]
    expected: 0
tests_versteckt:
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    expected: 2520
  - input: [[3, 5, 7]]
    expected: 105
  - input: [[6, 8, 12]]
    expected: 24
  - input: [[100]]
    expected: 100
starter_code: |
  def kgv_liste(zahlen: list[int]) -> int:
      # Deine Lösung hier -- kgV aller Zahlen, leere Liste → 0.
      pass
---

# Kleinstes gemeinsames Vielfaches

Schreibe eine Funktion `kgv_liste(zahlen)`, die das **kleinste
gemeinsame Vielfache** aller Zahlen in der Liste zurückgibt.

Leere Liste → `0`.

## Formel

Für zwei Zahlen:

$$
\text{kgV}(a, b) = \frac{a \cdot b}{\text{ggT}(a, b)}
$$

Für mehr Zahlen reduziere paarweise -- kgV ist assoziativ.

## Beispiele

| Liste                        | kgV    |
|------------------------------|--------|
| `[4, 6]`                     | `12`   |
| `[2, 3, 4]`                  | `12`   |
| `[3, 5, 7]`                  | `105`  |
| `[6, 8, 12]`                 | `24`   |
| `[1, 2, ..., 10]`            | `2520` |
| `[7]`                        | `7`    |
| `[]`                         | `0`    |

## Hintergrund

`[1..10]` mit kgV = 2520 ist eine klassische Project-Euler-Frage
(Problem 5: "kgV von 1..20" → 232792560).
