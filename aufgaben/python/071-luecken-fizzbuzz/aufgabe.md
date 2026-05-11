---
schema_version: 1
id: 071-luecken-fizzbuzz
revision: 1
titel: Lückentext -- Mini-FizzBuzz
sprache: python
task_type: lueckentext
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [lueckentext, modulo, if-else]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Erste Lückentext-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: drei_oder_fuenf
hints:
  - kosten: 0
    text: Lücke 1 ist der Modulo-Operator, Lücke 2 die Zahl 5.
  - kosten: 10
    text: |
      Lösung -- Lücke 1 = `%`, Lücke 2 = `5`, Lücke 3 = `"beides"`,
      Lücke 4 = `"keines"`.
tests_sichtbar:
  - input: [15]
    expected: "beides"
  - input: [9]
    expected: "drei"
  - input: [25]
    expected: "fuenf"
  - input: [7]
    expected: "keines"
tests_versteckt:
  - input: [30]
    expected: "beides"
  - input: [21]
    expected: "drei"
  - input: [50]
    expected: "fuenf"
  - input: [11]
    expected: "keines"
  - input: [0]
    expected: "beides"
lueckentext:
  template: |
    def drei_oder_fuenf(n):
        if n ___1___ 3 == 0 and n ___1___ ___2___ == 0:
            return ___3___
        if n ___1___ 3 == 0:
            return "drei"
        if n ___1___ ___2___ == 0:
            return "fuenf"
        return ___4___
  luecken:
    - nummer: 1
      hinweis: "Operator -- liefert den Rest der Division"
    - nummer: 2
      hinweis: "Zahl"
    - nummer: 3
      hinweis: "Zeichenkette in Anführungszeichen"
    - nummer: 4
      hinweis: "Zeichenkette in Anführungszeichen"
---

# Lückentext -- Mini-FizzBuzz

Eine vereinfachte Variante: gibt `"drei"`, `"fuenf"` oder `"beides"`
zurück, je nachdem ob `n` durch 3, durch 5, oder durch beides
teilbar ist. Wenn nichts passt: `"keines"`.

## Beispiele

| `n` | Ergebnis  |
|-----|-----------|
| 15  | `"beides"`|
| 9   | `"drei"`  |
| 25  | `"fuenf"` |
| 7   | `"keines"`|

## Hinweis

Der Code im Editor hat **vier Lücken** (`___1___` bis `___4___`).
Fuelle sie passend aus -- die gleiche Nummer kommt mehrfach vor und
soll identisch ersetzt werden.
