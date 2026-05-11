---
schema_version: 1
id: 181-sudoku-zeile
revision: 1
titel: Sudoku-Zeile gültig?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [listen, set, sudoku, validierung]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Sudoku-Stück
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: sudoku_zeile
hints:
  - kosten: 0
    text: |
      Eine Zeile (Liste der Laenge 9) ist gültig, wenn jede der
      Ziffern 1-9 GENAU EINMAL vorkommt. 0/None/leere Plätze sind
      hier NICHT erlaubt -- diese Aufgabe testet nur fertige Zeilen.
  - kosten: 10
    text: |
      sorted(zeile) == [1,2,3,4,5,6,7,8,9].
      Oder: set(zeile) == {1..9} und alle Werte sind ints.
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    expected: true
  - input: [[9, 8, 7, 6, 5, 4, 3, 2, 1]]
    expected: true
  - input: [[1, 1, 2, 3, 4, 5, 6, 7, 8]]
    expected: false
  - input: [[1, 2, 3, 4, 5, 6, 7, 8]]
    expected: false
tests_versteckt:
  - input: [[2, 4, 1, 6, 3, 8, 5, 7, 9]]
    expected: true
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 0]]
    expected: false
  - input: [[]]
    expected: false
  - input: [[5, 5, 5, 5, 5, 5, 5, 5, 5]]
    expected: false
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 10]]
    expected: false
  - input: [[3, 1, 4, 1, 5, 9, 2, 6, 5]]
    expected: false
starter_code: |
  def sudoku_zeile(zeile: list[int]) -> bool:
      # Deine Lösung hier -- exakt 1..9, jede einmal
      pass
---

# Sudoku-Zeile gültig?

Eine **Sudoku-Zeile** besteht aus den Ziffern `1` bis `9`, jede
**genau einmal**. Schreibe `sudoku_zeile(zeile)`, die `True`
zurückgibt, wenn die übergebene Liste eine solche Zeile bildet.

Diese Aufgabe testet **nur vollstaendige Zeilen** -- leere Plätze
oder `0` zählen nicht als gültig.

## Beispiele

| Zeile                          | Gültig? |
|--------------------------------|----------|
| `[1, 2, 3, 4, 5, 6, 7, 8, 9]`  | `True`   |
| `[9, 8, 7, 6, 5, 4, 3, 2, 1]`  | `True`   |
| `[2, 4, 1, 6, 3, 8, 5, 7, 9]`  | `True`   |
| `[1, 1, 2, 3, 4, 5, 6, 7, 8]`  | `False`  |
| `[1, 2, 3, 4, 5, 6, 7, 8, 0]`  | `False`  |
| `[1, 2, 3, 4, 5, 6, 7, 8]`     | `False`  |

## Idee

oder mit Set:

Beide Varianten erkennen Duplikate, fehlende Ziffern und falsche
Laengen automatisch.

## Erweiterungen (spaeter)

- **Sudoku-Spalte**: gleicher Test, andere Indexierung.
- **Sudoku-Block**: 3x3-Block aus dem 9x9-Brett extrahieren.
- **Sudoku-Brett**: alle 9 Zeilen + 9 Spalten + 9 Bloecke prüfen.

Aus diesen drei Bausteinen entsteht ein vollstaendiger Sudoku-Validator.
