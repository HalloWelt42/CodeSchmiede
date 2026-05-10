---
schema_version: 1
id: 039-eratosthenes
revision: 1
titel: Sieb des Eratosthenes
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 22
schaetz_minuten: 15
tags: [algorithmen, primzahlen, listen]
pfade: [python_algorithmen]
voraussetzungen: [019-primfaktoren]
quelle:
  url: https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes
  notiz: Klassischer Algorithmus
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: primzahlen_bis
hints:
  - kosten: 0
    text: |
      Lege eine Liste an, die fuer jede Zahl markiert "ist Primzahl?".
      Streiche alle Vielfachen jeder gefundenen Primzahl ab i*i.
  - kosten: 20
    text: |
      ```
      ist_prim = [True] * (n + 1)
      ist_prim[0] = ist_prim[1] = False
      for i in range(2, int(n ** 0.5) + 1):
          if ist_prim[i]:
              for k in range(i*i, n+1, i):
                  ist_prim[k] = False
      return [i for i in range(n+1) if ist_prim[i]]
      ```
tests_sichtbar:
  - input: [10]
    expected: [2, 3, 5, 7]
  - input: [2]
    expected: [2]
  - input: [1]
    expected: []
  - input: [30]
    expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
tests_versteckt:
  - input: [0]
    expected: []
  - input: [3]
    expected: [2, 3]
  - input: [50]
    expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
  - input: [100]
    expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
starter_code: |
  def primzahlen_bis(n: int) -> list[int]:
      # Deine Lösung hier -- alle Primzahlen <= n, aufsteigend.
      pass
---

# Sieb des Eratosthenes

Schreibe eine Funktion `primzahlen_bis(n)`, die alle **Primzahlen
bis einschliesslich n** in aufsteigender Reihenfolge zurueckgibt.

## Beispiele

| `n` | Ergebnis                                                          |
|-----|-------------------------------------------------------------------|
| `10`| `[2,3,5,7]`                                                       |
| `2` | `[2]`                                                             |
| `1` | `[]`                                                              |
| `30`| `[2,3,5,7,11,13,17,19,23,29]`                                     |

## Idee: das Sieb

1. Lege eine Liste `ist_prim` der Laenge `n+1` an, initial alle `True`
2. Setze `ist_prim[0] = ist_prim[1] = False`
3. Fuer jede `i` von 2 bis `sqrt(n)`: wenn `ist_prim[i]`, streiche alle
   Vielfachen ab `i*i` (kleinere Vielfache wurden schon gestrichen)
4. Sammle alle Indizes mit `ist_prim[i] == True`

## Komplexitaet

Das Sieb ist mit $O(n \log \log n)$ deutlich schneller als jedes
Element einzeln auf Primalitaet zu prüfen ($O(n \sqrt{n})$). Bei
$n = 1.000.000$ ist der Unterschied praktisch riesig.

## Hintergrund

Der Algorithmus stammt von **Eratosthenes von Kyrene** (ca. 276-194
v. Chr.), Bibliothekar der Bibliothek von Alexandria. Er ist eines
der schoensten Beispiele dafuer, dass ein guter Algorithmus zwei
Jahrtausende ueberdauern kann.
