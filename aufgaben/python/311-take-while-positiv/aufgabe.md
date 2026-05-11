---
schema_version: 1
id: 311-take-while-positiv
revision: 1
titel: Take-While positiv
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [generator, yield, listen, takewhile]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: itertools.takewhile nachbauen
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: take_while_positiv
hints:
  - kosten: 0
    text: |
      Nimm Elemente vom Anfang der Liste, SOLANGE sie POSITIV (>0) sind.
      Sobald ein <= 0 kommt: STOP, alles danach ignorieren.
      Intern Generator mit yield + break.
  - kosten: 12
    text: |
      def gen(): for x in liste: if x>0: yield x; else: break
tests_sichtbar:
  - input: [[1, 2, 3, -1, 5]]
    expected: [1, 2, 3]
  - input: [[]]
    expected: []
  - input: [[-1, 2, 3]]
    expected: []
  - input: [[1, 2, 3]]
    expected: [1, 2, 3]
tests_versteckt:
  - input: [[5, 4, 3, 2, 1]]
    expected: [5, 4, 3, 2, 1]
  - input: [[0, 1, 2]]
    expected: []
  - input: [[10, 0, 5]]
    expected: [10]
  - input: [[1]]
    expected: [1]
  - input: [[-5]]
    expected: []
  - input: [[1, 2, 3, 4, 5, -1, 100, 200]]
    expected: [1, 2, 3, 4, 5]
  - input: [[100]]
    expected: [100]
starter_code: |
  def take_while_positiv(liste: list[int]) -> list[int]:
      # Tipp: Generator mit yield + break
      pass
---

# Take-While positiv

Schreibe `take_while_positiv(liste)`, die Elemente vom Anfang der
Liste nimmt -- **solange sie positiv (`> 0`)** sind. Beim ersten
nicht-positiven Element (`0` oder negativ) wird **abgebrochen**;
der Rest wird **nicht** mitgenommen.

## Beispiele

| Eingabe                  | Ergebnis           |
|--------------------------|---------------------|
| `[1, 2, 3, -1, 5]`       | `[1, 2, 3]`         |
| `[5, 4, 3, 2, 1]`        | `[5, 4, 3, 2, 1]`   |
| `[10, 0, 5]`             | `[10]`              |
| `[-1, 2, 3]`             | `[]`                |
| `[0, 1, 2]`              | `[]`                |
| `[1, 2, 3, -1, 100, 200]`| `[1, 2, 3]`         |

## Idee -- Generator mit break

`break` beendet den Generator -- alle Werte nach dem ersten
nicht-positiven werden übersprungen.

## Mit itertools.takewhile

`takewhile` ist exakt dafür gemacht: nimmt Elemente, solange das
Predicate True liefert, bricht beim ersten False ab.

## Vergleich -- filter vs takewhile

| Funktion    | Verhalten                                |
|-------------|------------------------------------------|
| `filter`    | nimmt **alle** Elemente, die das Predicate erfüllen |
| `takewhile` | nimmt vom **Anfang**, bis Predicate False |
| `dropwhile` | übersprungt vom **Anfang**, bis Predicate False, dann **alles** |

`filter` auf `[1, 2, -1, 3]` mit `>0` liefert `[1, 2, 3]`.
`takewhile` liefert nur `[1, 2]`.

## Anwendung

- Konfigurations-Header lesen, bis erste leere Zeile
- Sensor-Daten verarbeiten, bis Fehler-Marker
- Stream-Verarbeitung mit Stop-Bedingung
