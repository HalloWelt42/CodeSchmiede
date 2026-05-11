---
schema_version: 1
id: 115-klammer-balance
revision: 1
titel: Klammern balanciert?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [strings, stack, parsing]
pfade: [python_algorithmen2]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Stack-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: balanciert
hints:
  - kosten: 0
    text: |
      Erlaubt: ()[]{}. Andere Zeichen ignorieren. Stack-Verfahren:
      öffnende Klammern push, bei schließenden den Top vergleichen.
  - kosten: 15
    text: |
      Mapping `{'(': ')', '[': ']', '{': '}'}`. Bei schließender:
      Stack leer? → False. Top mismatch? → False. Sonst pop.
      Am Ende: Stack muss leer sein.
tests_sichtbar:
  - input: ["()"]
    expected: true
  - input: ["([{}])"]
    expected: true
  - input: ["(]"]
    expected: false
  - input: ["{[}]"]
    expected: false
tests_versteckt:
  - input: [""]
    expected: true
  - input: ["((()))"]
    expected: true
  - input: ["(("]
    expected: false
  - input: ["))"]
    expected: false
  - input: ["What (is) [this] {today}?"]
    expected: true
  - input: ["[1, [2, 3]]"]
    expected: true
  - input: ["a + b * (c - d)"]
    expected: true
  - input: ["a + b * (c - d"]
    expected: false
starter_code: |
  def balanciert(text: str) -> bool:
      # Deine Lösung hier -- nur (), [], {} pruefen, Rest ignorieren.
      pass
---

# Klammern balanciert?

Schreibe eine Funktion `balanciert(text)`, die prüft, ob die
Klammern `()`, `[]`, `{}` im Text **korrekt verschachtelt** sind.
Andere Zeichen werden ignoriert.

## Beispiele

| Eingabe                   | Ergebnis |
|---------------------------|----------|
| `"()"`                    | `True`   |
| `"([{}])"`                | `True`   |
| `"((()))"`                | `True`   |
| `"(]"`                    | `False`  |
| `"{[}]"`                  | `False`  |
| `"(("`                    | `False`  |
| `"What (is) [this]?"`     | `True`   |
| `"a + b * (c - d"`        | `False`  |

## Algorithmus

Stack:
- Öffnende Klammer → auf Stack
- Schließende Klammer → mit Top-of-Stack vergleichen, bei Match poppen,
  bei Mismatch `False`
- Am Ende muss der Stack leer sein

## Hintergrund

Das Pattern ist die Eintrittskarte zu **Parsern**, **Compilern** und
**JSON/XML-Validierung**. Der erste richtig instruktive Stack-Algorithmus
in jedem Datenstrukturen-Kurs.
