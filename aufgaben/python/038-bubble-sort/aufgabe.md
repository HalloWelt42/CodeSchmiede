---
schema_version: 1
id: 038-bubble-sort
revision: 1
titel: Bubble-Sort von Hand
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [algorithmen, sortieren, listen]
pfade: [python_algorithmen]
voraussetzungen: [012-listen-sortieren]
quelle:
  url: https://de.wikipedia.org/wiki/Bubblesort
  notiz: Lehrbuch-Algorithmus
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: bubble_sort
hints:
  - kosten: 0
    text: |
      Doppelte Schleife. Vergleiche jeweils Nachbarn, vertausche, falls
      links größer ist als rechts. Wiederhole, bis nichts mehr
      vertauscht wurde.
  - kosten: 11
    text: |
      Aussere Schleife `n` mal, innere von 0 bis n-i-1. Vertauschen mit
      Tuple-Unpacking: `a[j], a[j+1] = a[j+1], a[j]`.
tests_sichtbar:
  - input: [[3, 1, 2]]
    expected: [1, 2, 3]
  - input: [[]]
    expected: []
  - input: [[1]]
    expected: [1]
  - input: [[5, 4, 3, 2, 1]]
    expected: [1, 2, 3, 4, 5]
tests_versteckt:
  - input: [[2, 2, 1, 1]]
    expected: [1, 1, 2, 2]
  - input: [[1, 2, 3, 4, 5]]
    expected: [1, 2, 3, 4, 5]
  - input: [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
    expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  - input: [[42]]
    expected: [42]
starter_code: |
  def bubble_sort(liste: list[int]) -> list[int]:
      # Deine Lösung hier -- ohne sorted() oder list.sort().
      pass
---

# Bubble-Sort von Hand

Schreibe eine Funktion `bubble_sort(liste)`, die die Liste mit
**Bubble-Sort** sortiert -- ohne `sorted()` oder `list.sort()` zu
verwenden.

## Idee

Vergleiche **benachbarte Elemente** und vertausche sie, falls sie in
falscher Reihenfolge sind. Wiederhole das, bis kein Tausch mehr
nötig ist. Bei jedem Durchlauf "blubbert" das jeweils größte
verbliebene Element ans Ende -- daher der Name.

## Beispiele

| Eingabe          | Ergebnis        |
|------------------|-----------------|
| `[3,1,2]`        | `[1,2,3]`       |
| `[5,4,3,2,1]`    | `[1,2,3,4,5]`   |
| `[]`             | `[]`            |
| `[42]`           | `[42]`          |

## Komplexitaet

Bubble-Sort ist mit $O(n^2)$ **deutlich langsamer** als die in der
Standardbibliothek eingebauten Sortierverfahren ($O(n \log n)$). In
echtem Code nimm immer `sorted()`. Hier geht es ums **Verstehen**, wie
ein Sortierverfahren von innen aussieht.

## Stabilitaet

Bubble-Sort ist **stabil**: gleiche Werte behalten ihre relative
Reihenfolge. Beim Programmieren darauf achten, **nicht** zu tauschen,
wenn die Werte gleich sind (`>` statt `>=`).
