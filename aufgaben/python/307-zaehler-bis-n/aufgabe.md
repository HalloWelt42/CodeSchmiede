---
schema_version: 1
id: 307-zaehler-bis-n
revision: 1
titel: Eigener Zähler-Generator (Liste)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [generator, yield, listen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Generator-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zaehler_bis
hints:
  - kosten: 0
    text: |
      Liefere die Zahlen 1, 2, ..., n als Liste.
      Implementiere INTERN einen Generator (yield), wandle dann zu Liste.
      n <= 0 → [].
  - kosten: 10
    text: |
      def gen(): for i in range(1, n+1): yield i
      Funktion gibt list(gen()) zurück.
tests_sichtbar:
  - input: [3]
    expected: [1, 2, 3]
  - input: [0]
    expected: []
  - input: [1]
    expected: [1]
  - input: [-5]
    expected: []
tests_versteckt:
  - input: [5]
    expected: [1, 2, 3, 4, 5]
  - input: [10]
    expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  - input: [2]
    expected: [1, 2]
  - input: [4]
    expected: [1, 2, 3, 4]
  - input: [6]
    expected: [1, 2, 3, 4, 5, 6]
starter_code: |
  def zaehler_bis(n: int) -> list[int]:
      # Tipp: Innerer Generator mit yield, dann list(...)
      pass
---

# Eigener Zähler-Generator (Liste)

Schreibe `zähler_bis(n)`, die die Zahlen `1, 2, ..., n` als Liste
liefert. **Implementiere intern einen Generator** mit `yield` --
auch wenn die finale Form eine Liste ist.

`n <= 0` → `[]`.

## Beispiele

| `n` | Ergebnis           |
|-----|---------------------|
| `3` | `[1, 2, 3]`         |
| `5` | `[1, 2, 3, 4, 5]`   |
| `1` | `[1]`               |
| `0` | `[]`                |
| `-5`| `[]`                |

## Idee -- Generator intern

```python
def zähler_bis(n):
    def gen():
        for i in range(1, n + 1):
            yield i
    return list(gen())
```

`yield` macht aus einer Funktion einen **Generator**. `list(gen())`
materialisiert ihn zur Liste.

## Warum nicht direkt `list(range(...))`?

Weil das Lehrziel der **Generator-Mechanismus** ist. In echtem
Code wäre `list(range(1, n+1))` natuerlich kürzer.

## Generator-Vorteile (in echten Anwendungen)

- **Speicherung**: kein doppelter Speicher für Zwischen-Liste.
- **Lazy Evaluation**: Werte erst bei Bedarf.
- **Unendliche Folgen**: Generatoren können ewig laufen
  (`while True: yield ...`), Listen können das nicht.

## Pattern -- Generator-Funktion

In den nächsten Aufgaben (308-314) kommen die wichtigen
Generator-Patterns: Fibonacci, Pairwise, Take-While, Accumulate, etc.
