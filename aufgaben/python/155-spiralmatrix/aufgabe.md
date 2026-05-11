---
schema_version: 1
id: 155-spiralmatrix
revision: 1
titel: Matrix als Spirale lesen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 55
schaetz_minuten: 25
tags: [matrix, listen, 2d, spirale, simulation]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode-Klassiker 54
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: spirale_lesen
hints:
  - kosten: 0
    text: |
      Lese eine MxN-Matrix in Spirale (rechts-unten-links-oben), starte
      links oben. Liefere die Werte als flache Liste.
      Bei [] -> [].
  - kosten: 25
    text: |
      Schichtweise abarbeiten: oberste Zeile von links nach rechts,
      rechte Spalte von oben nach unten, untere Zeile von rechts
      nach links, linke Spalte von unten nach oben. Dann eine Schicht
      reinzoomen. Auf "noch was übrig?" prüfen!
tests_sichtbar:
  - input: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]
  - input: [[[1, 2], [3, 4]]]
    expected: [1, 2, 4, 3]
  - input: [[]]
    expected: []
  - input: [[[1]]]
    expected: [1]
tests_versteckt:
  - input: [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
    expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
  - input: [[[1], [2], [3]]]
    expected: [1, 2, 3]
  - input: [[[1, 2, 3, 4]]]
    expected: [1, 2, 3, 4]
  - input: [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]
    expected: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
  - input: [[[7, 8], [9, 10], [11, 12]]]
    expected: [7, 8, 10, 12, 11, 9]
starter_code: |
  def spirale_lesen(matrix: list[list[int]]) -> list[int]:
      # Deine Lösung hier -- schichtweise abarbeiten
      pass
---

# Matrix als Spirale lesen

Schreibe eine Funktion `spirale_lesen(matrix)`, die eine MxN-Matrix
**im Uhrzeigersinn als Spirale** abarbeitet -- start oben links --
und alle Werte als **flache Liste** zurückgibt.

## Beispiel 3x3

```
1 → 2 → 3
        ↓
4 → 5   6
↑       ↓
7 ← 8 ← 9
```

→ `[1, 2, 3, 6, 9, 8, 7, 4, 5]`

## Beispiel 3x4

```
1  2  3  4
5  6  7  8
9 10 11 12
```

→ `[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]`

## Idee -- Grenzen einsperren

Vier Grenzen `oben`, `unten`, `links`, `rechts`. In jedem Zyklus:

1. Oberste Zeile von `links` bis `rechts` (dann `oben += 1`)
2. Rechte Spalte von `oben` bis `unten` (dann `rechts -= 1`)
3. Wenn noch Zeilen übrig: untere Zeile von `rechts` bis `links` (dann `unten -= 1`)
4. Wenn noch Spalten übrig: linke Spalte von `unten` bis `oben` (dann `links += 1`)

Wiederholen, bis alle Werte eingesammelt.

## Stolpersteine

- **Asymmetrische Matrizen** (z.B. 1xN oder Nx1) brauchen die
  beiden `if`-Prüfungen, sonst werden Elemente doppelt gelesen.
- Klassiker für Bewerbungsgespraeche -- viele Naive-Implementierungen
  stolpern an genau diesen Sonderfaellen.
