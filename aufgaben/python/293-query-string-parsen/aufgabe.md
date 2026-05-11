---
schema_version: 1
id: 293-query-string-parsen
revision: 1
titel: URL-Query-String parsen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [strings, parsing, dict, url]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Web-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: query_parse
hints:
  - kosten: 0
    text: |
      Parse einen Query-String "a=1&b=2&c=3" zu Dict {"a": "1", ...}.
      Werte BLEIBEN STRINGS (kein int-cast).
      Optionales fuehrendes "?" abstrippen.
      Leerer/None String → {}. Bei "k=" → {"k": ""}. Bei "k" ohne "=" → {"k": ""}.
  - kosten: 15
    text: |
      Vorab "?" entfernen, dann split("&"), pro Paar split("=", 1).
      Bei nur Key (kein =) → wert = "".
tests_sichtbar:
  - input: ["a=1&b=2"]
    expected: {"a": "1", "b": "2"}
  - input: [""]
    expected: {}
  - input: ["?x=hallo"]
    expected: {"x": "hallo"}
  - input: ["leer="]
    expected: {"leer": ""}
tests_versteckt:
  - input: ["?a=1&b=2&c=3"]
    expected: {"a": "1", "b": "2", "c": "3"}
  - input: ["nur_key"]
    expected: {"nur_key": ""}
  - input: ["a=hallo welt"]
    expected: {"a": "hallo welt"}
  - input: ["x=1&y=2&z="]
    expected: {"x": "1", "y": "2", "z": ""}
  - input: ["?"]
    expected: {}
  - input: ["a=b=c"]
    expected: {"a": "b=c"}
  - input: ["foo=bar&baz=quux&hello=world"]
    expected: {"foo": "bar", "baz": "quux", "hello": "world"}
starter_code: |
  def query_parse(s: str) -> dict:
      # Deine Lösung hier -- ohne urllib.parse
      pass
---

# URL-Query-String parsen

Schreibe `query_parse(s)`, die einen Query-String wie `"a=1&b=2"`
in ein Dict `{"a": "1", "b": "2"}` umwandelt.

Regeln:
- Optionales fuehrendes `?` wird abgestrippt.
- Werte bleiben **Strings** (kein int/float-Cast).
- `"key="` → `{"key": ""}` (leerer Wert).
- `"key"` ohne `=` → `{"key": ""}`.
- `"key=val=ue"` → `{"key": "val=ue"}` (nur am ersten `=` splitten).
- Leere Eingabe oder nur `"?"` → `{}`.

## Beispiele

| Eingabe                         | Ergebnis                              |
|---------------------------------|----------------------------------------|
| `"a=1&b=2"`                     | `{"a": "1", "b": "2"}`                |
| `"?x=hallo"`                    | `{"x": "hallo"}`                      |
| `"leer="`                       | `{"leer": ""}`                        |
| `"nur_key"`                     | `{"nur_key": ""}`                     |
| `"a=hallo welt"`                | `{"a": "hallo welt"}`                 |
| `"a=b=c"`                       | `{"a": "b=c"}`                        |
| `"?"`                           | `{}`                                  |

## Idee

`split("=", 1)` mit Limit 1: spaltet nur am **ersten** `=`,
spaetere bleiben Teil des Werts.

## Stolperstein -- URL-Encoding

Echte Query-Strings sind **URL-encoded** (Leerzeichen als `%20`,
Sonderzeichen als `%XX`). `urllib.parse.parse_qs` und
`urllib.parse.unquote` machen das automatisch. Hier vereinfachen
wir und erwarten unkodierte Strings.

## Anwendung

Web-Server, REST-Clients, Browser-History-Parsing, Konfigurations-
DSLs (z.B. ".env"-Dateien sind ähnlich aufgebaut).
