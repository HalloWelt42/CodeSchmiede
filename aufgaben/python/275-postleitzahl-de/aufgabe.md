---
schema_version: 1
id: 275-postleitzahl-de
revision: 3
titel: Deutsche Postleitzahl validieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [strings, regex, validierung]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Regex-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ist_plz
hints:
  - kosten: 0
    text: |
      Prüfe ob ein String eine deutsche Postleitzahl ist:
      genau 5 Ziffern, nichts sonst. Whitespace zählt nicht.
      "12345" → True. " 12345" → False. "1234" → False.
  - kosten: 5
    text: |
      re.fullmatch(r"\d{5}", s) ist True wenn der GANZE String
      genau 5 Ziffern enthält.
tests_sichtbar:
  - input: ["12345"]
    expected: true
  - input: ["1234"]
    expected: false
  - input: ["abcde"]
    expected: false
  - input: [""]
    expected: false
tests_versteckt:
  - input: ["00042"]
    expected: true
  - input: ["99999"]
    expected: true
  - input: ["987654"]
    expected: false
  - input: ["12 45"]
    expected: false
  - input: [" 54321"]
    expected: false
  - input: ["12345 "]
    expected: false
  - input: ["98b76"]
    expected: false
  - input: ["80331"]
    expected: true
starter_code: |
  import re

  def ist_plz(s: str) -> bool:
      # Deine Lösung hier - genau 5 Ziffern
      pass
---

# Deutsche Postleitzahl validieren

Schreibe `ist_plz(s)`, die `True` zurückgibt, wenn der String eine
**deutsche Postleitzahl** ist - **genau 5 Ziffern**, sonst nichts.

Whitespace, Buchstaben, andere Längen → `False`.

## Beispiele

| Eingabe    | Gültig? |
|------------|----------|
| `"12345"`  | `True`   |
| `"00000"`  | `True`   |
| `"10115"`  | `True` (Berlin) |
| `"1234"`   | `False` |
| `"123456"` | `False` |
| `"abcde"`  | `False` |
| `" 12345"` | `False` (führendes Leerzeichen) |
| `"1a345"`  | `False` |
| `""`       | `False` |

## Idee - Regex

`re.fullmatch` erwartet, dass das **gesamte String** dem Pattern
entspricht (im Gegensatz zu `match`, das nur am Anfang prüft).
`\d{5}` heißt "genau 5 Ziffern".

## Variante ohne Regex

Funktioniert auch - `str.isdigit` schließt `' '` und Buchstaben aus.
`len(s) == 5` hängt mit dran.

## Hintergrund

Deutsche PLZ haben **5 Ziffern** seit 1993 (vorher 4-stellig). Es
gibt etwa 8200 PLZ in Deutschland. Manche Sonderfälle (Postfächer,
Großempfänger) haben eigene PLZ - die kann man mit der einfachen
Regex aber nicht von normalen unterscheiden.
