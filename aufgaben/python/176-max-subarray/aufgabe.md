---
schema_version: 1
id: 176-max-subarray
revision: 1
titel: Maximale Teilfolgen-Summe (Kadane)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 38
schaetz_minuten: 15
tags: [listen, dp, algorithmen, kadane]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode 53 -- Maximum Subarray (Kadane 1984)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: max_summe
hints:
  - kosten: 0
    text: |
      Liefere die maximale Summe einer zusammenhängenden Teil-Liste.
      Bei nur negativen Werten: das größte Element.
      Bei leerer Liste -> 0.
  - kosten: 20
    text: |
      Kadane: laufende Summe, die bei negativem Wert auf 0 reset wird.
      In O(n):
        akt = max(x, akt + x)
        bestes = max(bestes, akt)
tests_sichtbar:
  - input: [[-2, 1, -3, 4, -1, 2, 1, -5, 4]]
    expected: 6
  - input: [[1, 2, 3, 4]]
    expected: 10
  - input: [[-1, -2, -3]]
    expected: -1
  - input: [[]]
    expected: 0
tests_versteckt:
  - input: [[5]]
    expected: 5
  - input: [[-5]]
    expected: -5
  - input: [[0, 0, 0, 0]]
    expected: 0
  - input: [[1, -1, 1, -1, 1, -1]]
    expected: 1
  - input: [[10, -3, 4, -1, 5]]
    expected: 15
  - input: [[-2, -3, 4, -1, -2, 1, 5, -3]]
    expected: 7
  - input: [[100, -1000, 100]]
    expected: 100
starter_code: |
  def max_summe(zahlen: list[int]) -> int:
      # Deine Lösung hier -- Kadane in O(n)
      pass
---

# Maximale Teilfolgen-Summe (Kadane)

Schreibe `max_summe(zahlen)`, die die **größte Summe** einer
zusammenhängenden Teil-Liste liefert.

- Leere Liste → `0`.
- Liste nur mit negativen Werten → größtes (am wenigsten negatives) Element.

## Beispiele

| Liste                                  | Max-Summe | Teilfolge        |
|----------------------------------------|-----------|------------------|
| `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`      | `6`       | `[4, -1, 2, 1]`  |
| `[1, 2, 3, 4]`                         | `10`      | gesamte Liste    |
| `[-1, -2, -3]`                         | `-1`      | `[-1]`           |
| `[10, -3, 4, -1, 5]`                   | `15`      | gesamte Liste    |

## Kadane-Algorithmus (1984)

Linear, ohne DP-Tabelle:

Pro Element entscheiden wir: **dranbleiben** an der laufenden Summe,
oder mit dem aktuellen Element **neu starten**. Die maximale
gesehene Summe wird laufend mitgefuehrt.

## Erweiterung

Soll auch die **Teilfolge selbst** zurückgegeben werden, brauchen wir
zwei extra Indizes (Start des aktuellen Laufs, Start/Ende des bisher
besten Laufs). Komplexitaet bleibt `O(n)`.

## Hintergrund

Joseph Born Kadane fand den Algorithmus 1984 in seiner Statistik-
Vorlesung an der Carnegie Mellon University. Vorher waren nur
`O(n^2)`- und `O(n^3)`-Lösungen bekannt. Heute Standard-Beispiel
für **eindimensionale dynamische Programmierung**.
