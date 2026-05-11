---
schema_version: 1
id: 320-js-objekt-keys-sort
revision: 1
titel: JavaScript -- Objekt-Keys alphabetisch sortiert
sprache: javascript
task_type: code_schreiben
runner_type: webworker_js
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [javascript, object, array, sort, modern]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Object.keys + sort
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: keysSortiert
hints:
  - kosten: 0
    text: |
      Liefere die Keys eines Objekts alphabetisch sortiert als Array.
      Object.keys(obj) liefert die Keys, .sort() sortiert sie.
      Object.keys liefert IMMER Strings.
  - kosten: 5
    text: |
      Object.keys(obj).sort()
tests_sichtbar:
  - input: [{"b": 1, "a": 2, "c": 3}]
    expected: ["a", "b", "c"]
  - input: [{}]
    expected: []
  - input: [{"x": 100}]
    expected: ["x"]
  - input: [{"zebra": 1, "apfel": 2, "maus": 3}]
    expected: ["apfel", "maus", "zebra"]
starter_code: |
  function keysSortiert(obj) {
      // Tipp: Object.keys + sort
  }
---

# JavaScript -- Objekt-Keys alphabetisch sortiert

Schreibe `keysSortiert(obj)`, die die Keys eines Objekts als Array
zurückgibt -- **alphabetisch sortiert**.

Bei leerem Objekt → `[]`.

## Beispiele

| Objekt                          | Keys                  |
|---------------------------------|------------------------|
| `{b: 1, a: 2, c: 3}`            | `["a", "b", "c"]`     |
| `{x: 100}`                      | `["x"]`               |
| `{zebra: 1, apfel: 2, maus: 3}` | `["apfel","maus","zebra"]` |
| `{}`                            | `[]`                  |

## Idee -- modernes JS

`Object.keys(obj)` liefert ein Array aller eigenen, enumerable
Keys -- immer als **Strings** (auch wenn die Keys Zahlen wären).
`Array.sort()` sortiert in-place und liefert das sortierte Array
zurück.

## Stolperstein -- numerische Keys

In JavaScript werden **numerische Keys** in Objekten automatisch
zu Strings konvertiert UND iteriert in numerischer Reihenfolge:

Das ist ein **historischer Quirk** von JavaScript. Bei rein
numerischen Keys liefert `.sort()` lexikographisch (`["1","2","3"]`),
das ist hier OK.

## Verwandt -- Object.values, Object.entries

| Methode             | Liefert            |
|---------------------|---------------------|
| `Object.keys(o)`    | `["a", "b"]`        |
| `Object.values(o)`  | `[1, 2]`            |
| `Object.entries(o)` | `[["a",1], ["b",2]]`|

`Object.entries` plus `Object.fromEntries` ist das **moderne JS-
Idiom** für Objekt-Transformationen.
