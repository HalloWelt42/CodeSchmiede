---
schema_version: 1
id: 092-fibonacci-folge
revision: 1
titel: Fibonacci-Folge bis n
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [zahlen, listen, schleifen, fibonacci]
pfade: [python_mathe]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Fibonacci-Folge
  notiz: Variante des Klassikers, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: fibonacci_folge
hints:
  - kosten: 0
    text: |
      Fibonacci: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).
      Liefere die ersten n Zahlen als Liste.
  - kosten: 7
    text: |
      Iterativ in einer Schleife mit zwei Variablen `a, b`. Pro Schritt
      `a, b = b, a+b` und `a` an die Liste anhängen.
tests_sichtbar:
  - input: [0]
    expected: []
  - input: [1]
    expected: [0]
  - input: [2]
    expected: [0, 1]
  - input: [10]
    expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
tests_versteckt:
  - input: [3]
    expected: [0, 1, 1]
  - input: [5]
    expected: [0, 1, 1, 2, 3]
  - input: [15]
    expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
  - input: [20]
    expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
starter_code: |
  def fibonacci_folge(n: int) -> list[int]:
      # Deine Lösung hier -- erste n Zahlen der Fibonacci-Folge.
      pass
---

# Fibonacci-Folge bis n

Schreibe eine Funktion `fibonacci_folge(n)`, die die **ersten n** Zahlen
der Fibonacci-Folge als Liste zurückgibt.

## Definition

$$
F_0 = 0, \quad F_1 = 1, \quad F_n = F_{n-1} + F_{n-2}
$$

## Beispiele

| `n`  | Ergebnis                                   |
|------|--------------------------------------------|
| `0`  | `[]`                                       |
| `1`  | `[0]`                                      |
| `2`  | `[0, 1]`                                   |
| `10` | `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`        |

## Hintergrund

Die Folge erscheint überall in der Natur -- Sonnenblumen-Spiralen,
Schneckenhäuser, Tannenzapfen. Leonardo von Pisa (Fibonacci) führte
sie 1202 in Europa ein, in China und Indien war sie schon vorher
bekannt.

## Verwandt

Bei Aufgabe `003-fibonacci` haben wir die n-te Zahl berechnet --
hier liefern wir die **ganze Folge** als Liste.
