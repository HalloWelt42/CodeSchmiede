---
schema_version: 1
id: 190-leetspeak
revision: 1
titel: Leetspeak-Konvertierung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [strings, dict, mapping, replace, fun]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Internet-Folklore
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: leetspeak
hints:
  - kosten: 0
    text: |
      Ersetze einzelne Buchstaben durch Leetspeak-Ziffern:
      a→4, e→3, i→1, o→0, s→5, t→7. Sonst unveraendert.
      Eingabe ist case-insensitive bei der Suche, Ausgabe ist klein.
  - kosten: 10
    text: |
      Dict mit Mapping. Iteriere Zeichen fuer Zeichen,
      nimm c.lower() um zu mappen.
tests_sichtbar:
  - input: ["tea"]
    expected: "734"
  - input: ["hallo"]
    expected: "h4ll0"
  - input: [""]
    expected: ""
  - input: ["abc"]
    expected: "4bc"
tests_versteckt:
  - input: ["TEST"]
    expected: "7357"
  - input: ["Hello World"]
    expected: "h3ll0 w0rld"
  - input: ["Python"]
    expected: "py7h0n"
  - input: ["1234"]
    expected: "1234"
  - input: ["xyz"]
    expected: "xyz"
  - input: ["AEIOST"]
    expected: "431057"
starter_code: |
  def leetspeak(text: str) -> str:
      # Deine Lösung hier -- klein-Ausgabe, Mapping a→4, e→3, ...
      pass
---

# Leetspeak-Konvertierung

In **Leetspeak** ("1337-speak") werden Buchstaben durch optisch
aehnliche Ziffern ersetzt. Schreibe `leetspeak(text)`, das ein
einfaches Subset umsetzt:

| Buchstabe | Ziffer |
|-----------|--------|
| `a`       | `4`    |
| `e`       | `3`    |
| `i`       | `1`    |
| `o`       | `0`    |
| `s`       | `5`    |
| `t`       | `7`    |

Andere Zeichen bleiben unveraendert. Die Eingabe darf gemischte
Gross/Kleinschreibung haben -- die Ausgabe ist **immer klein**.

## Beispiele

| Eingabe         | Leetspeak       |
|-----------------|-----------------|
| `"tea"`         | `"734"`         |
| `"hallo"`       | `"h4ll0"`       |
| `"Python"`      | `"py7h0n"`      |
| `"Hello World"` | `"h3ll0 w0rld"` |
| `"TEST"`        | `"7357"`        |
| `"AEIOST"`      | `"431057"`      |

## Idee

```python
TABELLE = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "t": "7"}

def leetspeak(text):
    return "".join(TABELLE.get(c, c) for c in text.lower())
```

`dict.get(c, c)` liefert die Ziffer, wenn vorhanden, sonst das
Original-Zeichen.

## Mit `str.translate`

Effizienter ueber Python-Translate-Tabelle:

```python
TRANS = str.maketrans({"a":"4","e":"3","i":"1","o":"0","s":"5","t":"7"})

def leetspeak(text):
    return text.lower().translate(TRANS)
```

## Hintergrund

Leetspeak entstand in den 80ern in BBS-Foren als Code, um
Filter-Wortlisten (z.B. fuer "elite") auszuhebeln. Aus "elite"
wurde "1337" -- daher der Name. Heute eher Internet-Folklore als
Kommunikations-Geheimcode.
