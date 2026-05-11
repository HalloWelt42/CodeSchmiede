---
schema_version: 1
id: 107-rpn-rechner
revision: 1
titel: Reverse Polish Notation
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [stack, strings, parsing, taschenrechner]
pfade: [python_algorithmen2]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Umgekehrte_polnische_Notation
  notiz: Klassische Stack-Aufgabe, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: rpn_auswerten
hints:
  - kosten: 0
    text: |
      RPN: Operanden auf Stack pushen. Bei Operator: zwei oberste
      Werte poppen, Operator anwenden, Ergebnis pushen.
      Operatoren: +, -, *, /. Division: Ganzzahl-Division (//).
  - kosten: 12
    text: |
      Eingabe als Whitespace-getrennter String. `tokens = ausdruck.split()`.
      Bei ungültigem Ausdruck (Stack leer beim Operator, oder am Ende
      != 1 Wert übrig) → None zurückgeben.
tests_sichtbar:
  - input: ["3 4 +"]
    expected: 7
  - input: ["5 1 2 + 4 * + 3 -"]
    expected: 14
  - input: ["10 2 /"]
    expected: 5
  - input: ["2 3 *"]
    expected: 6
tests_versteckt:
  - input: ["7"]
    expected: 7
  - input: ["1 2 3 +"]
    expected: null
  - input: ["+"]
    expected: null
  - input: [""]
    expected: null
  - input: ["10 5 -"]
    expected: 5
  - input: ["20 5 / 3 +"]
    expected: 7
  - input: ["100 50 - 5 / 2 *"]
    expected: 20
starter_code: |
  def rpn_auswerten(ausdruck: str) -> int | None:
      # Deine Lösung hier -- bei ungültiger Eingabe None.
      # Division ist Ganzzahl-Division.
      pass
---

# Reverse Polish Notation

Schreibe eine Funktion `rpn_auswerten(ausdruck)`, die einen Ausdruck
in **Umgekehrter Polnischer Notation** auswertet.

In RPN steht der Operator **nach** den Operanden:

| Infix              | RPN                       |
|--------------------|---------------------------|
| `3 + 4`            | `3 4 +`                   |
| `(1 + 2) * 4 - 3`  | `1 2 + 4 * 3 -`           |
| `5 + (1+2)*4 - 3`  | `5 1 2 + 4 * + 3 -`       |

Operatoren: `+`, `-`, `*`, `/`. Division ist **Ganzzahl-Division**
(`//`). Operanden sind ganze Zahlen, Whitespace-getrennt.

## Algorithmus

1. Token für Token gehen
2. Zahl → auf Stack
3. Operator → zwei Werte poppen, anwenden, Ergebnis auf Stack
4. Am Ende: genau ein Wert auf dem Stack -- das Ergebnis

Bei ungültigem Input (zu wenige Operanden, am Ende mehr als 1 Wert,
unbekannter Operator) → `None`.

## Hintergrund

Die Notation stammt vom polnischen Logiker **Jan Łukasiewicz** (1924).
Stack-Maschinen wie die HP-Taschenrechner nutzten sie -- und unter
der Haube benutzen Compiler genau dieses Pattern bei Ausdrucksauswertung.
