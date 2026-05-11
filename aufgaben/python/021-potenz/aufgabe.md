---
schema_version: 1
id: 021-potenz
revision: 1
titel: Eigene Potenzfunktion
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [zahlen, schleifen, rekursion]
pfade: [python_mathe]
voraussetzungen: [017-fakultät]
quelle:
  url: null
  notiz: Klassische Reimplementierung von ** als Lernübung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: potenz
hints:
  - kosten: 0
    text: |
      Per Definition: `basis^0 = 1`. Sonst Schleife: `ergebnis = 1`,
      dann `n` mal mit `basis` multiplizieren.
  - kosten: 15
    text: |
      Schöner mit `range(n)`:

      ```
      ergebnis = 1
      for _ in range(n):
          ergebnis *= basis
      ```
tests_sichtbar:
  - input: [2, 10]
    expected: 1024
  - input: [5, 0]
    expected: 1
  - input: [3, 4]
    expected: 81
  - input: [1, 100]
    expected: 1
tests_versteckt:
  - input: [10, 5]
    expected: 100000
  - input: [7, 3]
    expected: 343
  - input: [0, 5]
    expected: 0
  - input: [2, 20]
    expected: 1048576
  - input: [-2, 3]
    expected: -8
starter_code: |
  def potenz(basis: int, exponent: int) -> int:
      # Deine Lösung hier -- ohne ** und ohne pow()
      pass
---

# Eigene Potenzfunktion

Schreibe eine Funktion `potenz(basis, exponent)`, die `basis` hoch
`exponent` zurückgibt -- ohne `**` und ohne `pow()` zu verwenden.
Der Exponent ist immer eine nicht-negative ganze Zahl.

## Beispiele

| `basis` | `exponent` | `potenz`  |
|---------|------------|-----------|
| `2`     | `10`       | `1024`    |
| `5`     | `0`        | `1`       |
| `3`     | `4`        | `81`      |
| `-2`    | `3`        | `-8`      |

## Idee

Per Definition ist $b^0 = 1$. Für $n > 0$ gilt $b^n = b \cdot b^{n-1}$.
Daraus laesst sich sowohl eine **Schleife** als auch eine **rekursive**
Lösung bauen.

## Wofür ist das gut?

Reimplementierungen von Standardfunktionen sind eine schöne
Lernübung -- man lernt, was die Sprache eigentlich für einen
erledigt. Später (in einer separaten Aufgabe) kann man das gleiche
Problem mit **schneller Exponentiation** in $O(\log n)$ statt $O(n)$
lösen.
