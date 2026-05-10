---
schema_version: 1
id: 054-sliding-summe
revision: 1
titel: Maximum-Summe in Sliding-Window
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [listen, schleifen, sliding-window]
pfade: [python_listen3]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Klassisches Sliding-Window-Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: max_fenster_summe
hints:
  - kosten: 0
    text: |
      Naive Loesung: alle Fenster der Groesse k pruefen, jeweils
      summieren. O(n*k).
  - kosten: 15
    text: |
      Schneller: berechne die Summe des ersten Fensters einmal. Dann
      "rolle" das Fenster: addiere das neue Element rechts, ziehe
      das verlorene Element links ab.
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 2]
    expected: 9
  - input: [[5, 1, 1, 1, 5], 3]
    expected: 7
  - input: [[1], 1]
    expected: 1
  - input: [[3, -1, 2, -1, 5], 2]
    expected: 4
tests_versteckt:
  - input: [[10, 20, 30, 40, 50], 1]
    expected: 50
  - input: [[1, 2, 3, 4, 5], 5]
    expected: 15
  - input: [[-1, -2, -3, -4], 2]
    expected: -3
  - input: [[2, 1, 5, 1, 3, 2], 3]
    expected: 9
  - input: [[], 3]
    expected: 0
starter_code: |
  def max_fenster_summe(zahlen: list[int], k: int) -> int:
      # Deine Loesung hier -- groesste Summe ueber k aufeinander-
      # folgenden Elementen. Bei leerer Liste oder k > len(zahlen)
      # liefere 0.
      pass
---

# Maximum-Summe in Sliding-Window

Gegeben eine Liste von Zahlen und eine Fenstergroesse `k`. Finde die
**groesste Summe** ueber `k` aufeinanderfolgenden Elementen.

## Beispiele

| Liste              | k  | Ergebnis | Wegen           |
|--------------------|----|----------|-----------------|
| `[1,2,3,4,5]`      | 2  | `9`      | `4+5`           |
| `[5,1,1,1,5]`      | 3  | `7`      | `5+1+1` und `1+1+5` (egal) |
| `[1]`              | 1  | `1`      |                 |
| `[3,-1,2,-1,5]`    | 2  | `4`      | `-1+5`          |
| `[]`               | 3  | `0`      | leer            |

## Sliding-Window-Trick

Statt jedes Fenster komplett neu zu summieren, "rolle" das Fenster:

- Berechne die Summe des **ersten** Fensters einmal
- Schiebe es weiter: subtrahiere das verlorene linke Element, addiere
  das neue rechte Element

So sparen wir uns Rechenzeit -- $O(n)$ statt $O(n \cdot k)$.

## Hintergrund

Sliding-Window ist eines der wichtigsten Pattern fuer Listen-Probleme.
Wer das einmal verstanden hat, sieht es bei vielen scheinbar
unverwandten Aufgaben wieder.
