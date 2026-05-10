---
schema_version: 1
id: 034-caesar
revision: 1
titel: Caesar-Verschluesselung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [strings, krypto, modulo, ord]
pfade: [python_strings]
voraussetzungen: [005-text-umkehren]
quelle:
  url: https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung
  notiz: Klassiker, eigene Reformulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: caesar
hints:
  - kosten: 0
    text: |
      `ord('A')` liefert den ASCII-Wert. Verschiebe um `k`, dann
      `chr()` zurueck. Modulo `26` halt den Buchstaben im Alphabet.
  - kosten: 15
    text: |
      Pro Zeichen: pruefen ob Buchstabe (`isalpha`), bei Grossbuchstabe
      `'A'`-Basis verwenden, bei Kleinbuchstabe `'a'`-Basis.
      Nicht-Buchstaben unveraendert lassen.
  - kosten: 30
    text: |
      ```
      basis = ord('A') if c.isupper() else ord('a')
      neu = (ord(c) - basis + k) % 26 + basis
      return chr(neu)
      ```
tests_sichtbar:
  - input: ["abc", 1]
    expected: "bcd"
  - input: ["xyz", 3]
    expected: "abc"
  - input: ["Hallo Welt", 13]
    expected: "Unyyb Jryg"
  - input: ["", 5]
    expected: ""
tests_versteckt:
  - input: ["ABC", 25]
    expected: "ZAB"
  - input: ["Python 3.11!", 5]
    expected: "Udymts 3.11!"
  - input: ["abc", 0]
    expected: "abc"
  - input: ["abc", 26]
    expected: "abc"
  - input: ["The quick brown fox", 13]
    expected: "Gur dhvpx oebja sbk"
starter_code: |
  def caesar(text: str, k: int) -> str:
      # Deine Loesung hier -- nur a-z und A-Z verschieben, Rest unveraendert.
      pass
---

# Caesar-Verschluesselung

Schreibe eine Funktion `caesar(text, k)`, die jeden **Buchstaben** im
String um `k` Positionen im Alphabet verschiebt. Gross-/Kleinschreibung
bleibt erhalten. Nicht-Buchstaben (Leerzeichen, Ziffern,
Satzzeichen, ...) bleiben unveraendert.

## Beispiele

| Text             | k  | Ergebnis              |
|------------------|----|-----------------------|
| `"abc"`          | 1  | `"bcd"`               |
| `"xyz"`          | 3  | `"abc"`               |
| `"Hallo Welt"`   | 13 | `"Unyyb Jryg"`        |
| `"Python 3.11!"` | 5  | `"Udymts 3.11!"`      |

## Idee

Pro Zeichen:

1. Falls Buchstabe: Basis ermitteln (`'A'` oder `'a'`)
2. `(ord(c) - basis + k) % 26 + basis` ist der neue Code
3. Falls kein Buchstabe: 1:1 uebernehmen

## Hintergrund

Die Caesar-Chiffre ist eine der **aeltesten Verschluesselungen**, von
Julius Caesar fuer militaerische Korrespondenz benutzt (mit `k = 3`).
Sie ist heute trivial zu brechen -- es gibt nur 25 sinnvolle
Schluessel -- aber didaktisch hervorragend, weil sie modulares
Rechnen anschaulich macht.

`k = 13` ist als **ROT13** bekannt: zwei Anwendungen heben sich auf.
