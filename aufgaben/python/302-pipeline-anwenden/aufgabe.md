---
schema_version: 1
id: 302-pipeline-anwenden
revision: 1
titel: Pipeline mehrerer Operationen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [funktional, listen, pipeline, dispatch]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Funktionales Pipeline-Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: pipeline
hints:
  - kosten: 0
    text: |
      Wende mehrere Operationen NACHEINANDER auf jedes Element an.
      Operations: "double", "square", "negate", "increment", "absolute"
      ["double", "increment"] auf 3 → ((3 * 2) + 1) = 7.
      Bei leerer ops-Liste → liste unverändert.
      Bei UNBEKANNTER Op → Op überspringen.
  - kosten: 15
    text: |
      Pro Element: durch alle Ops durchlaufen.
      Oder: pro Op die ganze Liste mit map_op transformieren.
tests_sichtbar:
  - input: [[1, 2, 3], ["double", "increment"]]
    expected: [3, 5, 7]
  - input: [[1, 2, 3], []]
    expected: [1, 2, 3]
  - input: [[1, 2, 3], ["square"]]
    expected: [1, 4, 9]
  - input: [[1, 2, 3], ["unknown"]]
    expected: [1, 2, 3]
tests_versteckt:
  - input: [[1, 2, 3], ["double", "double"]]
    expected: [4, 8, 12]
  - input: [[5], ["increment", "square"]]
    expected: [36]
  - input: [[-3, 2, -1], ["absolute", "double"]]
    expected: [6, 4, 2]
  - input: [[], ["double"]]
    expected: []
  - input: [[10], ["square", "negate"]]
    expected: [-100]
  - input: [[2, 3], ["increment", "increment", "increment"]]
    expected: [5, 6]
starter_code: |
  def pipeline(liste: list, ops: list[str]) -> list:
      # Tipp: Operations-Dispatch und durchlaufen
      pass
---

# Pipeline mehrerer Operationen

Schreibe `pipeline(liste, ops)`, die eine **Folge von Operationen**
auf jedes Element der Liste anwendet -- nacheinander, von links
nach rechts.

## Verfügbare Operationen

| String        | Wirkung    |
|---------------|------------|
| `"double"`    | x * 2      |
| `"square"`    | x ** 2     |
| `"negate"`    | -x         |
| `"increment"` | x + 1      |
| `"absolute"`  | abs(x)     |

Unbekannte Operation wird **übersprungen** (silently ignored).
Leere Op-Liste → Original-Liste zurück.

## Beispiele

| Liste       | Ops                          | Ergebnis     | Begruendung |
|-------------|------------------------------|---------------|-------------|
| `[1, 2, 3]` | `["double", "increment"]`    | `[3, 5, 7]`   | x*2+1      |
| `[5]`       | `["increment", "square"]`    | `[36]`        | (5+1)²     |
| `[10]`      | `["square", "negate"]`       | `[-100]`      | -(10²)     |
| `[-3, 2]`   | `["absolute", "double"]`     | `[6, 4]`      | abs(x)*2   |
| `[1, 2, 3]` | `[]`                         | `[1, 2, 3]`   | unverändert|

## Idee

Pro Operation wird die ganze Liste neu transformiert -- klar lesbar,
einfach zu erweitern.

## Aequivalente Variante

Pro Element wird durch alle Ops gefaltet. Aequivalent für pure
Funktionen, anders bei seitlichen Effekten (z.B. Logging pro Op).

## Pattern

Pipelines sind in **Stream-Processing** (RxJS, Kafka), **Image-
Filtern** (PIL/OpenCV), **Build-Tools** (Webpack-Loaders) und
**Daten-Transformation** allgegenwaertig.
