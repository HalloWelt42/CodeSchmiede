---
schema_version: 1
id: 065-magisches-quadrat
revision: 1
titel: Magisches Quadrat pruefen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [matrix, listen, schleifen, sum]
pfade: [python_logik]
voraussetzungen: [064-diagonale-summe]
quelle:
  url: https://de.wikipedia.org/wiki/Magisches_Quadrat
  notiz: Klassische Aufgabe, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_magisch
hints:
  - kosten: 0
    text: |
      Alle Zeilen-, Spalten- und Diagonalsummen muessen gleich sein.
  - kosten: 15
    text: |
      Berechne alle Summen, sammle sie in einem Set. Wenn das Set
      genau ein Element enthaelt, ist die Matrix magisch.
tests_sichtbar:
  - input: [[[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    expected: true
  - input: [[[1, 2], [3, 4]]]
    expected: false
  - input: [[[1]]]
    expected: true
  - input: [[[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]]
    expected: true
tests_versteckt:
  - input: [[[1, 1, 1], [1, 1, 1], [1, 1, 1]]]
    expected: true
  - input: [[[2, 7, 6], [9, 5, 0], [4, 3, 8]]]
    expected: false
  - input: [[[8, 1, 6], [3, 5, 7], [4, 9, 2]]]
    expected: true
starter_code: |
  def ist_magisch(matrix: list[list[int]]) -> bool:
      # Deine Loesung hier -- alle Zeilen-, Spalten- und Diagonal-
      # summen muessen gleich sein.
      pass
---

# Magisches Quadrat pruefen

Schreibe eine Funktion `ist_magisch(matrix)`, die prueft, ob eine
quadratische Matrix ein **magisches Quadrat** ist -- also die Summen
aller Zeilen, aller Spalten und beider Diagonalen identisch sind.

## Beispiele

Lo-Shu (klassisches 3x3):

```
2 7 6
9 5 1
4 3 8
```
Alle Summen = 15. **Magisch.**

Dürer-Quadrat (4x4):

```
16  3  2 13
 5 10 11  8
 9  6  7 12
 4 15 14  1
```
Alle Summen = 34. **Magisch.**

## Idee

Berechne alle Summen, sammle sie in einem Set. Genau ein Wert =
magisch.

## Hintergrund

Magische Quadrate sind seit ca. 2000 v. Chr. bekannt -- das aelteste
Lo-Shu-Quadrat geht zurueck auf eine chinesische Legende ueber eine
Schildkroete am Lo-Fluss. Albrecht Duerer baute eines in seinen
Kupferstich "Melancolia I" ein, mit `1514` (dem Jahr der Entstehung)
in der unteren Zeile.
