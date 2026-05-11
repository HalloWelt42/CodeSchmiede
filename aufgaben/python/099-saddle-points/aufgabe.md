---
schema_version: 1
id: 099-saddle-points
revision: 1
titel: Sattel-Punkte einer Matrix
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [matrix, listen, max-min]
pfade: [python_logik]
voraussetzungen: [063-spalten-summe]
quelle:
  url: null
  notiz: Inspiration aus Exercism (saddle-points), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: sattel_punkte
hints:
  - kosten: 0
    text: |
      Ein Sattel-Punkt ist ein Element, das **maximal in seiner Zeile**
      UND **minimal in seiner Spalte** ist.
      Liefere die Liste der Koordinaten (zeile, spalte), 0-basiert,
      sortiert nach Zeile dann Spalte.
  - kosten: 15
    text: |
      Vorab pro Zeile das Maximum, pro Spalte das Minimum berechnen.
      Dann doppelte Schleife: wenn Element == zeilen_max[i] UND
      element == spalten_min[j], dann Sattel.
tests_sichtbar:
  - input: [[[9, 8, 7], [5, 3, 2], [6, 6, 7]]]
    expected: [[1, 0]]
  - input: [[[4, 5, 4], [3, 5, 5], [1, 5, 4]]]
    expected: [[0, 1], [1, 1], [2, 1]]
  - input: [[[1]]]
    expected: [[0, 0]]
  - input: [[[1, 2, 3], [3, 1, 2], [2, 3, 1]]]
    expected: []
tests_versteckt:
  - input: [[]]
    expected: []
  - input: [[[2, 1, 4, 5, 3], [3, 5, 1, 2, 4], [1, 2, 5, 3, 4], [5, 4, 2, 1, 3], [4, 3, 5, 4, 2]]]
    expected: []
  - input: [[[5, 5, 5], [5, 5, 5], [5, 5, 5]]]
    expected: [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
  - input: [[[8, 7, 9], [6, 7, 6], [3, 2, 5]]]
    expected: [[2, 2]]
starter_code: |
  def sattel_punkte(matrix: list[list[int]]) -> list[list[int]]:
      # Deine Lösung hier -- (zeile, spalte) wo Element max in Zeile UND
      # min in Spalte ist. 0-basiert, sortiert.
      pass
---

# Sattel-Punkte einer Matrix

Schreibe eine Funktion `sattel_punkte(matrix)`, die alle
**Sattel-Punkte** zurückgibt: Positionen, an denen ein Element

- **maximal in seiner Zeile** und gleichzeitig
- **minimal in seiner Spalte** ist.

Rückgabe: Liste von `[zeile, spalte]`-Paaren (0-basiert), sortiert
nach Zeile dann Spalte.

## Beispiel

```
9 8 7
5 3 2
6 6 7
```

`5` ist max in Zeile 1 (5 > 3 > 2) und min in Spalte 0 (5 vs 9, 6).
**Sattel-Punkt bei `(1, 0)`**.

## Komplexitaet

Naive Lösung: pro Element zwei Schleifen → $O(n \cdot m \cdot (n+m))$.
Smart: zuerst pro Zeile das Maximum, pro Spalte das Minimum berechnen,
dann pro Element vergleichen → $O(n \cdot m)$.

## Hintergrund

In der Spieltheorie ist ein Sattel-Punkt eine **gemischte Strategie**,
die für beide Spieler optimal ist (Min-Max-Theorem). In diesem
Programmier-Sinne hier ist es nur eine geometrische Eigenschaft.
