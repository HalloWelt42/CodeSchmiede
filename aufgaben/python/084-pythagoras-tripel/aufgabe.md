---
schema_version: 1
id: 084-pythagoras-tripel
revision: 1
titel: Pythagoreisches Tripel
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [zahlen, schleifen, geometrie, project-euler]
pfade: [python_mathe2]
voraussetzungen: []
quelle:
  url: https://projecteuler.net/problem=9
  notiz: Inspiration aus Project Euler 9, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: pythagoras_tripel
hints:
  - kosten: 0
    text: |
      Suche a, b, c mit `a < b < c` und `a^2 + b^2 = c^2` und
      `a + b + c == n`.
  - kosten: 15
    text: |
      Doppelte Schleife: `for a in range(1, n//3)`, dann
      `for b in range(a+1, (n-a)//2 + 1)`. `c = n - a - b`. Prüfe
      `a*a + b*b == c*c`.
tests_sichtbar:
  - input: [12]
    expected: [[3, 4, 5]]
  - input: [60]
    expected: [[10, 24, 26], [15, 20, 25]]
  - input: [10]
    expected: []
  - input: [1000]
    expected: [[200, 375, 425]]
tests_versteckt:
  - input: [30]
    expected: [[5, 12, 13]]
  - input: [90]
    expected: [[9, 40, 41], [15, 36, 39]]
  - input: [840]
    expected: [[40, 399, 401], [56, 390, 394], [105, 360, 375], [120, 350, 370], [140, 336, 364], [168, 315, 357], [210, 280, 350], [240, 252, 348]]
  - input: [3]
    expected: []
  - input: [1]
    expected: []
starter_code: |
  def pythagoras_tripel(n: int) -> list[list[int]]:
      # Deine Lösung hier -- alle Tripel (a,b,c) mit a<b<c, a²+b²=c² und a+b+c=n.
      pass
---

# Pythagoreisches Tripel

Ein **pythagoreisches Tripel** ist ein Trio natürlicher Zahlen
$(a, b, c)$ mit $a < b < c$ und $a^2 + b^2 = c^2$.

Schreibe eine Funktion `pythagoras_tripel(n)`, die alle Tripel
zurückgibt, deren **Summe genau** $n$ ist -- aufsteigend sortiert
nach $a$.

## Beispiele

| `n`   | Ergebnis                                |
|-------|-----------------------------------------|
| `12`  | `[[3, 4, 5]]`                           |
| `30`  | `[[5, 12, 13]]`                         |
| `60`  | `[[10, 24, 26], [15, 20, 25]]`          |
| `1000`| `[[200, 375, 425]]`                     |
| `10`  | `[]`                                    |

## Hintergrund

Project Euler Problem 9: "Es gibt genau ein pythagoreisches Tripel,
für das $a + b + c = 1000$. Finde das Produkt $abc$." Die Antwort
ist $200 \cdot 375 \cdot 425 = 31\,875\,000$.
