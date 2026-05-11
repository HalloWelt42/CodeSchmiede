---
schema_version: 1
id: 027-eindeutige-reihenfolge
revision: 1
titel: Doppelte raus, Reihenfolge bleibt
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [listen, sets, schleifen]
pfade: [python_sets]
voraussetzungen: [025-set-schnitt]
quelle:
  url: null
  notiz: Klassische Aufgabe -- der Knackpunkt ist die Reihenfolge.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: eindeutige
hints:
  - kosten: 0
    text: |
      `list(set(a))` entfernt Doppelte, vermurkst aber die Reihenfolge.
      Du brauchst einen anderen Weg, der die Reihenfolge erhält.
  - kosten: 15
    text: |
      Ein "gesehen"-Set für den schnellen Lookup, dann pro Element
      prüfen und ggf. anhängen.
  - kosten: 25
    text: |
      Seit Python 3.7 garantiert `dict` Insertion-Order. Damit ist
      `list(dict.fromkeys(a))` ein eleganter One-Liner.
tests_sichtbar:
  - input: [[1, 2, 2, 3, 1, 4]]
    expected: [1, 2, 3, 4]
  - input: [[]]
    expected: []
  - input: [[1, 1, 1, 1]]
    expected: [1]
  - input: [["a", "b", "a", "c", "b"]]
    expected: ["a", "b", "c"]
tests_versteckt:
  - input: [[1]]
    expected: [1]
  - input: [[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]]
    expected: [3, 1, 4, 5, 9, 2, 6]
  - input: [["x", "x", "x"]]
    expected: ["x"]
starter_code: |
  def eindeutige(a: list) -> list:
      # Deine Lösung hier -- Doppelte raus, Reihenfolge wie in a.
      pass
---

# Doppelte raus, Reihenfolge bleibt

Schreibe eine Funktion `eindeutige(a)`, die jedes Element aus `a` nur
**einmal** im Ergebnis behaelt -- in der Reihenfolge des **ersten
Auftretens**.

## Beispiele

| Eingabe                     | Ergebnis            |
|-----------------------------|---------------------|
| `[1,2,2,3,1,4]`             | `[1,2,3,4]`         |
| `[]`                        | `[]`                |
| `[1,1,1,1]`                 | `[1]`               |
| `["a","b","a","c","b"]`     | `["a","b","c"]`     |

## Falle

`list(set(a))` zerstört die Reihenfolge -- Sets in Python sind nicht
ordnungserhaltend. Es gibt zwei saubere Wege:

1. Schleife mit `gesehen`-Set
2. `list(dict.fromkeys(a))` -- nutzt aus, dass Dicts seit 3.7
   Insertion-Order garantieren

Beide sind gültig.

## Hintergrund

Diese Aufgabe ist eines der typischen Beispiele dafür, dass eine
augenscheinlich passende Standardlösung (`set`) eine subtile
Schwaeche hat (Reihenfolge). Solche Faelle sind in echten Codebasen
sehr häufig.
