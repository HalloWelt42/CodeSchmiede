---
schema_version: 1
id: 127-primzahlen-bis-n-zahl
revision: 1
titel: Primzahlen bis n zählen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [zahlen, primzahlen, sieb, schleifen]
pfade: [python_mathe2]
voraussetzungen: [039-eratosthenes]
quelle:
  url: null
  notiz: Variante des Sieb-Problems
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: anzahl_primzahlen
hints:
  - kosten: 0
    text: |
      Wie viele Primzahlen <= n? Sieb des Eratosthenes, Anzahl
      True-Werte zaehlen.
  - kosten: 10
    text: |
      Bei n < 2 → 0. Sonst Sieb bauen, `sum(ist_prim)` zaehlt
      die True-Werte.
tests_sichtbar:
  - input: [10]
    expected: 4
  - input: [2]
    expected: 1
  - input: [1]
    expected: 0
  - input: [100]
    expected: 25
tests_versteckt:
  - input: [0]
    expected: 0
  - input: [3]
    expected: 2
  - input: [50]
    expected: 15
  - input: [1000]
    expected: 168
  - input: [10000]
    expected: 1229
starter_code: |
  def anzahl_primzahlen(n: int) -> int:
      # Deine Lösung hier -- Anzahl Primzahlen <= n.
      pass
---

# Primzahlen bis n zählen

Schreibe eine Funktion `anzahl_primzahlen(n)`, die die **Anzahl der
Primzahlen** kleiner oder gleich `n` zurückgibt.

## Beispiele

| `n`     | Anzahl |
|---------|--------|
| `1`     | `0`    |
| `2`     | `1`    |
| `10`    | `4`    | (2, 3, 5, 7)
| `100`   | `25`   |
| `1000`  | `168`  |
| `10000` | `1229` |

## Algorithmus

Sieb des Eratosthenes. `O(n log log n)` -- deutlich schneller als
jede Zahl einzeln zu testen.

## Hintergrund

Nach dem **Primzahlsatz** (Hadamard, de la Vallée Poussin, 1896)
verhalten sich die Primzahlen ungefaehr wie $n / \ln n$. Bei
$n = 10\,000$ sagt die Naeherung 1086, tatsaechlich 1229 -- die
Naeherung wird mit wachsendem n proportional besser.
