---
schema_version: 1
id: 193-dreieck-typ
revision: 1
titel: Dreieck-Typ aus drei Seiten
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [mathematik, geometrie, set, vergleich]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Klassifikation
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: dreieck_typ
hints:
  - kosten: 0
    text: |
      Bestimme den Dreieck-Typ aus drei Seitenlaengen:
      "ungültig" (Dreiecksungleichung verletzt oder Seite <= 0),
      "gleichseitig" (alle drei gleich),
      "gleichschenklig" (mind. zwei gleich),
      "ungleichseitig" (alle verschieden).
  - kosten: 10
    text: |
      Prüfe zuerst Gültigkeit: alle > 0 UND laengste Seite kleiner
      als Summe der anderen beiden. Dann set-Trick für den Typ.
tests_sichtbar:
  - input: [3, 3, 3]
    expected: "gleichseitig"
  - input: [3, 4, 5]
    expected: "ungleichseitig"
  - input: [5, 5, 8]
    expected: "gleichschenklig"
  - input: [1, 2, 5]
    expected: "ungueltig"
tests_versteckt:
  - input: [0, 1, 1]
    expected: "ungueltig"
  - input: [-3, 4, 5]
    expected: "ungueltig"
  - input: [2, 2, 4]
    expected: "ungueltig"
  - input: [1, 1, 1]
    expected: "gleichseitig"
  - input: [10, 10, 10]
    expected: "gleichseitig"
  - input: [7, 5, 5]
    expected: "gleichschenklig"
  - input: [6, 7, 8]
    expected: "ungleichseitig"
  - input: [5, 5, 5]
    expected: "gleichseitig"
starter_code: |
  def dreieck_typ(a: float, b: float, c: float) -> str:
      # Deine Lösung hier
      pass
---

# Dreieck-Typ aus drei Seiten

Schreibe `dreieck_typ(a, b, c)`, die anhand dreier Seitenlaengen
einen der vier Typen liefert:

| Typ                | Bedingung                           |
|--------------------|--------------------------------------|
| `"ungültig"`      | mindestens eine Seite ≤ 0 ODER Dreiecksungleichung verletzt |
| `"gleichseitig"`   | alle drei Seiten gleich              |
| `"gleichschenklig"`| genau zwei Seiten gleich             |
| `"ungleichseitig"` | alle drei verschieden                |

## Dreiecksungleichung

Damit drei Strecken überhaupt ein Dreieck bilden können, muss die
laengste Seite **kleiner** als die Summe der anderen beiden sein.

Beispiel: `(2, 2, 4)` ist **kein** Dreieck, weil `2 + 2 = 4`
(degeneriert zu einem Strich).

## Beispiele

| Seiten          | Typ                  |
|-----------------|----------------------|
| `(3, 3, 3)`     | `"gleichseitig"`     |
| `(5, 5, 8)`     | `"gleichschenklig"`  |
| `(3, 4, 5)`     | `"ungleichseitig"`   |
| `(1, 2, 5)`     | `"ungültig"`        |
| `(0, 1, 1)`     | `"ungültig"`        |
| `(2, 2, 4)`     | `"ungültig"`        |

## Idee

```python
def dreieck_typ(a, b, c):
    if min(a, b, c) <= 0:
        return "ungültig"
    seiten = sorted([a, b, c])
    if seiten[0] + seiten[1] <= seiten[2]:
        return "ungültig"
    eindeutig = len(set([a, b, c]))
    if eindeutig == 1:
        return "gleichseitig"
    if eindeutig == 2:
        return "gleichschenklig"
    return "ungleichseitig"
```

## Hintergrund

In der Geometrie sind Dreiecke die einfachste polygonale Figur und
gleichzeitig die **stabilste** (deshalb Fachwerk-Konstruktionen).
Klassifikation nach Seiten ist nur eine Sicht -- die andere ist
nach Winkeln (spitz / recht / stumpf).
