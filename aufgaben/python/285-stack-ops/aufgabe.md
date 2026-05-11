---
schema_version: 1
id: 285-stack-ops
revision: 1
titel: Stack mit Operations-Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [oop, klassen, stack, listen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Datenstruktur-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: stack_lauf
hints:
  - kosten: 0
    text: |
      Operationen auf einem Stack (LIFO):
      ["push", x] → x oben drauf
      ["pop"] → entfernt das oberste, ignoriert wenn leer
      Liefere den FINALEN Stack-Inhalt als Liste.
      Bei [] → [].
  - kosten: 12
    text: |
      Klasse Stack mit interner Liste, push/pop-Methoden.
      Liste ist von unten nach oben (Index 0 = unten).
tests_sichtbar:
  - input: [[["push", 1], ["push", 2], ["push", 3]]]
    expected: [1, 2, 3]
  - input: [[]]
    expected: []
  - input: [[["push", 1], ["pop"]]]
    expected: []
  - input: [[["push", 1], ["push", 2], ["pop"]]]
    expected: [1]
tests_versteckt:
  - input: [[["pop"]]]
    expected: []
  - input: [[["pop"], ["pop"], ["pop"]]]
    expected: []
  - input: [[["push", 5], ["push", 10], ["push", 15], ["pop"], ["pop"]]]
    expected: [5]
  - input: [[["push", "a"], ["push", "b"]]]
    expected: ["a", "b"]
  - input: [[["push", 1], ["push", 2], ["push", 3], ["push", 4], ["push", 5]]]
    expected: [1, 2, 3, 4, 5]
  - input: [[["push", 1], ["pop"], ["push", 2], ["pop"], ["push", 3]]]
    expected: [3]
starter_code: |
  def stack_lauf(operationen: list) -> list:
      # Tipp: Stack als Klasse mit push/pop, dann Liste zurueckgeben
      pass
---

# Stack mit Operations-Liste

Implementiere `stack_lauf(operationen)` -- ein **Stack** (LIFO,
"Last in, first out") wird mit einer Liste von Operationen
manipuliert. Liefere den **finalen Inhalt** des Stacks als Liste
(Index 0 = unten).

## Operationen

| Form              | Wirkung                                  |
|-------------------|-------------------------------------------|
| `["push", wert]`  | wert oben drauf                          |
| `["pop"]`         | entfernt das oberste; ignoriert wenn leer|

## Beispiele

| Operationen                                  | Finaler Stack |
|----------------------------------------------|----------------|
| `[["push",1],["push",2],["push",3]]`         | `[1,2,3]`      |
| `[["push",1],["pop"]]`                       | `[]`           |
| `[["push",1],["push",2],["pop"]]`            | `[1]`          |
| `[["push",5],["push",10],["push",15],["pop"],["pop"]]` | `[5]` |
| `[["pop"]]`                                  | `[]` (leerer Stack toleriert) |

## Warum Stack als Klasse?

Pythons `list` mit `append`/`pop()` IST schon ein Stack. Aber:

1. **Klare API**: nur `push`/`pop`/`top`, kein `insert(0, ...)` versehentlich.
2. **Kapselung**: spaeter könnte man Limits, Logging, Thread-Safety hinzufuegen.
3. **Lehrwert**: Stacks sind die Datenstruktur Nr. 1 in Compilerbau,
   Function-Calls, Backtracking.

## Anwendung

- **Function-Call-Stack**: jeder Funktionsaufruf macht push, return macht pop.
- **Klammern-Validierung** (Aufgabe 115).
- **RPN-Rechner** (Aufgabe 107).
- **Undo-Funktionen** in Editoren.
