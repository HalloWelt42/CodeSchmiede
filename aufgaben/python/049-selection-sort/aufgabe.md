---
schema_version: 1
id: 049-selection-sort
revision: 1
titel: Selection-Sort
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 9
tags: [algorithmen, sortieren, listen]
pfade: [python_algorithmen2]
voraussetzungen: [038-bubble-sort]
quelle:
  url: https://de.wikipedia.org/wiki/Selectionsort
  notiz: Lehrbuch-Algorithmus
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: selection_sort
hints:
  - kosten: 0
    text: |
      Suche das Minimum im unsortierten Teil und tausche es mit dem
      ersten Element des unsortierten Teils.
  - kosten: 9
    text: |
      Aussere Schleife `i in range(n)`. Innen: Index des Minimums in
      `liste[i:]` finden, dann mit `liste[i]` tauschen.
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
  - input: [[10, -1, 5, 0, -100, 42]]
    expected: [-100, -1, 0, 5, 10, 42]
  - input: [[42]]
    expected: [42]
starter_code: |
  def selection_sort(liste: list[int]) -> list[int]:
      # Deine Lösung hier -- ohne sorted() / list.sort().
      pass
---

# Selection-Sort

Schreibe eine Funktion `selection_sort(liste)`, die die Liste mit
**Selection-Sort** sortiert.

## Idee

In jedem Durchlauf:

1. Finde das **kleinste Element** im noch unsortierten Teil
2. Tausche es mit dem ersten Element des unsortierten Teils
3. Der sortierte Teil waechst um eins nach rechts

## Beispiele

| Eingabe       | Ergebnis      |
|---------------|---------------|
| `[3,1,2]`     | `[1,2,3]`     |
| `[5,4,3,2,1]` | `[1,2,3,4,5]` |
| `[]`          | `[]`          |

## Komplexitaet

$O(n^2)$ in **jedem** Fall -- auch wenn die Liste schon sortiert ist,
müssen alle Vergleiche gemacht werden. Das ist anders als bei
Bubble-Sort, der mit Early-Exit auf $O(n)$ schrumpft.

Die Anzahl der **Tauschoperationen** ist allerdings nur $O(n)$ -- genau
ein Tausch pro Durchlauf. Das macht Selection-Sort attraktiv, wenn
Tauschen teuer ist (z.B. bei sehr großen Datensätzen im RAM).
