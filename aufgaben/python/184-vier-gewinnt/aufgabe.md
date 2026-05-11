---
schema_version: 1
id: 184-vier-gewinnt
revision: 1
titel: Vier-Gewinnt -- gibt es einen Sieger?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 45
schaetz_minuten: 18
tags: [matrix, spiele, logik, suche]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Brettspiel-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: vier_gewinnt
hints:
  - kosten: 0
    text: |
      Brett ist 6 Zeilen x 7 Spalten, Zellen "X", "O" oder " ".
      Liefere "X", "O" oder None.
      Vier gleiche in Zeile, Spalte, Haupt- oder Nebendiagonale = Sieg.
  - kosten: 25
    text: |
      Pro Zelle (i, j) und vier Richtungen
      (0,1), (1,0), (1,1), (1,-1) prüfen, ob die nächsten 3
      gleich sind. Vorsicht beim Rand.
tests_sichtbar:
  - input: [[["X","X","X","X"," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]]
    expected: "X"
  - input: [[[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]]
    expected: null
  - input: [[["O"," "," "," "," "," "," "],["O"," "," "," "," "," "," "],["O"," "," "," "," "," "," "],["O"," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]]
    expected: "O"
  - input: [[["X","O","X","O","X","O","X"],["O","X","O","X","O","X","O"],["X","O","X","O","X","O","X"],["O","X","O","X","O","X","O"],["X","O","X","O","X","O","X"],["O","X","O","X","O","X","O"]]]
    expected: "X"
tests_versteckt:
  - input: [[[" "," "," "," "," "," "," "],[" ","X"," "," "," "," "," "],[" "," ","X"," "," "," "," "],[" "," "," ","X"," "," "," "],[" "," "," "," ","X"," "," "],[" "," "," "," "," "," "," "]]]
    expected: "X"
  - input: [[[" "," "," "," ","O"," "," "],[" "," "," ","O"," "," "," "],[" "," ","O"," "," "," "," "],[" ","O"," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]]
    expected: "O"
  - input: [[[" "," ","X","X","X"," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]]
    expected: null
  - input: [[[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," ","O","O","O","O"],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]]
    expected: "O"
starter_code: |
  def vier_gewinnt(brett: list[list[str]]):
      # Deine Lösung hier -- "X" / "O" / None
      pass
---

# Vier-Gewinnt: gibt es einen Sieger?

Schreibe `vier_gewinnt(brett)`, die für ein 6x7-Brett entscheidet,
ob `"X"` oder `"O"` vier gleiche Zellen in einer Reihe hat.

Vier in einer Reihe gibt es in **vier Richtungen**: horizontal,
vertikal, und beide Diagonalen. Reihenfolge der Prüfung egal --
sobald ein Sieger gefunden ist, kann man zurückgeben.

Wenn keiner gewonnen hat → `None`.

## Beispiel-Brett

```
. . . . . . .
. . . . . . .
. . . . . . .
. . . X . . .
. . X X . . .
. X X O O O O   <- O hat unten waagerecht 4
```

→ `"O"`.

## Idee -- vier Richtungen

```python
def vier_gewinnt(brett):
    if not brett or not brett[0]:
        return None
    rows, cols = len(brett), len(brett[0])
    DIR = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for i in range(rows):
        for j in range(cols):
            c = brett[i][j]
            if c == " ":
                continue
            for di, dj in DIR:
                if all(
                    0 <= i + k * di < rows
                    and 0 <= j + k * dj < cols
                    and brett[i + k * di][j + k * dj] == c
                    for k in range(4)
                ):
                    return c
    return None
```

Die Symmetrie der vier Richtungen ist wichtig: `(0,1)` deckt sowohl
"links nach rechts" als auch "rechts nach links" ab, weil wir
über alle Startpositionen iterieren.

## Hintergrund

Vier Gewinnt wurde 1995 vom belgischen Mathematiker Victor Allis
**komplett gelöst**: bei perfektem Spiel gewinnt **immer der
erste Spieler** (mit Stein in Spalte 4 als Eröffnung). Die
Berechnung dauerte 1988 monatelang, heute schafft das ein
Smartphone in Sekunden.
