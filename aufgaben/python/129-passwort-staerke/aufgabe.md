---
schema_version: 1
id: 129-passwort-staerke
revision: 1
titel: Passwort-Stärke bewerten
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, validierung, sicherheit]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Passwort-Validierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: passwort_staerke
hints:
  - kosten: 0
    text: |
      Punkte 0-5 nach Regeln:
      +1 wenn Länge >= 8
      +1 wenn mind. ein Kleinbuchstabe
      +1 wenn mind. ein Großbuchstabe
      +1 wenn mind. eine Ziffer
      +1 wenn mind. ein Sonderzeichen (alles außer alphanumerisch)
  - kosten: 8
    text: |
      `any(c.islower() for c in pw)`, analog für isupper/isdigit/non-alnum.
tests_sichtbar:
  - input: ["abc"]
    expected: 1
  - input: ["abcdefgh"]
    expected: 2
  - input: ["Abcdefgh"]
    expected: 3
  - input: ["Abcdefg1"]
    expected: 4
tests_versteckt:
  - input: [""]
    expected: 0
  - input: ["a"]
    expected: 1
  - input: ["A"]
    expected: 1
  - input: ["1"]
    expected: 1
  - input: ["!"]
    expected: 1
  - input: ["P@ssw0rd"]
    expected: 5
  - input: ["aB3!xY9$"]
    expected: 5
  - input: ["12345678"]
    expected: 2
  - input: ["AAAAAAAA"]
    expected: 2
starter_code: |
  def passwort_staerke(passwort: str) -> int:
      # Deine Lösung hier -- 0-5 Punkte nach Regeln im Hint.
      pass
---

# Passwort-Stärke bewerten

Schreibe eine Funktion `passwort_stärke(passwort)`, die ein Passwort
mit **0 bis 5 Punkten** bewertet.

## Punkte-Regeln (jede +1)

1. Länge **≥ 8**
2. Enthält mindestens einen **Kleinbuchstaben**
3. Enthält mindestens einen **Großbuchstaben**
4. Enthält mindestens eine **Ziffer**
5. Enthält mindestens ein **Sonderzeichen** (alles außer Buchstaben + Ziffern)

## Beispiele

| Passwort       | Punkte | Wegen                              |
|----------------|--------|------------------------------------|
| `""`           | `0`    | nichts                             |
| `"abc"`        | `1`    | nur Kleinbuchstaben                |
| `"abcdefgh"`   | `2`    | + Länge                            |
| `"Abcdefgh"`   | `3`    | + Groß                             |
| `"Abcdefg1"`   | `4`    | + Ziffer                           |
| `"P@ssw0rd"`   | `5`    | alle 5 Klassen                     |

## Hintergrund

Echte Passwort-Bewertung wie bei zxcvbn ist deutlich schlauer
(Wörterbuch-Angriffe, Substitutionen, Wiederholungen) -- diese Aufgabe
ist die einfache Schul-Variante.
