---
schema_version: 1
id: 292-dict-zu-json
revision: 1
titel: Dict zu JSON-String
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [json, serialisierung, dict]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 291
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: json_dump
hints:
  - kosten: 0
    text: |
      Serialisiere ein Python-Objekt (Dict, Liste, etc.) zu JSON-String.
      Schlüssel ALPHABETISCH sortiert.
      Keine Leerzeichen nach , und : (compact mode).
  - kosten: 10
    text: |
      json.dumps(obj, sort_keys=True, separators=(",", ":")).
tests_sichtbar:
  - input: [{"b": 2, "a": 1}]
    expected: '{"a":1,"b":2}'
  - input: [[]]
    expected: "[]"
  - input: [{}]
    expected: "{}"
  - input: [[1, 2, 3]]
    expected: "[1,2,3]"
tests_versteckt:
  - input: [{"x": "wert"}]
    expected: '{"x":"wert"}'
  - input: [42]
    expected: "42"
  - input: [null]
    expected: "null"
  - input: [true]
    expected: "true"
  - input: [{"name": "Hans", "alter": 30}]
    expected: '{"alter":30,"name":"Hans"}'
  - input: [{"verschachtelt": {"y": 2, "x": 1}}]
    expected: '{"verschachtelt":{"x":1,"y":2}}'
  - input: ["hallo"]
    expected: '"hallo"'
starter_code: |
  import json

  def json_dump(obj) -> str:
      # Deine Lösung hier -- sortiert, kompakt
      pass
---

# Dict zu JSON-String

Schreibe `json_dump(obj)`, die ein Python-Objekt in einen JSON-String
serialisiert -- mit zwei Konventionen:

1. **Schlüssel alphabetisch sortiert** (deterministische Ausgabe)
2. **Kompakt** (keine Leerzeichen nach `,` oder `:`)

## Beispiele

| Eingabe                          | JSON-String                         |
|----------------------------------|-------------------------------------|
| `{"b": 2, "a": 1}`               | `'{"a":1,"b":2}'`                   |
| `{"name": "Hans", "alter": 30}`  | `'{"alter":30,"name":"Hans"}'`      |
| `[1, 2, 3]`                      | `"[1,2,3]"`                         |
| `[]`                             | `"[]"`                              |
| `42`                             | `"42"`                              |
| `True`                           | `"true"`                            |
| `None`                           | `"null"`                            |
| `"hallo"`                        | `'"hallo"'`                         |

## Idee

`sort_keys=True` sortiert die Dict-Schlüssel.
`separators=(",", ":")` ist der **kompakte** Modus -- Default ist
`(", ", ": ")` mit Leerzeichen.

## Pendant

Aufgabe **291-json-zu-dict** macht den Weg zurück. Zusammen sind
es ein **Round-Trip**:

(mit Caveat: `tuple` wird zu `list`, weil JSON keine Tuple kennt)

## Anwendung -- Determinismus

In Tests, Diff-Vergleichen oder Hashing braucht man **deterministische
JSON-Ausgabe** -- gleicher Input → gleicher Output. Daher
`sort_keys=True`.

In API-Antworten ist das eher unwichtig, aber **Cache-Keys** und
**Signaturen** brauchen es zwingend.
