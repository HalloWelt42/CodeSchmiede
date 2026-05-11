---
schema_version: 1
id: 299-eigenes-map
revision: 1
titel: Eigenes map mit Operations-String
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [funktional, listen, mapping, dispatch]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Funktionales Pattern, Op als String
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: map_op
hints:
  - kosten: 0
    text: |
      Wende eine Operation auf jedes Element der Liste an.
      Operations: "double" (*2), "square" (^2), "negate" (-x),
      "increment" (+1), "absolute" (abs).
      Bei UNBEKANNTER Op → Original-Liste zurückgeben.
      Bei [] → [].
  - kosten: 10
    text: |
      Dict {op_name: lambda x: ...} und [tabelle[op](x) for x in liste].
      Bei unbekannter op → list(liste) zurück.
tests_sichtbar:
  - input: [[1, 2, 3], "double"]
    expected: [2, 4, 6]
  - input: [[1, 2, 3], "square"]
    expected: [1, 4, 9]
  - input: [[], "double"]
    expected: []
  - input: [[1, 2, 3], "unknown"]
    expected: [1, 2, 3]
tests_versteckt:
  - input: [[1, -2, 3], "negate"]
    expected: [-1, 2, -3]
  - input: [[0, 1, 2], "increment"]
    expected: [1, 2, 3]
  - input: [[-3, -2, 5], "absolute"]
    expected: [3, 2, 5]
  - input: [[5], "double"]
    expected: [10]
  - input: [[1, 2, 3, 4, 5], "square"]
    expected: [1, 4, 9, 16, 25]
  - input: [[100], "negate"]
    expected: [-100]
starter_code: |
  def map_op(liste: list, op: str) -> list:
      # Tipp: Dict {op_name: lambda x: ...} fuer Dispatch
      pass
---

# Eigenes map mit Operations-String

Schreibe `map_op(liste, op)`, die eine Operation auf **jedes Element**
der Liste anwendet -- nach dem `map`-Pattern.

## Verfügbare Operationen

| String        | Wirkung    |
|---------------|------------|
| `"double"`    | x * 2      |
| `"square"`    | x ** 2     |
| `"negate"`    | -x         |
| `"increment"` | x + 1      |
| `"absolute"`  | abs(x)     |

Unbekannte Operation → unveränderte Liste zurückgeben.

## Beispiele

| Liste            | Op            | Ergebnis           |
|------------------|---------------|---------------------|
| `[1, 2, 3]`      | `"double"`    | `[2, 4, 6]`        |
| `[1, 2, 3]`      | `"square"`    | `[1, 4, 9]`        |
| `[1, -2, 3]`     | `"negate"`    | `[-1, 2, -3]`      |
| `[0, 1, 2]`      | `"increment"` | `[1, 2, 3]`        |
| `[-3, -2, 5]`    | `"absolute"`  | `[3, 2, 5]`        |
| `[1, 2, 3]`      | `"unknown"`   | `[1, 2, 3]`        |

## Idee -- Dispatch-Dict

`abs` ist schon eine Funktion, kein Lambda nötig.

## Lehrziel

In echtem Python würde man die Funktion **direkt** übergeben:

Aber JSON-Tests können keine Funktionen serialisieren -- daher
der **String-Workaround**. Das Pattern (Dispatch-Dict) ist auch
in echten Code-Basen üblich, z.B. für **Plugin-Registries**
(siehe Aufgabe **165-tuerme-von-hanoi** wäre falsch -- besseres
Beispiel: die Prüfer-Registry des Codeschmiede-Backends).

## Pendant

- Aufgabe **300-eigenes-filter** mit Predicate-String.
- Aufgabe **301-eigenes-reduce** mit Op-String.
