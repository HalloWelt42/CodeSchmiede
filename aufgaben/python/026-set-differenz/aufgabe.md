---
schema_version: 1
id: 026-set-differenz
revision: 1
titel: A ohne B
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [listen, sets, schleifen]
pfade: [python_sets]
voraussetzungen: [025-set-schnitt]
quelle:
  url: null
  notiz: Standard-Set-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ohne
hints:
  - kosten: 0
    text: Behalte alle Elemente aus `a`, die nicht in `b` vorkommen. Reihenfolge wie in a, ohne Doppelte.
  - kosten: 10
    text: |
      `set(b)` fuer schnellen Lookup, dann List-Comprehension mit
      Duplikat-Filter.
tests_sichtbar:
  - input: [[1, 2, 3, 4], [3, 4]]
    expected: [1, 2]
  - input: [[1, 2, 3], []]
    expected: [1, 2, 3]
  - input: [[1, 1, 2, 2, 3, 3], [2]]
    expected: [1, 3]
  - input: [["a", "b", "c"], ["b"]]
    expected: ["a", "c"]
tests_versteckt:
  - input: [[], [1, 2]]
    expected: []
  - input: [[1, 2, 3], [1, 2, 3]]
    expected: []
  - input: [[5, 4, 3, 2, 1], [3, 1]]
    expected: [5, 4, 2]
starter_code: |
  def ohne(a: list, b: list) -> list:
      # Deine Lösung hier -- a in seiner Reihenfolge, ohne b und ohne Doppelte.
      pass
---

# A ohne B

Schreibe eine Funktion `ohne(a, b)`, die alle Elemente von `a`
zurueckgibt, **die nicht in `b`** vorkommen. Reihenfolge wie in `a`,
jedes Element nur einmal.

## Beispiele

| `a`                | `b`     | Ergebnis    |
|--------------------|---------|-------------|
| `[1,2,3,4]`        | `[3,4]` | `[1,2]`     |
| `[1,2,3]`          | `[]`    | `[1,2,3]`   |
| `[1,1,2,2,3,3]`    | `[2]`   | `[1,3]`     |
| `["a","b","c"]`    | `["b"]` | `["a","c"]` |

## Idee

`set(b)` macht den "ist drin?"-Test schnell. Dann eine Schleife ueber
`a` mit Duplikat-Tracking -- entweder ueber ein zweites Set oder
implizit ueber das Prüfen `x not in ergebnis`.

## Vergleich mit Set-Operationen

In Python kannst du `set(a) - set(b)` schreiben -- das gibt dir aber
ein **Set ohne Reihenfolge**. Hier wollen wir die Reihenfolge von `a`
erhalten und brauchen daher die Schleifen-Variante.
