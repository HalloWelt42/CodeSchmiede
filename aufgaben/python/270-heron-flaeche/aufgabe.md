---
schema_version: 1
id: 270-heron-flaeche
revision: 1
titel: Dreiecks-Flaeche nach Heron
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [mathematik, geometrie, sqrt, dreieck]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Heron-Formel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: dreieck_flaeche
hints:
  - kosten: 0
    text: |
      Flaeche aus drei Seitenlaengen via Heron.
      s = (a + b + c) / 2
      A = sqrt(s * (s-a) * (s-b) * (s-c))
      Auf 4 Nachkommastellen.
      Bei UNGUELTIGEM Dreieck (negative Seiten oder Dreiecks-
      ungleichung verletzt) → 0.0.
  - kosten: 15
    text: |
      Prüfe alle Seiten > 0 UND laengste < Summe der anderen.
      Dann Heron.
tests_sichtbar:
  - input: [3, 4, 5]
    expected: 6.0
  - input: [5, 5, 5]
    expected: 10.8253
  - input: [0, 1, 1]
    expected: 0.0
  - input: [1, 2, 5]
    expected: 0.0
tests_versteckt:
  - input: [6, 8, 10]
    expected: 24.0
  - input: [5, 12, 13]
    expected: 30.0
  - input: [7, 24, 25]
    expected: 84.0
  - input: [1, 1, 1]
    expected: 0.4330
  - input: [2, 2, 2]
    expected: 1.7321
  - input: [-1, 4, 5]
    expected: 0.0
  - input: [3, 3, 6]
    expected: 0.0
starter_code: |
  import math

  def dreieck_flaeche(a: float, b: float, c: float) -> float:
      # Deine Lösung hier -- Heron, ungueltig → 0.0
      pass
---

# Dreiecks-Flaeche nach Heron

Schreibe `dreieck_flaeche(a, b, c)`, die die Flaeche eines Dreiecks
aus drei Seitenlaengen berechnet -- via **Heron-Formel**.

Bei ungültigen Eingaben (Seite ≤ 0 oder Dreiecks-Ungleichung
verletzt) → `0.0`. Auf **4 Nachkommastellen** gerundet.

## Heron-Formel

$$s = \frac{a + b + c}{2} \qquad A = \sqrt{s(s-a)(s-b)(s-c)}$$

## Beispiele

| a | b | c  | Flaeche  | Bemerkung           |
|---|---|----|----------|---------------------|
| 3 | 4 | 5  | `6.0`    | rechtwinklig 3-4-5  |
| 6 | 8 | 10 | `24.0`   | doppelt 3-4-5       |
| 5 | 12| 13 | `30.0`   | rechtwinklig 5-12-13|
| 5 | 5 | 5  | `10.8253`| gleichseitig        |
| 1 | 1 | 1  | `0.4330` | Einheits-Dreieck    |
| 1 | 2 | 5  | `0.0`    | Ungültig (1+2 < 5) |

## Vergleich mit alternativer Formel

Bei spitzwinkligen Dreiecken auch:

$$A = \frac{1}{2} \cdot a \cdot b \cdot \sin(\gamma)$$

Brauchst Du den Winkel γ. Heron braucht **nur die Seitenlaengen**
-- daher beliebter, wenn keine Winkel gegeben sind.

## Hintergrund

Heron von Alexandria (ca. 60 n.Chr.) bewies die Formel. Sie ist eine
der wenigen geometrischen Formeln, die ohne Winkelfunktionen
auskommen -- und damit für **Vermessungen** vor der Trigonometrie
unbezahlbar war.
