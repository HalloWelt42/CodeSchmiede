---
schema_version: 1
id: 020-collatz
revision: 1
titel: Collatz-Folge Laenge
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [zahlen, schleifen, beruehmt]
pfade: [python_mathe]
voraussetzungen: [017-fakultät]
quelle:
  url: https://de.wikipedia.org/wiki/Collatz-Problem
  notiz: Beruehmtes ungelöstes Problem, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: collatz_laenge
hints:
  - kosten: 0
    text: |
      Wenn die Zahl gerade ist, halbiere sie. Wenn ungerade, mal 3 plus 1.
      Zähle die Schritte bis du bei 1 ankommst.
  - kosten: 10
    text: |
      Schleife `while n != 1`, mit Schrittzähler. Achtung: bei `n == 1`
      sofort 0 Schritte zurückgeben.
tests_sichtbar:
  - input: [1]
    expected: 0
  - input: [2]
    expected: 1
  - input: [6]
    expected: 8
  - input: [27]
    expected: 111
tests_versteckt:
  - input: [3]
    expected: 7
  - input: [16]
    expected: 4
  - input: [97]
    expected: 118
  - input: [871]
    expected: 178
starter_code: |
  def collatz_laenge(n: int) -> int:
      # Deine Lösung hier
      pass
---

# Collatz-Folge: Laenge bis zur 1

Die **Collatz-Folge** ist nach folgender Regel definiert:

- ist $n$ **gerade**, dann ist das nächste Glied $n / 2$
- ist $n$ **ungerade**, dann ist das nächste Glied $3n + 1$
- die Folge endet, sobald $n = 1$ erreicht wird

Schreibe eine Funktion `collatz_laenge(n)`, die die **Anzahl Schritte**
zurückgibt, bis die Folge ausgehend von `n` die 1 erreicht. Wer schon
bei 1 startet, braucht 0 Schritte.

## Beispiele

| Start | Folge                        | Schritte |
|-------|------------------------------|----------|
| `1`   | `1`                          | `0`      |
| `2`   | `2, 1`                       | `1`      |
| `6`   | `6, 3, 10, 5, 16, 8, 4, 2, 1`| `8`      |
| `27`  | (lange Folge)                | `111`    |

## Hintergrund

Die **Collatz-Vermutung** behauptet, dass diese Folge für **jede**
positive Startzahl irgendwann bei 1 endet. Stand 2026: bewiesen ist
das immer noch nicht -- aber bis weit jenseits von $2^{68}$ stimmt es
empirisch. Ein beruehmtes ungelöstes Problem der Mathematik, mit
einer fast albern einfachen Formulierung.
