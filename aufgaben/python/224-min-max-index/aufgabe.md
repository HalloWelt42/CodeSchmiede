---
schema_version: 1
id: 224-min-max-index
revision: 1
titel: Index von Minimum und Maximum
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [listen, suchen, min, max]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Listen-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: min_max_index
hints:
  - kosten: 0
    text: |
      Liefere [index_min, index_max] der Liste.
      Bei mehreren gleichen Min/Max-Werten: ERSTER Treffer.
      Bei leerer Liste → [-1, -1].
  - kosten: 7
    text: |
      liste.index(min(liste)) und liste.index(max(liste)).
tests_sichtbar:
  - input: [[3, 1, 4, 1, 5]]
    expected: [1, 4]
  - input: [[5]]
    expected: [0, 0]
  - input: [[]]
    expected: [-1, -1]
  - input: [[2, 2, 2]]
    expected: [0, 0]
tests_versteckt:
  - input: [[1, 2, 3, 4, 5]]
    expected: [0, 4]
  - input: [[5, 4, 3, 2, 1]]
    expected: [4, 0]
  - input: [[-3, -1, -5, -2]]
    expected: [2, 1]
  - input: [[10, 5, 10, 5, 10]]
    expected: [1, 0]
  - input: [[7, 7, 7, 1, 1]]
    expected: [3, 0]
  - input: [[100, -100]]
    expected: [1, 0]
starter_code: |
  def min_max_index(liste: list) -> list[int]:
      # Deine Lösung hier -- bei Gleichstand erster Treffer
      pass
---

# Index von Minimum und Maximum

Schreibe `min_max_index(liste)`, die `[index_min, index_max]`
zurückgibt -- die Positionen des kleinsten und größten Elements.

Bei mehreren gleichen Werten: **erster** Treffer.
Bei leerer Liste → `[-1, -1]`.

## Beispiele

| Liste              | Indizes  | Bemerkung               |
|--------------------|----------|-------------------------|
| `[3, 1, 4, 1, 5]`  | `[1, 4]` | min=1 bei 1, max=5 bei 4|
| `[5, 4, 3, 2, 1]`  | `[4, 0]` | min hinten, max vorn     |
| `[5]`              | `[0, 0]` | Min == Max               |
| `[2, 2, 2]`        | `[0, 0]` | erster bei Gleichstand   |
| `[]`               | `[-1, -1]`| leer                    |

## Idee 1 -- Builtins

Sehr lesbar, aber **3 Iterationen** durch die Liste (`min`, `max`,
`index`).

## Idee 2 -- in einer Schleife

Eine Schleife, weniger Vergleiche -- bei sehr großen Listen
relevant. Pythons Builtins sind aber so optimiert, dass die
Drei-Pass-Variante meist trotzdem schneller laeuft.

## Verwandt

- `min(liste)` / `max(liste)` → nur die **Werte**.
- `liste.index(x)` → nur **erster** Treffer eines Wertes.
- Aufgabe **161-median**, **162-häufigster-wert**.
