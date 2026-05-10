---
schema_version: 1
id: 012-listen-sortieren
revision: 1
titel: Liste absteigend sortieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 14
schaetz_minuten: 6
tags: [listen, sortieren]
pfade: [python_listen]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Sortier-Grundlagen
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: sortiere_absteigend
hints:
  - kosten: 0
    text: Python hat `sorted()` als Built-In.
  - kosten: 10
    text: |
      `sorted()` hat einen Parameter `reverse=True` für absteigende
      Reihenfolge.
  - kosten: 25
    text: |
      ```
      return sorted(zahlen, reverse=True)
      ```
tests_sichtbar:
  - input: [[3, 1, 4, 1, 5]]
    expected: [5, 4, 3, 1, 1]
  - input: [[]]
    expected: []
  - input: [[1]]
    expected: [1]
  - input: [[-1, -3, -2]]
    expected: [-1, -2, -3]
tests_versteckt:
  - input: [[10, 20, 30]]
    expected: [30, 20, 10]
  - input: [[5, 5, 5]]
    expected: [5, 5, 5]
  - input: [[100, -100, 0]]
    expected: [100, 0, -100]
  - input: [[1, 2, 3, 4, 5]]
    expected: [5, 4, 3, 2, 1]
starter_code: |
  def sortiere_absteigend(zahlen: list[int]) -> list[int]:
      # Deine Lösung hier
      pass
---

# Liste absteigend sortieren

Schreibe eine Funktion `sortiere_absteigend(zahlen)`, die eine **neue**
Liste zurückgibt -- die Elemente vom größten zum kleinsten.

## Beispiele

| Eingabe              | Ausgabe              |
|----------------------|----------------------|
| `[3, 1, 4, 1, 5]`    | `[5, 4, 3, 1, 1]`    |
| `[10, 20, 30]`       | `[30, 20, 10]`       |
| `[]`                 | `[]`                 |
| `[-1, -3, -2]`       | `[-1, -2, -3]`       |

## Hinweise

- Gleiche Werte bleiben nebeneinander stehen (`[1, 1]` bleibt `[1, 1]`).
- Die Originalliste soll **nicht** verändert werden -- gib eine neue
  zurück. (`sorted()` macht genau das, `.sort()` würde in-place ändern.)
