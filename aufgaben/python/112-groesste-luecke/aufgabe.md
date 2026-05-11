---
schema_version: 1
id: 112-groesste-luecke
revision: 1
titel: Größte Lücke in sortierter Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [listen, schleifen, sortieren, max]
pfade: [python_listen3]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Aufwaerm-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: groesste_luecke
hints:
  - kosten: 0
    text: |
      Sortiere die Liste, dann max der Differenzen aufeinanderfolgender
      Werte. Bei < 2 Elementen → 0.
  - kosten: 7
    text: |
      `s = sorted(zahlen)`, dann `max(b - a for a, b in zip(s, s[1:]))`.
tests_sichtbar:
  - input: [[1, 5, 10, 11]]
    expected: 5
  - input: [[1, 2, 3, 4]]
    expected: 1
  - input: [[42]]
    expected: 0
  - input: [[]]
    expected: 0
tests_versteckt:
  - input: [[10, 1, 100]]
    expected: 90
  - input: [[5, 5, 5, 5]]
    expected: 0
  - input: [[-10, 0, 10]]
    expected: 10
  - input: [[3, 6, 9, 1, 8, 2, 7, 4, 5]]
    expected: 1
  - input: [[100, 1, 1000, 50]]
    expected: 900
starter_code: |
  def groesste_luecke(zahlen: list[int]) -> int:
      # Deine Lösung hier -- nach Sortierung größter Abstand zweier Nachbarn.
      pass
---

# Größte Lücke in sortierter Liste

Schreibe eine Funktion `größte_lücke(zahlen)`, die die **größte
Lücke** zwischen zwei aufeinanderfolgenden Werten in der **sortierten**
Liste zurückgibt.

## Beispiele

| Eingabe          | Ergebnis | Wegen                |
|------------------|----------|----------------------|
| `[1, 5, 10, 11]` | `5`      | 10 - 5               |
| `[1, 2, 3, 4]`   | `1`      |                      |
| `[10, 1, 100]`   | `90`     | 100 - 10             |
| `[5, 5, 5, 5]`   | `0`      |                      |
| `[42]`           | `0`      | weniger als 2 Werte  |
| `[]`             | `0`      |                      |

## Idee

```
sortiert = sorted(zahlen)
return max(b - a for a, b in zip(sortiert, sortiert[1:]))
```

`zip(s, s[1:])` ist die Standard-Methode für Paare aus Nachbarn in
Python.
