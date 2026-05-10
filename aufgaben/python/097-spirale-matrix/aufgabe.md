---
schema_version: 1
id: 097-spirale-matrix
revision: 1
titel: Zahlen in Spirale anordnen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 22
schaetz_minuten: 14
tags: [matrix, schleifen, richtung, listen]
pfade: [python_logik]
voraussetzungen: [062-matrix-transponieren]
quelle:
  url: null
  notiz: Inspiration aus Exercism (spiral-matrix), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: spirale
hints:
  - kosten: 0
    text: |
      Lege eine n×n Matrix mit Nullen an. Setze die Zahlen 1, 2, ...
      in Spirale: nach rechts, dann unten, dann links, dann oben,
      und so weiter -- jeweils bis du an einen Rand oder bereits
      gefuelltes Feld stoesst.
  - kosten: 25
    text: |
      Richtungs-Vektoren `[(0,1), (1,0), (0,-1), (-1,0)]`. Pro Schritt
      pruefen ob naechste Position frei und im Raster ist. Falls nicht:
      Richtung wechseln.
tests_sichtbar:
  - input: [1]
    expected: [[1]]
  - input: [2]
    expected: [[1, 2], [4, 3]]
  - input: [3]
    expected: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
  - input: [4]
    expected: [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
tests_versteckt:
  - input: [0]
    expected: []
  - input: [5]
    expected: [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
  - input: [6]
    expected: [[1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [19, 32, 33, 34, 25, 8], [18, 31, 36, 35, 26, 9], [17, 30, 29, 28, 27, 10], [16, 15, 14, 13, 12, 11]]
starter_code: |
  def spirale(n: int) -> list[list[int]]:
      # Deine Lösung hier -- Zahlen 1..n² in Spirale, beginnend oben links.
      pass
---

# Zahlen in Spirale anordnen

Schreibe eine Funktion `spirale(n)`, die eine `n×n` Matrix mit den
Zahlen `1, 2, ..., n²` anordnet -- in Spirale, beginnend oben links
und im Uhrzeigersinn nach innen.

## Beispiel n=3

```
1 2 3
8 9 4
7 6 5
```

## Beispiel n=4

```
 1  2  3  4
12 13 14  5
11 16 15  6
10  9  8  7
```

## Idee

Vier Richtungs-Vektoren: rechts (0, 1), unten (1, 0), links (0, -1),
oben (-1, 0). Sobald du an einen Rand oder eine bereits gesetzte
Zahl stossen wuerdest, wechsle zur naechsten Richtung.

## Hintergrund

Spiralen sind ein Klassiker bei Coding-Interviews. Sie schulen das
Denken in **Richtungswechseln** und **Grenzen-Pruefungen** -- Sachen,
die man fuer alle moeglichen Grid-Algorithmen braucht.
