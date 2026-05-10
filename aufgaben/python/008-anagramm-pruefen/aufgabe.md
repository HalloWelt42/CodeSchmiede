---
schema_version: 1
id: 008-anagramm-pruefen
revision: 1
titel: Anagramm-Prüfung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [strings, sortieren, vergleich]
pfade: [python_strings]
voraussetzungen: [007-buchstaben-haeufigkeit]
quelle:
  url: https://de.wikipedia.org/wiki/Anagramm
  notiz: Klassische String-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_anagramm
hints:
  - kosten: 0
    text: Zwei Wörter sind Anagramme, wenn sie aus genau denselben Buchstaben bestehen.
  - kosten: 15
    text: |
      Wenn man beide Wörter sortiert, müssen sie gleich aussehen.
      Strings kann man mit `sorted()` zu Listen sortieren.
  - kosten: 25
    text: |
      ```
      return sorted(a) == sorted(b)
      ```
tests_sichtbar:
  - input: ["abc", "cba"]
    expected: true
  - input: ["abc", "abd"]
    expected: false
  - input: ["", ""]
    expected: true
  - input: ["a", "a"]
    expected: true
tests_versteckt:
  - input: ["lager", "regal"]
    expected: true
  - input: ["mond", "demo"]
    expected: false
  - input: ["abc", "cb"]
    expected: false
  - input: ["aabb", "abab"]
    expected: true
  - input: ["Aa", "aA"]
    expected: true
starter_code: |
  def ist_anagramm(a: str, b: str) -> bool:
      # Deine Lösung hier
      pass
---

# Anagramm-Prüfung

Schreibe eine Funktion `ist_anagramm(a, b)`, die `True` zurückgibt,
wenn die beiden Strings **Anagramme** voneinander sind -- also aus
genau denselben Buchstaben in beliebiger Reihenfolge bestehen.

## Beispiele

| a          | b          | Ausgabe |
|------------|------------|---------|
| `"abc"`    | `"cba"`    | `True`  |
| `"lager"`  | `"regal"`  | `True`  |
| `"mond"`   | `"demo"`   | `False` |
| `""`       | `""`       | `True`  |

## Hinweise

- **Groß- und Kleinschreibung zählen** -- `"A"` und `"a"` sind
  unterschiedliche Buchstaben.
- Auch Leerzeichen werden mitgezählt.
- Zwei leere Strings sind per Konvention Anagramme voneinander.
