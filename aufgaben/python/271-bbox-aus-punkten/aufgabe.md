---
schema_version: 1
id: 271-bbox-aus-punkten
revision: 1
titel: Bounding-Box um Punkte
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [geometrie, listen, min, max]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Geo-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: bbox
hints:
  - kosten: 0
    text: |
      Liefere [xmin, ymin, xmax, ymax] -- die kleinste achsen-
      parallele Box, die alle Punkte enthält.
      Punkte sind [[x1, y1], [x2, y2], ...]. Bei [] → [0, 0, 0, 0].
  - kosten: 10
    text: |
      xs = [p[0] for p in punkte]; ys = [p[1] for p in punkte].
      [min(xs), min(ys), max(xs), max(ys)].
tests_sichtbar:
  - input: [[[0, 0], [10, 10]]]
    expected: [0, 0, 10, 10]
  - input: [[]]
    expected: [0, 0, 0, 0]
  - input: [[[5, 5]]]
    expected: [5, 5, 5, 5]
  - input: [[[1, 2], [3, 4], [-1, 5]]]
    expected: [-1, 2, 3, 5]
tests_versteckt:
  - input: [[[0, 0], [0, 0], [0, 0]]]
    expected: [0, 0, 0, 0]
  - input: [[[10, 20], [-5, 30], [50, -10]]]
    expected: [-5, -10, 50, 30]
  - input: [[[1, 1], [2, 2], [3, 3], [4, 4]]]
    expected: [1, 1, 4, 4]
  - input: [[[0, 100], [100, 0]]]
    expected: [0, 0, 100, 100]
  - input: [[[-1, -1], [-2, -2], [-3, -3]]]
    expected: [-3, -3, -1, -1]
starter_code: |
  def bbox(punkte: list[list]) -> list:
      # Deine Lösung hier -- [xmin, ymin, xmax, ymax]
      pass
---

# Bounding-Box um Punkte

Schreibe `bbox(punkte)`, die die **kleinste achsen-parallele Box**
liefert, die alle Punkte enthält -- als `[xmin, ymin, xmax, ymax]`.

Bei leerer Liste → `[0, 0, 0, 0]`.

## Beispiele

| Punkte                           | BBox                  |
|----------------------------------|-----------------------|
| `[[0, 0], [10, 10]]`             | `[0, 0, 10, 10]`      |
| `[[5, 5]]`                       | `[5, 5, 5, 5]`        |
| `[[1, 2], [3, 4], [-1, 5]]`      | `[-1, 2, 3, 5]`       |
| `[[10, 20], [-5, 30], [50, -10]]`| `[-5, -10, 50, 30]`   |
| `[]`                             | `[0, 0, 0, 0]`        |

## Idee

Vier `min`/`max`-Aufrufe -- konzeptuell vier Schleifen, real durch
Pythons C-Implementierung sehr schnell.

## Effizientere Variante (eine Schleife)

Für extrem große Listen schneller -- vier Builtins durch eine
Schleife ersetzt.

## Anwendung

- **Karten-Apps**: "Welcher Bereich enthält alle Pins?"
- **Bildverarbeitung**: kleinster Rahmen um detektierte Objekte.
- **Spatial Indexing**: R-Tree, Quadtree benutzen BBoxes als Filter.
