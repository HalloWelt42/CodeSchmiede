---
schema_version: 1
id: 339-josephus
revision: 1
titel: Josephus-Problem -- letzter Ueberlebender
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 12
tags: [algorithmen, listen, modulo, klassiker]
pfade: []
voraussetzungen: []
quelle:
  url: https://rosettacode.org/wiki/Josephus_problem
  notiz: Rosetta Code -- Josephus problem
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: josephus
hints:
  - kosten: 0
    text: |
      n Personen stehen im Kreis (Index 0..n-1). Beginnend bei 0
      wird jede k-te Person eliminiert. Liefere den Index des letzten
      Ueberlebenden.
      Beispiel: n=5, k=2 → Eliminations-Folge 1, 3, 0, 4 → Sieger ist 2.
      n <= 0 oder k <= 0 → -1.
  - kosten: 20
    text: |
      Iterativ in O(n): J(1) = 0; J(n) = (J(n-1) + k) % n.
  - kosten: 35
    text: |
      def josephus(n, k):
          if n <= 0 or k <= 0: return -1
          j = 0
          for i in range(2, n + 1):
              j = (j + k) % i
          return j
tests_sichtbar:
  - input: [5, 2]
    expected: 2
  - input: [1, 1]
    expected: 0
  - input: [0, 3]
    expected: -1
  - input: [7, 3]
    expected: 3
tests_versteckt:
  - input: [10, 1]
    expected: 9
  - input: [10, 2]
    expected: 4
  - input: [41, 3]
    expected: 30
  - input: [100, 7]
    expected: 49
  - input: [2, 5]
    expected: 1
  - input: [5, 0]
    expected: -1
  - input: [-3, 2]
    expected: -1
starter_code: |
  def josephus(n: int, k: int) -> int:
      # Tipp: iterative Rekurrenz J(i) = (J(i-1) + k) % i
      pass
---

# Josephus-Problem

`n` Personen stehen im Kreis (Index `0` bis `n-1`). Beginnend bei
Index 0 wird **jede k-te Person** eliminiert. Wer ueberlebt?

Liefere den **Index des letzten Ueberlebenden**.

`n <= 0` oder `k <= 0` → `-1`.

## Beispiele

| n  | k | Sieger | Eliminations-Folge        |
|----|---|--------|---------------------------|
| 5  | 2 | `2`    | 1, 3, 0, 4                |
| 7  | 3 | `3`    | 2, 5, 1, 6, 4, 0          |
| 10 | 1 | `9`    | 0, 1, 2, ..., 8           |
| 41 | 3 | `30`   | (Original-Josephus-Beispiel) |

## Idee -- iterative Rekurrenz O(n)

`J(1) = 0` (allein -> Sieger). Bei jedem Hinzufuegen einer Person
verschiebt sich der Sieger um `k` modulo der neuen Anzahl.

## Hintergrund

Der Algorithmus geht auf den juedischen Historiker **Flavius
Josephus** zurueck (1. Jh. n. Chr.). Bei der Belagerung von
Yodfat (67 n. Chr.) sollen sich er und 40 Soldaten in einer
Hoehle versteckt und einen Selbstmord-Pakt geschlossen haben:
im Kreis stehen, jeden dritten toeten. Josephus angeblich
berechnete seine Position so, dass er ueberlebte.

## Naive Variante mit Liste -- O(n²)

Klar lesbar, aber bei `n = 10000` schon merkbar langsam. Die
Rekurrenz oben ist viel eleganter.
