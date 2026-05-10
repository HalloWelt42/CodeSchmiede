---
schema_version: 1
id: 064-diagonale-summe
revision: 1
titel: Diagonal-Summe einer Matrix
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [matrix, listen, schleifen]
pfade: [python_logik]
voraussetzungen: [063-spalten-summe]
quelle:
  url: null
  notiz: Klassische Matrix-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: diagonal_summen
hints:
  - kosten: 0
    text: |
      Bei einer quadratischen Matrix gibt es zwei Diagonalen: von
      links-oben nach rechts-unten ("Haupt") und von rechts-oben nach
      links-unten ("Neben").
  - kosten: 15
    text: |
      Hauptdiagonale: `matrix[i][i]`. Nebendiagonale: `matrix[i][n-1-i]`.
tests_sichtbar:
  - input: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    expected: [15, 15]
  - input: [[[1]]]
    expected: [1, 1]
  - input: [[[1, 2], [3, 4]]]
    expected: [5, 5]
  - input: [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
    expected: [3, 1]
tests_versteckt:
  - input: [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]
    expected: [34, 34]
  - input: [[[5, 0], [0, 5]]]
    expected: [10, 0]
starter_code: |
  def diagonal_summen(matrix: list[list[int]]) -> list[int]:
      # Deine Loesung hier -- gibt [haupt, neben] zurueck.
      pass
---

# Diagonal-Summe einer Matrix

Schreibe eine Funktion `diagonal_summen(matrix)`, die fuer eine
**quadratische** Matrix die Summen beider Diagonalen zurueckgibt --
als Liste `[haupt, neben]`.

## Beispiele

| Matrix                        | Ergebnis      |
|-------------------------------|---------------|
| `[[1,2,3],[4,5,6],[7,8,9]]`   | `[15, 15]`    |
| `[[1]]`                       | `[1, 1]`      |
| `[[1,2],[3,4]]`               | `[5, 5]`      |
| `[[1,0,0],[0,1,0],[0,0,1]]`   | `[3, 1]`      |

## Idee

- **Hauptdiagonale**: `matrix[i][i]` fuer `i = 0..n-1`
- **Nebendiagonale**: `matrix[i][n-1-i]`

Bei einer 1x1-Matrix sind beide Diagonalen das einzige Element --
Wert wird also doppelt zurueckgegeben.
