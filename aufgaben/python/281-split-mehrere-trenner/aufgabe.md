---
schema_version: 1
id: 281-split-mehrere-trenner
revision: 1
titel: Text an mehreren Trennzeichen splitten
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 35
schaetz_minuten: 12
tags: [strings, regex, parsing]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: re.split-Klassiker
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: split_alles
hints:
  - kosten: 0
    text: |
      Splitte einen Text an JEDER der Trennzeichen ',', ';', '|' oder
      Whitespace -- in einem Aufruf. Leere Stücke entfernen.
      "a,b ;c|d  e" → ["a", "b", "c", "d", "e"].
  - kosten: 20
    text: |
      re.split(r"[,;|\s]+", text) splittet an einer ODER MEHRERER
      der Trennzeichen-Klasse. Dann leere Strings rausfiltern.
tests_sichtbar:
  - input: ["a,b;c|d e"]
    expected: ["a", "b", "c", "d", "e"]
  - input: [""]
    expected: []
  - input: ["solo"]
    expected: ["solo"]
  - input: ["a,b,c"]
    expected: ["a", "b", "c"]
tests_versteckt:
  - input: ["a;;;b"]
    expected: ["a", "b"]
  - input: [",,,a"]
    expected: ["a"]
  - input: ["a,,,"]
    expected: ["a"]
  - input: ["  viel    Whitespace  "]
    expected: ["viel", "Whitespace"]
  - input: ["a|b;c,d e"]
    expected: ["a", "b", "c", "d", "e"]
  - input: ["1;2,3|4 5"]
    expected: ["1", "2", "3", "4", "5"]
  - input: [",;|"]
    expected: []
starter_code: |
  import re

  def split_alles(text: str) -> list[str]:
      # Deine Lösung hier -- splitte an , ; | oder Whitespace
      pass
---

# Text an mehreren Trennzeichen splitten

Schreibe `split_alles(text)`, die einen Text an **jedem** dieser
Trennzeichen splittet:

- Komma `,`
- Semikolon `;`
- Pipe `|`
- beliebiges Whitespace (Leerzeichen, Tab, Newline)

**Mehrfache Trenner** (auch gemischt) zählen als ein Trenner.
**Leere Stücke** werden entfernt.

## Beispiele

| Eingabe                  | Ergebnis                        |
|--------------------------|----------------------------------|
| `"a,b;c|d e"`            | `["a","b","c","d","e"]`          |
| `"a;;;b"`                | `["a","b"]`                      |
| `",,,a"`                 | `["a"]`                          |
| `"  viel    Whitespace  "` | `["viel","Whitespace"]`        |
| `"1;2,3|4 5"`            | `["1","2","3","4","5"]`          |
| `",;|"`                  | `[]`                             |
| `""`                     | `[]`                             |

## Idee -- re.split + Filter

```python
import re

def split_alles(text):
    teile = re.split(r"[,;|\s]+", text)
    return [t for t in teile if t]
```

`[,;|\s]+` ist eine **Zeichen-Klasse**: matcht eines der
aufgefuehrten Zeichen, **`+`** matcht eines oder mehr (das
verschluckt mehrfache Trenner direkt).

`if t` filtert leere Strings (truthy-Check).

## Stolperstein -- leere Strings am Rand

`re.split(r"[,;|\s]+", ",a,")` liefert `["", "a", ""]` -- das
fuehrende und nachfolgende Trennzeichen erzeugt jeweils ein leeres
Element. Daher das `if t`-Filter.

## Vergleich mit `str.split`

`str.split` mit Argument splittet nur an **einem** Trennzeichen
und behaelt leere Stücke. Ohne Argument splittet es an Whitespace
und filtert. Wenn man mehrere Trennzeichen will, ist `re.split`
das Mittel der Wahl.

## Anwendung

- CSV/TSV-Dateien mit gemischten Trennern.
- Tag-Eingabefelder ("python, regex; parsing | text").
- Log-Parsing.
