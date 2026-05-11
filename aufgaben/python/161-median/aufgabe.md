---
schema_version: 1
id: 161-median
revision: 1
titel: Median einer Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [statistik, sortieren, listen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Statistik-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: median
hints:
  - kosten: 0
    text: |
      Liefere den Median einer Liste von Zahlen.
      Bei leerer Liste -> None.
      Bei gerader Anzahl Elemente -> Mittelwert der zwei mittleren
      (als float).
  - kosten: 10
    text: |
      Liste sortieren. n = len. mid = n // 2.
      n % 2 == 1 -> sorted[mid].
      Sonst (sorted[mid - 1] + sorted[mid]) / 2.
tests_sichtbar:
  - input: [[1, 2, 3]]
    expected: 2
  - input: [[1, 2, 3, 4]]
    expected: 2.5
  - input: [[]]
    expected: null
  - input: [[5]]
    expected: 5
tests_versteckt:
  - input: [[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]]
    expected: 4
  - input: [[1, 2]]
    expected: 1.5
  - input: [[10, 20, 30, 40, 50]]
    expected: 30
  - input: [[1, 1, 1, 1]]
    expected: 1.0
  - input: [[-3, -1, 1, 3]]
    expected: 0.0
  - input: [[7, 7, 7]]
    expected: 7
starter_code: |
  def median(zahlen: list):
      # Deine Lösung hier -- None bei leerer Liste
      pass
---

# Median einer Liste

Schreibe eine Funktion `median(zahlen)`, die den **Median** einer
Liste von Zahlen liefert.

- Leere Liste → `None`.
- Ungerade Anzahl Elemente → mittleres Element (nach Sortieren).
- Gerade Anzahl Elemente → **Mittelwert der zwei mittleren** als `float`.

## Beispiele

| Liste                           | Median |
|---------------------------------|--------|
| `[1, 2, 3]`                     | `2`    |
| `[1, 2, 3, 4]`                  | `2.5`  |
| `[5]`                           | `5`    |
| `[]`                            | `None` |
| `[3, 1, 4, 1, 5, 9, 2, 6, 5]`   | `4`    |
| `[-3, -1, 1, 3]`                | `0.0`  |

## Median vs. Mittelwert

Der **Mittelwert** (Durchschnitt) ist anfaellig für Ausreisser
-- ein Millionaer im Raum hebt das Durchschnittsgehalt drastisch.
Der **Median** dagegen bleibt gleich. Darum gibt die Statistik bei
Vermoegens- und Lohnverteilungen meist den Median an, nicht den
Durchschnitt.

## Effizienz

Mit Sortieren: `O(n log n)`.
Es gibt einen `O(n)`-Algorithmus (**Quickselect** / Median-of-Medians),
aber die Sortier-Variante ist klar und schnell genug für alle
realistischen Listen.
