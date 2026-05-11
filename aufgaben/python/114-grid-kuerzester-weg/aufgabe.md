---
schema_version: 1
id: 114-grid-kuerzester-weg
revision: 1
titel: Kürzester Weg im Raster (BFS)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 24
schaetz_minuten: 16
tags: [bfs, matrix, suche, algorithmen]
pfade: [python_algorithmen2]
voraussetzungen: [101-zwei-eimer]
quelle:
  url: null
  notiz: Klassischer Grid-BFS, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: kuerzester_weg
hints:
  - kosten: 0
    text: |
      Grid mit 0=frei, 1=Wand. Start oben links (0,0), Ziel unten
      rechts (n-1,m-1). Bewegung 4-fach (oben/unten/links/rechts).
      Liefere Anzahl Schritte oder -1.
  - kosten: 16
    text: |
      BFS mit deque. Zustand = (r, c). Visited-Set vermeidet Schleifen.
      Pro Schritt: 4 Nachbarn prüfen (Grenzen + Wand + nicht visited).
      Wenn Ziel erreicht: Schrittzahl zurück. Wenn Queue leer: -1.
tests_sichtbar:
  - input: [[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    expected: 4
  - input: [[[0]]]
    expected: 0
  - input: [[[0, 1], [0, 0]]]
    expected: 2
  - input: [[[0, 1], [1, 0]]]
    expected: -1
tests_versteckt:
  - input: [[[0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]]
    expected: 13
  - input: [[[1, 0], [0, 0]]]
    expected: -1
  - input: [[[0, 0], [0, 1]]]
    expected: -1
  - input: [[[0, 0, 0, 0, 0]]]
    expected: 4
  - input: [[]]
    expected: -1
starter_code: |
  def kuerzester_weg(grid: list[list[int]]) -> int:
      # Deine Lösung hier -- 0=frei, 1=Wand. Start (0,0), Ziel
      # (n-1, m-1). 4er-Bewegung. -1 wenn unerreichbar.
      pass
---

# Kürzester Weg im Raster (BFS)

Schreibe eine Funktion `kürzester_weg(grid)`, die im 2D-Raster
die **minimale Schrittzahl** vom oben-links nach unten-rechts findet.

- `0` ist begehbar
- `1` ist eine Wand
- Bewegung nur horizontal/vertikal (4-fach)
- Start `(0, 0)`, Ziel `(n-1, m-1)`
- Wenn unerreichbar oder Start/Ziel selbst eine Wand: `-1`
- Leeres Grid: `-1`

## Beispiele

| Grid                                     | Ergebnis |
|------------------------------------------|----------|
| `[[0,0,0],[0,0,0],[0,0,0]]`              | `4`      |
| `[[0]]`                                  | `0`      |
| `[[0,1],[0,0]]`                          | `2`      |
| `[[0,1],[1,0]]`                          | `-1`     |
| `[[1,0],[0,0]]`                          | `-1` (Start=Wand) |

## Algorithmus

**BFS** mit einer Queue. Pro Schritt alle 4 Nachbarn prüfen,
besuchte Felder merken. Erste Erreichung des Ziels = kürzester Weg.

## Hintergrund

Grid-BFS ist die Eintrittskarte zu **Pfadfindung**, vom 8-Bit-Spiel
bis hin zu Google Maps (allerdings dort gewichtet -- A*). Wer das
Pattern beherrscht, kann viele scheinbar verschiedene Probleme
lösen.
