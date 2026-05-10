---
schema_version: 1
id: 050-insertion-sort
revision: 1
titel: Insertion-Sort
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 9
tags: [algorithmen, sortieren, listen]
pfade: [python_algorithmen2]
voraussetzungen: [049-selection-sort]
quelle:
  url: https://de.wikipedia.org/wiki/Insertionsort
  notiz: Lehrbuch-Algorithmus
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: insertion_sort
hints:
  - kosten: 0
    text: |
      Stell dir vor, du sortierst Spielkarten in der Hand. Linke Seite
      ist sortiert. Nimm die nächste Karte und schiebe sie nach links,
      bis sie an der richtigen Stelle liegt.
  - kosten: 15
    text: |
      Aussere Schleife `i` von 1 bis n. Innere `j` von i abwaerts.
      Solange `liste[j-1] > liste[j]`: tauschen, j -= 1.
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
  def insertion_sort(liste: list[int]) -> list[int]:
      # Deine Lösung hier -- ohne sorted() / list.sort().
      pass
---

# Insertion-Sort

Schreibe eine Funktion `insertion_sort(liste)`, die die Liste mit
**Insertion-Sort** sortiert.

## Idee

Der **linke Teil** der Liste ist immer sortiert. Pro Durchlauf:

1. Nimm das nächste Element vom unsortierten Teil
2. Schiebe es nach links, bis es an der richtigen Stelle steht

Bildlich wie Spielkarten sortieren -- man hebt eine Karte hoch und
sortiert sie in die schon geordneten ein.

## Komplexitaet

$O(n^2)$ im Worst-Case, **aber $O(n)$ im Best-Case** (bereits
sortierte Liste). Damit ist Insertion-Sort fuer **fast sortierte**
Listen erstaunlich schnell -- besser als Selection-Sort, schneller
als die meisten "schnellen" Algorithmen fuer kleine Listen.

In der Praxis verwenden viele "schnelle" Sortier-Bibliotheken
Insertion-Sort fuer kleine Teilbereiche (z.B. unter 16 Elemente).
Pythons Timsort macht genau das.
