---
schema_version: 1
id: 342-js-equilibrium-index
revision: 1
titel: JavaScript -- Gleichgewichts-Index
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [javascript, array, prefix-sum, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Equilibrium_index
  notiz: Rosetta Code -- Equilibrium index, JS
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: gleichgewicht
hints:
  - kosten: 0
    text: |
      Indizes wo links-Summe == rechts-Summe (jeweils ohne arr[i]).
      [] → []. Einzelelement → [0].
  - kosten: 15
    text: |
      reduce zur Gesamtsumme, dann eine Schleife mit laufender
      links-Summe.
tests_sichtbar:
  - input: [[-7, 1, 5, 2, -4, 3, 0]]
    expected: [3, 6]
  - input: [[]]
    expected: []
  - input: [[5]]
    expected: [0]
  - input: [[1, 2, 3]]
    expected: []
starter_code: |
  function gleichgewicht(arr) {
      // Tipp: Gesamtsumme einmal, dann eine Schleife
  }
---

# JavaScript -- Gleichgewichts-Index

Liefere alle Indizes `i`, an denen die Summe links von `i` gleich
der Summe rechts von `i` ist (beides ohne `arr[i]`).

Bei leerem Array → `[]`. Einzelelement → `[0]`.

## Beispiele

| Eingabe                     | Ergebnis        |
|-----------------------------|-----------------|
| `[-7, 1, 5, 2, -4, 3, 0]`   | `[3, 6]`        |
| `[0, 0, 0]`                 | `[0, 1, 2]`     |
| `[10, -10, 10]`             | `[1]`           |
| `[1, 2, 3]`                 | `[]`            |

## Idee -- O(n)

Ein-Pass-Algorithmus mit konstantem Extra-Speicher.

## Anwendung

Klassisches Bewerbungs-Problem. Variante: "kleinster i" (return
beim ersten Treffer) oder "ein-passendes i existiert" (boolean).
