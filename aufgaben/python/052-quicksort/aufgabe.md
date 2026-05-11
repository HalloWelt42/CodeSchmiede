---
schema_version: 1
id: 052-quicksort
revision: 1
titel: Quicksort
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 22
schaetz_minuten: 16
tags: [algorithmen, sortieren, listen, divide-and-conquer, rekursion]
pfade: [python_algorithmen2]
voraussetzungen: [051-merge-sort]
quelle:
  url: https://de.wikipedia.org/wiki/Quicksort
  notiz: Klassischer Divide-and-Conquer-Algorithmus von Tony Hoare 1959
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: quicksort
hints:
  - kosten: 0
    text: |
      Waehle ein Pivot-Element. Teile die Liste in: kleiner als Pivot,
      gleich Pivot, größer als Pivot. Sortiere die beiden aeusseren
      Listen rekursiv und setze alles zusammen.
  - kosten: 15
    text: |
      Pythonic mit Comprehensions:

      ```
      pivot = liste[0]
      kleiner = [x for x in liste[1:] if x < pivot]
      größer = [x for x in liste[1:] if x >= pivot]
      return quicksort(kleiner) + [pivot] + quicksort(größer)
      ```
tests_sichtbar:
  - input: [[3, 1, 2]]
    expected: [1, 2, 3]
  - input: [[]]
    expected: []
  - input: [[5, 4, 3, 2, 1]]
    expected: [1, 2, 3, 4, 5]
  - input: [[1, 2, 3, 4, 5]]
    expected: [1, 2, 3, 4, 5]
tests_versteckt:
  - input: [[2, 2, 1, 1]]
    expected: [1, 1, 2, 2]
  - input: [[10, -1, 5, 0, -100, 42]]
    expected: [-100, -1, 0, 5, 10, 42]
  - input: [[42]]
    expected: [42]
  - input: [[3, 3, 3, 3]]
    expected: [3, 3, 3, 3]
starter_code: |
  def quicksort(liste: list[int]) -> list[int]:
      # Deine Lösung hier -- ohne sorted() / list.sort().
      pass
---

# Quicksort

Schreibe eine Funktion `quicksort(liste)`, die die Liste mit
**Quicksort** sortiert.

## Idee: Divide and Conquer

1. Liste mit 0 oder 1 Element: schon sortiert
2. Sonst: wähle ein **Pivot-Element**
3. Teile die Liste in `kleiner`, `gleich`, `größer`
4. Sortiere `kleiner` und `größer` rekursiv
5. Setze `kleiner_sortiert + gleich + größer_sortiert` zusammen

## Komplexitaet

Im **Mittel** $O(n \log n)$, im **Worst-Case** (z.B. immer das
schlechteste Pivot) $O(n^2)$. Praktisch sehr schnell, weil die
Cache-Effizienz gut ist.

## Geschichte

Tony Hoare entwickelte Quicksort 1959 mit 25 Jahren in Moskau --
ursprünglich, um russische Worte zu sortieren. Bis heute eines der
am häufigsten verwendeten Sortier-Verfahren der Welt.

## Tipp

Diese Variante ist nicht in-place und braucht $O(n)$ Extra-Speicher
für die Comprehensions. In-place-Quicksort mit Lomuto- oder
Hoare-Partitionierung ist eine separate Aufgabe.
