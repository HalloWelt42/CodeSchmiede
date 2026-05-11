---
schema_version: 1
id: 151-schnapszahl
revision: 1
titel: Schnapszahl-Prüfung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [zahlen, strings, set]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Ziffer-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ist_schnapszahl
hints:
  - kosten: 0
    text: |
      Eine Schnapszahl besteht aus mindestens 2 gleichen Ziffern --
      11, 22, 333, 7777. Nicht 1, nicht 12, nicht 122.
      Negative Zahlen verhalten sich wie ihr Betrag.
  - kosten: 10
    text: |
      str(abs(n)) liefert die Ziffern. set(...) → wenn nur ein
      Element drin ist UND die Zahl >= 2 Stellen hat, ist es Schnapszahl.
tests_sichtbar:
  - input: [11]
    expected: true
  - input: [12]
    expected: false
  - input: [333]
    expected: true
  - input: [7]
    expected: false
tests_versteckt:
  - input: [22222]
    expected: true
  - input: [1111111]
    expected: true
  - input: [122]
    expected: false
  - input: [0]
    expected: false
  - input: [-44]
    expected: true
  - input: [99]
    expected: true
  - input: [10]
    expected: false
  - input: [-100]
    expected: false
starter_code: |
  def ist_schnapszahl(n: int) -> bool:
      # Deine Lösung hier -- mind. 2 Stellen, alle gleich
      pass
---

# Schnapszahl-Prüfung

Eine **Schnapszahl** ist eine Zahl mit mindestens **zwei Stellen**, in
der **alle Ziffern gleich** sind: 11, 22, 333, 7777, ...

Einstellige Zahlen (`0`-`9`) sind keine Schnapszahlen, gemischte
auch nicht.

## Beispiele

| `n`         | Schnapszahl? |
|-------------|--------------|
| `11`        | `True`       |
| `333`       | `True`       |
| `1111111`   | `True`       |
| `7`         | `False`      |
| `12`        | `False`      |
| `122`       | `False`      |
| `0`         | `False`      |
| `-44`       | `True`       |

Negative Zahlen verhalten sich wie ihr **Betrag**: `-44` ist
Schnapszahl, weil `44` eine ist.

## Idee -- Set der Ziffern

Wenn `set(str(abs(n)))` genau 1 Element enthält UND die Zahl mindestens
2 Stellen hat, ist es eine Schnapszahl.

## Hintergrund

Der Name kommt aus dem Kartenspiel **Schnapsen** -- dort schreibt man
einen Punktestand wie 22, 33, 66 gerne als Schnapszahl auf, weil sie
sich gut einprägen. Im Deutschen werden auch Wiederholungen wie 121
oder 1221 (Palindrom-Zahlen) manchmal als Schnapszahl bezeichnet --
hier nutzen wir die strenge Definition.
