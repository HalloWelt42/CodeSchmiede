---
schema_version: 1
id: 145-tausender-trennzeichen
revision: 1
titel: Tausender-Trennzeichen (deutsch)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [strings, zahlen, formatierung]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Formatierungs-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: mit_punkten
hints:
  - kosten: 0
    text: |
      Formatiere eine ganze Zahl mit Punkt als Tausender-Trenner
      (deutsche Konvention): 1000000 → "1.000.000".
      Negative Zahlen mit Vorzeichen: -1234 → "-1.234".
  - kosten: 10
    text: |
      Format-String f"{n:_}" liefert "1_000_000" mit Unterstrich.
      Danach replace("_", ".").
tests_sichtbar:
  - input: [0]
    expected: "0"
  - input: [1234]
    expected: "1.234"
  - input: [1000000]
    expected: "1.000.000"
  - input: [-1234]
    expected: "-1.234"
tests_versteckt:
  - input: [999]
    expected: "999"
  - input: [1000]
    expected: "1.000"
  - input: [1234567890]
    expected: "1.234.567.890"
  - input: [-1000000000]
    expected: "-1.000.000.000"
  - input: [42]
    expected: "42"
  - input: [100000]
    expected: "100.000"
starter_code: |
  def mit_punkten(n: int) -> str:
      # Deine Lösung hier -- Punkt-Trenner alle 3 Stellen von rechts
      pass
---

# Tausender-Trennzeichen (deutsch)

Schreibe eine Funktion `mit_punkten(n)`, die eine ganze Zahl als
String mit **deutschem Tausender-Trennzeichen** (Punkt) zurueckgibt.

## Beispiele

| `n`            | Ergebnis            |
|----------------|---------------------|
| `0`            | `"0"`               |
| `1234`         | `"1.234"`           |
| `1000000`      | `"1.000.000"`       |
| `-1234`        | `"-1.234"`          |
| `1234567890`   | `"1.234.567.890"`   |

## Idee -- Format-String mit Unterstrich

Python kennt seit 3.6 das `_`-Format als Tausender-Trenner. Danach
einmal `replace`:

```python
def mit_punkten(n):
    return f"{n:_}".replace("_", ".")
```

## Alternative -- per Hand

```python
def mit_punkten(n):
    if n < 0:
        return "-" + mit_punkten(-n)
    s = str(n)
    teile = []
    while len(s) > 3:
        teile.append(s[-3:])
        s = s[:-3]
    teile.append(s)
    return ".".join(reversed(teile))
```

## Locale-Hinweis

Ueber `locale.format_string("%d", n, grouping=True)` ginge es auch,
aber Locales sind haeufig nicht installiert (Container, CI). Der
Format-String-Trick ist robust und braucht nichts ausser Python.
