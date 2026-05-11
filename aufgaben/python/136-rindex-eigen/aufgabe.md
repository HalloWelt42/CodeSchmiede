---
schema_version: 1
id: 136-rindex-eigen
revision: 1
titel: Letztes Vorkommen finden
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [listen, schleifen, suche]
pfade: [python_listen3]
voraussetzungen: []
quelle:
  url: null
  notiz: Eigene rindex-Reimplementierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: letztes_vorkommen
hints:
  - kosten: 0
    text: |
      Liste rückwärts durchgehen, ersten Treffer zurückgeben.
      Nicht gefunden → -1.
  - kosten: 5
    text: |
      `for i in range(len(liste) - 1, -1, -1)` geht von hinten.
      Pythonic mit reversed + enumerate ist auch okay.
tests_sichtbar:
  - input: [[1, 2, 3, 2, 1], 2]
    expected: 3
  - input: [[1, 2, 3], 4]
    expected: -1
  - input: [[], 1]
    expected: -1
  - input: [[5], 5]
    expected: 0
tests_versteckt:
  - input: [[1, 1, 1, 1, 1], 1]
    expected: 4
  - input: [["a", "b", "a", "c"], "a"]
    expected: 2
  - input: [[True, False, True], False]
    expected: 1
  - input: [[1, 2, 3], 1]
    expected: 0
  - input: [[None, None], None]
    expected: 1
starter_code: |
  def letztes_vorkommen(liste: list, ziel) -> int:
      # Deine Lösung hier -- letzter Index, sonst -1.
      pass
---

# Letztes Vorkommen finden

Schreibe eine Funktion `letztes_vorkommen(liste, ziel)`, die den
Index des **letzten Vorkommens** von `ziel` in der Liste zurückgibt.

Nicht gefunden → `-1`.

## Beispiele

| Liste            | Ziel | Ergebnis |
|------------------|------|----------|
| `[1,2,3,2,1]`    | `2`  | `3`      |
| `[1,2,3]`        | `4`  | `-1`     |
| `[]`             | `1`  | `-1`     |
| `[5]`            | `5`  | `0`      |
| `[1,1,1,1,1]`    | `1`  | `4`      |

## Idee

Schleife von hinten nach vorn, ersten Treffer zurückgeben:

```
for i in range(len(liste) - 1, -1, -1):
    if liste[i] == ziel:
        return i
return -1
```

## Vergleich mit Standard-Library

Strings haben `str.rfind(sub)` -- liefert `-1` bei nicht gefunden.
Listen haben `list.index(x)` (vorwärts) aber kein `rindex` direkt.
Hier baust du die fehlende Funktion.
