---
schema_version: 1
id: 258-liste-halbieren
revision: 1
titel: Liste in zwei Haelften aufteilen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [listen, slicing]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Aufteilung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: halbieren
hints:
  - kosten: 0
    text: |
      Teile die Liste in zwei Haelften: [erste_haelfte, zweite_haelfte].
      Bei UNGERADER Anzahl: das mittlere Element gehört zur ZWEITEN Haelfte.
      [1,2,3,4,5] → [[1,2], [3,4,5]].
      Bei [] → [[], []].
  - kosten: 10
    text: |
      mid = len(liste) // 2.
      [list(liste[:mid]), list(liste[mid:])].
tests_sichtbar:
  - input: [[1, 2, 3, 4]]
    expected: [[1, 2], [3, 4]]
  - input: [[1, 2, 3, 4, 5]]
    expected: [[1, 2], [3, 4, 5]]
  - input: [[]]
    expected: [[], []]
  - input: [[1]]
    expected: [[], [1]]
tests_versteckt:
  - input: [[1, 2]]
    expected: [[1], [2]]
  - input: [[1, 2, 3]]
    expected: [[1], [2, 3]]
  - input: [[1, 2, 3, 4, 5, 6]]
    expected: [[1, 2, 3], [4, 5, 6]]
  - input: [["a", "b", "c", "d", "e", "f", "g"]]
    expected: [["a", "b", "c"], ["d", "e", "f", "g"]]
  - input: [[10, 20, 30, 40, 50, 60, 70, 80]]
    expected: [[10, 20, 30, 40], [50, 60, 70, 80]]
starter_code: |
  def halbieren(liste: list) -> list[list]:
      # Deine Lösung hier -- bei ungerader Anzahl: mid in zweite Haelfte
      pass
---

# Liste in zwei Haelften aufteilen

Schreibe `halbieren(liste)`, die eine Liste in **zwei Haelften**
teilt: `[erste_haelfte, zweite_haelfte]`.

Bei **ungerader Anzahl**: das mittlere Element gehört zur **zweiten**
Haelfte.

## Beispiele

| Eingabe           | Ergebnis                  |
|-------------------|---------------------------|
| `[1, 2, 3, 4]`    | `[[1, 2], [3, 4]]`        |
| `[1, 2, 3, 4, 5]` | `[[1, 2], [3, 4, 5]]` (3 in 2. Haelfte) |
| `[1, 2, 3]`       | `[[1], [2, 3]]`           |
| `[1]`             | `[[], [1]]`               |
| `[]`              | `[[], []]`                |

## Idee

Pythons `//` rundet **ab** -- bei `len == 5` ist `mid = 2`, also
liegen Elemente 0-1 in der ersten Haelfte und 2-4 in der zweiten.

## Wenn die mittlere Stelle zur ERSTEN Haelfte soll

Mit `len == 5` ergibt das `3`, also `[1,2,3] | [4,5]`.

## Anwendung

- **Merge-Sort** (Aufgabe 051): rekursiv teilen.
- Layout-Engines: Eltern-Container in zwei Spalten teilen.
- Statistik: Median-Berechnung (Aufgabe 161).
