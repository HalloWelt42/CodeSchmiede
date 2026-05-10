---
schema_version: 1
id: 051-merge-sort
revision: 1
titel: Merge-Sort
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 22
schaetz_minuten: 18
tags: [algorithmen, sortieren, listen, divide-and-conquer, rekursion]
pfade: [python_algorithmen2]
voraussetzungen: [050-insertion-sort]
quelle:
  url: https://de.wikipedia.org/wiki/Mergesort
  notiz: Klassischer Divide-and-Conquer-Algorithmus
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: merge_sort
hints:
  - kosten: 0
    text: |
      Teile die Liste in zwei Haelften. Sortiere beide rekursiv.
      Verschmilz die zwei sortierten Haelften.
  - kosten: 20
    text: |
      Hilfsfunktion `merge(a, b)` -- nimmt zwei sortierte Listen,
      vergleicht jeweils Spitze von a vs. Spitze von b, fuegt das
      kleinere Element ans Ergebnis.
  - kosten: 30
    text: |
      Basisfall: Listen mit 0 oder 1 Element sind bereits sortiert.
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
  - input: [[7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]]
    expected: [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
starter_code: |
  def merge_sort(liste: list[int]) -> list[int]:
      # Deine Loesung hier -- ohne sorted() / list.sort().
      pass
---

# Merge-Sort

Schreibe eine Funktion `merge_sort(liste)`, die die Liste mit
**Merge-Sort** sortiert.

## Idee: Divide and Conquer

1. Liste mit 0 oder 1 Element: schon sortiert (Basisfall)
2. Sonst: in zwei Haelften teilen, beide rekursiv sortieren, dann
   verschmelzen ("merge")

## Merge-Schritt

Zwei sortierte Listen `a` und `b` zu einer sortierten Liste mischen:
nimm immer das kleinere der beiden vorderen Elemente. Wenn eine
Liste leer ist, haenge den Rest der anderen an.

## Komplexitaet

$O(n \log n)$ in **jedem** Fall -- Merge-Sort ist sehr vorhersagbar.
**Stabil**: gleiche Elemente behalten ihre Reihenfolge.
**Speicher**: $O(n)$ -- nicht in-place.

Pythons eingebauter `sorted()` (Timsort) ist ein hochoptimierter
Hybride aus Merge-Sort und Insertion-Sort.
