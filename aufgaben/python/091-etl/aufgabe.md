---
schema_version: 1
id: 091-etl
revision: 1
titel: ETL -- Punkte-Tabelle umbauen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 6
tags: [dict, transformation, schleifen]
pfade: [python_dicts]
voraussetzungen: [022-wortzaehler]
quelle:
  url: null
  notiz: Inspiration aus Exercism (etl), eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: transformiere
hints:
  - kosten: 0
    text: |
      Die Eingabe ist `{punkte: [buchstaben]}`. Ziel: `{buchstabe: punkte}`,
      wobei die Buchstaben kleingeschrieben sind.
  - kosten: 7
    text: |
      Mit Dict-Comprehension und doppeltem `for`:

      ```
      return {b.lower(): p for p, lst in alt.items() for b in lst}
      ```
tests_sichtbar:
  - input: [{ "1": ["A", "E", "I", "O", "U"] }]
    expected: { "a": 1, "e": 1, "i": 1, "o": 1, "u": 1 }
  - input: [{ "1": ["A", "E"], "2": ["D", "G"] }]
    expected: { "a": 1, "e": 1, "d": 2, "g": 2 }
  - input: [{}]
    expected: {}
  - input: [{ "5": ["K"] }]
    expected: { "k": 5 }
tests_versteckt:
  - input: [{ "10": ["Q", "Z"] }]
    expected: { "q": 10, "z": 10 }
  - input: [{ "1": ["A"], "8": ["X"] }]
    expected: { "a": 1, "x": 8 }
  - input: [{ "3": ["B", "C", "M", "P"] }]
    expected: { "b": 3, "c": 3, "m": 3, "p": 3 }
starter_code: |
  def transformiere(alt: dict) -> dict:
      # Deine Lösung hier -- Schluessel sind als String-Punkte da, Werte
      # sind Listen von Großbuchstaben. Ergebnis: {kleinbuchstabe: punkte}.
      pass
---

# ETL -- Punkte-Tabelle umbauen

Bei einem **alten** Format der Scrabble-Punkte sind die Werte
gruppiert: pro Punktzahl eine Liste der Buchstaben.

Du sollst das in das **neue** Format umbauen: pro Buchstabe die
Punktzahl, alles kleingeschrieben.

## Hintergrund

ETL = **Extract, Transform, Load** -- der Standard-Begriff für solche
Format-Umbauten. Diese Aufgabe ist ein Mini-T (transform), wie es
in jedem Daten-Pipeline-Job vorkommt.

## Hinweis

Im aufgaben.md-Test sind die Schlüssel als Strings, weil JSON keine
Integer-Schlüssel kennt. In Python landen sie aber genauso als
Strings. Behandle sie wie Strings.
