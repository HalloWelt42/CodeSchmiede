---
schema_version: 1
id: 218-harmonisches-mittel
revision: 1
titel: Harmonisches Mittel
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [statistik, mathematik, kehrwert]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Statistik-Mittel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: harmonisches_mittel
hints:
  - kosten: 0
    text: |
      H = n / (1/x1 + 1/x2 + ... + 1/xn).
      Auf 4 Nachkommastellen gerundet.
      Bei leerer Liste → 0.0.
      Bei einer Null oder negativen Zahl → 0.0.
  - kosten: 10
    text: |
      Prüfe alle > 0. Dann n / sum(1/x for x in zahlen).
tests_sichtbar:
  - input: [[1, 2, 4]]
    expected: 1.7143
  - input: [[2, 2, 2]]
    expected: 2.0
  - input: [[]]
    expected: 0.0
  - input: [[5]]
    expected: 5.0
tests_versteckt:
  - input: [[1, 1, 1]]
    expected: 1.0
  - input: [[60, 30]]
    expected: 40.0
  - input: [[1, 2, 3, 4, 5]]
    expected: 2.1898
  - input: [[10, 20, 30, 40]]
    expected: 19.2
  - input: [[1, 0, 5]]
    expected: 0.0
  - input: [[-2, 4, 6]]
    expected: 0.0
starter_code: |
  def harmonisches_mittel(zahlen: list[float]) -> float:
      # Deine Lösung hier -- alle > 0 noetig
      pass
---

# Harmonisches Mittel

Schreibe `harmonisches_mittel(zahlen)`, das **harmonische Mittel**
einer Liste:

$$H = \frac{n}{\sum_{i=1}^n \frac{1}{x_i}}$$

Auf **4 Nachkommastellen** gerundet. Bei leerer Liste oder Werten
≤ 0 → `0.0`.

## Beispiele

| Liste              | H        | Bemerkung                |
|--------------------|----------|---------------------------|
| `[2, 2, 2]`        | `2.0`    | konstant                  |
| `[1, 2, 4]`        | `1.7143` | sehr nahe an Minimum      |
| `[60, 30]`         | `40.0`   | klassisches Beispiel      |
| `[1, 0, 5]`        | `0.0`    | Null vorhanden            |
| `[10, 20, 30, 40]` | `19.2`   |                           |

## Idee

```python
def harmonisches_mittel(zahlen):
    if not zahlen:
        return 0.0
    if any(x <= 0 for x in zahlen):
        return 0.0
    return round(len(zahlen) / sum(1 / x for x in zahlen), 4)
```

## Klassisches Beispiel -- Durchschnittsgeschwindigkeit

Du faehrst die ersten 60 km mit 60 km/h und die zweiten 60 km mit
30 km/h. Welche Durchschnittsgeschwindigkeit?

- Arithmetisch: `(60 + 30)/2 = 45 km/h` -- **falsch!**
- Harmonisch: `H = 2 / (1/60 + 1/30) = 40 km/h` -- **korrekt**.

Beweis: 60 km bei 60 km/h = 1h, 60 km bei 30 km/h = 2h, total
120 km in 3h = 40 km/h.

## Mittelwert-Hierarchie

Für positive Zahlen gilt **immer**:

$$H \le G \le A$$

(harmonisch ≤ geometrisch ≤ arithmetisch). Gleichheit nur, wenn
alle Zahlen gleich sind.

## Anwendung

- Geschwindigkeiten über gleiche Strecke (s.o.).
- F1-Score in Machine Learning (harmonisches Mittel von Precision
  und Recall).
- Parallel-Widerstaende: $1/R_{ges} = 1/R_1 + ... + 1/R_n$.
