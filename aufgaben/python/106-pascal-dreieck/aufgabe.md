---
schema_version: 1
id: 106-pascal-dreieck
revision: 1
titel: Pascalsches Dreieck
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [zahlen, listen, kombinatorik]
pfade: [python_mathe2]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Pascalsches_Dreieck
  notiz: Klassische Mathe-Aufgabe, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: pascal
hints:
  - kosten: 0
    text: |
      Zeile 0: [1]. Zeile 1: [1, 1]. Jede weitere Zeile: aussen 1,
      innen Summe der zwei Werte direkt darüber.
  - kosten: 9
    text: |
      Aus Zeile `[a, b, c, d]` wird die nächste:
      `[1, a+b, b+c, c+d, 1]`.

      Mit zip eleganter:
      `[1] + [x+y for x, y in zip(zeile, zeile[1:])] + [1]`
tests_sichtbar:
  - input: [0]
    expected: []
  - input: [1]
    expected: [[1]]
  - input: [3]
    expected: [[1], [1, 1], [1, 2, 1]]
  - input: [5]
    expected: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
tests_versteckt:
  - input: [2]
    expected: [[1], [1, 1]]
  - input: [4]
    expected: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
  - input: [7]
    expected: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]
  - input: [10]
    expected: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
starter_code: |
  def pascal(n: int) -> list[list[int]]:
      # Deine Lösung hier -- erste n Zeilen des Pascalschen Dreiecks.
      pass
---

# Pascalsches Dreieck

Schreibe eine Funktion `pascal(n)`, die die ersten `n` Zeilen des
**Pascalschen Dreiecks** als Liste von Listen zurückgibt.

## Aufbau

```
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
   1 5 10 10 5 1
```

Außenrand immer `1`, jeder innere Wert ist die **Summe der zwei
Werte direkt darüber**.

## Beispiele

| `n` | Ergebnis                                                      |
|-----|---------------------------------------------------------------|
| `0` | `[]`                                                          |
| `1` | `[[1]]`                                                       |
| `3` | `[[1], [1,1], [1,2,1]]`                                       |
| `5` | `[[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]`               |

## Hintergrund

Die Werte sind die **Binomialkoeffizienten** $\binom{n}{k}$. Blaise
Pascal hat 1654 darüber geschrieben, aber die Anordnung war in
China und Persien Jahrhunderte vorher bekannt -- bei Yang Hui und
Omar Khayyám.
