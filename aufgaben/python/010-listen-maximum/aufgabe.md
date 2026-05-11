---
schema_version: 1
id: 010-listen-maximum
revision: 1
titel: Größtes Element einer Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 8
tags: [listen, vergleich, schleifen]
pfade: [python_listen]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Klassiker für Vergleichs-Übung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: maximum
hints:
  - kosten: 0
    text: Vergleich mit `>`. Merke dir das bisher größte Element.
  - kosten: 3
    text: |
      Initialisiere mit dem ersten Element der Liste, vergleiche jedes
      weitere damit. Aber: Vorsicht bei leerer Liste!
  - kosten: 5
    text: |
      ```
      return max(zahlen) if zahlen else None
      ```
tests_sichtbar:
  - input: [[3, 1, 4, 1, 5]]
    expected: 5
  - input: [[10]]
    expected: 10
  - input: [[-5, -2, -8]]
    expected: -2
  - input: [[]]
    expected: null
tests_versteckt:
  - input: [[7, 7, 7]]
    expected: 7
  - input: [[1, 2, 3, 4, 5, 100]]
    expected: 100
  - input: [[-1, 0, 1]]
    expected: 1
  - input: [[42]]
    expected: 42
starter_code: |
  def maximum(zahlen: list[int]) -> int | None:
      # Deine Lösung hier
      pass
---

# Größtes Element einer Liste

Schreibe eine Funktion `maximum(zahlen)`, die das größte Element einer
Liste von Zahlen zurückgibt. Bei einer leeren Liste soll `None`
zurückgegeben werden.

## Beispiele

| Eingabe              | Ausgabe |
|----------------------|---------|
| `[3, 1, 4, 1, 5]`    | `5`     |
| `[-5, -2, -8]`       | `-2`    |
| `[10]`               | `10`    |
| `[]`                 | `None`  |

## Hinweise

- Negative Zahlen sind erlaubt -- `-2` ist größer als `-5`.
- Eine **leere Liste** ist der Sonderfall: `None` zurückgeben.
- Du darfst `max()` benutzen oder von Hand vergleichen.
