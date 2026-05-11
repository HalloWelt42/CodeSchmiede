---
schema_version: 1
id: 130-zahl-zu-text
revision: 1
titel: Zahl 0-99 als Wort
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 14
schaetz_minuten: 9
tags: [zahlen, strings, deutsch, sprache]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Zahl-zu-Wort-Konversion auf Deutsch
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zahl_zu_wort
hints:
  - kosten: 0
    text: |
      0-19 sind eigene Wörter. 20, 30, ..., 90 auch. Sonst:
      Einer + "und" + Zehner -- z.B. 23 = "dreiundzwanzig".
      Bei n < 0 oder n > 99 → "" zurück.
  - kosten: 9
    text: |
      Lookup-Tabellen `EINER` (0-19) und `ZEHNER` (20, 30, ...).
      Sonderfall 1 in der Einer-Stelle wird "ein" (nicht "eins"):
      "einundzwanzig", "einunddreissig".
tests_sichtbar:
  - input: [0]
    expected: "null"
  - input: [7]
    expected: "sieben"
  - input: [13]
    expected: "dreizehn"
  - input: [20]
    expected: "zwanzig"
tests_versteckt:
  - input: [21]
    expected: "einundzwanzig"
  - input: [42]
    expected: "zweiundvierzig"
  - input: [99]
    expected: "neunundneunzig"
  - input: [11]
    expected: "elf"
  - input: [12]
    expected: "zwoelf"
  - input: [30]
    expected: "dreissig"
  - input: [60]
    expected: "sechzig"
  - input: [70]
    expected: "siebzig"
  - input: [-1]
    expected: ""
  - input: [100]
    expected: ""
starter_code: |
  def zahl_zu_wort(n: int) -> str:
      # Deine Lösung hier -- 0-99 als deutsches Wort.
      # Sonderschreibung: "zwoelf" (nicht "zwölf"), "dreissig", "sechzig"
      # (nicht "sechszig"), "siebzig" (nicht "siebenzig").
      pass
---

# Zahl 0-99 als Wort

Schreibe eine Funktion `zahl_zu_wort(n)`, die eine Zahl von 0 bis 99
als **deutsches Wort** zurückgibt.

Bei `n < 0` oder `n > 99` → `""`.

## Sonderfälle

- **0**: `"null"`
- **11, 12**: `"elf"`, `"zwölf"` (ohne Umlaut für ASCII-Tests)
- **30, 60, 70**: `"dreissig"`, `"sechzig"`, `"siebzig"` (ASCII-Schreibweisen)
- **Einer-Stelle 1** in zusammengesetzten Zahlen: `"ein"` (nicht `"eins"`):
  `"einundzwanzig"`, `"einundvierzig"`

## Beispiele

| `n`  | Wort                |
|------|---------------------|
| `0`  | `"null"`            |
| `7`  | `"sieben"`          |
| `11` | `"elf"`             |
| `12` | `"zwölf"`          |
| `13` | `"dreizehn"`        |
| `20` | `"zwanzig"`         |
| `21` | `"einundzwanzig"`   |
| `42` | `"zweiundvierzig"`  |
| `99` | `"neunundneunzig"`  |

## Hinweis zur Schreibweise

Wir nutzen ASCII-Schreibweisen (`zwölf`, `dreissig`), damit die
Tests einfach bleiben und Identifier-Vergleiche zuverlaessig sind.
Echte Lokalisierung würde "zwölf", "dreißig" verwenden.
