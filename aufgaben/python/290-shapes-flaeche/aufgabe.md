---
schema_version: 1
id: 290-shapes-flaeche
revision: 1
titel: Shapes mit Flaechen-Polymorphismus
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 40
schaetz_minuten: 15
tags: [oop, vererbung, polymorphismus, geometrie]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Polymorphismus-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: gesamt_flaeche
hints:
  - kosten: 0
    text: |
      Liste von Shape-Beschreibungen → Gesamt-Flaeche (auf 2 Nachkomma).
      Shape-Form: ["kreis", radius]
                  ["rechteck", breite, höhe]
                  ["dreieck", a, b, c]   (Heron)
      Negative oder ungültige Shapes → 0 (überspringen).
  - kosten: 25
    text: |
      Basis-Klasse Shape mit Methode flaeche().
      Subklassen Kreis/Rechteck/Dreieck implementieren flaeche().
      Funktion baut die Shapes und summiert flaeche().
tests_sichtbar:
  - input: [[["kreis", 1]]]
    expected: 3.14
  - input: [[]]
    expected: 0.0
  - input: [[["rechteck", 3, 4]]]
    expected: 12.0
  - input: [[["dreieck", 3, 4, 5]]]
    expected: 6.0
tests_versteckt:
  - input: [[["kreis", 2], ["rechteck", 2, 2]]]
    expected: 16.57
  - input: [[["kreis", 1], ["kreis", 1], ["kreis", 1]]]
    expected: 9.42
  - input: [[["dreieck", 5, 12, 13], ["rechteck", 10, 5]]]
    expected: 80.0
  - input: [[["kreis", -5]]]
    expected: 0.0
  - input: [[["rechteck", 0, 5]]]
    expected: 0.0
  - input: [[["dreieck", 1, 2, 5]]]
    expected: 0.0
  - input: [[["kreis", 10], ["unbekannt", 1, 2]]]
    expected: 314.16
starter_code: |
  import math

  def gesamt_flaeche(shapes: list) -> float:
      # Tipp: Basis-Klasse Shape, Subklassen Kreis/Rechteck/Dreieck
      pass
---

# Shapes mit Flaechen-Polymorphismus

Implementiere `gesamt_flaeche(shapes)` -- eine Liste von Shape-
Beschreibungen wird zur **Gesamt-Flaeche** addiert.

## Shape-Formate

| Form                      | Bedeutung                          |
|---------------------------|------------------------------------|
| `["kreis", r]`            | Kreis mit Radius r                 |
| `["rechteck", b, h]`      | Rechteck Breite x Höhe            |
| `["dreieck", a, b, c]`    | Dreieck mit Seitenlaengen a, b, c (Heron) |

Ungültige Shapes (negative Werte, unbekannter Typ, Dreiecks-
Ungleichung verletzt) zählen mit Flaeche **0**.

Auf **2 Nachkommastellen** gerundet.

## Beispiele

| Shapes                                  | Flaeche  |
|-----------------------------------------|----------|
| `[["kreis", 1]]`                        | `3.14`   |
| `[["rechteck", 3, 4]]`                  | `12.0`   |
| `[["dreieck", 3, 4, 5]]`                | `6.0`    |
| `[["kreis", 2], ["rechteck", 2, 2]]`    | `16.57`  |
| `[["dreieck", 5, 12, 13], ["rechteck", 10, 5]]` | `80.0` |
| `[["kreis", -5]]`                       | `0.0`    |
| `[["unbekannt", 1, 2]]`                 | `0.0`    |
| `[]`                                    | `0.0`    |

## Konzepte

- **Vererbung**: alle Shapes erben von der Basis.
- **Polymorphismus**: `shape.flaeche()` macht das Richtige, egal
  welche konkrete Klasse.
- **Factory-Pattern**: `baue(spec)` wählt die richtige Klasse.

## Anwendung

Diese Idee steckt in **CAD-Tools** (jede Form weiss ihre Flaeche),
**Spielen** (jede Figur weiss ihre Hitbox), **Layout-Engines**
(jedes Widget seine Größe).
