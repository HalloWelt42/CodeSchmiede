---
schema_version: 1
id: 306-pipe-mit-zwischen
revision: 1
titel: Pipe mit Zwischen-Ergebnissen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [funktional, pipe, listen, debug]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Funktionales Pattern + Inspector
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: pipe_mit_zwischen
hints:
  - kosten: 0
    text: |
      Wende eine Folge von Operationen auf einen Startwert an
      und liefere den Wert NACH JEDER Operation als Liste.
      Operations: "double", "square", "negate", "increment", "absolute"
      pipe_mit_zwischen(3, ["double", "increment", "square"]) →
      [6, 7, 49] (Schritte).
      Bei [] → []. Unbekannte Op → Wert unveraendert mitlesen.
  - kosten: 15
    text: |
      Akkumulator + Liste der Snapshots.
      Pro op: aktuell = OP(aktuell), append.
tests_sichtbar:
  - input: [3, ["double", "increment", "square"]]
    expected: [6, 7, 49]
  - input: [5, []]
    expected: []
  - input: [1, ["square"]]
    expected: [1]
  - input: [10, ["unknown"]]
    expected: [10]
tests_versteckt:
  - input: [2, ["double", "double", "double"]]
    expected: [4, 8, 16]
  - input: [-5, ["absolute", "increment", "square"]]
    expected: [5, 6, 36]
  - input: [10, ["negate", "absolute"]]
    expected: [-10, 10]
  - input: [0, ["increment", "increment", "increment"]]
    expected: [1, 2, 3]
  - input: [4, ["square", "negate", "absolute"]]
    expected: [16, -16, 16]
  - input: [3, ["double", "unknown", "increment"]]
    expected: [6, 6, 7]
starter_code: |
  def pipe_mit_zwischen(start, ops: list[str]) -> list:
      # Tipp: Akkumulator durch Ops, jeden Schritt sammeln
      pass
---

# Pipe mit Zwischen-Ergebnissen

Schreibe `pipe_mit_zwischen(start, ops)`, die einen Startwert durch
eine Folge von Operationen laufen laesst -- und **nach jeder
Operation** den aktuellen Wert in eine Liste schreibt.

Bei unbekannter Op wird sie als `identity` behandelt (Wert bleibt,
wird aber als Snapshot eingetragen).

## Verfuegbare Operationen

| String        | Wirkung    |
|---------------|------------|
| `"double"`    | x * 2      |
| `"square"`    | x ** 2     |
| `"negate"`    | -x         |
| `"increment"` | x + 1      |
| `"absolute"`  | abs(x)     |

## Beispiele

| Start | Ops                              | Snapshots         |
|-------|----------------------------------|--------------------|
| 3     | `["double","increment","square"]`| `[6, 7, 49]`       |
| -5    | `["absolute","increment","square"]`| `[5, 6, 36]`     |
| 4     | `["square","negate","absolute"]` | `[16, -16, 16]`    |
| 10    | `["negate","absolute"]`          | `[-10, 10]`        |
| 5     | `[]`                             | `[]`               |

## Idee

```python
OPS = {
    "double": lambda x: x * 2,
    "square": lambda x: x ** 2,
    "negate": lambda x: -x,
    "increment": lambda x: x + 1,
    "absolute": abs,
}


def pipe_mit_zwischen(start, ops):
    aktuell = start
    out = []
    for op in ops:
        if op in OPS:
            aktuell = OPS[op](aktuell)
        out.append(aktuell)
    return out
```

Pro Op: anwenden (oder bei unbekannt: ueberspringen) und Snapshot
einsammeln.

## Vergleich mit Pipeline (302)

| Aufgabe          | Was?                                     |
|------------------|------------------------------------------|
| **302-pipeline** | Wendet Ops auf **Liste** an, gibt Endergebnis |
| **306 hier**     | Wendet Ops auf **Skalar** an, gibt **alle Zwischen-Werte** |

Die Snapshot-Variante ist nuetzlich fuer **Debugging**, **Trace-
Logs**, **Animationen** und **Visualisierungen**.

## Anwendung

- **Animations-Frames** generieren ("zeige mir alle Zwischen-Stufen").
- **Trace-Logs** in Pipelines (welcher Schritt hat den Bug?).
- **Time-Travel-Debugger** (jeder Snapshot = ein Schritt zurueck).
