---
schema_version: 1
id: 278-telefon-de
revision: 1
titel: Deutsche Telefonnummer prüfen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 25
schaetz_minuten: 10
tags: [strings, regex, validierung]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Telefon-Validierung (vereinfacht)
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ist_telefon_de
hints:
  - kosten: 0
    text: |
      Prüfe ob String eine deutsche Telefonnummer ist (vereinfacht):
      Beginnt mit "+49 " ODER "0", danach 2-5 Ziffern Vorwahl,
      dann Leerzeichen oder /, dann mind. 4 Ziffern.
      Beispiele:
        "+49 30 12345678" → True
        "030/12345678"    → True
        "0151 1234567"    → True
        "12345"           → False
  - kosten: 20
    text: |
      Pattern wie r"^(?:\+49 |0)\d{2,5}[ /]\d{4,}$".
      re.fullmatch oder $-Anker verwenden.
tests_sichtbar:
  - input: ["+49 30 12345678"]
    expected: true
  - input: ["030/12345678"]
    expected: true
  - input: ["0151 1234567"]
    expected: true
  - input: ["12345"]
    expected: false
tests_versteckt:
  - input: ["+49 89 7654321"]
    expected: true
  - input: ["089/7654321"]
    expected: true
  - input: ["+1 555 1234567"]
    expected: false
  - input: [""]
    expected: false
  - input: ["030 12"]
    expected: false
  - input: ["abc 123 4567"]
    expected: false
  - input: ["+49 0 1234"]
    expected: false
  - input: ["0 1234 5678"]
    expected: false
starter_code: |
  import re

  def ist_telefon_de(s: str) -> bool:
      # Deine Lösung hier -- vereinfachte deutsche Format-Pruefung
      pass
---

# Deutsche Telefonnummer prüfen

Schreibe `ist_telefon_de(s)`, die `True` zurückgibt, wenn der String
eine **deutsche Telefonnummer** im einem dieser **vereinfachten
Formate** ist:

- beginnt mit `"+49 "` oder `"0"`
- gefolgt von **2-5 Ziffern Vorwahl** (mind. 2)
- dann ein **Leerzeichen oder `/`** als Trenner
- dann mindestens **4 Ziffern** Hauptnummer

## Beispiele

| Eingabe              | Gültig? |
|----------------------|----------|
| `"+49 30 12345678"`  | `True`   |
| `"030/12345678"`     | `True`   |
| `"0151 1234567"`     | `True`   |
| `"+49 89 7654321"`   | `True`   |
| `"089/7654321"`      | `True`   |
| `"+1 555 1234567"`   | `False` (US-Vorwahl) |
| `"12345"`            | `False` (kein Praefix) |
| `"030 12"`           | `False` (Hauptnummer zu kurz) |
| `"+49 0 1234"`       | `False` (Vorwahl zu kurz) |

## Idee

`(?:...)` ist eine **non-capturing** Gruppe -- gruppiert nur, ohne
das Ergebnis zu sammeln. `\d{2,5}` heisst "2 bis 5 Ziffern".

## Warum so vereinfacht?

Die echte E.164-Spec ist deutlich komplizierter (max. 15 Ziffern
international, viele optionale Format-Varianten, Klammern für Vorwahl,
Bindestriche, etc.). Hier reicht ein robustes Schul-Pattern für
typische deutsche Formate.

In der Praxis nutzt man für ernsthafte Anwendungen die
**libphonenumber**-Library von Google -- die kennt jedes Land und
jede Eigenheit.
