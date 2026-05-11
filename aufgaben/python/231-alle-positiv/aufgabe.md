---
schema_version: 1
id: 231-alle-positiv
revision: 1
titel: Alle Zahlen positiv?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [listen, all, vergleich]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Pruefung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: alle_positiv
hints:
  - kosten: 0
    text: |
      Pruefe ob alle Zahlen STRIKT positiv (> 0) sind.
      Null zaehlt nicht als positiv.
      Leere Liste → True (vacuous truth).
  - kosten: 5
    text: |
      all(x > 0 for x in zahlen).
tests_sichtbar:
  - input: [[1, 2, 3]]
    expected: true
  - input: [[1, 0, 2]]
    expected: false
  - input: [[]]
    expected: true
  - input: [[-1, 2]]
    expected: false
tests_versteckt:
  - input: [[1]]
    expected: true
  - input: [[0]]
    expected: false
  - input: [[-1]]
    expected: false
  - input: [[100, 200, 300]]
    expected: true
  - input: [[1, 2, 3, 4, 5, -1]]
    expected: false
  - input: [[0.5, 1.5, 2.5]]
    expected: true
  - input: [[1, 2, 0.0, 3]]
    expected: false
starter_code: |
  def alle_positiv(zahlen: list) -> bool:
      # Deine Lösung hier -- strikt > 0
      pass
---

# Alle Zahlen positiv?

Schreibe `alle_positiv(zahlen)`, die `True` zurueckgibt, wenn alle
Zahlen **strikt positiv** sind (`> 0`). Null zaehlt **nicht** als
positiv.

Leere Liste → `True` (vacuous truth).

## Beispiele

| Liste              | Alle positiv? |
|--------------------|---------------|
| `[1, 2, 3]`        | `True`        |
| `[1, 0, 2]`        | `False` (0 ist nicht positiv) |
| `[-1, 2]`          | `False`       |
| `[]`               | `True`        |
| `[0.5, 1.5, 2.5]`  | `True`        |
| `[100, 200, 300]`  | `True`        |

## Idee

```python
def alle_positiv(zahlen):
    return all(x > 0 for x in zahlen)
```

Pythons `all` liefert `True` bei leerem Iterable -- vacuous truth.
Bei nicht-leerem Iterable: `True` genau dann, wenn jedes Element
**truthy** ist. Mit dem Generator-Ausdruck pruefen wir die
Bedingung.

## Short-Circuit

`all` bricht beim **ersten False** ab -- bei `[1, 2, -1, 3, 4, 5, 6]`
wird nach `-1 > 0 → False` sofort zurueckgegeben. Effizient bei
langen Listen mit fruehem Treffer.

## Verwandte Pruefungen

| Funktion          | Beispiel-Code              | Bedeutung               |
|-------------------|-----------------------------|------------------------|
| `all(p)`          | `all(x > 0 for x in xs)`    | jede Bedingung wahr    |
| `any(p)`          | `any(x > 0 for x in xs)`    | mind. eine wahr        |
| `not any(p)`      | `not any(x < 0 for x in xs)`| keine wahr             |
| `not all(p)`      | `not all(x > 0 for x in xs)`| mind. eine falsch      |

Die DeMorgan-Tabelle in einer Tabelle.
