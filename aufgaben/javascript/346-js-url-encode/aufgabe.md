---
schema_version: 1
id: 346-js-url-encode
revision: 1
titel: JavaScript -- URL-Prozent-Codierung
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [javascript, strings, codierung, url, web]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/URL_encoding
  notiz: Rosetta Code -- URL encoding, JS
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: urlEncode
hints:
  - kosten: 0
    text: |
      URL-Encoding nach RFC 3986. Unreserviert (A-Z a-z 0-9 - _ . ~)
      bleibt, der Rest wird %XX (Hex gross).
      Tipp: encodeURIComponent + Workaround fuer ! * ' ( ) -- die werden
      nicht codiert vom Builtin, RFC 3986 will sie aber codiert.
  - kosten: 15
    text: |
      encodeURIComponent(s).replace(/[!*'()]/g, c => '%' + c.charCodeAt(0).toString(16).toUpperCase())
tests_sichtbar:
  - input: ["Hallo"]
    expected: "Hallo"
  - input: ["Hallo Welt"]
    expected: "Hallo%20Welt"
  - input: [""]
    expected: ""
  - input: ["abc-_.~"]
    expected: "abc-_.~"
starter_code: |
  function urlEncode(s) {
      // Tipp: encodeURIComponent + RFC-3986-Korrektur fuer ! * ' ( )
  }
---

# JavaScript -- URL-Prozent-Codierung

Schreibe `urlEncode(s)`, die einen String nach **RFC 3986** URL-
codiert.

Regel:
- Unreserviert (`A-Z a-z 0-9 - _ . ~`) bleibt
- Alles andere zu `%XX` (Hex, **gross**)

## Beispiele

| Eingabe        | Ergebnis           |
|----------------|---------------------|
| `"Hallo"`      | `"Hallo"`          |
| `"Hallo Welt"` | `"Hallo%20Welt"`   |
| `"abc-_.~"`    | `"abc-_.~"`        |
| `""`           | `""`               |

## Idee -- encodeURIComponent + Korrektur

`encodeURIComponent` macht 95 % der Arbeit -- aber **lasst die
Zeichen `! * ' ( )` unbehandelt**. RFC 3986 will sie aber codiert.
Daher der `replace`-Nachsatz.

## Stolperstein -- encodeURI vs encodeURIComponent

| Funktion             | Unbehandelt                  |
|----------------------|------------------------------|
| `encodeURI`          | `; / ? : @ & = + $ , #` (URI-Sonderzeichen) |
| `encodeURIComponent` | nur `A-Z a-z 0-9 - _ . ! ~ * ' ( )` |

`encodeURI` ist fuer GANZE URLs (laesst Sonderzeichen drin),
`encodeURIComponent` fuer **Werte** in URLs (codiert mehr) -- 
hier richtig.

## Vergleich mit Python

Python: `urllib.parse.quote(s, safe='')`. Hier wie in JS muss man
ueber den Builtin "drueberbessern" -- weil Standards leicht
abweichen vom RFC.
