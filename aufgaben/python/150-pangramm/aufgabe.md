---
schema_version: 1
id: 150-pangramm
revision: 1
titel: Pangramm-Pruefung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [strings, set, alphabet]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Set-Anwendung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: ist_pangramm
hints:
  - kosten: 0
    text: |
      Pruefe, ob ein Text ALLE 26 Buchstaben des englischen Alphabets
      enthaelt (Gross/Klein egal). Umlaute zaehlen nicht.
  - kosten: 10
    text: |
      Set der Buchstaben aus text.lower(), gefiltert auf isalpha
      und nur ASCII a-z. Vergleich mit set("abcdefghijklmnopqrstuvwxyz").
tests_sichtbar:
  - input: ["The quick brown fox jumps over the lazy dog"]
    expected: true
  - input: ["Hallo Welt"]
    expected: false
  - input: [""]
    expected: false
  - input: ["abcdefghijklmnopqrstuvwxyz"]
    expected: true
tests_versteckt:
  - input: ["Pack my box with five dozen liquor jugs"]
    expected: true
  - input: ["Sphinx of black quartz, judge my vow!"]
    expected: true
  - input: ["The quick brown fox jumps over the lazy do"]
    expected: false
  - input: ["ABCDEFGHIJKLMNOPQRSTUVWXY"]
    expected: false
  - input: ["abcdefghijklmnopqrstuvwxy z"]
    expected: true
  - input: ["Franz jagt im komplett verwahrlosten Taxi quer durch Bayern"]
    expected: true
starter_code: |
  def ist_pangramm(text: str) -> bool:
      # Deine Lösung hier -- alle 26 a-z Buchstaben muessen vorkommen
      pass
---

# Pangramm-Pruefung

Ein **Pangramm** ist ein Satz, der jeden Buchstaben des Alphabets
mindestens einmal enthaelt -- in Setzereien beliebt zur Schrift-
Vorschau.

Schreibe eine Funktion `ist_pangramm(text)`, die `True` zurueckgibt,
wenn `text` alle 26 Buchstaben `a-z` enthaelt (Gross/Klein egal,
Umlaute zaehlen nicht).

## Beispiele

| Text                                              | Pangramm? |
|---------------------------------------------------|-----------|
| `"The quick brown fox jumps over the lazy dog"`   | `True`    |
| `"Pack my box with five dozen liquor jugs"`       | `True`    |
| `"Sphinx of black quartz, judge my vow!"`         | `True`    |
| `"Hallo Welt"`                                    | `False`   |

## Klassisches deutsches Pangramm

*"Franz jagt im komplett verwahrlosten Taxi quer durch Bayern"* deckt
**alle 26 Buchstaben** a-z ab -- ein lupenreines Pangramm. Im
deutschsprachigen Raum ist es das wohl bekannteste Beispiel.

## Idee

Set-Differenz mit dem Alphabet:

```python
ALPHABET = set("abcdefghijklmnopqrstuvwxyz")

def ist_pangramm(text):
    return ALPHABET <= set(text.lower())
```

`ALPHABET <= S` testet, ob ALPHABET eine **Teilmenge** von S ist --
genau das, was wir wollen.
