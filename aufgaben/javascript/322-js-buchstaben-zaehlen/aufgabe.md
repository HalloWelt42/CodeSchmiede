---
schema_version: 1
id: 322-js-buchstaben-zaehlen
revision: 1
titel: JavaScript -- Buchstaben im Text zaehlen
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [javascript, object, string, reduce, modern]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: reduce zu Object-Counter
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: zaehleBuchstaben
hints:
  - kosten: 0
    text: |
      Zaehle wie oft jeder Buchstabe im Text vorkommt -- als Object
      {buchstabe: anzahl}. Case-insensitive (alle klein), Whitespace
      und Sonderzeichen IGNORIEREN (nur a-z). Keys ALPHABETISCH
      sortiert (sonst schlaegt der JSON-Vergleich fehl).
      Bei "" → {}.
  - kosten: 15
    text: |
      [...text.toLowerCase()].reduce((akk, c) => {
        if (c >= 'a' && c <= 'z') akk[c] = (akk[c] || 0) + 1;
        return akk;
      }, {})
      ... dann Object.fromEntries(Object.entries(z).sort())
tests_sichtbar:
  - input: ["abc"]
    expected: {"a": 1, "b": 1, "c": 1}
  - input: [""]
    expected: {}
  - input: ["aaa"]
    expected: {"a": 3}
  - input: ["Hallo Welt"]
    expected: {"a": 1, "e": 1, "h": 1, "l": 3, "o": 1, "t": 1, "w": 1}
starter_code: |
  function zaehleBuchstaben(text) {
      // Tipp: spread + reduce, nur a-z zaehlen
  }
---

# JavaScript -- Buchstaben im Text zaehlen

Schreibe `zaehleBuchstaben(text)`, die ein Object liefert, das jeden
**Buchstaben (a-z, lowercased)** im Text zaehlt.

- Whitespace, Ziffern, Sonderzeichen → ignorieren
- Gross/Klein → zu klein konvertieren
- Bei `""` → `{}`

## Beispiele

| Text            | Ergebnis                                              |
|-----------------|--------------------------------------------------------|
| `"abc"`         | `{a: 1, b: 1, c: 1}`                                  |
| `"aaa"`         | `{a: 3}`                                              |
| `"Hallo Welt"`  | `{a:1, e:1, h:1, l:3, o:1, t:1, w:1}`                 |
| `""`            | `{}`                                                  |

## Idee -- modernes JS

```javascript
function zaehleBuchstaben(text) {
    const z = [...text.toLowerCase()].reduce((akk, c) => {
        if (c >= 'a' && c <= 'z') {
            akk[c] = (akk[c] || 0) + 1;
        }
        return akk;
    }, {});
    return Object.fromEntries(Object.entries(z).sort());
}
```

**Patterns**:
- `[...text]` -- Spread macht aus String ein Array von Zeichen.
  Sicher fuer Unicode (anders als `text.split('')` bei Surrogate-Pairs).
- `text.toLowerCase()` -- Case-Folding.
- `(akk[c] || 0) + 1` -- short-circuit fuer "key existiert nicht
  → 0".
- Filter im if statt vorher: spart eine Schleife.

## Variante mit Object.fromEntries

Funktional auch elegant:

```javascript
const zaehleBuchstaben = (text) =>
    Object.fromEntries(
        Object.entries(
            [...text.toLowerCase()].reduce((a, c) => {
                if (c >= 'a' && c <= 'z') a[c] = (a[c] || 0) + 1;
                return a;
            }, {})
        ).sort()  // alphabetische Reihenfolge
    );
```

Lesbarkeit leidet -- die direkte Variante ist hier besser.

## Hintergrund

In Python wuerde man `collections.Counter` nehmen -- in JS gibt's
das nicht direkt. Ein `Map` waere theoretisch besser (schneller,
typensicher), aber Object ist idiomatischer fuer JSON-Output.
