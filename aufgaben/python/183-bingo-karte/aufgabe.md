---
schema_version: 1
id: 183-bingo-karte
revision: 1
titel: Bingo-Karte prüfen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 15
tags: [matrix, set, spiele, logik]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Spiel-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: hat_bingo
hints:
  - kosten: 0
    text: |
      Eine 5x5-Karte mit Zahlen, plus eine Liste gezogener Zahlen.
      "Bingo" liegt vor, wenn EINE Zeile, EINE Spalte oder
      EINE Hauptdiagonale komplett gezogen wurde.
      Gib True/False zurück.
  - kosten: 15
    text: |
      gezogen = set(zahlen). Pro Zeile: alle in gezogen → True.
      Spalten via zip(*karte). Diagonalen mit i,i und i,n-1-i.
tests_sichtbar:
  - input: [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], [1,2,3,4,5]]
    expected: true
  - input: [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], [1,6,11,16,21]]
    expected: true
  - input: [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], [1,7,13,19,25]]
    expected: true
  - input: [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], [1,2,3,4]]
    expected: false
tests_versteckt:
  - input: [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], [5,9,13,17,21]]
    expected: true
  - input: [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], [16,17,18,19,20]]
    expected: true
  - input: [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], [3,8,13,18,23]]
    expected: true
  - input: [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], [1,3,5,7,11]]
    expected: false
  - input: [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], []]
    expected: false
  - input: [[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]
    expected: true
starter_code: |
  def hat_bingo(karte: list[list[int]], gezogen: list[int]) -> bool:
      # Deine Lösung hier -- pruefe Zeilen, Spalten, Diagonalen
      pass
---

# Bingo-Karte prüfen

Beim Bingo erhaelt jeder Spieler eine **5x5-Karte** mit Zahlen.
Es werden Zahlen gezogen, und der erste, der eine **vollstaendige
Reihe** (Zeile, Spalte oder eine der zwei Diagonalen) hat, ruft
"Bingo!".

Schreibe `hat_bingo(karte, gezogen)`, die `True` zurückgibt, wenn
mindestens eine Reihe komplett aus gezogenen Zahlen besteht.

## Beispiele

Karte:
```
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
```

| Gezogene Zahlen        | Bingo?              |
|------------------------|---------------------|
| `[1,2,3,4,5]`          | `True` (Zeile 1)    |
| `[1,6,11,16,21]`       | `True` (Spalte 1)   |
| `[1,7,13,19,25]`       | `True` (Hauptdiag.) |
| `[5,9,13,17,21]`       | `True` (Nebendiag.) |
| `[1,3,5,7,11]`         | `False`             |

## Idee

```python
def hat_bingo(karte, gezogen):
    g = set(gezogen)
    n = len(karte)
    if n == 0:
        return False
    for i in range(n):
        if all(z in g for z in karte[i]):
            return True
    for j in range(n):
        if all(karte[i][j] in g for i in range(n)):
            return True
    if all(karte[i][i] in g for i in range(n)):
        return True
    if all(karte[i][n - 1 - i] in g for i in range(n)):
        return True
    return False
```

## Variante -- Zählen, nach wievielen Zuegen "Bingo" eintritt

Iteriere durch `gezogen`, fuelle laufend `g`, und liefere den Index
zurück, bei dem zum ersten Mal `hat_bingo` `True` wird. Klassische
Erweiterung für **Advent of Code 2021, Tag 4**.
