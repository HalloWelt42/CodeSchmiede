---
schema_version: 1
id: 108-permutationen
revision: 1
titel: Alle Permutationen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [strings, rekursion, kombinatorik]
pfade: [python_algorithmen2]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Rekursions-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: permutationen
hints:
  - kosten: 0
    text: |
      n! Permutationen. Rekursion: für jeden Buchstaben als Anfang
      die Permutationen des Restes davorsetzen. Liefere sortierte
      Liste eindeutiger Permutationen.
  - kosten: 20
    text: |
      `itertools.permutations` zählt alle (mit Doppelten bei doppelten
      Buchstaben). `set(...)` für Eindeutigkeit, `sorted(...)` für
      stabile Reihenfolge.
tests_sichtbar:
  - input: ["a"]
    expected: ["a"]
  - input: ["ab"]
    expected: ["ab", "ba"]
  - input: ["abc"]
    expected: ["abc", "acb", "bac", "bca", "cab", "cba"]
  - input: [""]
    expected: [""]
tests_versteckt:
  - input: ["aa"]
    expected: ["aa"]
  - input: ["aab"]
    expected: ["aab", "aba", "baa"]
  - input: ["abcd"]
    expected: ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "bacd", "badc", "bcad", "bcda", "bdac", "bdca", "cabd", "cadb", "cbad", "cbda", "cdab", "cdba", "dabc", "dacb", "dbac", "dbca", "dcab", "dcba"]
  - input: ["xy"]
    expected: ["xy", "yx"]
starter_code: |
  def permutationen(text: str) -> list[str]:
      # Deine Lösung hier -- alle eindeutigen Permutationen, sortiert.
      pass
---

# Alle Permutationen

Schreibe eine Funktion `permutationen(text)`, die **alle eindeutigen
Permutationen** der Buchstaben als Liste zurückgibt -- sortiert.

## Beispiele

| Eingabe | Ergebnis                              |
|---------|---------------------------------------|
| `"a"`   | `["a"]`                               |
| `"ab"`  | `["ab", "ba"]`                        |
| `"abc"` | `["abc","acb","bac","bca","cab","cba"]` |
| `"aab"` | `["aab","aba","baa"]` (eindeutig!)    |
| `""`    | `[""]`                                |

## Anzahl

Bei $n$ unterschiedlichen Zeichen sind es $n!$ Permutationen. Bei
doppelten Zeichen entsprechend weniger -- z.B. `"aab"` hat
$3!/2! = 3$ statt 6.

## Hintergrund

Permutationen sind die Eintrittskarte zur **Kombinatorik**. In
Algorithmen-Kursen oft als Beispiel für **Rekursion** mit Backtracking
benutzt -- aber `itertools.permutations` macht es in Python ohnehin
in einer Zeile.
