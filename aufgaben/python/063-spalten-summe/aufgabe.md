---
schema_version: 1
id: 063-spalten-summe
revision: 1
titel: Spaltensumme einer Matrix
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [matrix, listen, schleifen, sum]
pfade: [python_logik]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Klassische Matrix-Aufwaermübung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: spalten_summen
hints:
  - kosten: 0
    text: |
      Pro Spalte alle Einträge summieren. Liste der Spaltensummen
      zurückgeben.
  - kosten: 15
    text: |
      Mit zip + list comp:

      ```
      return [sum(spalte) for spalte in zip(*matrix)]
      ```
tests_sichtbar:
  - input: [[[1, 2, 3], [4, 5, 6]]]
    expected: [5, 7, 9]
  - input: [[[1]]]
    expected: [1]
  - input: [[[1, 1], [1, 1], [1, 1]]]
    expected: [3, 3]
  - input: [[]]
    expected: []
tests_versteckt:
  - input: [[[10, 20, 30]]]
    expected: [10, 20, 30]
  - input: [[[1, 2], [3, 4], [5, 6]]]
    expected: [9, 12]
  - input: [[[-1, 1], [-1, 1]]]
    expected: [-2, 2]
starter_code: |
  def spalten_summen(matrix: list[list[int]]) -> list[int]:
      # Deine Lösung hier
      pass
---

# Spaltensumme einer Matrix

Schreibe eine Funktion `spalten_summen(matrix)`, die für jede Spalte
einer Matrix die Summe ihrer Einträge zurückgibt.

## Beispiele

| Matrix                  | Ergebnis     |
|-------------------------|--------------|
| `[[1,2,3],[4,5,6]]`     | `[5,7,9]`    |
| `[[1]]`                 | `[1]`        |
| `[[1,1],[1,1],[1,1]]`   | `[3,3]`      |
| `[[10,20,30]]`          | `[10,20,30]` |
| `[]`                    | `[]`         |

## Idee

Mit `zip(*matrix)` bekommst du die Spalten als Tupel. Dann pro
Spalte `sum`.
