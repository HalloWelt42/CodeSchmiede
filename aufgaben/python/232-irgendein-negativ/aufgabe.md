---
schema_version: 1
id: 232-irgendein-negativ
revision: 1
titel: Gibt es eine negative Zahl?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [listen, any, vergleich]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Prüfung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: irgendein_negativ
hints:
  - kosten: 0
    text: |
      Prüfe ob mindestens eine Zahl negativ (< 0) ist.
      Null zählt nicht. Leere Liste → False.
  - kosten: 4
    text: |
      any(x < 0 for x in zahlen).
tests_sichtbar:
  - input: [[1, 2, -3]]
    expected: true
  - input: [[1, 2, 3]]
    expected: false
  - input: [[]]
    expected: false
  - input: [[0]]
    expected: false
tests_versteckt:
  - input: [[-1]]
    expected: true
  - input: [[1]]
    expected: false
  - input: [[-100, 200, 300]]
    expected: true
  - input: [[100, 200, -1]]
    expected: true
  - input: [[0, 0, 0, 0]]
    expected: false
  - input: [[-0.5, 1.5]]
    expected: true
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    expected: false
starter_code: |
  def irgendein_negativ(zahlen: list) -> bool:
      # Deine Lösung hier -- any mit < 0
      pass
---

# Gibt es eine negative Zahl?

Schreibe `irgendein_negativ(zahlen)`, die `True` zurückgibt, wenn
**mindestens eine** Zahl in der Liste **negativ** (`< 0`) ist.

Null zählt nicht. Leere Liste → `False`.

## Beispiele

| Liste              | Irgendeine negativ? |
|--------------------|----------------------|
| `[1, 2, -3]`       | `True`               |
| `[1, 2, 3]`        | `False`              |
| `[-1]`             | `True`               |
| `[]`               | `False`              |
| `[0]`              | `False` (0 ist nicht negativ) |
| `[100, 200, -1]`   | `True`               |

## Idee

Pythons `any` liefert `False` bei leerem Iterable, sonst `True`,
sobald **eine** Bedingung wahr ist.

## Short-Circuit

`any` bricht beim **ersten True** ab -- bei `[1, 2, -3, ...]` wird
sofort `True` zurückgegeben, ohne den Rest zu prüfen.

## DeMorgan-Tipp

Die folgenden Aussagen sind äquivalent:

- `any(x < 0 for x in xs)` (hier)
- `not all(x >= 0 for x in xs)`
- `min(xs, default=0) < 0` (etwas teurer, weil immer alles durch)

Aufgabe **231-alle-positiv** ist das Gegenstück.
