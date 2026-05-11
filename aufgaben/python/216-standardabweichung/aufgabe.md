---
schema_version: 1
id: 216-standardabweichung
revision: 1
titel: Standardabweichung (Population)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 28
schaetz_minuten: 12
tags: [statistik, mathematik, listen, sqrt]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Statistik-Formel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: stdabw
hints:
  - kosten: 0
    text: |
      Berechne die POPULATIONS-Standardabweichung sigma:
      mittel = sum / n
      varianz = sum((x - mittel)^2) / n
      sigma = sqrt(varianz)
      Auf 4 Nachkommastellen gerundet.
      Bei leerer oder 1-elementiger Liste → 0.0.
  - kosten: 15
    text: |
      Mittelwert vorab berechnen, dann Quadrat-Summe, dann sqrt.
      Achtung: Wir nehmen die POPULATION-Variante (durch n, nicht n-1).
tests_sichtbar:
  - input: [[2, 4, 4, 4, 5, 5, 7, 9]]
    expected: 2.0
  - input: [[]]
    expected: 0.0
  - input: [[5]]
    expected: 0.0
  - input: [[1, 1, 1, 1]]
    expected: 0.0
tests_versteckt:
  - input: [[1, 2, 3, 4, 5]]
    expected: 1.4142
  - input: [[10, 10, 10, 10, 10]]
    expected: 0.0
  - input: [[1, 5, 9]]
    expected: 3.266
  - input: [[100, 200, 300]]
    expected: 81.6497
  - input: [[-2, 0, 2]]
    expected: 1.633
  - input: [[7, 8, 9, 10, 11, 12, 13]]
    expected: 2.0
starter_code: |
  import math

  def stdabw(zahlen: list[float]) -> float:
      # Deine Lösung hier -- Population (durch n), 4 Nachkommastellen
      pass
---

# Standardabweichung (Population)

Schreibe `stdabw(zahlen)`, die die **Standardabweichung** berechnet
-- als Mass fuer die Streuung um den Mittelwert. Wir nehmen die
**Populations**-Variante (Division durch `n`), nicht die
**Stichproben**-Variante (durch `n-1`).

Auf **4 Nachkommastellen** gerundet. Bei leerer oder 1-elementiger
Liste → `0.0` (Streuung nicht definiert).

## Formel

$$\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2}$$

mit $\bar{x}$ = Mittelwert.

## Beispiele

| Zahlen                       | Sigma     | Bemerkung           |
|------------------------------|-----------|----------------------|
| `[2, 4, 4, 4, 5, 5, 7, 9]`   | `2.0`     | Lehrbuch-Klassiker   |
| `[10, 10, 10, 10, 10]`       | `0.0`     | keine Streuung       |
| `[1, 5, 9]`                  | `3.266`   | grosse Streuung      |
| `[100, 200, 300]`            | `81.6497` | linear verteilt      |
| `[-2, 0, 2]`                 | `1.633`   | symmetrisch um 0     |

## Idee

```python
import math

def stdabw(zahlen):
    n = len(zahlen)
    if n < 2:
        return 0.0
    mittel = sum(zahlen) / n
    varianz = sum((x - mittel) ** 2 for x in zahlen) / n
    return round(math.sqrt(varianz), 4)
```

## Population vs. Stichprobe

| Variante      | Divisor | Wann?                           |
|---------------|---------|----------------------------------|
| Population    | `n`     | Komplette Grundgesamtheit       |
| Stichprobe    | `n-1`   | Schaetzung aus Sample (Bessel)  |

Pythons `statistics.stdev` ist die Stichproben-Variante,
`statistics.pstdev` die Populations-Variante.

## Hintergrund

Die Standardabweichung ist DAS Streuungsmass schlechthin. In der
**Glockenkurve** (Normalverteilung) liegen 68 % der Werte innerhalb
von ±σ, 95 % innerhalb ±2σ und 99,7 % innerhalb ±3σ -- die
**68-95-99-Regel**.
