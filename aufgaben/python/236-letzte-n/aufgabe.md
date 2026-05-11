---
schema_version: 1
id: 236-letzte-n
revision: 1
titel: Letzte n Elemente einer Liste
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
  notiz: Pendant zu erste_n
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: letzte_n
hints:
  - kosten: 0
    text: |
      Liefere die letzten n Elemente einer Liste.
      n <= 0 → []. n > Listenlaenge → ganze Liste.
  - kosten: 10
    text: |
      list(liste[-n:]) hat einen Sonderfall: bei n == 0 ist [-0:]
      die ganze Liste, nicht []. Darum vorab prüfen.
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 3]
    expected: [3, 4, 5]
  - input: [[1, 2, 3], 0]
    expected: []
  - input: [[1, 2, 3], 10]
    expected: [1, 2, 3]
  - input: [[], 5]
    expected: []
tests_versteckt:
  - input: [[1, 2, 3], 1]
    expected: [3]
  - input: [[1, 2, 3], -1]
    expected: []
  - input: [["a", "b", "c", "d"], 2]
    expected: ["c", "d"]
  - input: [[1, 2, 3, 4, 5], 5]
    expected: [1, 2, 3, 4, 5]
  - input: [[42], 100]
    expected: [42]
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4]
    expected: [7, 8, 9, 10]
starter_code: |
  def letzte_n(liste: list, n: int) -> list:
      # Deine Lösung hier
      pass
---

# Letzte n Elemente einer Liste

Schreibe `letzte_n(liste, n)`, die die **letzten n Elemente** einer
Liste zurückgibt.

- `n <= 0` → `[]`
- `n > len(liste)` → ganze Liste

## Beispiele

| Liste              | n  | Ergebnis        |
|--------------------|----|-----------------|
| `[1, 2, 3, 4, 5]`  | 3  | `[3, 4, 5]`     |
| `[1, 2, 3]`        | 10 | `[1, 2, 3]`     |
| `[1, 2, 3]`        | 0  | `[]`            |
| `[1, 2, 3]`        | -1 | `[]`            |

## Idee

```python
def letzte_n(liste, n):
    if n <= 0:
        return []
    return list(liste[-n:])
```

## Stolperstein -- `liste[-0:]`

`liste[-0:]` ist nicht `[]`, sondern die **ganze Liste**, weil
`-0 == 0` und `liste[0:]` die ganze Liste ist. Darum `n <= 0`
explizit abfangen!

## Verwandt

- `erste_n` (Aufgabe 235): das andere Ende.
- `chunks` (Aufgabe 029): Liste in Bloecke teilen.
- `rotation` (030): zyklisch verschieben.
