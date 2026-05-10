---
schema_version: 1
id: 076-atbash
revision: 1
titel: Atbash-Chiffre
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 8
tags: [strings, krypto, alphabet, modulo]
pfade: [python_codes]
voraussetzungen: [034-caesar]
quelle:
  url: https://de.wikipedia.org/wiki/Atbash
  notiz: Inspiration aus Exercism (atbash-cipher), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: atbash_codiere
hints:
  - kosten: 0
    text: |
      Atbash spiegelt das Alphabet: a->z, b->y, c->x, ..., z->a.
      Großbuchstaben werden klein. Ziffern bleiben. Sonderzeichen weg.
      Ausgabe in Fünfer-Gruppen, durch Leerzeichen getrennt.
  - kosten: 20
    text: |
      Pro Zeichen: ist es Buchstabe → 25 - (ord(c) - ord('a')) als
      Index ins Alphabet. Ziffern direkt durchreichen. Andere Zeichen
      werden weggelassen. Am Ende in Gruppen zu je 5 splitten.
tests_sichtbar:
  - input: ["yes"]
    expected: "bvh"
  - input: ["no"]
    expected: "ml"
  - input: ["OMG"]
    expected: "lnt"
  - input: ["Testing, 1 2 3, testing."]
    expected: "gvhgr mt123 gvhgr mt"
tests_versteckt:
  - input: ["mindblowingly"]
    expected: "nrmwy oldrm tob"
  - input: ["x123 yes"]
    expected: "c123b vh"
  - input: [""]
    expected: ""
  - input: ["Truth is fiction."]
    expected: "gifgs rhurx grlm"
  - input: ["The quick brown fox jumps over the lazy dog."]
    expected: "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
starter_code: |
  def atbash_codiere(text: str) -> str:
      # Deine Lösung hier -- alle Buchstaben spiegeln, Output in
      # Fünfer-Gruppen.
      pass
---

# Atbash-Chiffre

Schreibe eine Funktion `atbash_codiere(text)`, die einen Text mit
**Atbash** verschlüsselt -- einer der ältesten bekannten Chiffren.

## Regeln

- Buchstaben werden im Alphabet **gespiegelt**: a↔z, b↔y, c↔x, ..., m↔n.
- Eingabe-Großbuchstaben werden klein.
- Ziffern bleiben **unverändert**.
- Andere Zeichen (Punkt, Komma, Leerzeichen, ...) werden **entfernt**.
- Ausgabe wird in **Fünfer-Gruppen** geschrieben, getrennt durch
  Leerzeichen.

## Beispiele

| Eingabe                    | Ergebnis            |
|----------------------------|---------------------|
| `"yes"`                    | `"bvh"`             |
| `"no"`                     | `"ml"`              |
| `"OMG"`                    | `"lnt"`             |
| `"Testing, 1 2 3, testing."` | `"gvhgr mt123 gvhgr mt"` |

## Hintergrund

Atbash stammt aus dem hebräischen Alphabet -- der Name ist eine
Konkatenation der Buchstaben Aleph (1.), Taw (letzter), Beth (2.),
Schin (vorletzter). Im Alten Testament wird die Chiffre benutzt,
etwa in Jeremia 25,26 (Babel → Sheshach).
