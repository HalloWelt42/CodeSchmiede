---
schema_version: 1
id: 338-js-map-range
revision: 1
titel: JavaScript -- Wert in anderen Bereich uebersetzen
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [javascript, mathematik, interpolation]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Map_range
  notiz: Rosetta Code -- Map range, JS
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: mapRange
hints:
  - kosten: 0
    text: |
      Linear-Interpolation: x aus [a1, a2] in [b1, b2].
      Auf 4 Nachkommastellen runden. Bei a1 == a2 -> b1.
  - kosten: 10
    text: |
      Math.round((b1 + (x - a1) * (b2 - b1) / (a2 - a1)) * 10000) / 10000
tests_sichtbar:
  - input: [5, 0, 10, 0, 100]
    expected: 50
  - input: [0, 0, 10, 0, 100]
    expected: 0
  - input: [10, 0, 10, 0, 100]
    expected: 100
  - input: [5, 0, 0, 100, 200]
    expected: 100
starter_code: |
  function mapRange(x, a1, a2, b1, b2) {
      // Tipp: lineare Formel + Math.round mit Faktor
  }
---

# JavaScript -- Wert in anderen Bereich uebersetzen

Schreibe `mapRange(x, a1, a2, b1, b2)`, die `x` aus `[a1, a2]`
linear in `[b1, b2]` uebersetzt.

Auf 4 Nachkommastellen gerundet. Bei `a1 == a2` -> `b1`.

## Formel

$$y = b_1 + (x - a_1) \cdot \frac{b_2 - b_1}{a_2 - a_1}$$

## Beispiele

| x   | [a1, a2] | [b1, b2]   | Ergebnis |
|-----|----------|------------|----------|
| `5` | `[0,10]` | `[0,100]`  | `50`     |
| `0` | `[0,10]` | `[0,100]`  | `0`      |
| `25`| `[0,100]`| `[-50,50]` | `-25`    |

## Idee

JavaScript hat kein `round(x, n)` mit Nachkommastellen-Argument
wie Python. Der Trick `Math.round(y * 10^n) / 10^n` macht es per
Hand.

## Anwendung in Web-UIs

- **CSS-Variablen** dynamisch berechnen: Slider-Wert -> Farbe
- **Canvas-Animationen**: Frame -> Position
- **Sensor-Daten** (Web-Bluetooth, MediaDevices) auf UI-Werte

## Stolperstein -- Float-Praezision

Float-Arithmetik kann Werte wie `49.99999999998` produzieren --
darum die explizite Rundung. Bei reiner Anzeige reicht
`y.toFixed(4)`, aber das liefert einen String. Hier wollen wir
ein Number.
