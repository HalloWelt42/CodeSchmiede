---
schema_version: 1
id: 148-woerter-umkehren
revision: 1
titel: Reihenfolge der Wörter umkehren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [strings, split, listen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Split/Join-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: woerter_umkehren
hints:
  - kosten: 0
    text: |
      Drehe die Reihenfolge der Wörter um. Mehrfache Leerzeichen
      werden zu einem Einzel-Leerzeichen reduziert.
      "Hallo  Welt" → "Welt Hallo".
  - kosten: 10
    text: |
      str.split() ohne Argument splittet an beliebigem Whitespace
      und entfernt leere Strings. Dann reversed() + " ".join().
tests_sichtbar:
  - input: ["Hallo Welt"]
    expected: "Welt Hallo"
  - input: [""]
    expected: ""
  - input: ["eins zwei drei"]
    expected: "drei zwei eins"
  - input: ["nur"]
    expected: "nur"
tests_versteckt:
  - input: ["  viele   Leerzeichen   hier  "]
    expected: "hier Leerzeichen viele"
  - input: ["a b c d e"]
    expected: "e d c b a"
  - input: ["    "]
    expected: ""
  - input: ["Der schnelle braune Fuchs"]
    expected: "Fuchs braune schnelle Der"
  - input: ["1 2 3"]
    expected: "3 2 1"
starter_code: |
  def woerter_umkehren(text: str) -> str:
      # Deine Lösung hier
      pass
---

# Reihenfolge der Wörter umkehren

Schreibe eine Funktion `wörter_umkehren(text)`, die die Reihenfolge
der Wörter im String **umdreht**. Mehrfache Leerzeichen werden
dabei zu einem einzelnen Leerzeichen reduziert; fuehrende und
nachfolgende Leerzeichen entfallen.

## Beispiele

| Eingabe                      | Ausgabe                      |
|------------------------------|------------------------------|
| `"Hallo Welt"`               | `"Welt Hallo"`               |
| `"eins zwei drei"`           | `"drei zwei eins"`           |
| `"  viele   Leerzeichen  "`  | `"Leerzeichen viele"`        |
| `""`                         | `""`                         |
| `"    "`                     | `""`                         |

## Idee

Pythons `str.split()` ohne Argument macht beide Dinge gleichzeitig:
es teilt an **beliebigem Whitespace** und filtert leere Stücke heraus.

## Vergleich mit Buchstaben-Umkehr

Nicht zu verwechseln mit `text[::-1]`, das **jeden einzelnen
Buchstaben** umdreht (`"Hallo Welt"` → `"tleW ollaH"`). Hier geht
es nur um die **Wort-Reihenfolge**.
