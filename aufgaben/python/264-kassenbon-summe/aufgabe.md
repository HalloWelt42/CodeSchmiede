---
schema_version: 1
id: 264-kassenbon-summe
revision: 1
titel: Kassenbon-Summe berechnen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [listen, schleifen, runden, geld]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Geld-Berechnung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: bon_summe
hints:
  - kosten: 0
    text: |
      Liste von [name, anzahl, einzelpreis]-Tripeln.
      Summe = sum(anzahl * einzelpreis).
      Auf 2 Nachkommastellen gerundet.
      Leere Liste → 0.0.
  - kosten: 8
    text: |
      sum(z[1] * z[2] for z in posten) und round(..., 2).
tests_sichtbar:
  - input: [[["Apfel", 3, 0.5], ["Brot", 1, 2.0]]]
    expected: 3.5
  - input: [[]]
    expected: 0.0
  - input: [[["Eis", 2, 1.5]]]
    expected: 3.0
  - input: [[["Wasser", 6, 1.0]]]
    expected: 6.0
tests_versteckt:
  - input: [[["A", 1, 1.0], ["B", 2, 2.0], ["C", 3, 3.0]]]
    expected: 14.0
  - input: [[["Milch", 1, 1.29], ["Brot", 1, 2.49], ["Butter", 1, 2.79]]]
    expected: 6.57
  - input: [[["Sale", 5, 9.99]]]
    expected: 49.95
  - input: [[["Free", 0, 100.0]]]
    expected: 0.0
  - input: [[["Bug", 1, -10.0], ["Pay", 1, 20.0]]]
    expected: 10.0
  - input: [[["Item", 100, 0.01]]]
    expected: 1.0
starter_code: |
  def bon_summe(posten: list[list]) -> float:
      # Deine Lösung hier -- 2 Nachkommastellen
      pass
---

# Kassenbon-Summe berechnen

Schreibe `bon_summe(posten)`, die für eine Liste von Kassenbon-
Posten die **Gesamtsumme** berechnet. Jeder Posten ist
`[name, anzahl, einzelpreis]`. Liefere auf **2 Nachkommastellen**
gerundet.

Bei leerer Liste → `0.0`.

## Beispiele

| Posten                                       | Summe |
|----------------------------------------------|-------|
| `[["Apfel", 3, 0.5], ["Brot", 1, 2.0]]`      | `3.5` |
| `[["Eis", 2, 1.5]]`                          | `3.0` |
| `[["Milch", 1, 1.29], ["Brot", 1, 2.49], ["Butter", 1, 2.79]]` | `6.57` |
| `[["Sale", 5, 9.99]]`                        | `49.95` |
| `[]`                                         | `0.0` |

## Idee

Generator-Expression in `sum`. Pro Posten: `anzahl * einzelpreis`.

## Float-Stolperstein

Mit Floats kann **Rundungs-Drift** entstehen:

Für **echte Geld-Anwendungen** sollte man `decimal.Decimal` nutzen
oder in **Cent-Ints** rechnen (`299` statt `2.99`). Pythons `round`
hilft, gibt aber keine Garantie auf perfekte Praezision.

## Erweiterung

Eine richtige Bon-Berechnung haette zusaetzlich:
- **MwSt** pro Posten (7% / 19% in DE).
- **Rabatte** (prozentual oder absolut).
- **Pfand**-Posten (separate Reihe).
- **Rundung** auf 5-Cent (in Schweiz).
