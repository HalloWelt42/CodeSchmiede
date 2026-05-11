---
schema_version: 1
id: 104-rot-chiffre
revision: 1
titel: ROT-N Chiffre
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [strings, krypto, modulo, alphabet]
pfade: [python_codes]
voraussetzungen: [034-caesar]
quelle:
  url: https://de.wikipedia.org/wiki/ROT13
  notiz: Verallgemeinerung von ROT13 für beliebigen Shift
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: rot
hints:
  - kosten: 0
    text: |
      ROT13 als Spezialfall von Caesar -- aber: Groß-/Kleinschreibung
      bleibt erhalten, Nicht-Buchstaben bleiben unverändert. Leerzeichen
      und Satzzeichen werden NICHT entfernt.
  - kosten: 15
    text: |
      Pro Zeichen: ist es Großbuchstabe → 'A'-Basis. Kleinbuchstabe →
      'a'-Basis. Sonst → unverändert. `(ord(c) - basis + n) % 26 + basis`.
tests_sichtbar:
  - input: ["a", 1]
    expected: "b"
  - input: ["Hello, World!", 5]
    expected: "Mjqqt, Btwqi!"
  - input: ["The quick brown fox jumps over the lazy dog.", 13]
    expected: "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
  - input: ["", 7]
    expected: ""
tests_versteckt:
  - input: ["Cool", 0]
    expected: "Cool"
  - input: ["Cool", 26]
    expected: "Cool"
  - input: ["Cool", -3]
    expected: "Zlli"
  - input: ["Same string can be read backwards.", 13]
    expected: "Fnzr fgevat pna or ernq onpxjneqf."
  - input: ["abc", 1000]
    expected: "mno"
starter_code: |
  def rot(text: str, n: int) -> str:
      # Deine Lösung hier -- ROT-N (verallgemeinerte Caesar-Chiffre).
      # Anders als 034-caesar: Sonderzeichen + Leerzeichen bleiben drin.
      pass
---

# ROT-N Chiffre

Schreibe eine Funktion `rot(text, n)`, die einen Text um `n`
Positionen im Alphabet rotiert -- die **verallgemeinerte
Caesar-Chiffre**.

## Unterschied zu Aufgabe 034 (Caesar)

| | Caesar (034) | ROT-N (hier) |
|---|---|---|
| Großschreibung | wird klein | bleibt |
| Sonderzeichen/Leerzeichen | werden entfernt | bleiben unverändert |
| Negative `n` | nicht behandelt | erlaubt |

## Beispiele

| Text                                            | n  | Ergebnis                                          |
|-------------------------------------------------|----|---------------------------------------------------|
| `"a"`                                           | 1  | `"b"`                                             |
| `"Hello, World!"`                               | 5  | `"Mjqqt, Btwqi!"`                                 |
| `"The quick brown fox jumps over the lazy dog."`| 13 | `"Gur dhvpx oebja sbk whzcf bire gur ynml qbt."`  |
| `"Cool"`                                        | -3 | `"Zlli"`                                          |
| `"abc"`                                         | 1000 | `"mno"` (1000 % 26 = 12)                        |

## Hintergrund

ROT13 ist die kleine Schwester der Caesar-Chiffre und ein
Internet-Klassiker -- in Usenet-Foren wurden Spoiler früher
"verschlüsselt", indem man sie mit ROT13 codierte.
