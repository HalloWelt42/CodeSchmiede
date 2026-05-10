---
schema_version: 1
id: 074-isbn
revision: 1
titel: ISBN-10 prüfen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [zahlen, strings, modulo, buchcodes]
pfade: [python_codes]
voraussetzungen: []
quelle:
  url: https://de.wikipedia.org/wiki/Internationale_Standardbuchnummer
  notiz: Inspiration aus Exercism (isbn-verifier), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: ist_isbn_gueltig
hints:
  - kosten: 0
    text: |
      ISBN-10 hat 10 Stellen. Letzte Stelle darf "X" sein -- als 10
      gewertet. Bindestriche werden ignoriert.
  - kosten: 15
    text: |
      Formel: $\sum_{i=1}^{10} d_i \cdot (11 - i) \equiv 0 \pmod{11}$
      mit $d_1$ als erster Ziffer.
tests_sichtbar:
  - input: ["3-598-21508-8"]
    expected: true
  - input: ["3-598-21508-9"]
    expected: false
  - input: ["3-598-21507-X"]
    expected: true
  - input: ["3598215088"]
    expected: true
tests_versteckt:
  - input: ["3-598-2X507-9"]
    expected: false
  - input: [""]
    expected: false
  - input: ["3-598-21508"]
    expected: false
  - input: ["3-598-21508-88"]
    expected: false
  - input: ["3-598-P1581-X"]
    expected: false
  - input: ["359821507X"]
    expected: true
starter_code: |
  def ist_isbn_gueltig(isbn: str) -> bool:
      # Deine Lösung hier -- ISBN-10 Format, 'X' nur am Ende.
      pass
---

# ISBN-10 prüfen

Schreibe eine Funktion `ist_isbn_gueltig(isbn)`, die prüft, ob ein
String eine **gültige ISBN-10** ist.

## Format

- **10 Stellen**, Bindestriche werden ignoriert
- Stellen 1-9: nur Ziffern
- Stelle 10: Ziffer **oder** `X` (steht für 10)

## Prüfformel

$$
\sum_{i=1}^{10} d_i \cdot (11 - i) \equiv 0 \pmod{11}
$$

mit $d_i$ als der $i$-ten Ziffer (von links). $X$ wird als 10
gewertet.

## Beispiele

| Eingabe              | Gültig? |
|----------------------|---------|
| `"3-598-21508-8"`    | `True`  |
| `"3-598-21508-9"`    | `False` |
| `"3-598-21507-X"`    | `True`  |
| `"3598215088"`       | `True`  |
| `"3-598-2X507-9"`    | `False` (X nur am Ende erlaubt) |
| `""`                 | `False` |

## Hintergrund

ISBN-10 wurde 1970 eingeführt und ist seit 2007 durch ISBN-13
abgelöst. Beide Varianten basieren auf einem Modulo-Check, der die
meisten Tippfehler abfängt.
