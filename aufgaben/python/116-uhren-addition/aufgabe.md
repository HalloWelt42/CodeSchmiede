---
schema_version: 1
id: 116-uhren-addition
revision: 1
titel: Uhrzeit + Minuten
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [zahlen, datum, modulo]
pfade: [python_datum]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (clock), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: uhrzeit_plus
hints:
  - kosten: 0
    text: |
      Eingabe: stunde (0-23), minute (0-59), zusatz_minuten (kann negativ
      sein). Liefere "HH:MM" als String. Modulo + Division regeln den
      Tagesübergang.
  - kosten: 15
    text: |
      `gesamt = stunde * 60 + minute + zusatz_minuten`. Dann
      `gesamt %= 24 * 60` (auch bei negativen Werten -- Python
      modulo macht das richtig). Format mit f"{h:02d}:{m:02d}".
tests_sichtbar:
  - input: [10, 0, 3]
    expected: "10:03"
  - input: [23, 30, 60]
    expected: "00:30"
  - input: [10, 30, -90]
    expected: "09:00"
  - input: [0, 0, 1440]
    expected: "00:00"
tests_versteckt:
  - input: [0, 0, 0]
    expected: "00:00"
  - input: [0, 0, -1]
    expected: "23:59"
  - input: [9, 45, 5]
    expected: "09:50"
  - input: [9, 45, 75]
    expected: "11:00"
  - input: [12, 0, -720]
    expected: "00:00"
  - input: [10, 30, -2940]
    expected: "09:30"
starter_code: |
  def uhrzeit_plus(stunde: int, minute: int, zusatz_minuten: int) -> str:
      # Deine Lösung hier -- Format "HH:MM", auch bei negativen Eingaben.
      pass
---

# Uhrzeit + Minuten

Schreibe eine Funktion `uhrzeit_plus(stunde, minute, zusatz_minuten)`,
die zur Eingabe-Zeit eine Anzahl Minuten (positiv oder negativ)
addiert und das Ergebnis als `"HH:MM"` zurueckgibt.

24-Stunden-Format. Tagesueberlauf wird gewickelt -- nur die
Tageszeit interessiert.

## Beispiele

| Stunde | Minute | + Min  | Ergebnis  |
|--------|--------|--------|-----------|
| `10`   | `0`    | `3`    | `"10:03"` |
| `23`   | `30`   | `60`   | `"00:30"` |
| `10`   | `30`   | `-90`  | `"09:00"` |
| `0`    | `0`    | `1440` | `"00:00"` |
| `0`    | `0`    | `-1`   | `"23:59"` |
| `12`   | `0`    | `-720` | `"00:00"` |

## Hintergrund

Klassische Modulo-Aufgabe. Pythons `%` macht negativ und positiv
einheitlich richtig (Ergebnis hat das Vorzeichen des Divisors), so
dass `(-1) % 1440 == 1439` automatisch funktioniert.
