---
schema_version: 1
id: 268-punkt-im-rechteck
revision: 1
titel: Punkt im Rechteck?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [mathematik, geometrie, vergleich]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Hit-Test-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: im_rechteck
hints:
  - kosten: 0
    text: |
      Prüfe ob Punkt [x, y] im achsen-parallelen Rechteck liegt,
      definiert durch [xmin, ymin, xmax, ymax].
      Inklusiv: Punkte AUF dem Rand zählen als drinnen.
  - kosten: 5
    text: |
      xmin <= x <= xmax und ymin <= y <= ymax.
tests_sichtbar:
  - input: [[5, 5], [0, 0, 10, 10]]
    expected: true
  - input: [[15, 5], [0, 0, 10, 10]]
    expected: false
  - input: [[0, 0], [0, 0, 10, 10]]
    expected: true
  - input: [[10, 10], [0, 0, 10, 10]]
    expected: true
tests_versteckt:
  - input: [[-1, 5], [0, 0, 10, 10]]
    expected: false
  - input: [[5, -1], [0, 0, 10, 10]]
    expected: false
  - input: [[5, 11], [0, 0, 10, 10]]
    expected: false
  - input: [[5, 0], [0, 0, 10, 10]]
    expected: true
  - input: [[0, 5], [0, 0, 10, 10]]
    expected: true
  - input: [[100, 100], [-50, -50, 50, 50]]
    expected: false
  - input: [[0, 0], [-50, -50, 50, 50]]
    expected: true
starter_code: |
  def im_rechteck(punkt: list, rect: list) -> bool:
      # Deine Lösung hier -- inklusiver Rand
      pass
---

# Punkt im Rechteck?

Schreibe `im_rechteck(punkt, rect)`, die `True` zurückgibt, wenn
der Punkt `[x, y]` innerhalb des achsen-parallelen Rechtecks liegt.
Rechteck = `[xmin, ymin, xmax, ymax]`. **Inklusive Raender**.

## Beispiele

| Punkt    | Rechteck           | Drinnen? |
|----------|---------------------|----------|
| `[5, 5]` | `[0, 0, 10, 10]`    | `True`   |
| `[15, 5]`| `[0, 0, 10, 10]`    | `False`  |
| `[0, 0]` | `[0, 0, 10, 10]`    | `True` (Rand) |
| `[10, 10]`| `[0, 0, 10, 10]`   | `True` (Rand) |
| `[5, -1]`| `[0, 0, 10, 10]`    | `False`  |

## Idee

```python
def im_rechteck(punkt, rect):
    x, y = punkt
    xmin, ymin, xmax, ymax = rect
    return xmin <= x <= xmax and ymin <= y <= ymax
```

Pythons **chained comparisons** machen das sehr lesbar.

## Variante -- exklusive Raender

Wenn Punkte **auf** dem Rand nicht zählen sollen: `<` statt `<=`.

```python
return xmin < x < xmax and ymin < y < ymax
```

## Anwendung

- **Hit-Tests** in UIs (Click in Button?).
- **Kollisions-Erkennung** in 2D-Spielen (AABB-Tests).
- **Geo-Filter** auf Karten ("Welche Cafes liegen im Sichtbereich?").
