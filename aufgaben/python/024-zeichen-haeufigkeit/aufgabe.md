---
schema_version: 1
id: 024-zeichen-häufigkeit
revision: 1
titel: Zeichen-Häufigkeit als Dict
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, dict, count]
pfade: [python_dicts]
voraussetzungen: [022-wortzaehler]
quelle:
  url: null
  notiz: Eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: zeichen_haeufigkeit
hints:
  - kosten: 0
    text: |
      Schleife über `text`, jedes Zeichen ins Dict zählen.
  - kosten: 8
    text: |
      `dict.get(c, 0) + 1` spart das if/else.
tests_sichtbar:
  - input: ["hallo"]
    expected: { "h": 1, "a": 1, "l": 2, "o": 1 }
  - input: [""]
    expected: {}
  - input: ["aaa"]
    expected: { "a": 3 }
  - input: ["abcabc"]
    expected: { "a": 2, "b": 2, "c": 2 }
tests_versteckt:
  - input: ["mississippi"]
    expected: { "m": 1, "i": 4, "s": 4, "p": 2 }
  - input: [" "]
    expected: { " ": 1 }
  - input: ["12321"]
    expected: { "1": 2, "2": 2, "3": 1 }
starter_code: |
  def zeichen_haeufigkeit(text: str) -> dict[str, int]:
      # Deine Lösung hier
      pass
---

# Zeichen-Häufigkeit

Schreibe eine Funktion `zeichen_häufigkeit(text)`, die zählt, wie oft
jedes einzelne **Zeichen** im String vorkommt -- inklusive Leerzeichen
und Sonderzeichen.

## Beispiele

| Eingabe       | Ergebnis                              |
|---------------|---------------------------------------|
| `"hallo"`     | `{"h":1, "a":1, "l":2, "o":1}`        |
| `""`          | `{}`                                  |
| `"aaa"`       | `{"a":3}`                             |
| `"abcabc"`    | `{"a":2, "b":2, "c":2}`               |
| `"mississippi"` | `{"m":1, "i":4, "s":4, "p":2}`      |

## Idee

Schleife über den String. Für jedes Zeichen: `zählung[c] = zählung.get(c, 0) + 1`.
Reihenfolge der Schlüssel im Ergebnis ist egal.

## Verwandt

Die Aufgabe ist die Buchstaben-Variante von [Wortzähler aus Satz](#).
Wer beide gemacht hat, hat das Standard-Pattern für Zähl-Dicts in
Python sicher drauf.
