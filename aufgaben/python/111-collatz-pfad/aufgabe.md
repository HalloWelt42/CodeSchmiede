---
schema_version: 1
id: 111-collatz-pfad
revision: 1
titel: Collatz-Pfad als Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [zahlen, listen, schleifen, beruehmt]
pfade: [python_mathe2]
voraussetzungen: [020-collatz]
quelle:
  url: https://de.wikipedia.org/wiki/Collatz-Problem
  notiz: Variante von 020-collatz mit ganzem Pfad
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: collatz_pfad
hints:
  - kosten: 0
    text: |
      Wie 020-collatz, aber liefere die ganze Folge als Liste --
      inkl. Startwert und finaler 1.
  - kosten: 7
    text: |
      `pfad = [n]`. while n != 1: n = n//2 oder 3n+1. pfad.append(n).
tests_sichtbar:
  - input: [1]
    expected: [1]
  - input: [2]
    expected: [2, 1]
  - input: [6]
    expected: [6, 3, 10, 5, 16, 8, 4, 2, 1]
  - input: [3]
    expected: [3, 10, 5, 16, 8, 4, 2, 1]
tests_versteckt:
  - input: [16]
    expected: [16, 8, 4, 2, 1]
  - input: [7]
    expected: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
  - input: [27]
    expected: [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
starter_code: |
  def collatz_pfad(n: int) -> list[int]:
      # Deine Lösung hier -- vollständige Folge inkl. Start und 1.
      pass
---

# Collatz-Pfad als Liste

Schreibe eine Funktion `collatz_pfad(n)`, die den **vollständigen
Pfad** der Collatz-Folge ausgehend von `n` als Liste zurückgibt --
inklusive Startwert und finaler `1`.

## Regeln (wie bei 020-collatz)

- gerade: $n / 2$
- ungerade: $3n + 1$
- stoppe bei $n = 1$

## Beispiele

| Start | Pfad                                         |
|-------|----------------------------------------------|
| `1`   | `[1]`                                        |
| `2`   | `[2, 1]`                                     |
| `6`   | `[6, 3, 10, 5, 16, 8, 4, 2, 1]`              |
| `7`   | 17 Schritte, endet bei 1                     |
| `27`  | 111 Schritte, höchster Wert: 9232           |

## Hintergrund

Die einfache Formulierung verbirgt eines der schwierigsten ungelösten
Probleme der Mathematik. Die Collatz-Vermutung (jede Folge endet bei
1) ist bis heute unbewiesen.
