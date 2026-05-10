---
schema_version: 1
id: 095-multiplikations-tabelle
revision: 1
titel: Multiplikations-Tabelle
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [matrix, listen, comprehension]
pfade: [python_logik]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Schul-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: einmaleins
hints:
  - kosten: 0
    text: |
      Doppelte Liste -- `[[1*1, 1*2, ...], [2*1, 2*2, ...], ...]`.
  - kosten: 10
    text: |
      Mit Comprehension:
      `[[i*j for j in range(1, n+1)] for i in range(1, n+1)]`.
tests_sichtbar:
  - input: [1]
    expected: [[1]]
  - input: [3]
    expected: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
  - input: [4]
    expected: [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
  - input: [0]
    expected: []
tests_versteckt:
  - input: [2]
    expected: [[1, 2], [2, 4]]
  - input: [5]
    expected: [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
  - input: [6]
    expected: [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18], [4, 8, 12, 16, 20, 24], [5, 10, 15, 20, 25, 30], [6, 12, 18, 24, 30, 36]]
starter_code: |
  def einmaleins(n: int) -> list[list[int]]:
      # Deine Lösung hier -- n×n Tabelle, Eintrag (i,j) = i*j (1-basiert).
      pass
---

# Multiplikations-Tabelle

Schreibe eine Funktion `einmaleins(n)`, die die n×n
Multiplikations-Tabelle als Liste von Listen zurückgibt.

Eintrag bei Zeile $i$, Spalte $j$ (1-basiert) ist $i \cdot j$.

## Beispiele

| `n` | Ergebnis                                                |
|-----|---------------------------------------------------------|
| `1` | `[[1]]`                                                 |
| `2` | `[[1, 2], [2, 4]]`                                      |
| `3` | `[[1, 2, 3], [2, 4, 6], [3, 6, 9]]`                     |
| `0` | `[]`                                                    |

## Hintergrund

Das **kleine Einmaleins** ist eine Tabelle, die viele schon in der
Schule auswendig lernen. Programmiertechnisch ist es das einfachste
Beispiel für eine Matrix-Erzeugung mit zwei verschachtelten Schleifen.
