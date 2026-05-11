---
schema_version: 1
id: 018-ggt
revision: 1
titel: Größter gemeinsamer Teiler
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 8
tags: [zahlen, schleifen, euklid, rekursion]
pfade: [python_mathe]
voraussetzungen: [016-quersumme]
quelle:
  url: https://de.wikipedia.org/wiki/Euklidischer_Algorithmus
  notiz: Klassiker, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ggt
hints:
  - kosten: 0
    text: |
      Euklidischer Algorithmus: solange `b != 0` ist, ersetze `(a, b)` durch
      `(b, a % b)`. Am Ende ist `a` der ggT.
  - kosten: 11
    text: |
      Eleganter mit Tuple-Unpacking:

      ```
      while b:
          a, b = b, a % b
      return a
      ```
tests_sichtbar:
  - input: [12, 8]
    expected: 4
  - input: [17, 5]
    expected: 1
  - input: [100, 25]
    expected: 25
  - input: [0, 7]
    expected: 7
tests_versteckt:
  - input: [48, 36]
    expected: 12
  - input: [1071, 462]
    expected: 21
  - input: [1, 1]
    expected: 1
  - input: [123456, 7890]
    expected: 6
  - input: [13, 0]
    expected: 13
starter_code: |
  def ggt(a: int, b: int) -> int:
      # Deine Lösung hier
      pass
---

# Größter gemeinsamer Teiler

Schreibe eine Funktion `ggt(a, b)`, die den **größten gemeinsamen
Teiler** zweier nicht-negativer ganzer Zahlen zurückgibt -- die
größte Zahl, durch die sowohl `a` als auch `b` ohne Rest teilbar sind.

## Beispiele

| `a`    | `b`   | `ggt(a, b)` |
|--------|-------|-------------|
| `12`   | `8`   | `4`         |
| `17`   | `5`   | `1`         |
| `100`  | `25`  | `25`        |
| `0`    | `7`   | `7`         |

## Idee: Euklidischer Algorithmus

Statt alle Teiler durchzuprobieren, gilt eine elegante Beobachtung
von Euklid:

$$
\gcd(a, b) = \gcd(b, a \bmod b)
$$

Wiederhole das, bis `b` null wird -- dann ist `a` der ggT.

## Hintergrund

Der euklidische Algorithmus ist einer der ältesten bekannten
Algorithmen überhaupt. Er steht in Buch VII der Elemente von Euklid
(ca. 300 v. Chr.) und ist auch heute noch Standard für ggT-Berechnungen.
