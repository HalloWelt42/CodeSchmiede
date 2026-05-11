---
schema_version: 1
id: 201-quadratzahl-pruefen
revision: 1
titel: Ist die Zahl ein Quadrat?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [mathematik, zahlen, sqrt]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Klassifikation
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ist_quadratzahl
hints:
  - kosten: 0
    text: |
      Prüfe, ob n eine Quadratzahl ist (1, 4, 9, 16, 25, 36, ...).
      n < 0 → False. 0 → True (= 0^2).
      Achtung: math.sqrt liefert Floats und ist bei großen n ungenau.
  - kosten: 15
    text: |
      math.isqrt(n) liefert die ganzzahlige Wurzel (immer exakt).
      Prüfe: w = isqrt(n); return w * w == n.
tests_sichtbar:
  - input: [0]
    expected: true
  - input: [1]
    expected: true
  - input: [4]
    expected: true
  - input: [10]
    expected: false
tests_versteckt:
  - input: [9]
    expected: true
  - input: [16]
    expected: true
  - input: [25]
    expected: true
  - input: [99]
    expected: false
  - input: [100]
    expected: true
  - input: [-4]
    expected: false
  - input: [10000]
    expected: true
  - input: [10001]
    expected: false
  - input: [99980001]
    expected: true
starter_code: |
  def ist_quadratzahl(n: int) -> bool:
      # Deine Lösung hier -- math.isqrt fuer exakte Pruefung
      pass
---

# Ist die Zahl ein Quadrat?

Schreibe `ist_quadratzahl(n)`, die `True` zurückgibt, wenn `n` eine
**Quadratzahl** ist -- also $n = k^2$ für ein nicht-negatives ganzes
$k$.

Bei `n < 0` → `False`. `0` zählt als Quadrat (`0 = 0^2`).

## Beispiele

| `n`      | Quadrat? | $\sqrt{n}$  |
|----------|----------|-------------|
| `0`      | `True`   | `0`         |
| `1`      | `True`   | `1`         |
| `4`      | `True`   | `2`         |
| `9`      | `True`   | `3`         |
| `100`    | `True`   | `10`        |
| `99`     | `False`  | `≈9.95`     |
| `10000`  | `True`   | `100`       |
| `99980001`| `True`  | `9999`      |

## Idee mit `math.isqrt` (exakt!)

`math.isqrt(n)` liefert die **ganzzahlige Wurzel** ohne Float-Rundung.
Damit ist die Prüfung auch für riesige Zahlen exakt.

## Warum nicht `math.sqrt`?

`math.sqrt` arbeitet mit Floats (`float64`). Bei sehr großen Zahlen
(> $2^{52}$) verliert `float` Genauigkeit:

Für "kleine" `n` reicht `int(math.sqrt(n) + 0.5)` plus Vergleich --
aber `isqrt` ist sauberer.

## Hintergrund

Quadratzahlen erscheinen in der **Pythagoras-Aufgabe** (084),
in der **Project-Euler-Reihe** (z.B. **Quadrat-Summen-Differenz**, 086),
und sind die Basis vieler **zahlentheoretischer Vermutungen**
(Lagrange: jede natuerliche Zahl ist Summe von höchstens vier Quadraten).
