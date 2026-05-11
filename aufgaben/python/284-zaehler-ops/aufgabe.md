---
schema_version: 1
id: 284-zaehler-ops
revision: 1
titel: Zähler mit Operations-Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [oop, klassen, listen, schleifen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: OOP-Klasse intern, API liefert Daten
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zaehler_lauf
hints:
  - kosten: 0
    text: |
      Operationen auf einem Zähler (Start 0):
      "inc" → +1
      "dec" → -1
      "reset" → 0
      "double" → mal 2
      Liefere den Zähler nach JEDER Operation als Liste.
      Bei [] → [].
  - kosten: 15
    text: |
      Klasse Zähler mit Methoden inc/dec/reset/double.
      Pro Op aufrufen, Wert appenden.
tests_sichtbar:
  - input: [["inc", "inc", "inc"]]
    expected: [1, 2, 3]
  - input: [[]]
    expected: []
  - input: [["inc", "double", "double"]]
    expected: [1, 2, 4]
  - input: [["inc", "inc", "reset", "inc"]]
    expected: [1, 2, 0, 1]
tests_versteckt:
  - input: [["dec", "dec", "dec"]]
    expected: [-1, -2, -3]
  - input: [["inc", "inc", "inc", "inc", "double"]]
    expected: [1, 2, 3, 4, 8]
  - input: [["reset"]]
    expected: [0]
  - input: [["inc", "dec", "inc", "dec"]]
    expected: [1, 0, 1, 0]
  - input: [["double"]]
    expected: [0]
  - input: [["inc", "double", "double", "double", "double"]]
    expected: [1, 2, 4, 8, 16]
starter_code: |
  def zaehler_lauf(operationen: list[str]) -> list[int]:
      # Tipp: nutze intern eine Zaehler-Klasse
      pass
---

# Zähler mit Operations-Liste

Implementiere `zähler_lauf(operationen)` -- ein Zähler startet bei
**0**, eine Liste von Operationen wird nacheinander angewendet, und
nach **jeder** Operation wird der aktuelle Wert in die Ausgabe-Liste
geschrieben.

| Operation  | Wirkung      |
|------------|--------------|
| `"inc"`    | Wert + 1     |
| `"dec"`    | Wert - 1     |
| `"reset"`  | Wert = 0     |
| `"double"` | Wert mal 2   |

Bei leerer Liste → `[]`.

## Beispiele

| Operationen                              | Ausgabe        |
|------------------------------------------|-----------------|
| `["inc","inc","inc"]`                    | `[1,2,3]`       |
| `["inc","double","double"]`              | `[1,2,4]`       |
| `["inc","inc","reset","inc"]`            | `[1,2,0,1]`     |
| `["inc","double","double","double","double"]` | `[1,2,4,8,16]` |
| `["double"]`                             | `[0]` (0×2 = 0) |

## Stilfrage -- Dispatch per Methode

Statt `if/elif`-Kette könnte man jede Op als eigene Methode
implementieren und per `getattr(z, op)()` aufrufen. Das ist
elegant -- aber **gefaehrlich**, wenn die Op-Strings von Nutzern
kommen (Method-Injection).

Sicher und kurz: explizites Dispatch-Dict:

## Anwendung

Operations-Listen sind die Basis für **Event-Sourcing**, **Undo-
Stacks** und **State-Machines**.
