---
schema_version: 1
id: 291-json-zu-dict
revision: 1
titel: JSON-String zu Dict parsen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [json, parsing, dict]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches JSON-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: json_parse
hints:
  - kosten: 0
    text: |
      Parse einen JSON-String zum entsprechenden Python-Objekt.
      Bei UNGUELTIGEM JSON → None.
      json-Modul ist erlaubt.
  - kosten: 5
    text: |
      json.loads(s) -- mit try/except json.JSONDecodeError.
tests_sichtbar:
  - input: ['{"a": 1, "b": 2}']
    expected: {"a": 1, "b": 2}
  - input: ['[]']
    expected: []
  - input: ['null']
    expected: null
  - input: ['nicht-json']
    expected: null
tests_versteckt:
  - input: ['{}']
    expected: {}
  - input: ['"hallo"']
    expected: "hallo"
  - input: ['42']
    expected: 42
  - input: ['true']
    expected: true
  - input: ['[1, 2, 3]']
    expected: [1, 2, 3]
  - input: ['{"verschachtelt": {"x": [1, 2]}}']
    expected: {"verschachtelt": {"x": [1, 2]}}
  - input: ['{ungueltig}']
    expected: null
starter_code: |
  import json

  def json_parse(s: str):
      # Deine Lösung hier -- ungueltig → None
      pass
---

# JSON-String zu Dict parsen

Schreibe `json_parse(s)`, die einen JSON-String in das entsprechende
Python-Objekt umwandelt. Bei ungueltigem JSON → `None`.

## Beispiele

| JSON-String                  | Ergebnis                |
|------------------------------|--------------------------|
| `'{"a": 1, "b": 2}'`         | `{"a": 1, "b": 2}`      |
| `'[1, 2, 3]'`                | `[1, 2, 3]`             |
| `'42'`                       | `42`                    |
| `'true'`                     | `True`                  |
| `'null'`                     | `None`                  |
| `'"hallo"'`                  | `"hallo"`               |
| `'{}'`                       | `{}`                    |
| `'nicht-json'`               | `None`                  |
| `'{ungueltig}'`              | `None`                  |

## Idee

```python
import json

def json_parse(s):
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        return None
```

## Stolperstein -- `'null'` gibt `None`

JSON's `null` ist Pythons `None`. Daher kann man **nicht** unterscheiden
zwischen "valider JSON-Wert null" und "Parse-Fehler" -- beide ergeben
`None`. Wenn das wichtig ist, braucht man eine Sentinel-Variante:

```python
SENTINEL = object()

def json_parse(s):
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        return SENTINEL
```

## Pendant

Aufgabe **292-dict-zu-json** macht den Weg zurueck.

## Anwendung

JSON-Parsing ist Standard fuer:
- **REST-APIs** (JSON-Bodies)
- **Konfigurations-Dateien**
- **Daten-Austausch** zwischen Programmen
- **Browser-LocalStorage**, IndexedDB, Cookies
