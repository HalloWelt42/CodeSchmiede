---
schema_version: 1
id: 250-einzigartige-werte
revision: 1
titel: Werte die nur einmal vorkommen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [listen, counter, dict, eindeutig]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Counter-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: einzigartig
hints:
  - kosten: 0
    text: |
      Liefere alle Werte, die in der Liste GENAU EINMAL vorkommen --
      sortiert.
      [1,2,2,3,3,4] → [1,4].
  - kosten: 10
    text: |
      collections.Counter -- dann Keys filtern, wo value == 1.
tests_sichtbar:
  - input: [[1, 2, 2, 3, 3, 4]]
    expected: [1, 4]
  - input: [[1, 2, 3]]
    expected: [1, 2, 3]
  - input: [[]]
    expected: []
  - input: [[1, 1, 1]]
    expected: []
tests_versteckt:
  - input: [[5]]
    expected: [5]
  - input: [["a", "b", "a", "c"]]
    expected: ["b", "c"]
  - input: [[1, 2, 3, 1, 2, 3, 1]]
    expected: []
  - input: [[10, 20, 30, 20, 10, 40]]
    expected: [30, 40]
  - input: [[1, 2, 1, 3, 1, 4, 1, 5]]
    expected: [2, 3, 4, 5]
  - input: [[7, 7, 7, 7, 7, 1]]
    expected: [1]
starter_code: |
  def einzigartig(liste: list) -> list:
      # Deine Lösung hier -- nur Werte mit Anzahl == 1, sortiert
      pass
---

# Werte die nur einmal vorkommen

Schreibe `einzigartig(liste)`, die alle Werte liefert, die in der
Liste **genau einmal** vorkommen -- als **sortierte** Liste.

## Beispiele

| Liste                  | Einzigartig    |
|------------------------|----------------|
| `[1, 2, 2, 3, 3, 4]`   | `[1, 4]`       |
| `[1, 2, 3]`            | `[1, 2, 3]`    |
| `[1, 1, 1]`            | `[]`           |
| `[7, 7, 7, 7, 7, 1]`   | `[1]`          |
| `[10, 20, 30, 20, 10, 40]` | `[30, 40]` |
| `[]`                   | `[]`           |

## Idee

`Counter` zählt jedes Vorkommen. `c.items()` liefert
`(key, count)`-Paare -- wir filtern auf `count == 1` und sortieren.

## Verwandt

| Aufgabe                  | Was?                          |
|--------------------------|--------------------------------|
| **011-listen-duplikate** | Werte die >= 2x vorkommen     |
| **027-eindeutige-reihenfolge** | Duplikate raus, Reihenfolge bewahrt |
| **162-häufigster-wert** | Modus (max-Anzahl)            |
| **250 hier**             | Werte mit Anzahl genau 1      |

## Anwendung

- **Singletons** in Daten finden: Verkaeufe, die nur einmal stattfanden.
- **Token-Filterung**: Hapax Legomena (Wörter die im Text einmal vorkommen)
  in Linguistik und Stilometrie.
- **Spurensuche**: in Logs ungewoehnliche IPs identifizieren.
