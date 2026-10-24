---
schema_version: 1
id: 143-coin-change
revision: 2
titel: Münz-Wechsel (Coin Change)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 55
schaetz_minuten: 20
tags: [dp, optimierung, listen, algorithmen]
voraussetzungen: []
quelle:
  url: null
  notiz: Klassiker der dynamischen Programmierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: muenz_wechsel
hints:
  - kosten: 0
    text: |
      Liefere die kleinste Anzahl Münzen, die genau "betrag" ergeben.
      Wenn unmöglich → -1. Jede Münz-Sorte beliebig oft verwendbar.
  - kosten: 25
    text: |
      DP-Tabelle dp[0..betrag]. dp[0] = 0.
      dp[k] = 1 + min(dp[k - m] for m in münzen if m <= k and dp[k-m] != inf).
      Am Ende: -1 falls dp[betrag] == inf.
tests_sichtbar:
  - input: [[1, 2, 5], 11]
    expected: 3
  - input: [[2], 3]
    expected: -1
  - input: [[1], 0]
    expected: 0
  - input: [[1, 2, 5], 0]
    expected: 0
tests_versteckt:
  - input: [[1, 2, 5], 100]
    expected: 20
  - input: [[2, 5, 10, 1], 27]
    expected: 4
  - input: [[186, 419, 83, 408], 6249]
    expected: 20
  - input: [[1, 2, 5], 1]
    expected: 1
  - input: [[7, 11], 23]
    expected: -1
  - input: [[1, 5, 10, 25], 30]
    expected: 2
starter_code: |
  def muenz_wechsel(muenzen: list[int], betrag: int) -> int:
      # Deine Lösung hier -- DP, -1 bei unmoeglich
      pass
---

# Münz-Wechsel (Coin Change)

Gegeben sind eine Liste verfügbarer **Münz-Werte** (jede Sorte
unbegrenzt oft) und ein Ziel-`betrag`. Schreibe eine Funktion
`muenz_wechsel(muenzen, betrag)`, die die **minimale Anzahl Münzen**
zurückgibt, mit der sich der Betrag genau zusammensetzen lässt.

Wenn keine Kombination existiert → `-1`.
Bei `betrag == 0` → `0` (keine Münzen nötig).

## Beispiele

| Münzen        | Betrag | Min. Anzahl | Aufteilung      |
|----------------|--------|-------------|-----------------|
| `[1, 2, 5]`    | `11`   | `3`         | `5 + 5 + 1`     |
| `[2]`          | `3`    | `-1`        | unmöglich      |
| `[1, 5, 10, 25]` | `30` | `2`         | `25 + 5`        |
| `[7, 11]`      | `23`   | `-1`        | unmöglich      |

## Idee - Bottom-Up-DP

`dp[k]` = minimale Anzahl Münzen für Betrag `k`.

## Vorsicht: Greedy reicht nicht!

Bei `[1, 3, 4]` und Betrag 6 gibt Greedy (immer größte Münze
zuerst) `4 + 1 + 1 = 3`, aber optimal ist `3 + 3 = 2`. Deswegen DP.

## Hintergrund

Coin-Change ist eine der kanonischen DP-Aufgaben. Verwandte Probleme:
**Anzahl der Wege** (statt Minimum), **Rucksack-Problem**, **Partition**.
Viele real existierende Münz-Systeme (Cent-Stückelung) sind so
gewählt, dass Greedy zufällig optimal ist.
