---
schema_version: 1
id: 257-woerter-kuerzer-als
revision: 1
titel: Woerter kuerzer als n
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [strings, listen, filter, split]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 256
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: kuerzer_als
hints:
  - kosten: 0
    text: |
      Liefere alle Woerter aus dem Text, die KUERZER als n Zeichen sind.
      Reihenfolge wie im Original.
  - kosten: 5
    text: |
      [w for w in text.split() if len(w) < n].
tests_sichtbar:
  - input: ["Hallo Welt", 5]
    expected: ["Welt"]
  - input: ["", 5]
    expected: []
  - input: ["a b cd", 2]
    expected: ["a", "b"]
  - input: ["zu lang", 0]
    expected: []
tests_versteckt:
  - input: ["der schnelle braune Fuchs", 6]
    expected: ["der", "Fuchs"]
  - input: ["ABC AB A", 3]
    expected: ["AB", "A"]
  - input: ["Hallo Welt", 100]
    expected: ["Hallo", "Welt"]
  - input: ["python", 10]
    expected: ["python"]
  - input: ["python", 6]
    expected: []
  - input: ["  drei  vier  fuenf  ", 5]
    expected: ["drei", "vier"]
starter_code: |
  def kuerzer_als(text: str, n: int) -> list[str]:
      # Deine Lösung hier
      pass
---

# Woerter kuerzer als n

Schreibe `kuerzer_als(text, n)`, die alle Woerter aus dem Text
zurueckgibt, die **kuerzer als n Zeichen** sind.

## Beispiele

| Text                      | n  | Ergebnis           |
|---------------------------|----|--------------------|
| `"Hallo Welt"`            | 5  | `["Welt"]`         |
| `"der schnelle braune Fuchs"` | 6 | `["der", "Fuchs"]` |
| `"ABC AB A"`              | 3  | `["AB", "A"]`      |
| `"a b cd"`                | 2  | `["a", "b"]`       |
| `"zu lang"`               | 0  | `[]`               |

## Idee

```python
def kuerzer_als(text, n):
    return [w for w in text.split() if len(w) < n]
```

Spiegelbild zu **256-woerter-laenger-als**: nur das Vergleichs-
Operator dreht.

## Verallgemeinerung

Mit Predicate-Funktion liesse sich beides in eine generische
"filter"-Funktion verpacken:

```python
def filter_woerter(text, predicate):
    return [w for w in text.split() if predicate(w)]

filter_woerter("Hallo Welt", lambda w: len(w) > 4)
filter_woerter("Hallo Welt", lambda w: len(w) < 5)
```

In Tests aber schwer zu serialisieren -- darum die spezialisierten
Aufgaben.

## Anwendung

- **Schreibtipp**: kurze Wuesterhilfe aussortieren ("Vermeide
  Fuell-Woerter mit unter 4 Zeichen").
- **Linter-Regel**: Variablen mit unter 3 Zeichen als Warnung.
