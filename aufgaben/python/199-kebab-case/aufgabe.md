---
schema_version: 1
id: 199-kebab-case
revision: 1
titel: kebab-case-Konvertierung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 8
tags: [strings, slugs, replace]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Web-Url-Slug-Klassiker
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: kebab_case
hints:
  - kosten: 0
    text: |
      Wandle einen Text in kebab-case: alle Buchstaben klein, Leerzeichen
      und Unterstriche zu Bindestrich. Mehrfache Trenner zu einem.
      Fuehrende/nachfolgende Bindestriche entfernen.
      Sonderzeichen (außer a-z, 0-9) entfernen.
  - kosten: 15
    text: |
      lower, alle Nicht-(a-z0-9) zu '-', mehrfache - kollabieren,
      strip('-'). Regex hilft: re.sub(r'[^a-z0-9]+', '-', text.lower()).
tests_sichtbar:
  - input: ["Hallo Welt"]
    expected: "hallo-welt"
  - input: [""]
    expected: ""
  - input: ["Mein erster Beitrag!"]
    expected: "mein-erster-beitrag"
  - input: ["snake_case_text"]
    expected: "snake-case-text"
tests_versteckt:
  - input: ["camelCaseText"]
    expected: "camelcasetext"
  - input: ["already-kebab-case"]
    expected: "already-kebab-case"
  - input: ["  trim  me  "]
    expected: "trim-me"
  - input: ["A B C"]
    expected: "a-b-c"
  - input: ["100% Erfolg in 2026!"]
    expected: "100-erfolg-in-2026"
  - input: ["___underscores___"]
    expected: "underscores"
  - input: ["a"]
    expected: "a"
starter_code: |
  def kebab_case(text: str) -> str:
      # Deine Lösung hier -- regex oder per Hand
      pass
---

# kebab-case-Konvertierung

Schreibe `kebab_case(text)`, die einen Text in **kebab-case**
umwandelt -- ein gaengiges URL-Slug-Format.

Regeln:

1. Alles in **Kleinbuchstaben**.
2. Alle Zeichen außer `a-z` und `0-9` werden zu **Bindestrich**.
3. **Mehrfache Bindestriche** werden zu einem.
4. **Fuehrende/Nachfolgende** Bindestriche werden entfernt.

## Beispiele

| Eingabe                   | Ausgabe                  |
|---------------------------|--------------------------|
| `"Hallo Welt"`            | `"hallo-welt"`           |
| `"Mein erster Beitrag!"`  | `"mein-erster-beitrag"`  |
| `"snake_case_text"`       | `"snake-case-text"`      |
| `"  trim  me  "`          | `"trim-me"`              |
| `"100% Erfolg in 2026!"`  | `"100-erfolg-in-2026"`   |
| `"___underscores___"`     | `"underscores"`          |

## Idee mit Regex

`[^a-z0-9]+` matcht eine **Folge** von Nicht-Slug-Zeichen → wird
durch ein einzelnes `-` ersetzt. `strip("-")` entfernt Rand-Trenner.

## Anwendung

URL-Slugs (`mein-blog/wie-ich-python-lernte`), CSS-Klassen
(`btn-primary-large`), Datei-Namen (`2026-05-11-notiz.md`).
Konsistenz hier zahlt sich aus -- Suchmaschinen und Tools moegen
es einheitlich.
