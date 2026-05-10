---
schema_version: 1
id: 061-tictactoe
revision: 1
titel: TicTacToe-Gewinner
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [matrix, schleifen, spiel]
pfade: [python_logik]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Brett-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: gewinner
hints:
  - kosten: 0
    text: |
      Pruefe alle 8 moeglichen Gewinn-Linien: 3 Zeilen, 3 Spalten,
      2 Diagonalen. Wenn alle 3 Felder gleich und nicht leer sind,
      ist das der Gewinner.
  - kosten: 15
    text: |
      Felder mit "."  bedeuten leer. Bei leerem Feld nicht als
      Gewinner zaehlen.
tests_sichtbar:
  - input: [[["X", "X", "X"], ["O", "O", "."], [".", ".", "."]]]
    expected: "X"
  - input: [[["X", ".", "O"], ["X", ".", "O"], ["X", ".", "."]]]
    expected: "X"
  - input: [[["X", ".", "."], [".", "X", "."], [".", ".", "X"]]]
    expected: "X"
  - input: [[["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]]
    expected: "."
tests_versteckt:
  - input: [[[".", ".", "."], [".", ".", "."], [".", ".", "."]]]
    expected: "."
  - input: [[["O", "O", "O"], [".", ".", "."], [".", ".", "."]]]
    expected: "O"
  - input: [[[".", ".", "X"], [".", "X", "."], ["X", ".", "."]]]
    expected: "X"
  - input: [[["O", ".", "."], [".", "O", "."], [".", ".", "O"]]]
    expected: "O"
  - input: [[["X", "X", "O"], ["O", "O", "X"], ["X", "X", "O"]]]
    expected: "."
starter_code: |
  def gewinner(brett: list[list[str]]) -> str:
      # Deine Loesung hier -- "X", "O" oder "." (kein Gewinner / unentschieden)
      pass
---

# TicTacToe-Gewinner

Schreibe eine Funktion `gewinner(brett)`, die fuer ein 3x3-TicTacToe-
Brett den Gewinner zurueckgibt -- `"X"` oder `"O"`. Wenn keiner
gewonnen hat, gib `"."` zurueck.

Felder enthalten `"X"`, `"O"` oder `"."` (leer).

## Beispiele

| Brett                                       | Gewinner |
|---------------------------------------------|----------|
| `XXX / OO. / ...` (Zeile 1)                 | `"X"`    |
| `X.. / X.. / X..` (Spalte 1)                | `"X"`    |
| `X.. / .X. / ..X` (Diagonale)               | `"X"`    |
| `OOO / ... / ...`                           | `"O"`    |
| ...                                         | `"."`    |

## Idee

Pruefe alle 8 Linien:

- 3 Zeilen: `brett[i][0] == brett[i][1] == brett[i][2]`
- 3 Spalten: `brett[0][j] == brett[1][j] == brett[2][j]`
- 2 Diagonalen

Wenn alle drei Felder einer Linie gleich sind und **nicht leer**, ist
das der Gewinner.

## Annahme

Wir nehmen an, das Brett ist gueltig -- es gibt also nicht zwei
Gewinner gleichzeitig.
