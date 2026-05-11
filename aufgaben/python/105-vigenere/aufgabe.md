---
schema_version: 1
id: 105-vigenere
revision: 1
titel: Vigenère-Verschlüsselung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [strings, krypto, modulo, schluessel]
pfade: [python_codes]
voraussetzungen: [104-rot-chiffre]
quelle:
  url: https://de.wikipedia.org/wiki/Vigen%C3%A8re-Chiffre
  notiz: Klassische Polyalphabet-Chiffre, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: vigenere
hints:
  - kosten: 0
    text: |
      Wie ROT-N, aber pro Position eine andere Verschiebung -- bestimmt
      durch den Schlüssel. Schlüssel 'a'=0, 'b'=1, ..., 'z'=25.
      Schlüssel wird zyklisch wiederholt; Nicht-Buchstaben überspringen
      die Schlüsselposition NICHT.
  - kosten: 12
    text: |
      Pro Buchstabe: shift = ord(schlüssel[i % len(schlüssel)]) - ord('a').
      Verschiebung wie bei ROT, Groß/Klein bleibt erhalten.
tests_sichtbar:
  - input: ["abc", "a"]
    expected: "abc"
  - input: ["abc", "b"]
    expected: "bcd"
  - input: ["Hello", "key"]
    expected: "Rijvs"
  - input: ["Hello, World!", "key"]
    expected: "Rijvs, Uyvjn!"
tests_versteckt:
  - input: ["", "key"]
    expected: ""
  - input: ["AaAaAa", "abc"]
    expected: "AbCaBc"
  - input: ["mrttaqrhknsw ih puiqzqu", "abcd"]
    expected: "msvwartkkouz ii rxirbtu"
  - input: ["lebewohl", "geheim"]
    expected: "riiieanp"
starter_code: |
  def vigenere(text: str, schluessel: str) -> str:
      # Deine Lösung hier -- pro Position andere Verschiebung.
      pass
---

# Vigenère-Verschlüsselung

Schreibe eine Funktion `vigenere(text, schlüssel)`, die einen Text
mit der **Vigenère-Chiffre** verschlüsselt.

Im Unterschied zu Caesar/ROT-N variiert die Verschiebung pro Position --
gesteuert durch einen wiederholten Schlüssel.

## Regel

Position $i$:

$$
c_i = (t_i + k_{i \bmod |k|}) \bmod 26
$$

mit $a=0, b=1, ..., z=25$. Groß-/Kleinschreibung bleibt erhalten,
Nicht-Buchstaben werden 1:1 durchgereicht. Der Schlüssel-Index
wandert **nur** bei Buchstaben weiter -- Sonderzeichen überspringen
ihn nicht.

## Beispiele

| Text             | Schlüssel | Ergebnis           |
|------------------|-----------|--------------------|
| `"abc"`          | `"a"`     | `"abc"` (kein Shift) |
| `"abc"`          | `"b"`     | `"bcd"`            |
| `"Hello"`        | `"key"`   | `"Rijvs"`          |
| `"Hello, World!"`| `"key"`   | `"Rijvs, Uyvjn!"`  |

## Hintergrund

Beschrieben 1553 von Giovan Battista Bellaso, dann faelschlich
nach Blaise de Vigenère benannt. Galt 300 Jahre als unknackbar
("le chiffre indéchiffrable"), bis Charles Babbage und Friedrich
Kasiski sie 1854 / 1863 mit Periodenanalyse brachen.
