---
schema_version: 1
id: 137-naechste-permutation
revision: 1
titel: Nächste Permutation
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 22
schaetz_minuten: 15
tags: [listen, permutationen, algorithmus, in-place]
pfade: [python_algorithmen2]
voraussetzungen: [108-permutationen]
quelle:
  url: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
  notiz: Klassischer Algorithmus, eigene Formulierung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: naechste_permutation
hints:
  - kosten: 0
    text: |
      Liefere die nächste Permutation in lexikographischer Reihenfolge.
      Wenn aktuell die letzte ist, sortiert zurückgeben.
  - kosten: 30
    text: |
      Algorithmus:
      1. Suche größtes i mit a[i] < a[i+1] (Pivot von rechts).
      2. Wenn keines existiert: alles aufsteigend sortiert (war letzte).
      3. Suche größtes j > i mit a[j] > a[i].
      4. Tausche a[i] und a[j].
      5. Reverse a[i+1:].
tests_sichtbar:
  - input: [[1, 2, 3]]
    expected: [1, 3, 2]
  - input: [[3, 2, 1]]
    expected: [1, 2, 3]
  - input: [[1, 1, 5]]
    expected: [1, 5, 1]
  - input: [[1, 3, 2]]
    expected: [2, 1, 3]
tests_versteckt:
  - input: [[]]
    expected: []
  - input: [[1]]
    expected: [1]
  - input: [[1, 2]]
    expected: [2, 1]
  - input: [[2, 1]]
    expected: [1, 2]
  - input: [[1, 2, 3, 4]]
    expected: [1, 2, 4, 3]
  - input: [[4, 3, 2, 1]]
    expected: [1, 2, 3, 4]
  - input: [[1, 5, 1]]
    expected: [5, 1, 1]
starter_code: |
  def naechste_permutation(a: list[int]) -> list[int]:
      # Deine Lösung hier -- naechste lex. Permutation, sonst sortiert.
      pass
---

# Nächste Permutation

Schreibe eine Funktion `nächste_permutation(a)`, die die nächste
Permutation in **lexikographischer Reihenfolge** zurückgibt.
Wenn die Eingabe bereits die letzte (absteigend sortierte) ist,
liefere sie aufsteigend sortiert.

## Algorithmus

1. Suche das **größte** $i$ mit $a[i] < a[i+1]$.
2. Wenn keines existiert -- Liste ist absteigend sortiert -- liefere
   sie aufsteigend sortiert.
3. Suche das **größte** $j > i$ mit $a[j] > a[i]$.
4. Tausche $a[i]$ und $a[j]$.
5. Drehe $a[i+1:]$ um.

## Beispiele

| Eingabe       | Naechste      |
|---------------|---------------|
| `[1, 2, 3]`   | `[1, 3, 2]`   |
| `[3, 2, 1]`   | `[1, 2, 3]`   | (war letzte)
| `[1, 1, 5]`   | `[1, 5, 1]`   |
| `[1, 3, 2]`   | `[2, 1, 3]`   |
| `[1, 2, 3, 4]`| `[1, 2, 4, 3]`|

## Hintergrund

Die Algorithmus stammt aus den 1960ern und ist die Grundlage von
`std::next_permutation` in C++. Damit kann man in einer Schleife
**alle Permutationen** in lexikographischer Reihenfolge erzeugen,
ohne sie alle vorab zu speichern -- $O(n)$ pro Schritt.
