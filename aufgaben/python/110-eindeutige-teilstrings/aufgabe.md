---
schema_version: 1
id: 110-eindeutige-teilstrings
revision: 1
titel: Eindeutige Teilstrings zählen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, sets, schleifen]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische String-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: anzahl_teilstrings
hints:
  - kosten: 0
    text: |
      Alle möglichen zusammenhängenden Teilstrings sammeln, in einem
      Set deduplizieren, Länge zurückgeben. Leerer String → 0.
  - kosten: 8
    text: |
      Doppelte Schleife: i von 0 bis n, j von i+1 bis n+1. Slicing
      `text[i:j]` ist der Teilstring.
tests_sichtbar:
  - input: ["abc"]
    expected: 6
  - input: ["a"]
    expected: 1
  - input: ["aaaa"]
    expected: 4
  - input: [""]
    expected: 0
tests_versteckt:
  - input: ["ab"]
    expected: 3
  - input: ["abab"]
    expected: 7
  - input: ["abcd"]
    expected: 10
  - input: ["mississippi"]
    expected: 53
starter_code: |
  def anzahl_teilstrings(text: str) -> int:
      # Deine Lösung hier -- alle eindeutigen, nicht-leeren, zusammenhängenden Teilstrings.
      pass
---

# Eindeutige Teilstrings zählen

Schreibe eine Funktion `anzahl_teilstrings(text)`, die zählt, wie
viele **eindeutige** zusammenhängende Teilstrings der Eingabe-String
hat.

Leerer Substring zählt nicht mit.

## Beispiele

| Eingabe       | Anzahl | Wegen                                   |
|---------------|--------|-----------------------------------------|
| `"abc"`       | `6`    | a, b, c, ab, bc, abc                    |
| `"a"`         | `1`    | a                                       |
| `"aaaa"`      | `4`    | a, aa, aaa, aaaa                        |
| `"ab"`        | `3`    | a, b, ab                                |
| `"abab"`      | `7`    | a, b, ab, ba, aba, bab, abab            |
| `""`          | `0`    |                                         |

## Idee

Doppelte Schleife mit Slicing erzeugt **alle** Teilstrings (mit
Doppelten). `set(...)` macht sie eindeutig, `len(...)` zählt.

## Komplexitaet

$O(n^3)$ wegen $O(n^2)$ Substrings × $O(n)$ Hash-Berechnung pro
Substring. Für kleine Strings okay; bei großen würde man auf
**Suffix-Bäume** ausweichen.
