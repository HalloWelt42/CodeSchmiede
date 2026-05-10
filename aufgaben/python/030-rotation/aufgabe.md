---
schema_version: 1
id: 030-rotation
revision: 1
titel: Liste rotieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [listen, slicing, modulo]
pfade: [python_listen]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Klassische Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: rotiere
hints:
  - kosten: 0
    text: |
      `k` Positionen nach links: nimm die ersten `k` Elemente und haenge
      sie ans Ende. Aber pass auf: `k` kann größer sein als die Liste.
  - kosten: 15
    text: |
      Mit Modulo gegen Ueberlauf:

      ```
      k = k % len(liste)
      return liste[k:] + liste[:k]
      ```
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 2]
    expected: [3, 4, 5, 1, 2]
  - input: [[1, 2, 3], 0]
    expected: [1, 2, 3]
  - input: [[1, 2, 3], 3]
    expected: [1, 2, 3]
  - input: [[1, 2, 3, 4], 5]
    expected: [2, 3, 4, 1]
tests_versteckt:
  - input: [[], 7]
    expected: []
  - input: [[1], 100]
    expected: [1]
  - input: [["a", "b", "c", "d", "e"], 1]
    expected: ["b", "c", "d", "e", "a"]
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7]
    expected: [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
starter_code: |
  def rotiere(liste: list, k: int) -> list:
      # Deine Lösung hier -- k Positionen nach links.
      pass
---

# Liste rotieren

Schreibe eine Funktion `rotiere(liste, k)`, die die Liste um `k`
Positionen **nach links** rotiert.

## Beispiele

| Eingabe              | Ergebnis           |
|----------------------|--------------------|
| `[1,2,3,4,5], 2`     | `[3,4,5,1,2]`      |
| `[1,2,3], 0`         | `[1,2,3]`          |
| `[1,2,3], 3`         | `[1,2,3]`          |
| `[1,2,3,4], 5`       | `[2,3,4,1]`        |
| `[], 7`              | `[]`               |

## Knackpunkt: k > len(liste)

`k` kann größer sein als die Liste. `5` Rotationen bei einer
4-elementigen Liste sind dasselbe wie `5 % 4 = 1` Rotation. Ohne
Modulo bekommst du einen `IndexError` -- oder schlimmer, einen still
falschen Wert.

Auch der **leere Fall** ist eine Falle: `len(liste) == 0` darf nicht
zur Division durch Null fuehren.

## Idee

```
k = k % len(liste)  # Achtung leerer Fall!
return liste[k:] + liste[:k]
```
