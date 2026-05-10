---
schema_version: 1
id: 048-laengstes-wort
revision: 1
titel: Laengstes Wort eines Satzes
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [strings, split, max]
pfade: [python_strings3]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassischer Aufwaermer
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: laengstes_wort
hints:
  - kosten: 0
    text: |
      `text.split()` zerlegt nach Whitespace. Dann `max(woerter, key=len)`.
  - kosten: 10
    text: |
      Bei mehreren gleich langen Woertern soll das **erste** zurück.
      `max()` mit `key=len` waehlt automatisch das erste.
tests_sichtbar:
  - input: ["Hallo Welt"]
    expected: "Hallo"
  - input: ["der die das"]
    expected: "der"
  - input: ["Donaudampfschifffahrt ist toll"]
    expected: "Donaudampfschifffahrt"
  - input: [""]
    expected: ""
tests_versteckt:
  - input: ["a"]
    expected: "a"
  - input: ["abc def ghi"]
    expected: "abc"
  - input: ["one two three four five six"]
    expected: "three"
  - input: ["    leerzeichen    "]
    expected: "leerzeichen"
starter_code: |
  def laengstes_wort(text: str) -> str:
      # Deine Lösung hier -- bei Gleichstand das erste.
      pass
---

# Laengstes Wort eines Satzes

Schreibe eine Funktion `laengstes_wort(text)`, die das **laengste
Wort** im String zurueckgibt. Bei mehreren gleich langen das **erste**.

Bei leerem String oder String ohne Woerter liefere einen leeren String.

## Beispiele

| Eingabe                            | Ergebnis                  |
|------------------------------------|---------------------------|
| `"Hallo Welt"`                     | `"Hallo"`                 |
| `"der die das"`                    | `"der"`                   |
| `"Donaudampfschifffahrt ist toll"` | `"Donaudampfschifffahrt"` |
| `""`                               | `""`                      |

## Idee

`split()` ohne Argument splittet an Whitespace und ignoriert leere
Bestandteile. Dann `max(...)` mit `key=len` -- bei Gleichstand
nimmt `max` das **erste** maximale Element, das passt hier perfekt.

## Falle

Bei einem leeren Iterable wirft `max()` einen `ValueError`. Den
leeren Fall vorher abfangen.
