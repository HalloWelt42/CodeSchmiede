---
schema_version: 1
id: 029-chunks
revision: 1
titel: Liste in n-grosse Stücke teilen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 9
tags: [listen, slicing, schleifen]
pfade: [python_listen]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Klassische Aufgabe -- Slicing mit Schrittweite.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: chunks
hints:
  - kosten: 0
    text: |
      Schleife `for i in range(0, len(liste), n)` und nimm jeweils
      `liste[i:i+n]` als nächstes Stück.
  - kosten: 15
    text: |
      Eine Zeile mit Comprehension:

      ```
      return [liste[i:i+n] for i in range(0, len(liste), n)]
      ```

      Kein Padding -- der letzte Block kann kürzer sein.
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 2]
    expected: [[1, 2], [3, 4], [5]]
  - input: [[1, 2, 3, 4, 5, 6], 3]
    expected: [[1, 2, 3], [4, 5, 6]]
  - input: [[], 4]
    expected: []
  - input: [[1, 2, 3], 5]
    expected: [[1, 2, 3]]
tests_versteckt:
  - input: [[1, 2, 3, 4, 5, 6, 7], 1]
    expected: [[1], [2], [3], [4], [5], [6], [7]]
  - input: [["a", "b", "c", "d"], 2]
    expected: [["a", "b"], ["c", "d"]]
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4]
    expected: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
starter_code: |
  def chunks(liste: list, n: int) -> list[list]:
      # Deine Lösung hier -- letzter Block darf kürzer sein.
      pass
---

# Liste in n-grosse Stücke teilen

Schreibe eine Funktion `chunks(liste, n)`, die die Liste in
**zusammenhaengende Bloecke** der Groesse `n` zerlegt. Der letzte
Block darf kürzer sein, falls die Laenge nicht aufgeht.

## Beispiele

| Eingabe                       | Ergebnis                          |
|-------------------------------|-----------------------------------|
| `[1,2,3,4,5], 2`              | `[[1,2],[3,4],[5]]`               |
| `[1,2,3,4,5,6], 3`            | `[[1,2,3],[4,5,6]]`               |
| `[], 4`                       | `[]`                              |
| `[1,2,3], 5`                  | `[[1,2,3]]`                       |
| `[1,2,3,4,5,6,7], 1`          | `[[1],[2],[3],[4],[5],[6],[7]]`   |

## Idee

Schleife mit Schrittweite: `for i in range(0, len(liste), n)`. In jedem
Schritt liefert `liste[i:i+n]` den naechsten Block.

## Wo das nuetzlich ist

Pagination, Batch-Processing, Tabellen mit fester Zeilenzahl --
"chunked" Iteration ist eines der haeufigsten Pattern in
Daten-Pipelines.
