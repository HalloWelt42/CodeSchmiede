---
schema_version: 1
id: 324-js-power-set
revision: 1
titel: JavaScript -- Potenzmenge
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [javascript, kombinatorik, array, reduce, modern]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Power_set
  notiz: Rosetta Code -- Power Set, JS-Version
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: potenzmenge
hints:
  - kosten: 0
    text: |
      Liefere alle Teilmengen eines Arrays als Array von Arrays.
      Reihenfolge: nach Groesse aufsteigend, gleich gross dann
      lexikographisch.
      Bei [] -> [[]].
  - kosten: 20
    text: |
      Bit-Maskierung: fuer m = 0..2^n - 1 die Bits ausziehen.
      Dann sortieren mit (a.length - b.length) || a.localeCompare-Trick.
tests_sichtbar:
  - input: [[]]
    expected: [[]]
  - input: [[1]]
    expected: [[], [1]]
  - input: [[1, 2]]
    expected: [[], [1], [2], [1, 2]]
  - input: [[1, 2, 3]]
    expected: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
starter_code: |
  function potenzmenge(arr) {
      // Tipp: Bit-Maskierung von 0 bis 2^n - 1
  }
---

# JavaScript -- Potenzmenge

Schreibe `potenzmenge(arr)`, die alle Teilmengen eines Arrays
zurueckgibt -- inklusive leerer Menge und Gesamtmenge.

Reihenfolge: zuerst **Groesse aufsteigend**, innerhalb gleicher
Groesse **lexikographisch**.

## Beispiele

| Eingabe     | Ausgabe                                                 |
|-------------|---------------------------------------------------------|
| `[]`        | `[[]]`                                                  |
| `[1]`       | `[[], [1]]`                                             |
| `[1, 2]`    | `[[], [1], [2], [1, 2]]`                                |
| `[1, 2, 3]` | `[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]`     |

Anzahl: $2^n$ Teilmengen.

## Idee -- Bit-Maskierung

Jede Teilmenge entspricht einer Binaerzahl von 0 bis $2^n - 1$.
Bit `i` gesetzt ↔ Element `i` enthalten.

## Idee -- Reduce-Pattern (funktional)

Klassisches funktionales Pattern: starte mit `[[]]`, fuer jedes
Element x verdopple die Menge -- einmal ohne x, einmal mit x.

## Vergleich mit Python

Pythons `itertools.combinations(arr, k)` liefert gleich
gruppiert nach Groesse. In JS gibt es kein `itertools` -- man
baut es per `reduce` oder Bit-Maske selbst.
