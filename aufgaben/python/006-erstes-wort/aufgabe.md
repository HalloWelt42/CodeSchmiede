---
schema_version: 1
id: 006-erstes-wort
revision: 1
titel: Erstes Wort eines Satzes
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 8
tags: [strings, split]
pfade: [python_strings]
voraussetzungen: []
quelle:
  url: null
  notiz: Einstieg in String-Methoden
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: erstes_wort
hints:
  - kosten: 0
    text: Strings haben eine Methode `.split()`, die an Leerzeichen teilt.
  - kosten: 15
    text: |
      `.split()` ohne Argument behandelt mehrere aufeinanderfolgende
      Leerzeichen als ein Trennzeichen.
  - kosten: 25
    text: |
      ```
      return text.split()[0] if text.split() else ""
      ```
tests_sichtbar:
  - input: ["Hallo Welt"]
    expected: "Hallo"
  - input: ["nur eins"]
    expected: "nur"
  - input: ["einzeln"]
    expected: "einzeln"
  - input: [""]
    expected: ""
tests_versteckt:
  - input: ["   abstand   davor"]
    expected: "abstand"
  - input: ["ein zwei drei vier"]
    expected: "ein"
  - input: ["    "]
    expected: ""
  - input: ["a b"]
    expected: "a"
starter_code: |
  def erstes_wort(text: str) -> str:
      # Deine Lösung hier
      pass
---

# Erstes Wort eines Satzes

Schreibe eine Funktion `erstes_wort(text)`, die das erste Wort eines
Satzes zurückgibt. Wenn der Satz leer ist oder nur aus Leerzeichen
besteht, gib einen leeren String zurück.

## Beispiele

| Eingabe                | Ausgabe     |
|------------------------|-------------|
| `"Hallo Welt"`         | `"Hallo"`   |
| `"   abstand davor"`   | `"abstand"` |
| `""`                   | `""`        |

## Hinweise

- Mehrere Leerzeichen am Anfang sollen ignoriert werden.
- Ein leerer String und ein String aus nur Leerzeichen sollen beide
  einen leeren String zurückgeben.
