---
schema_version: 1
id: 273-polyline-laenge
revision: 1
titel: Gesamtlaenge eines Polygonzugs
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [geometrie, listen, distanz, schleifen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Polyline-Berechnung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: polyline
hints:
  - kosten: 0
    text: |
      Summe der euklidischen Distanzen zwischen aufeinander folgenden
      Punkten. Bei < 2 Punkten → 0.0.
      Auf 4 Nachkommastellen.
  - kosten: 15
    text: |
      sum(math.hypot(p2[0]-p1[0], p2[1]-p1[1])
          for p1, p2 in zip(punkte, punkte[1:]))
tests_sichtbar:
  - input: [[[0, 0], [3, 4]]]
    expected: 5.0
  - input: [[]]
    expected: 0.0
  - input: [[[5, 5]]]
    expected: 0.0
  - input: [[[0, 0], [3, 4], [3, 0]]]
    expected: 9.0
tests_versteckt:
  - input: [[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]]
    expected: 4.0
  - input: [[[0, 0], [10, 0]]]
    expected: 10.0
  - input: [[[0, 0], [3, 4], [6, 8]]]
    expected: 10.0
  - input: [[[1, 1], [1, 1]]]
    expected: 0.0
  - input: [[[0, 0], [1, 1], [2, 0], [3, 1]]]
    expected: 4.2426
  - input: [[[0, 0], [0, 5], [5, 5], [5, 0], [0, 0]]]
    expected: 20.0
starter_code: |
  import math

  def polyline(punkte: list[list]) -> float:
      # Deine Lösung hier -- 4 Nachkommastellen
      pass
---

# Gesamtlaenge eines Polygonzugs

Schreibe `polyline(punkte)`, die die **Gesamtlaenge** eines
Polygonzugs (Folge von Punkten) berechnet -- als Summe der
**Distanzen** zwischen aufeinanderfolgenden Punkten.

Bei < 2 Punkten → `0.0`. Auf 4 Nachkommastellen.

## Beispiele

| Punkte                          | Laenge | Bemerkung           |
|---------------------------------|--------|---------------------|
| `[[0, 0], [3, 4]]`              | `5.0`  | eine Strecke (3-4-5)|
| `[[0, 0], [3, 4], [3, 0]]`      | `9.0`  | 5 + 4               |
| `[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]` | `4.0` | Quadrat-Umfang |
| `[[0, 0], [3, 4], [6, 8]]`      | `10.0` | 5 + 5 (linear)      |
| `[]`                            | `0.0`  |                     |
| `[[5, 5]]`                      | `0.0`  | Einzelpunkt         |

## Idee

`zip(punkte, punkte[1:])` paart **aufeinanderfolgende** Punkte --
ein Pattern, das wir auch in **230-ist-aufsteigend** und
**240-wechsel-zählen** nutzen.

## Geschlossene Polygone

Wenn der erste und letzte Punkt **gleich** sind, ist es ein
geschlossenes Polygon (z.B. das Quadrat im Beispiel oben). Die
Laenge ist dann der **Umfang**.

## Anwendung

- **Karten-Apps**: Routenlaenge zwischen Stationen.
- **Geometrie**: Polygon-Umfang.
- **Spiele**: Patrol-Path-Laenge für NPCs.
- **3D-Grafik**: Spline-Approximation, Kanten-Laengen-Berechnung.
