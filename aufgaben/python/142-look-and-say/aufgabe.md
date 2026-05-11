---
schema_version: 1
id: 142-look-and-say
revision: 1
titel: Look-and-Say-Folge
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 40
schaetz_minuten: 15
tags: [strings, folgen, gruppieren, itertools]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische rekursive Folge nach John Conway
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: look_and_say
hints:
  - kosten: 0
    text: |
      Start "1". Jeder Schritt: lese den vorherigen String laut vor.
      "1" -> "11" (eine Eins) -> "21" (zwei Einsen) ->
      "1211" (eine Zwei, eine Eins) -> "111221" -> ...
      Liefere das n-te Glied (n=1 → "1").
  - kosten: 15
    text: |
      itertools.groupby gruppiert aufeinanderfolgende gleiche Zeichen.
      Pro Gruppe: str(len(list(g))) + zeichen.
tests_sichtbar:
  - input: [1]
    expected: "1"
  - input: [2]
    expected: "11"
  - input: [3]
    expected: "21"
  - input: [4]
    expected: "1211"
tests_versteckt:
  - input: [5]
    expected: "111221"
  - input: [6]
    expected: "312211"
  - input: [7]
    expected: "13112221"
  - input: [8]
    expected: "1113213211"
  - input: [10]
    expected: "13211311123113112211"
starter_code: |
  def look_and_say(n: int) -> str:
      # Deine Lösung hier -- start "1", n Iterationen
      pass
---

# Look-and-Say-Folge

Die **Look-and-Say-Folge** entsteht, indem man jeden Term **laut vorliest**:

```
1
11        eine Eins
21        zwei Einsen
1211      eine Zwei, eine Eins
111221    eine Eins, eine Zwei, zwei Einsen
312211    drei Einsen, zwei Zweien, eine Eins
...
```

Schreibe eine Funktion `look_and_say(n)`, die das **n-te Glied** der
Folge zurueckgibt (`n = 1` → `"1"`).

## Beispiele

| `n` | Term                         |
|-----|------------------------------|
| `1` | `"1"`                        |
| `2` | `"11"`                       |
| `3` | `"21"`                       |
| `4` | `"1211"`                     |
| `5` | `"111221"`                   |
| `6` | `"312211"`                   |
| `7` | `"13112221"`                 |

## Idee

`itertools.groupby` gruppiert aufeinanderfolgende gleiche Zeichen.
Pro Gruppe: Anzahl + Zeichen.

```python
from itertools import groupby

def schritt(s):
    return "".join(f"{len(list(g))}{z}" for z, g in groupby(s))

def look_and_say(n):
    s = "1"
    for _ in range(n - 1):
        s = schritt(s)
    return s
```

## Hintergrund

John Conway hat 1986 das **kosmologische Theorem** bewiesen: jeder
Term der Folge zerfaellt schliesslich in 92 "Atome" (kleine wiederkehrende
Bausteine, benannt nach chemischen Elementen). Das Wachstum jedes Terms
strebt gegen Conways Konstante $\lambda \approx 1{,}3036$.
