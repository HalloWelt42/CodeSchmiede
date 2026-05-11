---
schema_version: 1
id: 310-pairwise
revision: 1
titel: Pairwise -- aufeinanderfolgende Paare
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [generator, yield, listen, paare]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: itertools.pairwise nachbauen
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: pairwise
hints:
  - kosten: 0
    text: |
      Liefere alle UEBERLAPPENDEN Paare aufeinander folgender Elemente.
      [1,2,3,4] → [[1,2], [2,3], [3,4]].
      Intern Generator mit yield. Bei Liste der Laenge < 2 → [].
  - kosten: 15
    text: |
      Generator: for i in range(len-1): yield [a[i], a[i+1]].
      Oder zip(a, a[1:]).
tests_sichtbar:
  - input: [[1, 2, 3, 4]]
    expected: [[1, 2], [2, 3], [3, 4]]
  - input: [[]]
    expected: []
  - input: [[1]]
    expected: []
  - input: [[1, 2]]
    expected: [[1, 2]]
tests_versteckt:
  - input: [["a", "b", "c"]]
    expected: [["a", "b"], ["b", "c"]]
  - input: [[1, 1, 1, 1]]
    expected: [[1, 1], [1, 1], [1, 1]]
  - input: [[5, 10, 15, 20, 25]]
    expected: [[5, 10], [10, 15], [15, 20], [20, 25]]
  - input: [[true, false, true]]
    expected: [[true, false], [false, true]]
  - input: [[1, 2, 3, 4, 5, 6]]
    expected: [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
starter_code: |
  def pairwise(a: list) -> list[list]:
      # Tipp: yield in Generator, oder zip(a, a[1:])
      pass
---

# Pairwise -- aufeinanderfolgende Paare

Schreibe `pairwise(a)`, die alle **überlappenden Paare** aufeinander
folgender Elemente liefert.

Bei Liste der Laenge < 2 → `[]`.

## Beispiele

| Eingabe              | Ergebnis                                        |
|----------------------|--------------------------------------------------|
| `[1, 2, 3, 4]`       | `[[1, 2], [2, 3], [3, 4]]`                      |
| `[1, 2]`             | `[[1, 2]]`                                      |
| `[1]`                | `[]`                                            |
| `[]`                 | `[]`                                            |
| `["a", "b", "c"]`    | `[["a", "b"], ["b", "c"]]`                      |
| `[5, 10, 15, 20]`    | `[[5,10], [10,15], [15,20]]`                    |

## Idee 2 -- zip mit Slice (Pythonisch)

`zip(a, a[1:])` paart Element 0 mit 1, 1 mit 2, etc. -- super
elegant und in der Praxis das übliche Idiom.

## Idee 3 -- itertools.pairwise (Python 3.10+)

Die `pairwise`-Funktion gibt es seit Python 3.10 in `itertools`.

## Anwendung

- Differenzen aufeinander folgender Werte (Steigungen)
- "Hat sich was geändert?" Vergleich (Aufgabe 240)
- Bigram-Analyse in Texten
- Pfad-Segmente in Polylinien
