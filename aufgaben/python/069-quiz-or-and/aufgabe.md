---
schema_version: 1
id: 069-quiz-or-and
revision: 1
titel: "or und and -- was kommt zurück?"
sprache: python
task_type: output_quiz
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 4
tags: [quiz, boolean, output, lesen]
pfade: [python_quiz]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Truthy/Falsy-Falle
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
hints: []
quiz:
  code: |
    a = 0 or "hallo"
    b = "" or [1, 2]
    c = "x" and 0
    d = 1 and 2 and 3
    print(a, b, c, d)
  optionen:
    - "True True False True"
    - "hallo [1, 2] 0 3"
    - "hallo [1, 2] False 3"
    - "0 [1, 2] 0 3"
  richtig_index: 1
---

# `or` und `and`: was kommt zurück?

Was wird hier gedruckt?

## Hintergrund

In Python liefern `or` und `and` **nicht** einfach `True` oder `False`,
sondern **einen der beiden Operanden**:

- `a or b`: liefert `a`, wenn `a` truthy ist; sonst `b`.
- `a and b`: liefert `a`, wenn `a` falsy ist; sonst `b`.

Falsy-Werte in Python: `False`, `0`, `0.0`, `""`, `[]`, `{}`,
`None`.

## Schritt für Schritt

| Ausdruck       | Ergebnis  | Wegen                         |
|----------------|-----------|-------------------------------|
| `0 or "hallo"` | `"hallo"` | `0` falsy -> nimm zweites     |
| `"" or [1,2]`  | `[1,2]`   | `""` falsy -> nimm zweites    |
| `"x" and 0`    | `0`       | `"x"` truthy -> nimm zweites  |
| `1 and 2 and 3`| `3`       | alle truthy -> letztes        |

## Praktischer Nutzen

`name = eingabe or "Anonym"` ist ein idiomatisches Default-Pattern.
