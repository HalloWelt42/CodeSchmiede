---
schema_version: 1
id: 286-queue-ops
revision: 1
titel: Queue (FIFO) mit Operations-Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [oop, klassen, queue, deque]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Datenstruktur-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: queue_lauf
hints:
  - kosten: 0
    text: |
      Operationen auf einer Queue (FIFO, "First in, first out"):
      ["enqueue", x] → x hinten anfügen
      ["dequeue"] → vorderstes entfernen, ignoriert wenn leer
      Liefere den FINALEN Queue-Inhalt als Liste (vorne zuerst).
  - kosten: 15
    text: |
      collections.deque ist die effiziente Wahl: O(1) für beide Enden.
      Eine Klasse mit deque intern, oder direkt Methoden.
tests_sichtbar:
  - input: [[["enqueue", 1], ["enqueue", 2], ["enqueue", 3]]]
    expected: [1, 2, 3]
  - input: [[]]
    expected: []
  - input: [[["enqueue", 1], ["dequeue"]]]
    expected: []
  - input: [[["enqueue", 1], ["enqueue", 2], ["dequeue"]]]
    expected: [2]
tests_versteckt:
  - input: [[["dequeue"]]]
    expected: []
  - input: [[["enqueue", "a"], ["enqueue", "b"], ["enqueue", "c"], ["dequeue"], ["dequeue"]]]
    expected: ["c"]
  - input: [[["enqueue", 1], ["enqueue", 2], ["enqueue", 3], ["dequeue"], ["enqueue", 4]]]
    expected: [2, 3, 4]
  - input: [[["enqueue", 5], ["dequeue"], ["enqueue", 10], ["dequeue"]]]
    expected: []
  - input: [[["enqueue", 1], ["enqueue", 2], ["enqueue", 3], ["dequeue"], ["dequeue"], ["dequeue"], ["dequeue"]]]
    expected: []
starter_code: |
  from collections import deque

  def queue_lauf(operationen: list) -> list:
      # Tipp: Queue als Klasse mit deque intern
      pass
---

# Queue (FIFO) mit Operations-Liste

Implementiere `queue_lauf(operationen)` -- eine **Queue** (FIFO --
"First in, first out") wird mit einer Operations-Liste manipuliert.
Liefere den finalen Queue-Inhalt als Liste, vorne zuerst.

## Operationen

| Form                | Wirkung                       |
|---------------------|-------------------------------|
| `["enqueue", wert]` | wert hinten anfügen          |
| `["dequeue"]`       | vorderstes entfernen; ignoriert wenn leer |

## Beispiele

| Operationen                                                    | Queue        |
|----------------------------------------------------------------|---------------|
| `[["enqueue",1],["enqueue",2],["enqueue",3]]`                  | `[1,2,3]`     |
| `[["enqueue",1],["dequeue"]]`                                  | `[]`          |
| `[["enqueue",1],["enqueue",2],["dequeue"]]`                    | `[2]`         |
| `[["enqueue",1],["enqueue",2],["enqueue",3],["dequeue"],["enqueue",4]]` | `[2,3,4]` |

## Idee -- Klasse mit deque

```python
from collections import deque


class Queue:
    def __init__(self):
        self.daten = deque()

    def enqueue(self, wert):
        self.daten.append(wert)

    def dequeue(self):
        if self.daten:
            self.daten.popleft()


def queue_lauf(operationen):
    q = Queue()
    for op in operationen:
        if op[0] == "enqueue":
            q.enqueue(op[1])
        else:
            q.dequeue()
    return list(q.daten)
```

## Warum `deque` und nicht `list`?

`list.pop(0)` ist `O(n)` -- alle Elemente müssen nach links
verschoben werden. `deque.popleft()` ist `O(1)`. Bei vielen
dequeue-Operationen macht das den Unterschied zwischen "schnell"
und "unbenutzbar".

`deque` aus `collections` ist eine **doppelt verkettete Liste**
mit konstanter Zeit für beide Enden -- perfekt für Queues.

## Anwendung

- **Task-Queues** (z.B. Print-Spooler).
- **BFS** (Breitensuche) -- Aufgabe 114.
- **Producer-Consumer**-Patterns.
- **Sliding-Window**-Algorithmen.
