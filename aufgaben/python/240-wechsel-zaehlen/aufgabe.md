---
schema_version: 1
id: 240-wechsel-zaehlen
revision: 1
titel: Wechsel zum Vorgaenger zaehlen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [listen, vergleich, zip]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Adjacent-Differenz
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: wechsel
hints:
  - kosten: 0
    text: |
      Zaehle, wie oft sich ein Element zum direkten Vorgaenger
      unterscheidet.
      [1,1,2,2,3] → 2 (1->2 und 2->3).
      [] / [x] → 0.
  - kosten: 10
    text: |
      sum(1 for a, b in zip(liste, liste[1:]) if a != b).
tests_sichtbar:
  - input: [[1, 1, 2, 2, 3]]
    expected: 2
  - input: [[1, 1, 1]]
    expected: 0
  - input: [[]]
    expected: 0
  - input: [[1, 2, 3, 4]]
    expected: 3
tests_versteckt:
  - input: [[5]]
    expected: 0
  - input: [[1, 2, 1, 2, 1]]
    expected: 4
  - input: [["a", "a", "b", "b", "a", "a"]]
    expected: 2
  - input: [[true, false, true]]
    expected: 2
  - input: [[1, 1, 1, 1, 1, 1, 2]]
    expected: 1
  - input: [[1, 2, 2, 3, 3, 3, 4]]
    expected: 3
starter_code: |
  def wechsel(liste: list) -> int:
      # Deine Lösung hier
      pass
---

# Wechsel zum Vorgaenger zaehlen

Schreibe `wechsel(liste)`, die zaehlt, wie oft sich ein Element zum
direkten **Vorgaenger** unterscheidet.

Bei leerer oder einelementiger Liste → `0`.

## Beispiele

| Liste                    | Wechsel | Erklaerung                |
|--------------------------|---------|----------------------------|
| `[1, 1, 2, 2, 3]`        | `2`     | 1→2, 2→3                   |
| `[1, 1, 1]`              | `0`     | nichts wechselt            |
| `[1, 2, 3, 4]`           | `3`     | jeder Schritt              |
| `[1, 2, 1, 2, 1]`        | `4`     | hin und her                |
| `["a","a","b","b","a"]`  | `2`     | a→b, b→a                   |

## Idee

```python
def wechsel(liste):
    return sum(1 for a, b in zip(liste, liste[1:]) if a != b)
```

`zip(liste, liste[1:])` paart aufeinanderfolgende Elemente -- ein
Pattern, das auch in **230-ist-aufsteigend** vorkommt.

## Verwandt -- Run-Length-Encoding

Die Anzahl der Wechsel ist gleich (Anzahl Runs - 1):

```
[1, 1, 2, 2, 3]
 \__/ \__/ \_/  → 3 Runs → 2 Wechsel
```

Wer Aufgabe **035-run-length** geloest hat, sieht das Pattern.

## Anwendung

- **Edge Detection** in Bildreihen (1D).
- **Trends** in Zeitreihen: wie oft kippt der Vorzeichen-Wechsel?
- **Kontur-Analyse** in Pixel-Reihen.
