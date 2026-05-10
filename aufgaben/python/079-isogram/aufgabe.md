---
schema_version: 1
id: 079-isogram
revision: 1
titel: Isogramm-Test
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [strings, sets, alphabet]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Isogramm
  notiz: Inspiration aus Exercism (isogram), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_isogramm
hints:
  - kosten: 0
    text: |
      Ein Isogramm hat **keinen Buchstaben mehrfach**. Bindestriche und
      Leerzeichen werden ignoriert. Groß-/Kleinschreibung egal.
  - kosten: 10
    text: |
      Filtere alle Buchstaben, vergleiche `len(buchstaben) == len(set(buchstaben))`.
tests_sichtbar:
  - input: ["lumberjacks"]
    expected: true
  - input: ["isograms"]
    expected: false
  - input: ["six-year-old"]
    expected: true
  - input: [""]
    expected: true
tests_versteckt:
  - input: ["isogram"]
    expected: true
  - input: ["eleven"]
    expected: false
  - input: ["zzyzx"]
    expected: false
  - input: ["subdermatoglyphic"]
    expected: true
  - input: ["Emily Jung Schwartzkopf"]
    expected: true
  - input: ["accentor"]
    expected: false
starter_code: |
  def ist_isogramm(text: str) -> bool:
      # Deine Lösung hier
      pass
---

# Isogramm-Test

Schreibe eine Funktion `ist_isogramm(text)`, die prüft, ob der Text
ein **Isogramm** ist -- also kein Buchstabe mehrfach vorkommt.

- Groß-/Kleinschreibung wird ignoriert
- Bindestriche und Leerzeichen werden ignoriert
- Leerer String ist ein Isogramm

## Beispiele

| Eingabe                | Ergebnis |
|------------------------|----------|
| `"lumberjacks"`        | `True`   |
| `"isograms"`           | `False`  |
| `"six-year-old"`       | `True`   |
| `"subdermatoglyphic"`  | `True`   |
| `"Emily Jung Schwartzkopf"` | `True` |
| `"accentor"`           | `False` (zwei c) |

## Hintergrund

`"subdermatoglyphic"` ist mit 17 Buchstaben das **längste bekannte
Isogramm** der englischen Sprache. Im Deutschen ist
"Boxkampf" mit 8 verschiedenen Buchstaben ein nettes Beispiel.
