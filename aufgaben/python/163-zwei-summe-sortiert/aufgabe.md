---
schema_version: 1
id: 163-zwei-summe-sortiert
revision: 1
titel: Zwei-Summe in sortierter Liste (Two Pointers)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [listen, two-pointers, suchen, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode 167 -- Two Sum II
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zwei_summe_sortiert
hints:
  - kosten: 0
    text: |
      Gegeben: aufsteigend sortierte Liste, Zielwert ziel.
      Liefere [i, j] (i < j) mit zahlen[i] + zahlen[j] == ziel.
      Wenn keine Lösung: [].
  - kosten: 15
    text: |
      Two Pointers: links=0, rechts=n-1. Bei summe < ziel: links += 1.
      Bei summe > ziel: rechts -= 1. Bei == ziel: gefunden!
tests_sichtbar:
  - input: [[1, 2, 3, 4, 6], 6]
    expected: [1, 3]
  - input: [[2, 7, 11, 15], 9]
    expected: [0, 1]
  - input: [[1, 2, 3], 7]
    expected: []
  - input: [[1, 2], 3]
    expected: [0, 1]
tests_versteckt:
  - input: [[-3, -1, 0, 2, 4, 5], 1]
    expected: [0, 4]
  - input: [[1, 1, 2, 2], 4]
    expected: [2, 3]
  - input: [[5, 10, 15], 25]
    expected: [1, 2]
  - input: [[-5, -3, -1, 0, 1], -8]
    expected: [0, 1]
  - input: [[], 5]
    expected: []
  - input: [[3], 3]
    expected: []
starter_code: |
  def zwei_summe_sortiert(zahlen: list[int], ziel: int) -> list[int]:
      # Deine Lösung hier -- Two Pointers in O(n)
      pass
---

# Zwei-Summe in sortierter Liste

Gegeben ist eine **aufsteigend sortierte** Liste und ein Zielwert.
Schreibe `zwei_summe_sortiert(zahlen, ziel)`, die `[i, j]` mit
`i < j` und `zahlen[i] + zahlen[j] == ziel` liefert -- oder `[]`,
falls kein Paar existiert.

## Beispiele

| Liste                 | Ziel | Indizes  | `zahlen[i] + zahlen[j]` |
|-----------------------|------|----------|-------------------------|
| `[2, 7, 11, 15]`      | `9`  | `[0, 1]` | `2 + 7 = 9`             |
| `[1, 2, 3, 4, 6]`     | `6`  | `[1, 3]` | `2 + 4 = 6`             |
| `[-3, -1, 0, 2, 4, 5]`| `1`  | `[1, 3]` | `-1 + 2 = 1`            |
| `[1, 2, 3]`           | `7`  | `[]`     | unmoeglich              |

## Idee -- Two Pointers (O(n))

Da die Liste sortiert ist, können wir mit zwei Zeigern von aussen
nach innen wandern.

```python
def zwei_summe_sortiert(zahlen, ziel):
    links, rechts = 0, len(zahlen) - 1
    while links < rechts:
        s = zahlen[links] + zahlen[rechts]
        if s == ziel:
            return [links, rechts]
        if s < ziel:
            links += 1
        else:
            rechts -= 1
    return []
```

## Warum nicht Brute-Force?

Bei `n = 10000` wären das 50 Mio. Vergleiche. Mit Two Pointers nur
10000. Ohne Sortierung müsste man Hash-Lookup nutzen (nachfolgende
Aufgabe 164).

## Vergleichbar

- **3-Sum**: drei Indizes mit Summe = Ziel (klassische Erweiterung).
- **K-Sum**: rekursive Verallgemeinerung.
- In der **Trapping-Rain-Water**-Aufgabe sind Two Pointers ebenfalls
  der Schlüssel.
