---
schema_version: 1
id: 344-js-padovan-folge
revision: 1
titel: JavaScript -- Padovan-Folge
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [javascript, array, folgen, mathematik]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Padovan_sequence
  notiz: Rosetta Code -- Padovan sequence, JS
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: padovan
hints:
  - kosten: 0
    text: |
      P(0)=P(1)=P(2)=1, P(n) = P(n-2) + P(n-3).
      Liefere die ersten n Glieder. n <= 0 → [].
  - kosten: 10
    text: |
      Array mit [1,1,1] starten, in Schleife folge[folge.length - 2]
      + folge[folge.length - 3] anhaengen.
tests_sichtbar:
  - input: [0]
    expected: []
  - input: [1]
    expected: [1]
  - input: [3]
    expected: [1, 1, 1]
  - input: [10]
    expected: [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
starter_code: |
  function padovan(n) {
      // Tipp: Array mit [1,1,1] starten, Rekurrenz aus den letzten beiden
  }
---

# JavaScript -- Padovan-Folge

Schreibe `padovan(n)`, die die ersten `n` Glieder der Padovan-Folge
liefert.

`P(0) = P(1) = P(2) = 1`, `P(n) = P(n-2) + P(n-3)`.

`n <= 0` → `[]`.

## Beispiele

| n  | Folge                                          |
|----|------------------------------------------------|
| 0  | `[]`                                           |
| 3  | `[1, 1, 1]`                                    |
| 10 | `[1, 1, 1, 2, 2, 3, 4, 5, 7, 9]`               |

## Idee

```javascript
function padovan(n) {
    if (n <= 0) return [];
    const folge = [1, 1, 1];
    while (folge.length < n) {
        folge.push(folge[folge.length - 2] + folge[folge.length - 3]);
    }
    return folge.slice(0, n);
}
```

`folge.slice(0, n)` schneidet auf genau `n` Elemente -- bei `n < 3`
landen wir mit weniger als 3 Werten am Ende.

## Hintergrund

Padovan ist die "kleine Schwester" von Fibonacci -- gleiche Familie
linearer Rekurrenzen, andere Verzoegerung. Das Verhaeltnis
benachbarter Werte konvergiert gegen die **plastische Zahl**
$\rho \approx 1{,}3247$.
