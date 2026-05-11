---
schema_version: 1
id: 340-js-josephus
revision: 1
titel: JavaScript -- Josephus-Problem
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [javascript, algorithmen, modulo, klassiker]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Josephus_problem
  notiz: Rosetta Code -- Josephus problem, JS
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: josephus
hints:
  - kosten: 0
    text: |
      n Personen im Kreis, jede k-te eliminiert. Liefere Index des
      Letzten. n <= 0 oder k <= 0 → -1.
      Beispiel: n=5, k=2 → 2.
  - kosten: 20
    text: |
      Iterative Rekurrenz: let j = 0; for (let i = 2; i <= n; i++) j = (j + k) % i;
tests_sichtbar:
  - input: [5, 2]
    expected: 2
  - input: [1, 1]
    expected: 0
  - input: [0, 3]
    expected: -1
  - input: [7, 3]
    expected: 3
starter_code: |
  function josephus(n, k) {
      // Tipp: iterative Rekurrenz J(i) = (J(i-1) + k) % i
  }
---

# JavaScript -- Josephus-Problem

`n` Personen stehen im Kreis (Index `0..n-1`). Jede `k`-te wird
eliminiert. Wer überlebt?

`n <= 0` oder `k <= 0` → `-1`.

## Beispiele

| n  | k | Sieger |
|----|---|--------|
| 5  | 2 | `2`    |
| 7  | 3 | `3`    |
| 10 | 1 | `9`    |
| 41 | 3 | `30`   |

## Idee -- Rekurrenz O(n)

`J(1) = 0`. Pro hinzukommender Person verschiebt sich der Sieger
um `k` modulo der neuen Anzahl.

## Hintergrund

Benannt nach **Flavius Josephus** (1. Jh.), der laut Legende
diesen Trick beim Yodfat-Selbstmord-Pakt nutzte um zu überleben.

## Vergleich mit Python

Beide Sprachen haben den selben Modulo-Operator `%` und gleiche
for-Loop-Syntax -- die Lösungen sind nahezu identisch. Auch die
asymptotische Laufzeit `O(n)` ist gleich.
