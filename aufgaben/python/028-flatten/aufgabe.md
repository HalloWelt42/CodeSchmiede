---
schema_version: 1
id: 028-flatten
revision: 1
titel: Verschachtelte Liste flachklopfen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [listen, schleifen, comprehension]
pfade: [python_listen]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Standard-Aufgabe -- nur eine Ebene tief.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: flatten
hints:
  - kosten: 0
    text: |
      Eine doppelte Schleife: über die aeussere Liste, dann über jede
      innere Liste -- alle Elemente in eine flache Ergebnisliste schieben.
  - kosten: 15
    text: |
      Eine Zeile mit Comprehension:

      ```
      return [x for innen in liste for x in innen]
      ```
tests_sichtbar:
  - input: [[[1, 2], [3, 4]]]
    expected: [1, 2, 3, 4]
  - input: [[]]
    expected: []
  - input: [[[1], [2], [3]]]
    expected: [1, 2, 3]
  - input: [[["a", "b"], [], ["c"]]]
    expected: ["a", "b", "c"]
tests_versteckt:
  - input: [[[1, 2, 3]]]
    expected: [1, 2, 3]
  - input: [[[]]]
    expected: []
  - input: [[[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]]
    expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
starter_code: |
  def flatten(liste: list[list]) -> list:
      # Deine Lösung hier -- nur eine Ebene Verschachtelung.
      pass
---

# Verschachtelte Liste flachklopfen

Schreibe eine Funktion `flatten(liste)`, die eine Liste von Listen zu
einer **einzigen** Liste verschmilzt. Die Reihenfolge bleibt erhalten.

Wir betrachten nur **eine Ebene** Verschachtelung: die Eingabe ist
eine Liste von Listen, nicht beliebig tief verschachtelt.

## Beispiele

| Eingabe                  | Ergebnis           |
|--------------------------|--------------------|
| `[[1,2],[3,4]]`          | `[1,2,3,4]`        |
| `[]`                     | `[]`               |
| `[[1],[2],[3]]`          | `[1,2,3]`          |
| `[["a","b"],[],["c"]]`   | `["a","b","c"]`    |

## Wege

- **Doppelte Schleife** -- aeussere über `liste`, innere über jede
  Sub-Liste, anhängen.
- **List-Comprehension** -- die idiomatische Variante: kompakt, schnell,
  aber gewoehnungsbeduerftig in der Lesart von links nach rechts.

## Falle

`sum(liste, [])` funktioniert in Python, ist aber langsam (O(n^2)) und
gilt als Anti-Pattern. Bitte nicht.
