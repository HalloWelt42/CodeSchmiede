---
schema_version: 1
id: 202-dreieckszahl
revision: 1
titel: n-te Dreieckszahl
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [mathematik, zahlen, formel]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Mathe-Folge
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: dreieckszahl
hints:
  - kosten: 0
    text: |
      Liefere die n-te Dreieckszahl: T(n) = 1 + 2 + 3 + ... + n.
      n = 0 → 0. n < 0 → 0.
      T(1)=1, T(2)=3, T(3)=6, T(4)=10, T(5)=15, ...
  - kosten: 4
    text: |
      Direkte Formel (Gauss): T(n) = n * (n + 1) // 2.
tests_sichtbar:
  - input: [0]
    expected: 0
  - input: [1]
    expected: 1
  - input: [5]
    expected: 15
  - input: [10]
    expected: 55
tests_versteckt:
  - input: [-3]
    expected: 0
  - input: [2]
    expected: 3
  - input: [3]
    expected: 6
  - input: [4]
    expected: 10
  - input: [100]
    expected: 5050
  - input: [1000]
    expected: 500500
  - input: [50]
    expected: 1275
starter_code: |
  def dreieckszahl(n: int) -> int:
      # Deine Lösung hier -- Gauss-Formel
      pass
---

# n-te Dreieckszahl

Die **n-te Dreieckszahl** ist die Summe der ersten `n` natuerlichen
Zahlen:

$$T(n) = 1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}$$

Geometrisch entstehen sie aus aufeinandergeschichteten Reihen:

```
T(1) = 1     *
T(2) = 3     *
             * *
T(3) = 6     *
             * *
             * * *
T(4) = 10    *
             * *
             * * *
             * * * *
```

Schreibe `dreieckszahl(n)`. Bei `n <= 0` → `0`.

## Beispiele

| `n`    | `T(n)`   |
|--------|----------|
| `0`    | `0`      |
| `1`    | `1`      |
| `2`    | `3`      |
| `5`    | `15`     |
| `10`   | `55`     |
| `100`  | `5050`   |
| `1000` | `500500` |

## Idee -- Gauss-Formel

`O(1)` und exakt -- kein Float-Trick nötig.

## Anekdote -- Der kleine Gauss

Sein Lehrer wollte ihn beschaeftigen: "Addiere die Zahlen 1 bis 100."
Der neunjaehrige Carl-Friedrich Gauss **paarte 1+100, 2+99, ...** und
hatte sofort `50 * 101 = 5050`. So entstand die Formel zumindest
in der Anekdote -- in Wirklichkeit kannte sie schon Pythagoras.

## Verwandt

- **n-te Quadratzahl**: $n^2$ (siehe Aufgabe **201**)
- **n-te Pentagonzahl**: $\frac{n(3n-1)}{2}$
- Allgemein: **figurale Zahlen** als Polygon-Summen.
