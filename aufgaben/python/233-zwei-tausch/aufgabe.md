---
schema_version: 1
id: 233-zwei-tausch
revision: 1
titel: Zwei Werte tauschen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags: [tupel, basis, listen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Tupel-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: tauschen
hints:
  - kosten: 0
    text: |
      Liefere ein Liste [b, a] mit den Werten getauscht.
  - kosten: 5
    text: |
      Tupel-Zuweisung: a, b = b, a.
      Oder direkt return [b, a].
tests_sichtbar:
  - input: [1, 2]
    expected: [2, 1]
  - input: [0, 0]
    expected: [0, 0]
  - input: ["a", "b"]
    expected: ["b", "a"]
  - input: [-5, 5]
    expected: [5, -5]
tests_versteckt:
  - input: [100, 200]
    expected: [200, 100]
  - input: [null, 1]
    expected: [1, null]
  - input: [true, false]
    expected: [false, true]
  - input: [[1, 2], [3, 4]]
    expected: [[3, 4], [1, 2]]
  - input: ["x", "x"]
    expected: ["x", "x"]
  - input: [3.14, 2.71]
    expected: [2.71, 3.14]
starter_code: |
  def tauschen(a, b) -> list:
      # Deine Lösung hier
      pass
---

# Zwei Werte tauschen

Schreibe `tauschen(a, b)`, die ein Liste `[b, a]` zurückgibt --
die beiden Werte sind **vertauscht**.

Trivial in Python, aber ein didaktischer Einstieg in
**Tupel-Zuweisung**.

## Beispiele

| `a`      | `b`      | Ergebnis     |
|----------|----------|--------------|
| `1`      | `2`      | `[2, 1]`     |
| `0`      | `0`      | `[0, 0]`     |
| `"a"`    | `"b"`    | `["b", "a"]` |
| `[1, 2]` | `[3, 4]` | `[[3, 4], [1, 2]]` |

## Idee 1 -- direkt

Geht nicht kürzer.

## Idee 2 -- Tupel-Zuweisung (äquivalent, aber anschaulich)

Hier sieht man die **Pythonische Variablen-Tausch-Form**: `a, b = b, a`.
In C oder Java braucht man eine **Hilfsvariable**:

```c
int tmp = a;
a = b;
b = tmp;
```

In Python passiert das **atomar** -- die rechte Seite wird komplett
ausgewertet, bevor die linke zugewiesen wird.

## Anwendung

Tupel-Tausch ist die Basis vieler **Sortier-Algorithmen** (Bubble,
Selection, Insertion, Quicksort -- siehe Aufgaben 038, 049-052).
