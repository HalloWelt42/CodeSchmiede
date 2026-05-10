---
schema_version: 1
id: 078-pangram
revision: 1
titel: Pangramm-Test
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
  url: https://de.wikipedia.org/wiki/Pangramm
  notiz: Inspiration aus Exercism (pangram), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_pangramm
hints:
  - kosten: 0
    text: |
      Ein Pangramm enthält jeden Buchstaben des Alphabets a-z mindestens
      einmal. Groß-/Kleinschreibung egal.
  - kosten: 10
    text: |
      Mit Sets: `set(text.lower()) >= set("abcdefghijklmnopqrstuvwxyz")`
      oder kurz `set("abcdefghijklmnopqrstuvwxyz") <= set(text.lower())`.
tests_sichtbar:
  - input: ["The quick brown fox jumps over the lazy dog"]
    expected: true
  - input: ["a quick movement of the enemy will jeopardize five gunboats"]
    expected: false
  - input: [""]
    expected: false
  - input: ["abcdefghijklmnopqrstuvwxyz"]
    expected: true
tests_versteckt:
  - input: ["the 1 quick brown fox jumps over the 2 lazy dogs"]
    expected: true
  - input: ["pack my box with five dozen liquor jugs"]
    expected: true
  - input: ["the quick brown fish jumps over the lazy dog"]
    expected: false
  - input: ["abcdefghijklm"]
    expected: false
starter_code: |
  def ist_pangramm(text: str) -> bool:
      # Deine Lösung hier
      pass
---

# Pangramm-Test

Schreibe eine Funktion `ist_pangramm(text)`, die prüft, ob der Text
ein **Pangramm** ist -- also jeden Buchstaben des englischen Alphabets
(a-z) mindestens einmal enthält.

Groß-/Kleinschreibung wird ignoriert. Andere Zeichen (Ziffern,
Leerzeichen, Sonderzeichen) sind erlaubt, zählen aber nicht.

## Beispiele

| Eingabe                                        | Ergebnis |
|-----------------------------------------------|----------|
| `"The quick brown fox jumps over the lazy dog"` | `True`  |
| `"five boxing wizards jump quickly"`            | `True`  |
| `"the quick brown fish jumps over the lazy dog"` | `False` (kein x) |
| `""`                                            | `False`  |

## Hintergrund

"The quick brown fox jumps over the lazy dog" ist seit dem 19. Jh.
das Standard-Pangramm im Englischen -- benutzt um Schreibmaschinen
zu testen oder Schriftarten zu zeigen. Im Deutschen ist
"Franz jagt im komplett verwahrlosten Taxi quer durch Bayern" ein
gängiges Pangramm.
