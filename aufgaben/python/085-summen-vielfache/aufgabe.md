---
schema_version: 1
id: 085-summen-vielfache
revision: 1
titel: Summe der Vielfachen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [zahlen, schleifen, sets, project-euler]
pfade: [python_mathe2]
voraussetzungen: []
quelle:
  url: https://projecteuler.net/problem=1
  notiz: Variante von Project Euler 1, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: summe_vielfache
hints:
  - kosten: 0
    text: |
      Iteriere von 1 bis n-1. Wenn die Zahl Vielfaches von **mindestens einem**
      der Teiler ist, addiere sie. Vorsicht vor Doppelzählung!
  - kosten: 10
    text: |
      Set-Trick: `set()` aller Vielfachen, dann `sum`. Kein
      Doppelzählung-Problem mehr.
tests_sichtbar:
  - input: [10, [3, 5]]
    expected: 23
  - input: [1, [3, 5]]
    expected: 0
  - input: [4, [3]]
    expected: 3
  - input: [10, [7]]
    expected: 7
tests_versteckt:
  - input: [100, [3, 5]]
    expected: 2318
  - input: [1000, [3, 5]]
    expected: 233168
  - input: [20, [4]]
    expected: 40
  - input: [15, [3, 5]]
    expected: 45
  - input: [10000, [3, 5, 7]]
    expected: 27142139
  - input: [50, []]
    expected: 0
starter_code: |
  def summe_vielfache(n: int, teiler: list[int]) -> int:
      # Deine Lösung hier -- Summe aller Zahlen < n, die Vielfaches
      # von mindestens einem Teiler sind.
      pass
---

# Summe der Vielfachen

Schreibe eine Funktion `summe_vielfache(n, teiler)`, die die Summe
aller natürlichen Zahlen **kleiner als $n$** zurückgibt, die
Vielfaches **mindestens eines** der Teiler sind.

## Beispiele

| `n`   | `teiler` | Ergebnis | Wegen                       |
|-------|----------|----------|-----------------------------|
| `10`  | `[3, 5]` | `23`     | 3+5+6+9 = 23                |
| `100` | `[3, 5]` | `2318`   |                             |
| `1000`| `[3, 5]` | `233168` | (Project-Euler-Antwort)     |
| `4`   | `[3]`    | `3`      | nur die 3                   |
| `1`   | `[3, 5]` | `0`      | keine Zahl < 1              |

## Hintergrund

Project Euler Problem 1 fragt nach der Summe aller Vielfachen von 3
oder 5 unter 1000. Diese Aufgabe verallgemeinert das auf beliebige
Teiler-Listen.

## Vorsicht

Naive Doppelschleife zählt z.B. die 15 zweimal (für 3 und 5). Mit
einem **Set** umgehst du das elegant.
