---
schema_version: 1
id: 126-laengster-praefix
revision: 1
titel: Längster gemeinsamer Präfix
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, listen, vergleich, zip]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische LeetCode-Aufgabe (longest-common-prefix), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: gemeinsamer_praefix
hints:
  - kosten: 0
    text: |
      Längster Anfang, der bei allen Strings identisch ist.
      Leere Liste oder mind. ein leerer String → "".
  - kosten: 8
    text: |
      Schicker Trick mit zip(*strings): liefert pro Position alle
      Buchstaben dieser Position. Solange alle gleich sind,
      Buchstabe nehmen, sonst stoppen.
tests_sichtbar:
  - input: [["flower", "flow", "flight"]]
    expected: "fl"
  - input: [["dog", "racecar", "car"]]
    expected: ""
  - input: [["abc"]]
    expected: "abc"
  - input: [[]]
    expected: ""
tests_versteckt:
  - input: [[""]]
    expected: ""
  - input: [["a"]]
    expected: "a"
  - input: [["abc", "abcd", "abcde"]]
    expected: "abc"
  - input: [["abc", ""]]
    expected: ""
  - input: [["aaaa", "aaaaa", "aaaaaa"]]
    expected: "aaaa"
  - input: [["interspecies", "interstellar", "interstate"]]
    expected: "inters"
starter_code: |
  def gemeinsamer_praefix(strings: list[str]) -> str:
      # Deine Lösung hier -- längster Anfang, der bei allen gleich ist.
      pass
---

# Längster gemeinsamer Präfix

Schreibe eine Funktion `gemeinsamer_praefix(strings)`, die den
**längsten Anfang** zurückgibt, den alle Strings teilen.

Bei leerer Liste oder einem leeren String in der Liste → `""`.

## Beispiele

| Eingabe                                     | Präfix     |
|---------------------------------------------|------------|
| `["flower","flow","flight"]`                | `"fl"`     |
| `["dog","racecar","car"]`                   | `""`       |
| `["abc"]`                                   | `"abc"`    |
| `["interspecies","interstellar","interstate"]` | `"inters"` |
| `[]`                                        | `""`       |
| `["abc",""]`                                | `""`       |

## Idee

Mit `zip(*strings)` bekommst du pro Position die Spalte aller Strings.
Solange `set(spalte)` einen einzigen Eintrag hat, ist es ein
gemeinsamer Buchstabe.

