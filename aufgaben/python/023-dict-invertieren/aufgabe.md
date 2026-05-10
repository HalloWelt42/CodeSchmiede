---
schema_version: 1
id: 023-dict-invertieren
revision: 1
titel: Dictionary invertieren
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 5
tags: [dict, comprehension, schleifen]
pfade: [python_dicts]
voraussetzungen: [022-wortzaehler]
quelle:
  url: null
  notiz: Standard-Dict-Übung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: invertiere
hints:
  - kosten: 0
    text: |
      Ein neues Dict aufbauen, in dem fuer jedes (k, v) im Original
      ein Eintrag (v, k) landet.
  - kosten: 10
    text: |
      Mit Dict-Comprehension:

      ```
      return {v: k for k, v in d.items()}
      ```
tests_sichtbar:
  - input: [{ "a": 1, "b": 2, "c": 3 }]
    expected: { "1": "a", "2": "b", "3": "c" }
  - input: [{}]
    expected: {}
  - input: [{ "x": 42 }]
    expected: { "42": "x" }
tests_versteckt:
  - input: [{ "rot": 1, "gruen": 2, "blau": 3 }]
    expected: { "1": "rot", "2": "gruen", "3": "blau" }
  - input: [{ "eins": 1 }]
    expected: { "1": "eins" }
starter_code: |
  def invertiere(d: dict) -> dict:
      # Deine Lösung hier -- Schluessel und Werte tauschen.
      # Werte werden im Ergebnis als Strings verwendet (str(wert)).
      pass
---

# Dictionary invertieren

Schreibe eine Funktion `invertiere(d)`, die ein Dictionary so
umdreht, dass die **Werte zu Schluesseln** werden und umgekehrt.

Damit Schluessel im Ergebnis garantiert hashbar und vergleichbar sind,
werden die alten Werte mit `str(wert)` in Strings umgewandelt.

## Beispiele

| Eingabe                    | Ergebnis                          |
|----------------------------|-----------------------------------|
| `{"a":1, "b":2, "c":3}`    | `{"1":"a", "2":"b", "3":"c"}`     |
| `{}`                       | `{}`                              |
| `{"x":42}`                 | `{"42":"x"}`                      |

## Annahme

Wir setzen voraus, dass die Werte im Eingabe-Dictionary **eindeutig**
sind. Andernfalls wuerden mehrere Schluessel auf denselben neuen
Schluessel abgebildet, und nur der letzte ueberlebt.

## Hintergrund

Das Invertieren von Dictionaries ist eine haeufige Operation, wenn
man eine Lookup-Tabelle in beide Richtungen braucht -- etwa bei
Sprachcodes, Indizes oder Mapping-Tabellen.
