---
schema_version: 1
id: 170-drei-summe-null
revision: 1
titel: Drei-Summe gleich Null
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 60
schaetz_minuten: 25
tags: [listen, two-pointers, sortieren, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode 15 -- 3Sum
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: drei_summe
hints:
  - kosten: 0
    text: |
      Liefere alle eindeutigen Tripel [a, b, c] (a <= b <= c) aus der
      Liste, deren Summe 0 ist. Aussere Liste sortiert.
      Doppelte Werte überspringen.
  - kosten: 25
    text: |
      Liste sortieren. Iteriere a = zahlen[i] (0..n-3).
      Pro a: Two-Pointers (j=i+1, k=n-1). Bei a+b+c==0 sammeln,
      dann j und k weiter und Duplikate überspringen.
tests_sichtbar:
  - input: [[-1, 0, 1, 2, -1, -4]]
    expected: [[-1, -1, 2], [-1, 0, 1]]
  - input: [[]]
    expected: []
  - input: [[0, 0, 0]]
    expected: [[0, 0, 0]]
  - input: [[1, 2, 3]]
    expected: []
tests_versteckt:
  - input: [[0, 0, 0, 0]]
    expected: [[0, 0, 0]]
  - input: [[-2, 0, 1, 1, 2]]
    expected: [[-2, 0, 2], [-2, 1, 1]]
  - input: [[3, 0, -2, -1, 1, 2]]
    expected: [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
  - input: [[1, -1, -1, 0]]
    expected: [[-1, 0, 1]]
  - input: [[-1, -1, -1]]
    expected: []
  - input: [[-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]]
    expected: [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
starter_code: |
  def drei_summe(zahlen: list[int]) -> list[list[int]]:
      # Deine Lösung hier -- alle eindeutigen Tripel mit Summe 0
      pass
---

# Drei-Summe gleich Null

Schreibe eine Funktion `drei_summe(zahlen)`, die **alle eindeutigen
Tripel** `[a, b, c]` mit `a <= b <= c` aus der Liste liefert, deren
Summe `0` ist. Doppelte Tripel werden nur einmal aufgefuehrt.

Aussere Liste **lexikographisch sortiert**.

## Beispiele

| Eingabe                       | Tripel                                 |
|-------------------------------|----------------------------------------|
| `[-1, 0, 1, 2, -1, -4]`       | `[[-1, -1, 2], [-1, 0, 1]]`            |
| `[0, 0, 0, 0]`                | `[[0, 0, 0]]`                          |
| `[1, 2, 3]`                   | `[]` (keins moeglich)                  |
| `[-1, -1, -1]`                | `[]`                                   |

## Idee -- Sortieren + Two Pointers

Ohne Sortierung ist Brute-Force `O(n^3)` -- zu langsam für große `n`.
Mit Sortierung kann man für jedes festgesetzte `a` die übrigen zwei
Werte mit Two-Pointers in `O(n)` finden → insgesamt `O(n^2)`.

## Stolpersteine

- **Duplikate überspringen** ist Pflicht, sonst kommen `[-1, 0, 1]`
  doppelt vor.
- Sortier-Reihenfolge im Tripel entsteht **automatisch**, weil die
  Liste sortiert ist und `j > i, k > j`.

## Hintergrund

3-Sum ist die Aufwaerm-Form des allgemeinen **k-Sum**-Problems.
Erwartete Komplexitaet `O(n^{k-1})`. Für 4-Sum nimmt man zwei
Schleifen + Two-Pointers, für höhere `k` rekursive Reduktion.
