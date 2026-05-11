---
schema_version: 1
id: 169-laenger-collatz
revision: 1
titel: Collatz-Rekord unter n
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 35
schaetz_minuten: 15
tags: [collatz, mathematik, schleifen, optimierung]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Project-Euler-Aufgabe 14
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: laengster_collatz
hints:
  - kosten: 0
    text: |
      Finde unter allen Startwerten 1 <= s < n diejenige Zahl mit
      der laengsten Collatz-Folge (Anzahl Schritte bis 1).
      Bei Gleichstand: kleinste solche Zahl.
      n <= 1 → 0 (keine gültigen Startwerte).
  - kosten: 20
    text: |
      Memoization: Dict {1: 0}. Pro Zahl rekursiv Laenge berechnen
      (1 + laenge[n//2] bzw. 1 + laenge[3n+1]) und im Cache speichern.
tests_sichtbar:
  - input: [10]
    expected: 9
  - input: [1]
    expected: 0
  - input: [2]
    expected: 1
  - input: [100]
    expected: 97
tests_versteckt:
  - input: [1000]
    expected: 871
  - input: [10000]
    expected: 6171
  - input: [3]
    expected: 2
  - input: [5]
    expected: 3
  - input: [50]
    expected: 27
  - input: [0]
    expected: 0
starter_code: |
  def laengster_collatz(n: int) -> int:
      # Deine Lösung hier -- Startwert mit laengster Collatz-Folge unter n
      pass
---

# Collatz-Rekord unter n

Die **Collatz-Folge** (auch "3n+1") für einen Startwert `s`:

- `s` gerade → `s // 2`
- `s` ungerade → `3 * s + 1`
- weiter, bis `s == 1`.

Die **Laenge** ist die Anzahl der Schritte bis zur 1.

Schreibe `laengster_collatz(n)`, die unter allen Startwerten
`1 <= s < n` diejenige Zahl liefert, deren Collatz-Folge **am
laengsten** ist. Bei Gleichstand: die **kleinste** solche Zahl.

Bei `n <= 1` → `0`.

## Beispiele

| `n`    | Sieger | Laenge |
|--------|--------|--------|
| `2`    | `1`    | `0`    |
| `10`   | `9`    | `19`   |
| `100`  | `97`   | `118`  |
| `1000` | `871`  | `178`  |
| `10000`| `6171` | `261`  |

## Idee mit Memoization

Naive Schleife pro Startwert ist langsam, weil dieselben Zahlen oft
mehrfach durchgerechnet werden. Mit einem Cache:

```python
def laengster_collatz(n):
    if n <= 1:
        return 0
    laenge = {1: 0}

    def L(k):
        if k in laenge:
            return laenge[k]
        weiter = k // 2 if k % 2 == 0 else 3 * k + 1
        laenge[k] = 1 + L(weiter)
        return laenge[k]

    bester = 1
    beste_laenge = 0
    for s in range(1, n):
        ls = L(s)
        if ls > beste_laenge:
            bester, beste_laenge = s, ls
    return bester
```

## Bemerkung

Die **Collatz-Vermutung** besagt, dass jeder Startwert irgendwann bei
1 landet. Bewiesen ist das bis $2^{68}$, aber **kein allgemeiner
Beweis** bekannt -- Paul Erdoes meinte: "Mathematics may not be ready
for such problems."

Bei rekursiver Lösung Achtung: Pythons Stack-Limit erreicht man bei
hohen `n` schnell. Iterative Variante mit `while` ist robuster.
