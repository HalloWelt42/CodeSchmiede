---
schema_version: 1
id: 341-equilibrium-index
revision: 1
titel: Gleichgewichts-Index in Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [listen, summe, prefix, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Equilibrium_index
  notiz: Rosetta Code -- Equilibrium index
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: gleichgewicht
hints:
  - kosten: 0
    text: |
      Liefere alle Indizes i, an denen sum(liste[:i]) == sum(liste[i+1:]).
      Aufsteigend sortiert.
      Bei [] → []. Bei einem Element → [0] (beide Seiten leer = 0).
  - kosten: 15
    text: |
      gesamt = sum(liste). links = 0. Iteriere: rechts = gesamt - links - x.
      Wenn links == rechts → Treffer. Dann links += x.
tests_sichtbar:
  - input: [[-7, 1, 5, 2, -4, 3, 0]]
    expected: [3, 6]
  - input: [[]]
    expected: []
  - input: [[5]]
    expected: [0]
  - input: [[1, 2, 3]]
    expected: []
tests_versteckt:
  - input: [[1, -1, 1, -1]]
    expected: []
  - input: [[0, 0, 0]]
    expected: [0, 1, 2]
  - input: [[1, 2, 0, 3]]
    expected: [2]
  - input: [[10, -10, 10]]
    expected: [0, 1, 2]
  - input: [[1, 2, 3, 4, 6]]
    expected: [3]
  - input: [[2, 4, 6]]
    expected: []
starter_code: |
  def gleichgewicht(liste: list[int]) -> list[int]:
      # Tipp: Praefix-Summe + laufende Differenz, O(n)
      pass
---

# Gleichgewichts-Index in Liste

Schreibe `gleichgewicht(liste)`, die alle Indizes `i` liefert, an
denen die **Summe links** von `i` gleich der **Summe rechts** von
`i` ist (jeweils ohne `liste[i]` selbst).

Indizes aufsteigend sortiert. Bei leerer Liste → `[]`. Bei einem
Element → `[0]` (beide Seiten leer).

## Beispiele

| Liste                       | Indizes       | Begruendung               |
|-----------------------------|----------------|----------------------------|
| `[-7, 1, 5, 2, -4, 3, 0]`   | `[3, 6]`      | i=3: -1 == -1; i=6: 0 == 0 |
| `[5]`                       | `[0]`         | links + rechts beide 0    |
| `[0, 0, 0]`                 | `[0, 1, 2]`   | jeder Index passt          |
| `[10, -10, 10]`             | `[1]`         | i=1: 10 == 10              |
| `[1, 2, 3, 4, 6]`           | `[3]`         | i=3: 1+2+3 == 6            |
| `[1, 2, 3]`                 | `[]`          | nirgendwo Gleichgewicht   |

## Idee -- O(n) mit laufender Differenz

```python
def gleichgewicht(liste):
    gesamt = sum(liste)
    links = 0
    out = []
    for i, x in enumerate(liste):
        rechts = gesamt - links - x
        if links == rechts:
            out.append(i)
        links += x
    return out
```

Eine Schleife. `links` wird laufend aufaddiert, `rechts` ist
immer "gesamt - links - aktuelles_element".

## Naiv -- O(n²)

```python
def gleichgewicht(liste):
    return [
        i for i in range(len(liste))
        if sum(liste[:i]) == sum(liste[i+1:])
    ]
```

Lesbar, aber bei jeder Iteration neue Summe -- zu langsam fuer
grosse Listen.

## Anwendung

- **Lastverteilung**: gleicher Aufwand auf beiden Seiten eines
  Punkts
- **Algorithmen-Klassiker** in Bewerbungsgespraechen
- **Praefix-Summen-Optimierung** -- Grundlage vieler Listen-Tricks
