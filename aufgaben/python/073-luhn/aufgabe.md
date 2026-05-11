---
schema_version: 1
id: 073-luhn
revision: 1
titel: Luhn-Prüfziffer
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [zahlen, strings, modulo, kreditkarten]
pfade: [python_codes]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Luhn-Algorithmus
  notiz: Inspiration aus Exercism (luhn), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_luhn_gueltig
hints:
  - kosten: 0
    text: |
      Whitespace ignorieren. Zahl muss mind. 2 Ziffern haben, alles
      andere ungültig.
  - kosten: 15
    text: |
      Von rechts: jede zweite Ziffer verdoppeln. Falls > 9, ziehe 9 ab.
      Summe aller Ziffern muss durch 10 teilbar sein.
tests_sichtbar:
  - input: ["4539 1488 0343 6467"]
    expected: true
  - input: ["8273 1232 7352 0569"]
    expected: false
  - input: ["1"]
    expected: false
  - input: ["059"]
    expected: true
tests_versteckt:
  - input: ["059a"]
    expected: false
  - input: ["055 444 285"]
    expected: true
  - input: ["055-444-285"]
    expected: false
  - input: ["0"]
    expected: false
  - input: ["095 245 88"]
    expected: true
starter_code: |
  def ist_luhn_gueltig(kandidat: str) -> bool:
      # Deine Lösung hier
      pass
---

# Luhn-Prüfziffer

Schreibe eine Funktion `ist_luhn_gültig(kandidat)`, die prüft, ob ein
String die **Luhn-Prüfziffer-Regel** erfüllt -- der Klassiker für
Kreditkartennummern, IMEI und viele andere Identifikatoren.

## Regeln

1. Whitespace wird ignoriert.
2. Wer **andere Nicht-Ziffern** enthält, ist ungültig.
3. Wer weniger als **2 Ziffern** hat, ist ungültig.
4. Algorithmus:
   - Lies die Ziffern **von rechts nach links**.
   - **Jede zweite** Ziffer (also Position 2, 4, 6, ... von rechts)
     wird verdoppelt.
   - Ist die verdoppelte Ziffer > 9, ziehe 9 ab.
   - Die Summe aller resultierenden Ziffern muss **durch 10 teilbar** sein.

## Beispiele

| Eingabe                  | Gültig? |
|--------------------------|---------|
| `"4539 1488 0343 6467"`  | `True`  |
| `"8273 1232 7352 0569"`  | `False` |
| `"1"`                    | `False` |
| `"059"`                  | `True`  |
| `"059a"`                 | `False` |

## Hintergrund

Hans Peter Luhn hat den Algorithmus 1954 bei IBM entwickelt. Er
fängt die meisten **Tippfehler** in Identifikatoren ab -- vor allem
einzelne falsche Ziffern und Vertauschen benachbarter Ziffern.
