---
schema_version: 1
id: 047-substring-anzahl
revision: 1
titel: Substring zählen (mit Überlappung)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, slicing, schleifen]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: null
  notiz: Variation des Klassikers, mit Überlappung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: zaehle_vorkommen
hints:
  - kosten: 0
    text: |
      `text.count(sub)` ohne Überlappung. Hier soll Überlappung
      mitgezählt werden -- "aaa" enthält "aa" zweimal!
  - kosten: 15
    text: |
      Schleife mit Index: `for i in range(len(text) - len(sub) + 1)`,
      prüfen `text[i:i+len(sub)] == sub`.
tests_sichtbar:
  - input: ["aaaa", "aa"]
    expected: 3
  - input: ["abababab", "abab"]
    expected: 3
  - input: ["hello", "ll"]
    expected: 1
  - input: ["abc", "d"]
    expected: 0
tests_versteckt:
  - input: ["", "a"]
    expected: 0
  - input: ["aaa", ""]
    expected: 0
  - input: ["abc", "abc"]
    expected: 1
  - input: ["abcabcabc", "abc"]
    expected: 3
  - input: ["aaaaa", "aaa"]
    expected: 3
starter_code: |
  def zaehle_vorkommen(text: str, sub: str) -> int:
      # Deine Lösung hier -- mit Ueberlappung. Leerer sub liefert 0.
      pass
---

# Substring zählen (mit Überlappung)

Schreibe eine Funktion `zähle_vorkommen(text, sub)`, die zählt, wie
oft `sub` in `text` vorkommt -- inklusive **überlappender** Treffer.

`"aaaa"` enthält den Substring `"aa"` an Position 0, 1 und 2 --
also dreimal.

## Beispiele

| Text       | Sub    | Ergebnis |
|------------|--------|----------|
| `"aaaa"`   | `"aa"` | `3`      |
| `"abababab"` | `"abab"` | `3`  |
| `"hello"`  | `"ll"` | `1`      |
| `"abc"`    | `"d"`  | `0`      |
| `""`       | `"a"`  | `0`      |
| `"aaa"`    | `""`   | `0`      |

## Falle

Pythons eingebautes `str.count()` zählt **ohne** Überlappung --
für `"aaaa".count("aa")` bekommst du `2`. Hier brauchen wir die
Überlappung.

## Idee

Schleife durch alle möglichen Startpositionen, an jeder den Substring
mit Slicing herausschneiden und vergleichen.
