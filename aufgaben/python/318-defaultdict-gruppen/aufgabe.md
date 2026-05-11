---
schema_version: 1
id: 318-defaultdict-gruppen
revision: 1
titel: Strings nach Anfangsbuchstabe gruppieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [defaultdict, dicts, gruppieren, strings]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: collections.defaultdict-Klassiker
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: gruppiere_anfang
hints:
  - kosten: 0
    text: |
      Gruppiere Strings nach ihrem ersten Buchstaben (kleinbuch).
      Liefere ein Dict {letter: [strings]} -- innen alphabetisch sortiert,
      aussen nach key sortiert.
      Leere Strings → ueberspringen.
  - kosten: 10
    text: |
      defaultdict(list) erlaubt direktes append ohne if-pruefung.
      dict(sortierte items) gibt Python-3.7+ insertion-order zurueck.
tests_sichtbar:
  - input: [["Anna", "Bob", "Alice"]]
    expected: {"a": ["Alice", "Anna"], "b": ["Bob"]}
  - input: [[]]
    expected: {}
  - input: [["solo"]]
    expected: {"s": ["solo"]}
  - input: [["", "leer", ""]]
    expected: {"l": ["leer"]}
tests_versteckt:
  - input: [["apple", "banana", "ananas", "berry", "cherry"]]
    expected: {"a": ["ananas", "apple"], "b": ["banana", "berry"], "c": ["cherry"]}
  - input: [["X", "x", "Y"]]
    expected: {"x": ["X", "x"], "y": ["Y"]}
  - input: [["zebra"]]
    expected: {"z": ["zebra"]}
  - input: [["one", "two", "three", "four", "five"]]
    expected: {"f": ["five", "four"], "o": ["one"], "t": ["three", "two"]}
  - input: [["aaa", "aab", "abc"]]
    expected: {"a": ["aaa", "aab", "abc"]}
starter_code: |
  from collections import defaultdict

  def gruppiere_anfang(strings: list[str]) -> dict:
      # Tipp: defaultdict(list), dann sortiert ausgeben
      pass
---

# Strings nach Anfangsbuchstabe gruppieren

Schreibe `gruppiere_anfang(strings)`, die eine Liste von Strings
nach **erstem Buchstaben** (kleingeschrieben) gruppiert.

Liefere ein Dict `{letter: [strings]}`:
- aussen: nach Letter alphabetisch sortiert
- innen: alphabetisch sortiert

Leere Strings werden uebersprungen.

## Beispiele

| Eingabe                    | Ergebnis                                   |
|----------------------------|--------------------------------------------|
| `["Anna","Bob","Alice"]`   | `{"a": ["Alice","Anna"], "b": ["Bob"]}`    |
| `["X","x","Y"]`            | `{"x": ["X","x"], "y": ["Y"]}`             |
| `["one","two","three","four","five"]` | `{"f":["five","four"], "o":["one"], "t":["three","two"]}` |
| `[]`                       | `{}`                                       |

## Idee

```python
from collections import defaultdict

def gruppiere_anfang(strings):
    gruppen = defaultdict(list)
    for s in strings:
        if not s:
            continue
        gruppen[s[0].lower()].append(s)
    # Innen alphabetisch sortieren, aussen sortiert ausgeben
    return {k: sorted(v) for k, v in sorted(gruppen.items())}
```

`defaultdict(list)` legt automatisch eine leere Liste an, wenn ein
Key zum ersten Mal angefasst wird -- spart die `if key in dict`-
Pruefung.

## Vergleich mit `dict.setdefault`

```python
gruppen = {}
for s in strings:
    if s:
        gruppen.setdefault(s[0].lower(), []).append(s)
```

Funktioniert auch, ist aber laenger zu lesen. `defaultdict` ist
idiomatischer.

## Anwendung

- **Telefonbuch** nach Anfangsbuchstabe sortiert.
- **Histogramme** nach beliebigem Schluessel.
- **GroupBy** in Datenanalyse (vor pandas).
