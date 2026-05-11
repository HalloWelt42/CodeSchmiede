---
schema_version: 1
id: 272-zentroid-aus-punkten
revision: 1
titel: Zentroid (Schwerpunkt) aus Punktwolke
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [geometrie, mathematik, durchschnitt]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Geometrie
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zentroid
hints:
  - kosten: 0
    text: |
      Berechne den Mittelpunkt (Schwerpunkt) einer Punktwolke:
      [Mittelwert(x), Mittelwert(y)].
      Bei leerer Liste → [0.0, 0.0].
      Auf 4 Nachkommastellen.
  - kosten: 5
    text: |
      sum(p[0] for p in punkte) / n und sum(p[1] for p in punkte) / n.
tests_sichtbar:
  - input: [[[0, 0], [10, 10]]]
    expected: [5.0, 5.0]
  - input: [[]]
    expected: [0.0, 0.0]
  - input: [[[5, 5]]]
    expected: [5.0, 5.0]
  - input: [[[0, 0], [4, 0], [4, 3]]]
    expected: [2.6667, 1.0]
tests_versteckt:
  - input: [[[1, 1], [2, 2], [3, 3]]]
    expected: [2.0, 2.0]
  - input: [[[-1, -1], [1, 1]]]
    expected: [0.0, 0.0]
  - input: [[[0, 0], [0, 0], [0, 0], [0, 0]]]
    expected: [0.0, 0.0]
  - input: [[[10, 0], [0, 10]]]
    expected: [5.0, 5.0]
  - input: [[[1, 0], [0, 1], [1, 1], [0, 0]]]
    expected: [0.5, 0.5]
  - input: [[[100, 200]]]
    expected: [100.0, 200.0]
starter_code: |
  def zentroid(punkte: list[list]) -> list[float]:
      # Deine Lösung hier -- [mean_x, mean_y], 4 Nachkommastellen
      pass
---

# Zentroid (Schwerpunkt) aus Punktwolke

Schreibe `zentroid(punkte)`, die den **Schwerpunkt** einer Punktwolke
berechnet -- den arithmetischen Mittelpunkt aller Koordinaten.

`[Mittelwert(x), Mittelwert(y)]` auf 4 Nachkommastellen.

Bei leerer Liste → `[0.0, 0.0]`.

## Beispiele

| Punkte                          | Zentroid           |
|---------------------------------|---------------------|
| `[[0, 0], [10, 10]]`            | `[5.0, 5.0]`        |
| `[[5, 5]]`                      | `[5.0, 5.0]`        |
| `[[1, 1], [2, 2], [3, 3]]`      | `[2.0, 2.0]`        |
| `[[0, 0], [4, 0], [4, 3]]`      | `[2.6667, 1.0]`     |
| `[[-1, -1], [1, 1]]`            | `[0.0, 0.0]`        |
| `[[10, 0], [0, 10]]`            | `[5.0, 5.0]`        |
| `[]`                            | `[0.0, 0.0]`        |

## Mit `zip` etwas pythonischer

`zip(*punkte)` "transponiert" die Punkte-Liste: aus `[[1,2], [3,4]]`
werden `(1, 3)` und `(2, 4)`.

## Anwendung

- **Cluster-Algorithmen** (k-Means).
- **Statistik**: Mittelpunkt einer Verteilung.
- **Computergrafik**: Mittelpunkt von Vertices für Pivot-Punkte.
- **Geo**: Stadt-Mittelpunkt aus Adress-Liste.

## Hinweis -- Polygon-Schwerpunkt

Bei einem **gefuellten Polygon** ist der Schwerpunkt nicht einfach
der Mittelwert der Eck-Punkte! Dort braucht man eine
**flaechen-gewichtete** Formel mit dem Polygon-Inhalt.
