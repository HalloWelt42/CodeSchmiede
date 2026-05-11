---
schema_version: 1
id: 032-mittelwert
revision: 1
titel: Mittelwert einer Liste
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 5
tags: [listen, statistik, sum]
pfade: [python_listen]
voraussetzungen: [009-listen-summe]
quelle:
  url: null
  notiz: Klassische Statistik-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: mittelwert
hints:
  - kosten: 0
    text: |
      Summe / Anzahl. Achtung beim leeren Fall: gib `0.0` zurück.
  - kosten: 5
    text: |
      ```
      if not zahlen:
          return 0.0
      return sum(zahlen) / len(zahlen)
      ```
tests_sichtbar:
  - input: [[1, 2, 3, 4]]
    expected: 2.5
  - input: [[10]]
    expected: 10.0
  - input: [[]]
    expected: 0.0
  - input: [[5, 5, 5, 5]]
    expected: 5.0
tests_versteckt:
  - input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    expected: 5.5
  - input: [[-1, 1]]
    expected: 0.0
  - input: [[100, 200, 300]]
    expected: 200.0
  - input: [[7]]
    expected: 7.0
starter_code: |
  def mittelwert(zahlen: list[float]) -> float:
      # Deine Lösung hier -- leere Liste liefert 0.0
      pass
---

# Mittelwert einer Liste

Schreibe eine Funktion `mittelwert(zahlen)`, die den **arithmetischen
Mittelwert** der Liste zurückgibt. Bei leerer Liste liefere `0.0`.

## Beispiele

| Eingabe         | Ergebnis |
|-----------------|----------|
| `[1, 2, 3, 4]`  | `2.5`    |
| `[10]`          | `10.0`   |
| `[]`            | `0.0`    |
| `[5,5,5,5]`     | `5.0`    |

## Idee

`sum(zahlen) / len(zahlen)`. Der einzige Fallstrick ist die leere
Liste -- dann wäre `len == 0` und du würdest durch null teilen.

## Hintergrund

Mittelwerte sind die Eintrittskarte zur Statistik. Mit dieser Funktion
kannst du z.B. einen Notenschnitt, eine Durchschnittstemperatur oder
einen mittleren Verbrauch ermitteln.
