---
schema_version: 1
id: 221-vorkommen-zaehlen
revision: 1
titel: Vorkommen eines Werts in Liste zählen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [listen, zaehlen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Listen-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: vorkommen
hints:
  - kosten: 0
    text: |
      Wie oft kommt "wert" in der Liste vor?
      [1,2,3,2,1] mit wert=2 → 2.
      Bei leerer Liste -> 0.
  - kosten: 5
    text: |
      list.count(wert) macht es in einem Aufruf.
tests_sichtbar:
  - input: [[1, 2, 3, 2, 1], 2]
    expected: 2
  - input: [[], 5]
    expected: 0
  - input: [[1, 1, 1], 1]
    expected: 3
  - input: [[1, 2, 3], 4]
    expected: 0
tests_versteckt:
  - input: [["a", "b", "a", "c", "a"], "a"]
    expected: 3
  - input: [[true, false, true, true], true]
    expected: 3
  - input: [[null, null, 1], null]
    expected: 2
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5]
    expected: 1
  - input: [[0, 0, 0, 0, 0], 0]
    expected: 5
  - input: [[1.5, 2.5, 1.5], 1.5]
    expected: 2
starter_code: |
  def vorkommen(liste: list, wert) -> int:
      # Deine Lösung hier
      pass
---

# Vorkommen eines Werts in Liste zählen

Schreibe `vorkommen(liste, wert)`, die zählt, wie oft `wert` in
`liste` vorkommt.

Bei leerer Liste → `0`.

## Beispiele

| Liste              | Wert | Anzahl |
|--------------------|------|--------|
| `[1, 2, 3, 2, 1]`  | `2`  | `2`    |
| `[1, 1, 1]`        | `1`  | `3`    |
| `[1, 2, 3]`        | `4`  | `0`    |
| `["a", "b", "a"]`  | `"a"`| `2`    |
| `[]`               | `5`  | `0`    |

## Idee 1 -- Builtin

`list.count` ist in C implementiert -- maximal schnell.

## Idee 2 -- per Comprehension

Lehrreich, weil es das Pattern "zähle wie oft Bedingung wahr ist"
zeigt -- mit `sum(1 for ... if ...)`.

## Vergleich -- `count` vs `Counter`

| Aufgabe                          | Was?                  |
|----------------------------------|-----------------------|
| `liste.count(wert)`              | EINE Anzahl           |
| `Counter(liste)`                 | ALLE Anzahlen         |
| `Counter(liste).most_common(3)`  | Top 3 häufigste      |

Wenn man **mehrere** Werte zählen will, ist `Counter` effizienter
(eine Schleife), sonst ist `count` direkt.
