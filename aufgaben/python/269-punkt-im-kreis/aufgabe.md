---
schema_version: 1
id: 269-punkt-im-kreis
revision: 1
titel: Punkt im Kreis?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [mathematik, geometrie, distanz]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Hit-Test-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: im_kreis
hints:
  - kosten: 0
    text: |
      Pruefe ob Punkt [x, y] im Kreis liegt -- Mittelpunkt [cx, cy],
      Radius r. Inklusiv: Punkt AUF dem Kreis zaehlt als drinnen.
      Distanz zum Mittelpunkt <= r.
  - kosten: 10
    text: |
      (x - cx)^2 + (y - cy)^2 <= r^2 -- ohne sqrt schneller!
tests_sichtbar:
  - input: [[0, 0], [0, 0], 5]
    expected: true
  - input: [[3, 4], [0, 0], 5]
    expected: true
  - input: [[3, 5], [0, 0], 5]
    expected: false
  - input: [[10, 10], [0, 0], 5]
    expected: false
tests_versteckt:
  - input: [[5, 0], [0, 0], 5]
    expected: true
  - input: [[0, 5], [0, 0], 5]
    expected: true
  - input: [[6, 0], [0, 0], 5]
    expected: false
  - input: [[1, 1], [1, 1], 0]
    expected: true
  - input: [[2, 1], [1, 1], 0]
    expected: false
  - input: [[-3, -4], [0, 0], 5]
    expected: true
  - input: [[5, 5], [3, 3], 3]
    expected: true
starter_code: |
  def im_kreis(punkt: list, mittelpunkt: list, r: float) -> bool:
      # Deine Lösung hier -- inklusiv (auf Rand = drinnen)
      pass
---

# Punkt im Kreis?

Schreibe `im_kreis(punkt, mittelpunkt, r)`, die `True` zurueckgibt,
wenn `punkt` innerhalb (oder auf dem Rand) eines Kreises liegt.

Punkt = `[x, y]`, Mittelpunkt = `[cx, cy]`, Radius = `r`.

## Beispiele

| Punkt    | Mittelpunkt | r | Drinnen? |
|----------|-------------|---|----------|
| `[0, 0]` | `[0, 0]`    | 5 | `True`   |
| `[3, 4]` | `[0, 0]`    | 5 | `True` (auf Rand: 3²+4²=25=5²) |
| `[5, 0]` | `[0, 0]`    | 5 | `True` (auf Rand) |
| `[6, 0]` | `[0, 0]`    | 5 | `False`  |
| `[3, 5]` | `[0, 0]`    | 5 | `False` (3²+5²=34>25) |
| `[1, 1]` | `[1, 1]`    | 0 | `True` (Punkt-Kreis) |

## Idee -- ohne sqrt!

```python
def im_kreis(punkt, mittelpunkt, r):
    dx = punkt[0] - mittelpunkt[0]
    dy = punkt[1] - mittelpunkt[1]
    return dx * dx + dy * dy <= r * r
```

**Wichtig**: Wir vergleichen **Distanz²** mit **Radius²**, nicht
Distanz mit Radius. Das spart die teure `sqrt`-Berechnung und
vermeidet Float-Praezisionsprobleme.

## Vergleich -- mit sqrt

```python
import math

def im_kreis(punkt, mittelpunkt, r):
    return math.hypot(
        punkt[0] - mittelpunkt[0],
        punkt[1] - mittelpunkt[1]
    ) <= r
```

Funktioniert auch, aber langsamer und numerisch leicht schlechter.

## Anwendung

- **Spiele**: Reichweiten-Skill ("Wer steht im Wirkungsradius?").
- **Geo-Apps**: "Cafes in 500m Umkreis" (vereinfacht eben).
- **Cluster-Analyse**: Naechste-Nachbarn-Suche.
