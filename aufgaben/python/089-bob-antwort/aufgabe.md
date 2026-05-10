---
schema_version: 1
id: 089-bob-antwort
revision: 1
titel: Bob antwortet
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, if-else, dialog]
pfade: [python_logik]
voraussetzungen: []
quelle:
  url: null
  notiz: Inspiration aus Exercism (bob), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: bob_antwort
hints:
  - kosten: 0
    text: |
      Bob ist ein Teenager mit klaren Regeln:
      - Nichts gesagt → "Manno, sag was."
      - Geschrien (alle Buchstaben gross) UND Frage → "Schrei mich nicht an, was willst du?!"
      - Nur geschrien → "Schrei mich nicht an!"
      - Nur Frage → "Klar."
      - Sonst → "Naja."
  - kosten: 15
    text: |
      Test fürs Schreien: Text muss mindestens einen Buchstaben haben
      UND alle Buchstaben sind Grossbuchstaben.
tests_sichtbar:
  - input: ["Tom-ay-to, tom-aaaah-to."]
    expected: "Naja."
  - input: ["WATCH OUT!"]
    expected: "Schrei mich nicht an!"
  - input: ["Does this cryogenic chamber make me look fat?"]
    expected: "Klar."
  - input: ["WHAT THE HECK WERE YOU THINKING?"]
    expected: "Schrei mich nicht an, was willst du?!"
tests_versteckt:
  - input: [""]
    expected: "Manno, sag was."
  - input: ["         "]
    expected: "Manno, sag was."
  - input: ["1, 2, 3"]
    expected: "Naja."
  - input: ["4?"]
    expected: "Klar."
  - input: ["ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"]
    expected: "Schrei mich nicht an!"
  - input: ["Let's go make out behind the gym!"]
    expected: "Naja."
starter_code: |
  def bob_antwort(text: str) -> str:
      # Deine Lösung hier -- 5 mögliche Antworten.
      pass
---

# Bob antwortet

Bob ist ein Teenager. Auf alles, was du sagst, antwortet er knapp.
Schreibe eine Funktion `bob_antwort(text)`, die seine Antwort liefert.

## Regeln

1. **Nichts gesagt** (leer oder nur Whitespace) → `"Manno, sag was."`
2. **Schreien + Frage** (alles GROSSBUCHSTABEN, endet mit `?`) →
   `"Schrei mich nicht an, was willst du?!"`
3. **Nur schreien** → `"Schrei mich nicht an!"`
4. **Nur Frage** → `"Klar."`
5. **Sonst** → `"Naja."`

## "Schreien" definieren

Mindestens ein Buchstabe + alle Buchstaben sind Großbuchstaben.

## Beispiele

| Eingabe                                          | Antwort                                  |
|--------------------------------------------------|------------------------------------------|
| `"Tom-ay-to, tom-aaaah-to."`                     | `"Naja."`                                |
| `"WATCH OUT!"`                                   | `"Schrei mich nicht an!"`                |
| `"Does this make me look fat?"`                  | `"Klar."`                                |
| `"WHAT THE HECK WERE YOU THINKING?"`             | `"Schrei mich nicht an, was willst du?!"`|
| `""`                                             | `"Manno, sag was."`                      |
| `"4?"`                                           | `"Klar."`                                |
| `"ZOMG ZOMBIES!!"`                               | `"Schrei mich nicht an!"`                |

## Hintergrund

Klassiker auf Exercism. Schöne Übung für **if/elif** mit klaren
Bedingungen, die sich nicht überschneiden dürfen.
