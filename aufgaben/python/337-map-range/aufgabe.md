---
schema_version: 1
id: 337-map-range
revision: 1
titel: Wert linear in anderen Bereich übersetzen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [zahlen, mathematik, interpolation]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Map_range
  notiz: Rosetta Code -- Map range
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: map_range
hints:
  - kosten: 0
    text: |
      Wert x liegt in [a1, a2]. Liefere den entsprechenden Wert
      im Bereich [b1, b2] -- linear gemappt.
      Beispiel: x=5 in [0, 10] -> in [0, 100] = 50.
      Auf 4 Nachkommastellen runden.
      Wenn a1 == a2 -> b1 (Division durch 0 vermeiden).
  - kosten: 10
    text: |
      b1 + (x - a1) * (b2 - b1) / (a2 - a1) ist die Standard-Formel.
tests_sichtbar:
  - input: [5, 0, 10, 0, 100]
    expected: 50.0
  - input: [0, 0, 10, 0, 100]
    expected: 0.0
  - input: [10, 0, 10, 0, 100]
    expected: 100.0
  - input: [5, 0, 0, 100, 200]
    expected: 100.0
tests_versteckt:
  - input: [3, 0, 10, 0, 100]
    expected: 30.0
  - input: [50, 0, 100, 0, 1]
    expected: 0.5
  - input: [25, 0, 100, -50, 50]
    expected: -25.0
  - input: [0, -10, 10, 0, 100]
    expected: 50.0
  - input: [212, 32, 212, 0, 100]
    expected: 100.0
  - input: [98.6, 32, 212, 0, 100]
    expected: 37.0
  - input: [0, 0, 1, 100, 200]
    expected: 100.0
starter_code: |
  def map_range(x: float, a1: float, a2: float, b1: float, b2: float) -> float:
      # Tipp: lineare Formel, Division-by-zero abfangen
      pass
---

# Wert linear in anderen Bereich übersetzen

Schreibe `map_range(x, a1, a2, b1, b2)`, die einen Wert `x` aus dem
Bereich `[a1, a2]` linear in den Bereich `[b1, b2]` übersetzt.

Auf 4 Nachkommastellen gerundet. Bei `a1 == a2` (kein Bereich)
liefere `b1`.

## Formel

$$y = b_1 + (x - a_1) \cdot \frac{b_2 - b_1}{a_2 - a_1}$$

Die "Lineare Interpolation zwischen zwei Bereichen".

## Beispiele

| x  | [a1,a2]  | [b1,b2]   | Ergebnis | Bedeutung               |
|----|----------|-----------|----------|--------------------------|
| 5  | [0, 10]  | [0, 100]  | `50.0`   | Mitte -> Mitte           |
| 0  | [0, 10]  | [0, 100]  | `0.0`    | Anfang -> Anfang         |
| 10 | [0, 10]  | [0, 100]  | `100.0`  | Ende -> Ende             |
| 25 | [0, 100] | [-50, 50] | `-25.0`  | Verschiebung mit Skalierung |
| 98.6| [32,212]| [0, 100]  | `37.0`   | Fahrenheit -> Celsius    |

## Anwendung

- **Sensor-Werte**: Spannung 0-5V -> Temperatur -10..50°C
- **UI-Slider**: Position 0-100px -> Lautstärke 0.0-1.0
- **Animation**: Frame 0-60 -> Winkel 0-360°
- **Farbverlaeufe**: Gradient-Position -> Farbwert

## Erweiterung -- Clamp

Soll x **außerhalb** [a1, a2] auch korrekt arbeiten? Ohne Clamp
liegt das Ergebnis dann außerhalb [b1, b2]. Mit Clamp:

In Spielen oft so genutzt, damit kein Wert "explodiert".
