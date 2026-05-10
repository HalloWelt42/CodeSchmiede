---
schema_version: 1
id: 035-run-length
revision: 1
titel: Run-Length-Encoding
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [strings, kompression, schleifen]
pfade: [python_strings]
voraussetzungen: [007-buchstaben-häufigkeit]
quelle:
  url: https://de.wikipedia.org/wiki/Lauflaengenkodierung
  notiz: Klassischer Kompressionsalgorithmus
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: rle
hints:
  - kosten: 0
    text: |
      Schleife durch den String. Aktuelles Zeichen + Zähler merken.
      Wenn das nächste Zeichen anders ist: ans Ergebnis anhaengen,
      Zähler reset.
  - kosten: 15
    text: |
      Wenn der Zähler 1 ist, schreibe nur das Zeichen (z.B. `"a"`),
      sonst Zeichen + Zahl (z.B. `"a3"`).
tests_sichtbar:
  - input: ["aaabbc"]
    expected: "a3b2c"
  - input: ["abc"]
    expected: "abc"
  - input: [""]
    expected: ""
  - input: ["aaaa"]
    expected: "a4"
tests_versteckt:
  - input: ["aabbcc"]
    expected: "a2b2c2"
  - input: ["a"]
    expected: "a"
  - input: ["xxxxxxxxxx"]
    expected: "x10"
  - input: ["abbbbcccddde"]
    expected: "ab4c3d3e"
starter_code: |
  def rle(text: str) -> str:
      # Deine Lösung hier -- einzelne Zeichen ohne 1, Mehrfache mit Zahl.
      pass
---

# Run-Length-Encoding

Schreibe eine Funktion `rle(text)`, die einen String in seine
**Lauflaengen-Codierung** ueberfuehrt: gleiche aufeinanderfolgende
Zeichen werden durch das Zeichen + Anzahl ersetzt. Ein einzelnes
Vorkommen wird **ohne Zahl** geschrieben (also `"abc"` -> `"abc"`,
nicht `"a1b1c1"`).

## Beispiele

| Eingabe         | Ergebnis      |
|-----------------|---------------|
| `"aaabbc"`      | `"a3b2c"`     |
| `"abc"`         | `"abc"`       |
| `""`            | `""`          |
| `"aaaa"`        | `"a4"`        |
| `"xxxxxxxxxx"`  | `"x10"`       |

## Idee

Zwei "Zustaende" mitlaufen lassen: das **aktuelle Zeichen** und sein
**Zähler**. Bei jedem neuen Zeichen prüfen, ob es das gleiche ist.
Falls nicht: aktuelles Zeichen ans Ergebnis anhaengen (mit Zahl, falls
> 1) und Zustaende neu setzen.

## Hintergrund

RLE ist eine der **einfachsten Kompressionen**, die es gibt --
funktioniert hervorragend bei Daten mit langen Wiederholungen
(Faxbilder, Sprite-Grafiken), aber kann bei zufaelligen Daten sogar
**laenger** werden als das Original.
