---
schema_version: 1
id: 267-distanz-punkte
revision: 1
titel: Distanz zwischen zwei Punkten
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [mathematik, geometrie, sqrt, pythagoras]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Geometrie
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: distanz
hints:
  - kosten: 0
    text: |
      Berechne die euklidische Distanz zwischen zwei 2D-Punkten.
      Punkte sind Listen [x, y]. Auf 4 Nachkommastellen runden.
      Pythagoras: sqrt((x2-x1)^2 + (y2-y1)^2).
  - kosten: 10
    text: |
      math.hypot(x2 - x1, y2 - y1) ist die kürzeste Form.
tests_sichtbar:
  - input: [[0, 0], [3, 4]]
    expected: 5.0
  - input: [[1, 1], [1, 1]]
    expected: 0.0
  - input: [[0, 0], [1, 0]]
    expected: 1.0
  - input: [[0, 0], [1, 1]]
    expected: 1.4142
tests_versteckt:
  - input: [[5, 12], [0, 0]]
    expected: 13.0
  - input: [[-3, -4], [0, 0]]
    expected: 5.0
  - input: [[1, 1], [4, 5]]
    expected: 5.0
  - input: [[0, 0], [-3, -4]]
    expected: 5.0
  - input: [[10, 10], [10, 20]]
    expected: 10.0
  - input: [[1.5, 2.5], [4.5, 6.5]]
    expected: 5.0
starter_code: |
  import math

  def distanz(p1: list, p2: list) -> float:
      # Deine Lösung hier -- 4 Nachkommastellen
      pass
---

# Distanz zwischen zwei Punkten

Schreibe `distanz(p1, p2)`, die die **euklidische Distanz** zwischen
zwei 2D-Punkten berechnet. Punkte sind Listen `[x, y]`. Liefere auf
**4 Nachkommastellen** gerundet.

## Formel (Pythagoras in 2D)

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

## Beispiele

| `p1`         | `p2`         | Distanz   |
|--------------|--------------|-----------|
| `[0, 0]`     | `[3, 4]`     | `5.0`     |
| `[5, 12]`    | `[0, 0]`     | `13.0`    |
| `[1, 1]`     | `[1, 1]`     | `0.0`     |
| `[0, 0]`     | `[1, 1]`     | `1.4142`  |
| `[1.5, 2.5]` | `[4.5, 6.5]` | `5.0`     |

Klassische **3-4-5** und **5-12-13** Tripel ergeben ganze Zahlen.

## Idee

```python
import math

def distanz(p1, p2):
    return round(math.hypot(p2[0] - p1[0], p2[1] - p1[1]), 4)
```

`math.hypot(a, b)` ist genau `sqrt(a*a + b*b)` -- mit **besserer
numerischer Stabilitaet** bei extremen Werten (vermeidet Overflow
durch Vor-Skalierung).

## Erweiterung -- N Dimensionen

Für 3D oder beliebig:

```python
def distanz(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
```

Seit Python 3.8 kann `math.dist(p1, p2)` das direkt für beliebige
Dimensionen.

## Anwendung

- **Karten-Apps**: Luftlinie zwischen zwei Koordinaten (genauer:
  Haversine für Erd-Krummung).
- **Spiele**: Reichweiten-Prüfung, Kollisions-Erkennung.
- **Maschinenlernen**: k-Nearest-Neighbors.
