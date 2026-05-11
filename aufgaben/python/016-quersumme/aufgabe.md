---
schema_version: 1
id: 016-quersumme
revision: 1
titel: Quersumme einer Zahl
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [zahlen, schleifen, modulo, division]
pfade: [python_mathe]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Quersumme
  notiz: Klassische Mathe-Aufgabe, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: quersumme
hints:
  - kosten: 0
    text: Mit `% 10` bekommst du die letzte Ziffer einer Zahl.
  - kosten: 10
    text: Mit `// 10` schneidest du die letzte Ziffer ab.
  - kosten: 20
    text: |
      Schleife:

      ```
      summe = 0
      while n > 0:
          summe += n % 10
          n //= 10
      ```
tests_sichtbar:
  - input: [123]
    expected: 6
  - input: [9]
    expected: 9
  - input: [0]
    expected: 0
  - input: [99999]
    expected: 45
tests_versteckt:
  - input: [1000000]
    expected: 1
  - input: [10]
    expected: 1
  - input: [4711]
    expected: 13
  - input: [987654321]
    expected: 45
starter_code: |
  def quersumme(n: int) -> int:
      # Deine Lösung hier
      pass
---

# Quersumme einer Zahl

Schreibe eine Funktion `quersumme(n)`, die die **Quersumme** einer
nicht-negativen ganzen Zahl `n` zurückgibt -- also die Summe aller
Ziffern.

## Beispiele

| Eingabe | Ergebnis |
|---------|----------|
| `123`   | `6`      |
| `9`     | `9`      |
| `0`     | `0`      |
| `4711`  | `13`     |

## Idee

Mit `n % 10` bekommst du die letzte Ziffer von `n`. Mit `n // 10`
entfernst du sie. Wiederhole das, bis `n` null ist, und summiere
unterwegs alle Ziffern.

## Hintergrund

Die Quersumme spielt eine Rolle bei vielen Teilbarkeitsregeln -- eine
Zahl ist genau dann durch 3 (oder 9) teilbar, wenn ihre Quersumme es
ist. Mehr dazu unter [Wikipedia: Quersumme](https://de.wikipedia.org/wiki/Quersumme).
