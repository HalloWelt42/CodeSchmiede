---
schema_version: 1
id: 019-primfaktoren
revision: 1
titel: Primfaktorzerlegung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [zahlen, schleifen, primzahlen]
pfade: [python_mathe]
voraussetzungen: [018-ggt]
quelle:
  url: https://de.wikipedia.org/wiki/Primfaktorzerlegung
  notiz: Klassisches Mathe-Problem, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: primfaktoren
hints:
  - kosten: 0
    text: Teile `n` so oft wie möglich durch 2, dann durch 3, dann durch 5, ...
  - kosten: 4
    text: |
      Probiere alle Teiler ab 2 aufsteigend. Wenn `n % i == 0`, fuege `i`
      zur Liste hinzu und teile `n` durch `i`. Sonst erhöhe `i` um 1.
  - kosten: 8
    text: |
      Schlüsselbeobachtung: Wenn `i * i > n`, ist `n` selbst die letzte
      Primzahl in der Zerlegung. Damit kann die Schleife für große `n`
      vorzeitig abbrechen.
tests_sichtbar:
  - input: [12]
    expected: [2, 2, 3]
  - input: [13]
    expected: [13]
  - input: [1]
    expected: []
  - input: [60]
    expected: [2, 2, 3, 5]
tests_versteckt:
  - input: [2]
    expected: [2]
  - input: [97]
    expected: [97]
  - input: [100]
    expected: [2, 2, 5, 5]
  - input: [1024]
    expected: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
  - input: [999983]
    expected: [999983]
starter_code: |
  def primfaktoren(n: int) -> list[int]:
      # Deine Lösung hier
      pass
---

# Primfaktorzerlegung

Schreibe eine Funktion `primfaktoren(n)`, die eine Liste der
**Primfaktoren** von `n` in aufsteigender Reihenfolge zurückgibt.
Mehrfach vorkommende Faktoren werden mehrfach aufgelistet.

## Beispiele

| Eingabe | Ergebnis             |
|---------|----------------------|
| `12`    | `[2, 2, 3]`          |
| `13`    | `[13]`               |
| `1`     | `[]`                 |
| `60`    | `[2, 2, 3, 5]`       |
| `100`   | `[2, 2, 5, 5]`       |

## Vorgehen

Probiere Teiler $i$ ab 2 aufsteigend. Wenn $n$ durch $i$ teilbar ist,
schreibe $i$ in die Ergebnisliste und teile $n$ durch $i$. Sonst geh
zum nächsten $i$. Wiederhole, bis $n = 1$.

## Hintergrund

Der **Fundamentalsatz der Arithmetik** garantiert, dass jede natuerliche
Zahl größer 1 eine eindeutige Primfaktorzerlegung hat. Diese
Zerlegung ist die Grundlage vieler kryptographischer Verfahren -- die
Sicherheit von RSA beruht darauf, dass die Zerlegung sehr großer
Zahlen praktisch nicht in vertretbarer Zeit möglich ist.
