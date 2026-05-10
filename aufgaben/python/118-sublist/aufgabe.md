---
schema_version: 1
id: 118-sublist
revision: 1
titel: Listen-Beziehung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [listen, vergleich, slicing]
pfade: [python_listen3]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (sublist), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: vergleiche
hints:
  - kosten: 0
    text: |
      Vier Möglichkeiten:
      - "gleich": a == b
      - "sublist": a ist zusammenhängende Teilfolge von b
      - "superlist": b ist zusammenhängende Teilfolge von a
      - "ungleich": sonst
  - kosten: 15
    text: |
      Hilfsfunktion: ist `klein` Sublist von `gross`?
      `any(gross[i:i+len(klein)] == klein for i in range(len(gross)-len(klein)+1))`.
      Leere Liste ist Sublist von allem.
tests_sichtbar:
  - input: [[1, 2, 3], [1, 2, 3]]
    expected: "gleich"
  - input: [[1, 2, 3], [1, 2, 3, 4, 5]]
    expected: "sublist"
  - input: [[0, 1, 2, 3, 4], [1, 2, 3]]
    expected: "superlist"
  - input: [[1, 2, 3], [1, 2, 4]]
    expected: "ungleich"
tests_versteckt:
  - input: [[], []]
    expected: "gleich"
  - input: [[], [1, 2, 3]]
    expected: "sublist"
  - input: [[1, 2, 3], []]
    expected: "superlist"
  - input: [[1, 1, 2], [1, 2]]
    expected: "superlist"
  - input: [[3, 4, 5], [1, 2, 3, 4, 5, 6]]
    expected: "sublist"
  - input: [[1, 2, 3, 4, 5], [3, 4, 5]]
    expected: "superlist"
starter_code: |
  def vergleiche(a: list, b: list) -> str:
      # Deine Lösung hier -- liefert "gleich", "sublist", "superlist", "ungleich".
      pass
---

# Listen-Beziehung

Schreibe eine Funktion `vergleiche(a, b)`, die die Beziehung
zwischen zwei Listen klassifiziert:

- `"gleich"` — a und b sind identisch
- `"sublist"` — a ist eine **zusammenhängende Teilfolge** von b
- `"superlist"` — b ist eine zusammenhängende Teilfolge von a
- `"ungleich"` — keine der obigen

Die **leere Liste** ist Sublist von allem (auch von sich selbst).

## Beispiele

| a              | b                  | Ergebnis     |
|----------------|--------------------|--------------|
| `[1,2,3]`      | `[1,2,3]`          | `"gleich"`   |
| `[1,2,3]`      | `[1,2,3,4,5]`      | `"sublist"`  |
| `[0,1,2,3,4]`  | `[1,2,3]`          | `"superlist"`|
| `[1,2,3]`      | `[1,2,4]`          | `"ungleich"` |
| `[]`           | `[]`               | `"gleich"`   |
| `[]`           | `[1,2,3]`          | `"sublist"`  |

## Hintergrund

Das Pattern ist Vorstufe zu **Substring-Suche** (KMP-Algorithmus).
In O(n*m) ist die naive Variante okay, fuer große Listen waere
KMP die Wahl.
