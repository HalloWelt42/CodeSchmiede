---
schema_version: 1
id: 143-coin-change
revision: 1
titel: Muenz-Wechsel (Coin Change)
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 55
schaetz_minuten: 20
tags: [dp, optimierung, listen, algorithmen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: LeetCode-Klassiker 322
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: muenz_wechsel
hints:
  - kosten: 0
    text: |
      Liefere die kleinste Anzahl Muenzen, die genau "betrag" ergeben.
      Wenn unmoeglich → -1. Jede Muenz-Sorte beliebig oft verwendbar.
  - kosten: 25
    text: |
      DP-Tabelle dp[0..betrag]. dp[0] = 0.
      dp[k] = 1 + min(dp[k - m] for m in muenzen if m <= k and dp[k-m] != inf).
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

# Muenz-Wechsel (Coin Change)

Gegeben sind eine Liste verfügbarer **Muenz-Werte** (jede Sorte
unbegrenzt oft) und ein Ziel-`betrag`. Schreibe eine Funktion
`muenz_wechsel(muenzen, betrag)`, die die **minimale Anzahl Muenzen**
zurückgibt, mit der sich der Betrag genau zusammensetzen laesst.

Wenn keine Kombination existiert → `-1`.
Bei `betrag == 0` → `0` (keine Muenzen nötig).

## Beispiele

| Muenzen        | Betrag | Min. Anzahl | Aufteilung      |
|----------------|--------|-------------|-----------------|
| `[1, 2, 5]`    | `11`   | `3`         | `5 + 5 + 1`     |
| `[2]`          | `3`    | `-1`        | unmoeglich      |
| `[1, 5, 10, 25]` | `30` | `2`         | `25 + 5`        |
| `[7, 11]`      | `23`   | `-1`        | unmoeglich      |

## Idee -- Bottom-Up-DP

`dp[k]` = minimale Anzahl Muenzen für Betrag `k`.

## Vorsicht: Greedy reicht nicht!

Bei `[1, 3, 4]` und Betrag 6 gibt Greedy (immer größte Muenze
zuerst) `4 + 1 + 1 = 3`, aber optimal ist `3 + 3 = 2`. Deswegen DP.

## Hintergrund

Coin-Change ist eine der kanonischen DP-Aufgaben. Verwandte Probleme:
**Anzahl der Wege** (statt Minimum), **Rucksack-Problem**, **Partition**.
Viele real existierende Muenz-Systeme (Cent-Stückelung) sind so
gewählt, dass Greedy zufaellig optimal ist.
