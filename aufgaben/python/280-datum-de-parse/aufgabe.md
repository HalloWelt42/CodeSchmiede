---
schema_version: 1
id: 280-datum-de-parse
revision: 1
titel: Deutsches Datum DD.MM.YYYY parsen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 25
schaetz_minuten: 10
tags: [strings, regex, capture-groups, datum]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Capture-Group-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: datum_parse
hints:
  - kosten: 0
    text: |
      Parse Datum im Format "DD.MM.YYYY" zu [tag, monat, jahr].
      Tag/Monat 1-2 Ziffern, Jahr 4 Ziffern.
      Bei UNGUELTIGEM Format → [].
      Diese Aufgabe pruft NUR die Form, NICHT ob das Datum existiert
      (also "32.13.2026" wird als Form-OK akzeptiert).
  - kosten: 20
    text: |
      re.fullmatch(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", s).
      Wenn Match: groups() liefert Tupel der Capture-Groups
      → [int(tag), int(monat), int(jahr)].
tests_sichtbar:
  - input: ["11.05.2026"]
    expected: [11, 5, 2026]
  - input: ["1.1.2000"]
    expected: [1, 1, 2000]
  - input: ["abc"]
    expected: []
  - input: [""]
    expected: []
tests_versteckt:
  - input: ["31.12.1999"]
    expected: [31, 12, 1999]
  - input: ["01.01.2026"]
    expected: [1, 1, 2026]
  - input: ["32.13.2026"]
    expected: [32, 13, 2026]
  - input: ["11/05/2026"]
    expected: []
  - input: ["11.5.26"]
    expected: []
  - input: ["1.1.20000"]
    expected: []
  - input: ["1..2026"]
    expected: []
  - input: [" 1.1.2026"]
    expected: []
starter_code: |
  import re

  def datum_parse(s: str) -> list[int]:
      # Deine Lösung hier -- [tag, monat, jahr] oder []
      pass
---

# Deutsches Datum DD.MM.YYYY parsen

Schreibe `datum_parse(s)`, die ein deutsches Datum im Format
`"DD.MM.YYYY"` (mit oder ohne fuehrende Nullen) in eine Liste
`[tag, monat, jahr]` umwandelt.

Bei ungültigem Format → `[]`.

**Achtung**: Diese Aufgabe prüft nur die **Form**, nicht ob das
Datum tatsächlich existiert. `"32.13.2026"` wird als Form-OK
akzeptiert -- die semantische Prüfung wäre eine eigene Aufgabe.

## Beispiele

| Eingabe         | Ergebnis            |
|-----------------|---------------------|
| `"11.05.2026"`  | `[11, 5, 2026]`     |
| `"1.1.2000"`    | `[1, 1, 2000]`      |
| `"31.12.1999"`  | `[31, 12, 1999]`    |
| `"32.13.2026"`  | `[32, 13, 2026]` (Form OK!) |
| `"11/05/2026"`  | `[]` (falscher Trenner) |
| `"11.5.26"`     | `[]` (Jahr nicht 4-stellig) |
| `"abc"`         | `[]`                |
| `" 1.1.2026"`   | `[]` (fuehrendes Leerzeichen) |

## Idee -- Capture-Groups

`re.fullmatch` mit Capture-Groups: jedes Klammern-Paar ist eine
Gruppe, `m.group(i)` (1-basiert) liefert den Inhalt.

`\.` (mit Backslash) matcht den **literalen Punkt** -- ohne
Backslash wäre `.` "beliebiges Zeichen".

## Idiomatischer mit `groups()`

`m.groups()` liefert ein Tupel aller Capture-Groups, das wir
list-comprehensiv konvertieren.

## Anwendung

Datums-Parsing ist Standard in Log-Analyse, CSV-Import, Web-Form-
Validierung. Für **echte** Datums-Validierung mit Existenz-Prüfung
(siehe Aufgabe 254) nutzt man `datetime.strptime`:

