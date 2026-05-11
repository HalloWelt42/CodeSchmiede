---
schema_version: 1
id: 215-dict-aus-paaren
revision: 1
titel: Dict aus Schluessel-Wert-Paaren bauen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [dicts, listen, tupel]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Datenkonvertierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: paare_zu_dict
hints:
  - kosten: 0
    text: |
      Wandle eine Liste von [key, value]-Paaren in ein Dict.
      Bei doppelten Keys: der LETZTE Wert gewinnt.
      Leere Liste → {}.
  - kosten: 10
    text: |
      dict() akzeptiert Iterable von Paaren direkt:
      dict([("a", 1), ("b", 2)]).
tests_sichtbar:
  - input: [[["a", 1], ["b", 2]]]
    expected: {"a": 1, "b": 2}
  - input: [[]]
    expected: {}
  - input: [[["x", 42]]]
    expected: {"x": 42}
  - input: [[["a", 1], ["a", 2]]]
    expected: {"a": 2}
tests_versteckt:
  - input: [[["k1", "v1"], ["k2", "v2"], ["k3", "v3"]]]
    expected: {"k1": "v1", "k2": "v2", "k3": "v3"}
  - input: [[["eins", 1], ["zwei", 2], ["drei", 3]]]
    expected: {"eins": 1, "zwei": 2, "drei": 3}
  - input: [[["a", 1], ["b", 2], ["a", 99]]]
    expected: {"a": 99, "b": 2}
  - input: [[["leer", null]]]
    expected: {"leer": null}
  - input: [[["x", 1], ["x", 2], ["x", 3]]]
    expected: {"x": 3}
starter_code: |
  def paare_zu_dict(paare: list[list]) -> dict:
      # Deine Lösung hier -- bei doppelten Keys gewinnt der letzte Wert
      pass
---

# Dict aus Schluessel-Wert-Paaren bauen

Schreibe `paare_zu_dict(paare)`, die eine Liste von `[key, value]`-
Paaren in ein Dict umwandelt.

Bei **doppelten Keys** gewinnt der **letzte** Wert.
Leere Liste → `{}`.

## Beispiele

| Paare                             | Dict                       |
|-----------------------------------|-----------------------------|
| `[["a", 1], ["b", 2]]`            | `{"a": 1, "b": 2}`          |
| `[]`                              | `{}`                        |
| `[["x", 42]]`                     | `{"x": 42}`                 |
| `[["a", 1], ["a", 2]]`            | `{"a": 2}` (letzter wins)   |
| `[["x", 1], ["x", 2], ["x", 3]]`  | `{"x": 3}`                  |

## Idee

```python
def paare_zu_dict(paare):
    return dict(paare)
```

`dict()` akzeptiert ein Iterable von 2-Element-Iterables direkt.
Bei doppelten Keys gewinnt automatisch das **letzte** Paar -- weil
es spaeter eingesetzt wird und das fruehere ueberschreibt.

## Pendant -- Dict zu Paaren

```python
list(dict.items())   # [("a", 1), ("b", 2)]
```

## Hintergrund

Dieses Pattern ist allgegenwaertig:
- Beim Parsen von **Query-Strings** (`?key=value&key2=value2`).
- Bei **CSV-Headers** + Daten (zip(headers, row) → dict).
- Bei **JSON-Roundtrip** (Python ↔ JSON serialisiert dict zu Pairs).
