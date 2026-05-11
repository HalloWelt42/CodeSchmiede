---
schema_version: 1
id: 219-vereinigung
revision: 1
titel: Vereinigung zweier Listen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [listen, set, mengen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Set-Operation
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: vereinigung
hints:
  - kosten: 0
    text: |
      Liefere alle Elemente, die in a oder b vorkommen --
      eindeutig und aufsteigend sortiert.
  - kosten: 5
    text: |
      sorted(set(a) | set(b)) erledigt es in einem Ausdruck.
tests_sichtbar:
  - input: [[1, 2, 3], [3, 4, 5]]
    expected: [1, 2, 3, 4, 5]
  - input: [[], []]
    expected: []
  - input: [[1, 2], []]
    expected: [1, 2]
  - input: [[1, 1, 2, 2], [2, 2, 3, 3]]
    expected: [1, 2, 3]
tests_versteckt:
  - input: [[5, 5, 5], [5]]
    expected: [5]
  - input: [[10, 20, 30], [40, 50, 60]]
    expected: [10, 20, 30, 40, 50, 60]
  - input: [[-3, -1, 0], [-2, 0, 1]]
    expected: [-3, -2, -1, 0, 1]
  - input: [[1, 2, 3], [1, 2, 3]]
    expected: [1, 2, 3]
  - input: [[100], [200]]
    expected: [100, 200]
starter_code: |
  def vereinigung(a: list, b: list) -> list:
      # Deine Lösung hier -- aufsteigend sortiert, eindeutig
      pass
---

# Vereinigung zweier Listen

Schreibe `vereinigung(a, b)`, die alle Elemente aus `a` oder `b` als
**aufsteigend sortierte, eindeutige** Liste zurückgibt.

## Beispiele

| `a`              | `b`              | Vereinigung           |
|------------------|------------------|------------------------|
| `[1, 2, 3]`      | `[3, 4, 5]`      | `[1, 2, 3, 4, 5]`      |
| `[]`             | `[]`             | `[]`                   |
| `[1, 1, 2, 2]`   | `[2, 2, 3, 3]`   | `[1, 2, 3]`            |
| `[1, 2, 3]`      | `[1, 2, 3]`      | `[1, 2, 3]`            |

## Idee -- Set-Operation

Der `|`-Operator ist die Set-Vereinigung. Sehr lesbar, sehr schnell
(`O(n + m)`).

## Verwandte Operationen

| Operator | Bedeutung           | Aufgabe |
|----------|---------------------|---------|
| `&`      | Schnitt             | 171     |
| `\|`     | Vereinigung         | hier    |
| `-`      | Differenz           | 172     |
| `^`      | Symmetrische Diff.  | 220     |

## Anwendung

In Versionskontrolle: alle in mindestens einer Branch vorhandenen
Datei-Pfade. In Datenbank-Anfragen: `UNION` von zwei `SELECT`-
Ergebnissen.
