---
schema_version: 1
id: 120-trennzeichen-akronym
revision: 1
titel: Akronym mit gemischten Trennzeichen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, regex, parsing]
pfade: [python_strings3]
voraussetzungen: [036-acronym]
quelle:
  url: null
  notiz: Variante von 036-acronym mit mehr Trennzeichen
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: akronym_plus
hints:
  - kosten: 0
    text: |
      Wörter werden durch Whitespace, Bindestrich und Unterstrich
      getrennt. Pro Wort ersten Buchstaben in Großschreibung.
      camelCase wird auch aufgespalten -- jedes Großbuchstaben-Vorkommen
      mitten im Wort startet ein neues Wort.
  - kosten: 20
    text: |
      Mit `re.split(r"[\s_-]+", text)` zerlegen, leere Bestandteile
      filtern. Pro Wort: erster Buchstabe gross. Fuer camelCase einfach:
      wenn ein Buchstabe direkt am Wortanfang gross ist, einfach
      übernehmen; ansonsten zusätzlich gross machen.
tests_sichtbar:
  - input: ["Portable Network Graphics"]
    expected: "PNG"
  - input: ["Ruby on Rails"]
    expected: "ROR"
  - input: ["HyperText Markup Language"]
    expected: "HTML"
  - input: ["First in, first out"]
    expected: "FIFO"
tests_versteckt:
  - input: [""]
    expected: ""
  - input: ["go"]
    expected: "G"
  - input: ["Complementary metal-oxide semiconductor"]
    expected: "CMOS"
  - input: ["the_quick_brown fox"]
    expected: "TQBF"
  - input: ["camelCase rocks"]
    expected: "CCR"
starter_code: |
  def akronym_plus(text: str) -> str:
      # Deine Lösung hier -- Trennzeichen: Whitespace, '-', '_'.
      # Auch camelCase splitten.
      pass
---

# Akronym mit gemischten Trennzeichen

Schreibe eine Funktion `akronym_plus(text)`, die ein Akronym aus
einem Text bildet -- erweitert um mehr Trennzeichen als
[Aufgabe 036](036-acronym).

## Trennzeichen

- Whitespace (Leerzeichen, Tab, Newline)
- Bindestrich `-`
- Unterstrich `_`
- camelCase: jeder Großbuchstabe mitten im Wort beginnt ein
  neues Wort

## Beispiele

| Eingabe                               | Akronym  |
|---------------------------------------|----------|
| `"Portable Network Graphics"`         | `"PNG"`  |
| `"HyperText Markup Language"`         | `"HTML"` |
| `"First in, first out"`               | `"FIFO"` |
| `"the_quick_brown fox"`               | `"TQBF"` |
| `"camelCase rocks"`                   | `"CCR"`  |
| `""`                                  | `""`     |

## Hintergrund

Variante des klassischen Akronym-Problems. Die camelCase-Erweiterung
macht es zur typischen Tooling-Aufgabe -- Linter und Code-Generatoren
brauchen genau diese Logik.
