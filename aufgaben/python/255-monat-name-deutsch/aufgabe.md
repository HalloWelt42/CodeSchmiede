---
schema_version: 1
id: 255-monat-name-deutsch
revision: 2
titel: Deutscher Monatsname aus Nummer
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags: [datum, mapping, listen]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Lookup
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: monatsname
hints:
  - kosten: 0
    text: |
      Liefere den DEUTSCHEN Monatsnamen aus der Monatsnummer 1-12.
      1 → "Januar", ..., 12 → "Dezember".
      Ungültige Eingaben → "".
  - kosten: 2
    text: |
      Liste mit 13 Einträgen (Index 0 = Füller). Prüfe Bereich.
tests_sichtbar:
  - input: [1]
    expected: "Januar"
  - input: [12]
    expected: "Dezember"
  - input: [5]
    expected: "Mai"
  - input: [0]
    expected: ""
tests_versteckt:
  - input: [2]
    expected: "Februar"
  - input: [3]
    expected: "Maerz"
  - input: [4]
    expected: "April"
  - input: [6]
    expected: "Juni"
  - input: [7]
    expected: "Juli"
  - input: [8]
    expected: "August"
  - input: [9]
    expected: "September"
  - input: [10]
    expected: "Oktober"
  - input: [11]
    expected: "November"
  - input: [13]
    expected: ""
  - input: [-1]
    expected: ""
starter_code: |
  def monatsname(monat: int) -> str:
      # Deine Lösung hier -- 1..12 → Name, sonst ""
      pass
---

# Deutscher Monatsname aus Nummer

Schreibe `monatsname(monat)`, die zur Monatsnummer den deutschen
Namen liefert. Ungültige Eingaben → `""`.

| Nr | Name        |
|----|-------------|
| 1  | `"Januar"`  |
| 2  | `"Februar"` |
| 3  | `"März"`   |
| 4  | `"April"`   |
| 5  | `"Mai"`     |
| 6  | `"Juni"`    |
| 7  | `"Juli"`    |
| 8  | `"August"`  |
| 9  | `"September"`|
| 10 | `"Oktober"` |
| 11 | `"November"`|
| 12 | `"Dezember"`|

## Idee

Liste-Lookup mit Index 0 als Füller - damit `monat == 1`
direkt `NAMEN[1]` ist.

## Hinweis - März ohne Umlaut

In den Tests verwenden wir `"März"` statt `"März"` - der Test-
String wird durch JSON serialisiert und Umlaute können in manchen
Test-Engines Ärger machen. In echten UIs natürlich `März`
schreiben.

## Verwandt

- **058-schaltjahr**, **059-monatstage**, **060-wochentag**: Mehr
  Datums-Aufgaben.
- **195-jahreszeit**: Monats-Nr → Jahreszeit.
