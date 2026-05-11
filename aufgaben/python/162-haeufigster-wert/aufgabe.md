---
schema_version: 1
id: 162-haeufigster-wert
revision: 1
titel: Häufigster Wert (Modus)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [statistik, dicts, counter, listen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Statistik-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: haeufigster
hints:
  - kosten: 0
    text: |
      Liefere den häufigsten Wert (Modus) einer Liste. Bei
      Gleichstand: den **kleinsten** der häufigsten Werte.
      Bei leerer Liste -> None.
  - kosten: 12
    text: |
      collections.Counter(...) liefert die Häufigkeiten.
      max-Anzahl bestimmen, dann unter allen mit dieser Anzahl
      das Minimum wählen.
tests_sichtbar:
  - input: [[1, 2, 2, 3]]
    expected: 2
  - input: [[1, 1, 2, 2]]
    expected: 1
  - input: [[]]
    expected: null
  - input: [[5]]
    expected: 5
tests_versteckt:
  - input: [[7, 7, 7, 1, 1]]
    expected: 7
  - input: [[3, 3, 1, 1, 2]]
    expected: 1
  - input: [[1, 2, 3, 4, 5]]
    expected: 1
  - input: [[-1, -1, 0, 0, 1]]
    expected: -1
  - input: [[42, 42, 42, 42]]
    expected: 42
  - input: [[10, 20, 20, 30, 30, 40]]
    expected: 20
starter_code: |
  def haeufigster(zahlen: list):
      # Deine Lösung hier -- bei Gleichstand: kleinster Wert
      pass
---

# Häufigster Wert (Modus)

Schreibe eine Funktion `häufigster(zahlen)`, die den **häufigsten
Wert** einer Liste zurückgibt.

- Bei mehreren Werten mit gleicher Spitzenhäufigkeit: **kleinster**
  davon.
- Bei leerer Liste → `None`.

## Beispiele

| Liste                  | Modus | Begruendung           |
|------------------------|-------|------------------------|
| `[1, 2, 2, 3]`         | `2`   | 2 kommt zweimal vor    |
| `[1, 1, 2, 2]`         | `1`   | Gleichstand → kleinster|
| `[3, 3, 1, 1, 2]`      | `1`   | 1 und 3 je 2x → 1      |
| `[1, 2, 3, 4, 5]`      | `1`   | alle 1x → kleinster    |
| `[]`                   | `None`|                        |

## Tie-Breaking

Standard-`Counter.most_common(1)` liefert bei Gleichstand das **zuerst
gesehene** Element -- nicht das kleinste. Darum hier die explizite
Filter-und-Min-Variante.

## Statistik-Hintergrund

Modus, **Median** (Aufgabe 161) und **Mittelwert** sind die drei
Lagemasse. Bei kategorischen Daten (z.B. Lieblings-Eis-Sorten) ist
der Modus oft die einzig sinnvolle Statistik -- du kannst nicht
"den Durchschnitt aus Vanille und Schoko" bilden.
