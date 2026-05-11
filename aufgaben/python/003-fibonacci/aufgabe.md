---
schema_version: 1
id: 003-fibonacci
revision: 1
titel: Fibonacci-Zahl
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 35
schaetz_minuten: 20
tags: [rekursion, iteration, memoisierung, performance]
pfade: [python_grundlagen]
voraussetzungen: [001-fizzbuzz]
quelle:
  url: https://de.wikipedia.org/wiki/Fibonacci-Folge
  notiz: Klassiker für Performance-Vergleiche, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: fibonacci
hints:
  - kosten: 0
    text: Die Fibonacci-Folge beginnt mit 0, 1, jede weitere Zahl ist die Summe der beiden vorigen.
  - kosten: 15
    text: Eine rekursive Loesung ist kurz, wird aber fuer grosse n sehr langsam (exponentielle Laufzeit). Iterativ ist linear.
  - kosten: 30
    text: |
      Iterative Variante:

      ```
      a, b = 0, 1
      for _ in range(n):
          a, b = b, a + b
      return a
      ```
tests_sichtbar:
  - input: [0]
    expected: 0
  - input: [1]
    expected: 1
  - input: [2]
    expected: 1
  - input: [10]
    expected: 55
tests_versteckt:
  - input: [3]
    expected: 2
  - input: [5]
    expected: 5
  - input: [15]
    expected: 610
  - input: [20]
    expected: 6765
  - input: [30]
    expected: 832040
starter_code: |
  def fibonacci(n: int) -> int:
      # Deine Loesung hier
      pass
---

# Fibonacci-Zahl

Schreibe eine Funktion `fibonacci(n)`, die die `n`-te Zahl der
**Fibonacci-Folge** zurückgibt.

## Definition

$$F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2} \text{ für } n \ge 2$$

## Beispiele

| n  | F(n) |
|---:|-----:|
|  0 |    0 |
|  1 |    1 |
|  2 |    1 |
|  3 |    2 |
|  5 |    5 |
| 10 |   55 |

## Worauf zu achten ist

- Eine **rekursive** Lösung ist sehr kurz, hat aber **exponentielle Laufzeit**
  -- bei `n = 30` werden bereits über 1,3 Mio. Funktionsaufrufe ausgefuehrt
- Eine **iterative** Lösung laeuft in **linearer Zeit** $O(n)$ und
  konstantem Speicher
- Mit `functools.lru_cache` lassen sich rekursive Aufrufe **memoisieren**
  und damit ebenfalls auf $O(n)$ drücken

## Vergleich der Ansätze

```mermaid
flowchart TD
    A[fibonacci 5] --> B[fibonacci 4]
    A --> C[fibonacci 3]
    B --> D[fibonacci 3]
    B --> E[fibonacci 2]
    C --> F[fibonacci 2]
    C --> G[fibonacci 1]
    D --> H[...]
    D --> I[...]
```

Die naive Rekursion berechnet `fibonacci(3)` und `fibonacci(2)` mehrfach.
Memoisierung speichert Ergebnisse und vermeidet Doppelarbeit.
