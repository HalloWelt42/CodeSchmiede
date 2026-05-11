---
schema_version: 1
id: 279-passwort-regex
revision: 1
titel: Passwort-Prüfung mit Lookahead-Regex
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [strings, regex, lookahead, sicherheit]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Lookahead-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: passwort_ok
hints:
  - kosten: 0
    text: |
      Prüfe ob das Passwort ALLE vier Bedingungen erfüllt:
      - Laenge >= 8
      - mind. 1 Kleinbuchstabe
      - mind. 1 Großbuchstabe
      - mind. 1 Ziffer
      Liefere True/False -- KEIN Score wie 129.
  - kosten: 25
    text: |
      Mit Lookahead-Asseritionen alle Bedingungen in einem Pattern:
      r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$".
      (?=...) prüft OHNE den Cursor zu bewegen.
tests_sichtbar:
  - input: ["Passwort1"]
    expected: true
  - input: ["passwort"]
    expected: false
  - input: ["PASSWORT1"]
    expected: false
  - input: ["pass1"]
    expected: false
tests_versteckt:
  - input: ["Abcdefg1"]
    expected: true
  - input: ["abcdefgh"]
    expected: false
  - input: ["ABCDEFGH"]
    expected: false
  - input: ["12345678"]
    expected: false
  - input: ["Aa1Aa1Aa1"]
    expected: true
  - input: ["Aa1"]
    expected: false
  - input: [""]
    expected: false
  - input: ["NurEinPasswort"]
    expected: false
starter_code: |
  import re

  def passwort_ok(p: str) -> bool:
      # Deine Lösung hier -- Regex mit Lookahead
      pass
---

# Passwort-Prüfung mit Lookahead-Regex

Schreibe `passwort_ok(p)`, die `True` zurückgibt, wenn das Passwort
**alle vier** Bedingungen erfüllt:

1. Laenge **mindestens 8** Zeichen
2. **mindestens 1 Kleinbuchstabe** (`a-z`)
3. **mindestens 1 Großbuchstabe** (`A-Z`)
4. **mindestens 1 Ziffer** (`0-9`)

## Beispiele

| Eingabe          | Gültig? | Begruendung               |
|------------------|----------|---------------------------|
| `"Passwort1"`    | `True`   | alle vier erfüllt        |
| `"Abcdefg1"`     | `True`   |                           |
| `"Aa1Aa1Aa1"`    | `True`   |                           |
| `"passwort"`     | `False`  | kein Großbuchstabe + Ziffer |
| `"PASSWORT1"`    | `False`  | kein Kleinbuchstabe       |
| `"pass1"`        | `False`  | zu kurz, kein Groß       |
| `"Aa1"`          | `False`  | zu kurz                   |
| `"12345678"`     | `False`  | nur Ziffern               |

## Idee -- Lookahead-Regex

`(?=...)` ist eine **Lookahead-Assertion**: prüft das Pattern,
bewegt den Cursor aber **nicht weiter**. Damit können wir mehrere
unabhängige Bedingungen "an die selbe Stelle" hängen.

`.{8,}` matcht dann tatsächlich die mindestens 8 Zeichen.

## Wie liest man die Regex?

```
(?=.*[a-z])  # Lookahead: irgendwo muss ein Kleinbuchstabe kommen
(?=.*[A-Z])  # Lookahead: irgendwo muss ein Großbuchstabe kommen
(?=.*\d)     # Lookahead: irgendwo muss eine Ziffer kommen
.{8,}        # Match: mindestens 8 beliebige Zeichen
```

Alle drei Lookaheads prüfen zuerst -- nur wenn alle erfüllt sind,
wird die "echte" Match-Bedingung getestet.

## Vergleich mit Aufgabe 129

Aufgabe **129-passwort-stärke** liefert einen Score 0-5 (mit
Sonderzeichen-Bonus). Hier nur True/False mit 4 Kriterien -- ein
einziger Regex statt einer Schleife durch Bedingungen.

## Anwendung

Lookaheads sind ein zentrales Regex-Feature, das in einfachen
Form-Validierungen, URL-Routing, Code-Highlighting und SearchEngine-
Filtern auftaucht.
