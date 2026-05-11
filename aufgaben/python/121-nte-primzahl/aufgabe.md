---
schema_version: 1
id: 121-nte-primzahl
revision: 1
titel: n-te Primzahl
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 8
tags: [zahlen, primzahlen, schleifen]
pfade: [python_mathe2]
voraussetzungen: [019-primfaktoren]
quelle:
  url: null
  notiz: Inspiration aus Exercism (nth-prime), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: nte_primzahl
hints:
  - kosten: 0
    text: |
      n-te Primzahl: 1 → 2, 2 → 3, 3 → 5, ... Bei n < 1 → -1.
  - kosten: 8
    text: |
      Schleife: gefunden = 0, kandidat = 1.
      Solange gefunden < n: kandidat += 1; wenn prim, gefunden += 1.
      Primalitaet via i*i <= n bis sqrt.
tests_sichtbar:
  - input: [1]
    expected: 2
  - input: [2]
    expected: 3
  - input: [6]
    expected: 13
  - input: [0]
    expected: -1
tests_versteckt:
  - input: [3]
    expected: 5
  - input: [4]
    expected: 7
  - input: [5]
    expected: 11
  - input: [10]
    expected: 29
  - input: [100]
    expected: 541
  - input: [1000]
    expected: 7919
  - input: [-1]
    expected: -1
starter_code: |
  def nte_primzahl(n: int) -> int:
      # Deine Lösung hier -- 1 → 2, ungültige Eingabe → -1.
      pass
---

# n-te Primzahl

Schreibe eine Funktion `nte_primzahl(n)`, die die n-te Primzahl
liefert (1-basiert, also `nte_primzahl(1) == 2`).

Bei `n < 1` → `-1`.

## Beispiele

| `n`   | Primzahl |
|-------|----------|
| `1`   | `2`      |
| `2`   | `3`      |
| `3`   | `5`      |
| `6`   | `13`     |
| `10`  | `29`     |
| `100` | `541`    |
| `1000`| `7919`   |
| `0`   | `-1`     |

## Algorithmus

Naive Variante: Zahlen aufzählen, jede auf Primalität prüfen,
zählen bis n. $O(\sqrt{p})$ pro Test, daher insgesamt $O(p \sqrt{p})$
mit $p$ = n-te Primzahl.

Schneller wäre ein **Sieb des Eratosthenes** -- aber dafür braucht
man eine Obergrenze. Praktisch für große n nimmt man eine grobe
Schätzung wie $n \cdot (\ln n + \ln \ln n)$.
