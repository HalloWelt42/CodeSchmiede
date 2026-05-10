---
schema_version: 1
id: 057-paare-mit-summe
revision: 1
titel: Anzahl Paare mit Zielsumme
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 9
tags: [listen, sets, paare, hashing]
pfade: [python_listen3]
voraussetzungen: [053-two-sum]
quelle:
  url: null
  notiz: Variante des Two-Sum-Problems
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: paare_anzahl
hints:
  - kosten: 0
    text: |
      Naive Loesung: doppelte Schleife, Paare zaehlen.
  - kosten: 15
    text: |
      Schneller mit Counter: pro Wert x pruefen, wie oft (ziel - x)
      vorkommt. Nicht doppelt zaehlen.
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 6]
    expected: 2
  - input: [[1, 1, 1, 1], 2]
    expected: 6
  - input: [[5], 5]
    expected: 0
  - input: [[], 5]
    expected: 0
tests_versteckt:
  - input: [[1, 2, 3], 100]
    expected: 0
  - input: [[3, 3, 3, 3], 6]
    expected: 6
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11]
    expected: 5
  - input: [[0, 0, 0], 0]
    expected: 3
starter_code: |
  def paare_anzahl(zahlen: list[int], ziel: int) -> int:
      # Deine Loesung hier -- ungeordnete Paare (i,j) mit i<j zaehlen,
      # bei denen zahlen[i] + zahlen[j] == ziel.
      pass
---

# Anzahl Paare mit Zielsumme

Schreibe eine Funktion `paare_anzahl(zahlen, ziel)`, die die **Anzahl
der Index-Paare** `(i, j)` mit `i < j` zaehlt, deren Werte sich zur
`ziel`-Summe addieren.

## Beispiele

| Liste              | Ziel | Ergebnis | Wegen                    |
|--------------------|------|----------|--------------------------|
| `[1,2,3,4,5]`      | `6`  | `2`      | `(1,5), (2,4)`           |
| `[1,1,1,1]`        | `2`  | `6`      | alle 4 ueber 2 Paare = 6 |
| `[5]`              | `5`  | `0`      | nur ein Element          |
| `[3,3,3,3]`        | `6`  | `6`      | $\binom{4}{2} = 6$       |
| `[0,0,0]`          | `0`  | `3`      | $\binom{3}{2} = 3$       |

## Komplexitaet

| Variante      | Zeit     |
|---------------|----------|
| Doppelschleife| $O(n^2)$ |
| Mit Counter   | $O(n)$   |

Mit `collections.Counter` zaehlst du erst alle Vorkommen, dann
iterierst du einmal durch. Pro Wert `x` ist die Anzahl Paare:
`counter[x] * counter[ziel-x]`. Beim Sonderfall `ziel-x == x` musst
du die Formel anpassen, sonst zaehlst du Paare doppelt.
