---
schema_version: 1
id: 244-gleitender-mittelwert
revision: 1
titel: Gleitender Mittelwert (Sliding Mean)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 25
schaetz_minuten: 12
tags: [listen, statistik, sliding-window]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassiker aus Zeitreihen-Analyse
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: gleitend
hints:
  - kosten: 0
    text: |
      Berechne den gleitenden Mittelwert über Fenstergröße k.
      Liste hat n Elemente -> Ergebnis hat (n - k + 1) Elemente.
      Werte auf 4 Nachkommastellen.
      Wenn k > n oder k <= 0 -> [].
  - kosten: 15
    text: |
      Pro Fenster: sum(liste[i:i+k]) / k. Komprehension über
      i in range(n - k + 1).
tests_sichtbar:
  - input: [[1, 2, 3, 4, 5], 3]
    expected: [2.0, 3.0, 4.0]
  - input: [[1, 2, 3], 1]
    expected: [1.0, 2.0, 3.0]
  - input: [[], 3]
    expected: []
  - input: [[1, 2, 3], 5]
    expected: []
tests_versteckt:
  - input: [[1, 2, 3, 4, 5], 5]
    expected: [3.0]
  - input: [[10, 20, 30, 40], 2]
    expected: [15.0, 25.0, 35.0]
  - input: [[1, 1, 1, 1, 1], 3]
    expected: [1.0, 1.0, 1.0]
  - input: [[1, 2, 3, 4, 5], 0]
    expected: []
  - input: [[5, 10, 15, 20, 25, 30], 3]
    expected: [10.0, 15.0, 20.0, 25.0]
  - input: [[100], 1]
    expected: [100.0]
starter_code: |
  def gleitend(zahlen: list[float], k: int) -> list[float]:
      # Deine Lösung hier -- Fenstergroesse k, jedes Fenster Mittelwert
      pass
---

# Gleitender Mittelwert (Sliding Mean)

Schreibe `gleitend(zahlen, k)`, die einen **gleitenden Mittelwert**
über die Liste mit Fenstergröße `k` berechnet. Liste der Laenge
`n` → Ergebnis der Laenge `n - k + 1`. Werte auf **4 Nachkomma**.

Bei `k > n` oder `k <= 0` → `[]`.

## Beispiele

| Liste              | k | Ergebnis            |
|--------------------|---|---------------------|
| `[1,2,3,4,5]`      | 3 | `[2.0, 3.0, 4.0]`   |
| `[1,2,3]`          | 1 | `[1.0, 2.0, 3.0]`   |
| `[1,2,3,4,5]`      | 5 | `[3.0]`             |
| `[10,20,30,40]`    | 2 | `[15.0, 25.0, 35.0]`|
| `[1,2,3]`          | 5 | `[]`                |

## Effizienz-Hinweis

Diese naive Variante ist `O(n * k)`. Mit einer **rollierenden Summe**
geht es in `O(n)`:

Bei sehr großen Listen oder großem `k` macht das einen Unterschied.

## Anwendung

- Zeitreihen-Glaettung (Finanzdaten, Sensor-Messungen).
- Bewegungsdaten (Schritte pro Tag, gleitend über 7 Tage).
- Bildverarbeitung: 1D-Box-Filter ist genau das.
