---
schema_version: 1
id: 007-buchstaben-haeufigkeit
revision: 1
titel: Buchstaben-Häufigkeit
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 28
schaetz_minuten: 12
tags: [strings, dict, count]
pfade: [python_strings]
voraussetzungen: [004-vokale-zaehlen]
quelle:
  url: null
  notiz: Klassischer Counter-Klassiker
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: buchstaben_haeufigkeit
hints:
  - kosten: 0
    text: Ein Dictionary mappt Buchstaben auf Anzahl.
  - kosten: 15
    text: |
      `dict.get(schluessel, 0)` liefert den aktuellen Wert oder 0
      wenn der Schlüssel noch nicht existiert.
  - kosten: 25
    text: |
      Idiomatisch mit `collections.Counter`:

      ```
      from collections import Counter
      return dict(Counter(text))
      ```
tests_sichtbar:
  - input: ["aab"]
    expected: {"a": 2, "b": 1}
  - input: [""]
    expected: {}
  - input: ["xyz"]
    expected: {"x": 1, "y": 1, "z": 1}
tests_versteckt:
  - input: ["aaaa"]
    expected: {"a": 4}
  - input: ["abcabc"]
    expected: {"a": 2, "b": 2, "c": 2}
  - input: ["Hallo"]
    expected: {"H": 1, "a": 1, "l": 2, "o": 1}
  - input: ["a a"]
    expected: {"a": 2, " ": 1}
starter_code: |
  def buchstaben_haeufigkeit(text: str) -> dict[str, int]:
      # Deine Lösung hier
      pass
---

# Buchstaben-Häufigkeit

Schreibe eine Funktion `buchstaben_haeufigkeit(text)`, die ein
Dictionary zurückgibt, in dem jedem im Text vorkommenden Zeichen seine
Häufigkeit zugeordnet ist.

## Beispiele

| Eingabe       | Ausgabe                                |
|---------------|----------------------------------------|
| `"aab"`       | `{"a": 2, "b": 1}`                     |
| `"xyz"`       | `{"x": 1, "y": 1, "z": 1}`             |
| `""`          | `{}`                                   |
| `"Hallo"`     | `{"H": 1, "a": 1, "l": 2, "o": 1}`     |

## Hinweise

- **Groß- und Kleinschreibung sind unterschiedliche Zeichen** --
  `"H"` und `"h"` sind getrennte Schlüssel.
- Auch Leerzeichen sind ein Zeichen und werden gezählt.
- Die Reihenfolge der Schlüssel im Dictionary ist egal -- Python-
  Dictionaries gelten als gleich, wenn sie die gleichen Schlüssel-
  Wert-Paare enthalten.
