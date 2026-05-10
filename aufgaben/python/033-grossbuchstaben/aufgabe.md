---
schema_version: 1
id: 033-grossbuchstaben
revision: 1
titel: Grossbuchstaben zählen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [strings, schleifen, methoden]
pfade: [python_strings]
voraussetzungen: []
quelle:
  url: null
  notiz: Aufwaermer fuer String-Methoden
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: zaehle_gross
hints:
  - kosten: 0
    text: Jedes Zeichen hat eine `.isupper()`-Methode.
  - kosten: 10
    text: |
      Mit `sum(...)`:

      ```
      return sum(1 for c in text if c.isupper())
      ```
tests_sichtbar:
  - input: ["Hallo Welt"]
    expected: 2
  - input: ["abc"]
    expected: 0
  - input: ["ABC"]
    expected: 3
  - input: [""]
    expected: 0
tests_versteckt:
  - input: ["Code Schmiede"]
    expected: 2
  - input: ["1234"]
    expected: 0
  - input: ["AaBbCc"]
    expected: 3
  - input: ["The Quick BROWN Fox"]
    expected: 7
starter_code: |
  def zaehle_gross(text: str) -> int:
      # Deine Lösung hier
      pass
---

# Grossbuchstaben zählen

Schreibe eine Funktion `zaehle_gross(text)`, die zählt, wie viele
**Grossbuchstaben** im String vorkommen.

## Beispiele

| Eingabe                | Ergebnis |
|------------------------|----------|
| `"Hallo Welt"`         | `2`      |
| `"abc"`                | `0`      |
| `"ABC"`                | `3`      |
| `""`                   | `0`      |
| `"The Quick BROWN Fox"`| `7`      |

## Idee

Schleife ueber jedes Zeichen, Test mit `c.isupper()`, Zähler hoch.

## Verwandt

Pythons String-Methoden sind ueberraschend reichhaltig: `isupper`,
`islower`, `isdigit`, `isalpha`, `isspace`, `isalnum` -- alle sehr
nuetzlich, um schnell Strings zu klassifizieren.
