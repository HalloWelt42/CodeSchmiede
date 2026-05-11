---
schema_version: 1
id: 294-query-string-bauen
revision: 1
titel: URL-Query-String aus Dict bauen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 22
schaetz_minuten: 10
tags: [strings, dict, url, formatierung]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Pendant zu 293
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: query_build
hints:
  - kosten: 0
    text: |
      Wandle ein Dict in einen Query-String "a=1&b=2".
      Schlüssel ALPHABETISCH sortiert (deterministisch).
      Werte werden mit str() konvertiert.
      Bei {} → "".
  - kosten: 15
    text: |
      "&".join(f"{k}={v}" for k, v in sorted(d.items())).
tests_sichtbar:
  - input: [{"a": 1, "b": 2}]
    expected: "a=1&b=2"
  - input: [{}]
    expected: ""
  - input: [{"x": "hallo"}]
    expected: "x=hallo"
  - input: [{"b": 1, "a": 2}]
    expected: "a=2&b=1"
tests_versteckt:
  - input: [{"foo": "bar", "baz": "qux"}]
    expected: "baz=qux&foo=bar"
  - input: [{"leer": ""}]
    expected: "leer="
  - input: [{"k": 100}]
    expected: "k=100"
  - input: [{"name": "Hans", "alter": 30}]
    expected: "alter=30&name=Hans"
  - input: [{"a": true, "b": false}]
    expected: "a=True&b=False"
  - input: [{"z": 1, "a": 2, "m": 3}]
    expected: "a=2&m=3&z=1"
starter_code: |
  def query_build(d: dict) -> str:
      # Deine Lösung hier -- alphabetisch sortiert
      pass
---

# URL-Query-String aus Dict bauen

Schreibe `query_build(d)`, die ein Dict in einen Query-String
`"a=1&b=2"` umwandelt -- mit Schlüsseln **alphabetisch sortiert**
(deterministisch).

Werte werden mit `str()` zu String konvertiert.
Bei leerem Dict → `""`.

## Beispiele

| Dict                         | Query-String              |
|------------------------------|---------------------------|
| `{"a": 1, "b": 2}`           | `"a=1&b=2"`               |
| `{"b": 1, "a": 2}`           | `"a=2&b=1"` (sortiert)    |
| `{"foo": "bar", "baz": "qux"}` | `"baz=qux&foo=bar"`     |
| `{"leer": ""}`               | `"leer="`                 |
| `{"a": True, "b": False}`    | `"a=True&b=False"`        |
| `{}`                         | `""`                      |

## Idee

`sorted(d.items())` sortiert nach Schlüssel (alphabetisch).
`f"{k}={v}"` formatiert pro Eintrag, `"&".join(...)` verkettet.

## Pendant -- Round-Trip

Achtung: Werte werden in `query_build` zu Strings, in `query_parse`
bleiben sie Strings. Ein vollstaendiger Round-Trip braucht
**string-Werte** auf beiden Seiten.

## Stolperstein -- URL-Encoding (wieder)

Wenn Werte Leerzeichen, `&`, `=` oder Sonderzeichen enthalten,
muss man **URL-encoden** (Leerzeichen → `%20`). `urllib.parse.urlencode`
macht das automatisch -- wir vereinfachen hier.

## Anwendung

- HTTP-Client baut URL-Parameter.
- Form-Submission als GET-Request.
- Konfigurations-Strings serialisieren.
