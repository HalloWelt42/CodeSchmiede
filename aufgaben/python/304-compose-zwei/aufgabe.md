---
schema_version: 1
id: 304-compose-zwei
revision: 1
titel: Zwei Operationen verschachteln (compose)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [funktional, compose, mathematik]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Funktionales Compose-Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: compose_anwenden
hints:
  - kosten: 0
    text: |
      Wende ZWEI Operationen verschachtelt auf x an: (g . f)(x) = g(f(x)).
      Operationen: "double", "square", "negate", "increment", "absolute".
      compose_anwenden(3, "increment", "square") = (3+1)² = 16.
      Bei UNBEKANNTER Op → x unverändert.
  - kosten: 15
    text: |
      g(f(x)) -- erst f anwenden, dann g auf das Ergebnis.
tests_sichtbar:
  - input: [3, "increment", "square"]
    expected: 16
  - input: [3, "square", "increment"]
    expected: 10
  - input: [5, "double", "double"]
    expected: 20
  - input: [5, "unknown", "double"]
    expected: 10
tests_versteckt:
  - input: [-3, "absolute", "square"]
    expected: 9
  - input: [4, "negate", "absolute"]
    expected: 4
  - input: [2, "square", "square"]
    expected: 16
  - input: [10, "increment", "increment"]
    expected: 12
  - input: [0, "increment", "square"]
    expected: 1
  - input: [7, "double", "increment"]
    expected: 15
  - input: [3, "square", "unknown"]
    expected: 9
starter_code: |
  def compose_anwenden(x, f: str, g: str):
      # Tipp: g(f(x)) -- erst f, dann g
      pass
---

# Zwei Operationen verschachteln (compose)

Schreibe `compose_anwenden(x, f, g)`, die zwei Operationen **kombiniert**
auf `x` anwendet -- nach mathematischer Konvention:

$$(g \circ f)(x) = g(f(x))$$

Das heisst: **erst f**, dann **g auf das Ergebnis**.

Bei unbekannter Op wird sie als `identity` behandelt (gibt x zurück).

## Verfügbare Operationen

| String        | Wirkung    |
|---------------|------------|
| `"double"`    | x * 2      |
| `"square"`    | x ** 2     |
| `"negate"`    | -x         |
| `"increment"` | x + 1      |
| `"absolute"`  | abs(x)     |

## Beispiele

| `x` | `f`           | `g`         | Ergebnis | Berechnung    |
|-----|---------------|-------------|----------|---------------|
| 3   | `"increment"` | `"square"`  | 16       | (3+1)² = 16   |
| 3   | `"square"`    | `"increment"`| 10      | 3²+1 = 10     |
| 5   | `"double"`    | `"double"`  | 20       | 5*2*2 = 20    |
| -3  | `"absolute"`  | `"square"`  | 9        | abs(-3)² = 9  |
| 4   | `"negate"`    | `"absolute"`| 4        | abs(-4) = 4   |

## Idee

`OPS.get(name, IDENTITY)` -- bei unbekanntem Namen das Identitaets-
Lambda als Fallback.

## Mathematik -- Komposition

Komposition `g ∘ f` ist eine der grundlegendsten Operationen in der
Mathematik:

- Identitaet: `id ∘ f = f ∘ id = f`
- Assoziativitaet: `(h ∘ g) ∘ f = h ∘ (g ∘ f)`
- I.A. **nicht kommutativ**: `g ∘ f ≠ f ∘ g`

Beispiel oben: `square ∘ increment` (3 → 4 → 16) ≠
`increment ∘ square` (3 → 9 → 10).

## Verwandt

- Aufgabe **302-pipeline**: beliebig viele Ops nacheinander.
- Aufgabe **305-curry**: partielle Anwendung.

In FP-Sprachen wie Haskell ist Komposition ein **Operator** (`.`):
`g . f`. In Python muss man es per Funktion bauen.
