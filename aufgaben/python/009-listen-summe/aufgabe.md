---
schema_version: 1
id: 009-listen-summe
revision: 1
titel: Summe einer Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [listen, schleifen, akkumulator]
pfade: [python_listen]
voraussetzungen: []
quelle:
  url: null
  notiz: Erstes Beispiel im Aufgaben-Format-Dokument
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: summe
hints:
  - kosten: 0
    text: Eine Schleife mit `for` durchläuft alle Elemente.
  - kosten: 15
    text: |
      Initialisiere eine Variable mit `0`, addiere in der Schleife jedes
      Element dazu.
  - kosten: 30
    text: |
      Idiomatisch:

      ```
      return sum(zahlen)
      ```
tests_sichtbar:
  - input: [[1, 2, 3]]
    expected: 6
  - input: [[]]
    expected: 0
  - input: [[10]]
    expected: 10
  - input: [[-5, 5]]
    expected: 0
tests_versteckt:
  - input: [[1, -1, 1, -1]]
    expected: 0
  - input: [[100, 200, 300]]
    expected: 600
  - input: [[-5, -5, -5]]
    expected: -15
  - input: [[0, 0, 0, 0, 0]]
    expected: 0
starter_code: |
  def summe(zahlen: list[int]) -> int:
      # Deine Lösung hier
      pass
---

# Summe einer Liste

Schreibe eine Funktion `summe(zahlen)`, die die Summe aller Elemente
einer Liste von ganzen Zahlen zurückgibt.

## Beispiele

| Eingabe        | Ausgabe |
|----------------|--------:|
| `[1, 2, 3]`    | `6`     |
| `[]`           | `0`     |
| `[-5, 5]`      | `0`     |

## Hinweise

- Eine **leere Liste** soll `0` zurückgeben (Konvention: die Summe
  über das leere Produkt ist das neutrale Element der Addition).
- Negative Zahlen sind erlaubt.

> Mathematisch:
>
> $$\text{summe}([a_1, a_2, \dots, a_n]) = \sum_{i=1}^{n} a_i$$
