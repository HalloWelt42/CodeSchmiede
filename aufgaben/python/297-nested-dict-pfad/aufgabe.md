---
schema_version: 1
id: 297-nested-dict-pfad
revision: 1
titel: Nested-Dict via dotted path lesen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 40
schaetz_minuten: 15
tags: [dict, parsing, nested, recursion]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassisches Config-Lookup-Pattern
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: dict_pfad
hints:
  - kosten: 0
    text: |
      Lies einen Wert aus verschachteltem Dict via dotted path.
      "a.b.c" → d["a"]["b"]["c"].
      Bei FEHLENDEM Pfad → default (default-Wert ist Argument).
      Pfad "" oder None nicht vorgesehen, hier mit default_wert.
  - kosten: 20
    text: |
      Loop über pfad.split("."), pro Schritt prüfen ob Key existiert
      und Wert ein dict ist (sonst Pfad bricht ab).
tests_sichtbar:
  - input: [{"a": {"b": {"c": 42}}}, "a.b.c", null]
    expected: 42
  - input: [{"a": 1}, "a", null]
    expected: 1
  - input: [{"a": {"b": 2}}, "a.b", null]
    expected: 2
  - input: [{}, "x", "default"]
    expected: "default"
tests_versteckt:
  - input: [{"a": {"b": {"c": {"d": "tief"}}}}, "a.b.c.d", null]
    expected: "tief"
  - input: [{"a": {"b": 1}}, "a.b.c", null]
    expected: null
  - input: [{"a": {"b": 1}}, "a.x", "fallback"]
    expected: "fallback"
  - input: [{"a": [1, 2, 3]}, "a.0", null]
    expected: null
  - input: [{"a": null}, "a.b", "weg"]
    expected: "weg"
  - input: [{"server": {"port": 8080}}, "server.port", 0]
    expected: 8080
  - input: [{"a": {"b": false}}, "a.b", "default"]
    expected: false
starter_code: |
  def dict_pfad(d: dict, pfad: str, default):
      # Deine Lösung hier
      pass
---

# Nested-Dict via dotted path lesen

Schreibe `dict_pfad(d, pfad, default)`, die einen Wert aus einem
verschachtelten Dict über einen **Punkt-getrennten Pfad** liest.

`"a.b.c"` entspricht `d["a"]["b"]["c"]`.

Bei fehlendem Schlüssel oder wenn ein Zwischen-Wert kein Dict ist
→ `default` zurückgeben.

**Wichtig**: Wenn der Pfad existiert UND der Wert ist `False`/`0`/`None`,
muss der **echte Wert** zurückkommen -- nicht der `default`.

## Beispiele

| Dict                              | Pfad        | Default     | Ergebnis    |
|-----------------------------------|-------------|-------------|-------------|
| `{"a": {"b": {"c": 42}}}`         | `"a.b.c"`   | `None`      | `42`        |
| `{"a": 1}`                        | `"a"`       | `None`      | `1`         |
| `{"server": {"port": 8080}}`      | `"server.port"` | `0`     | `8080`      |
| `{}`                              | `"x"`       | `"default"` | `"default"` |
| `{"a": {"b": 1}}`                 | `"a.b.c"`   | `None`      | `None`      |
| `{"a": {"b": false}}`             | `"a.b"`     | `"default"` | `False`     |
| `{"a": null}`                     | `"a.b"`     | `"weg"`     | `"weg"`     |

## Idee

Pro Schritt:
1. Prüfen, ob aktueller `d` ein Dict ist UND der Schlüssel drin.
2. Falls nicht → default.
3. Falls ja → eine Ebene tiefer.

## Stolperstein -- `False` vs. `default`

Wer es so schreibt:

bekommt es bei einer Ebene noch hin, aber nicht für Pfade. Und
**`d.get` mit Default** unterscheidet nicht zwischen "Key da, Wert ist
None" und "Key nicht da". Daher die explizite `in`-Prüfung.

## Anwendung

- **Konfigurations-Lookup**: `config.get("server.timeout", 30)`.
- **Json-Path-Light** (echtes JSONPath ist maechtiger).
- **Template-Engines**: `{{user.address.city}}`-Lookup.
