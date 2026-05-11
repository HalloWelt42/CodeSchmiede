---
schema_version: 1
id: 222-alle-gleich
revision: 1
titel: Alle Elemente gleich?
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [listen, vergleich, set]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Listen-Prüfung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: alle_gleich
hints:
  - kosten: 0
    text: |
      Liefere True, wenn ALLE Elemente in der Liste gleich sind.
      Leere Liste → True (vacuous truth).
      Ein Element → True.
  - kosten: 10
    text: |
      len(set(liste)) <= 1.
      Oder: all(x == liste[0] for x in liste).
tests_sichtbar:
  - input: [[1, 1, 1]]
    expected: true
  - input: [[1, 2, 3]]
    expected: false
  - input: [[]]
    expected: true
  - input: [[5]]
    expected: true
tests_versteckt:
  - input: [["a", "a", "a", "a"]]
    expected: true
  - input: [["a", "A"]]
    expected: false
  - input: [[true, true, true]]
    expected: true
  - input: [[1, 1, 1, 2]]
    expected: false
  - input: [[null, null]]
    expected: true
  - input: [[1.0, 1.0, 1.0]]
    expected: true
  - input: [[0, 0.0]]
    expected: true
starter_code: |
  def alle_gleich(liste: list) -> bool:
      # Deine Lösung hier -- leere Liste -> True
      pass
---

# Alle Elemente gleich?

Schreibe `alle_gleich(liste)`, die `True` zurückgibt, wenn alle
Elemente in der Liste **gleich** sind. Leere Liste → `True`.

## Beispiele

| Liste              | Alle gleich? |
|--------------------|--------------|
| `[1, 1, 1]`        | `True`       |
| `[1, 2, 3]`        | `False`      |
| `[]`               | `True`       |
| `[5]`              | `True`       |
| `["a", "a", "a"]`  | `True`       |
| `["a", "A"]`       | `False`      |
| `[0, 0.0]`         | `True` (Wert-gleich, Typ egal) |

## Idee 1 -- Set-Trick

Wenn das Set höchstens **ein Element** hat, sind alle gleich (oder
es gibt keine).

## Idee 2 -- All mit Vergleich

Spart die Set-Konstruktion -- bei sehr großen Listen mit vielen
unterschiedlichen Werten ein **Short-Circuit**: bricht beim ersten
Mismatch ab.

## Stolperstein -- Hashbarkeit

`set(liste)` setzt voraus, dass alle Elemente **hashbar** sind --
bei Listen oder Dicts in der Liste schlaegt das fehl. Idee 2 hat
diese Einschraenkung nicht.

## Mathematische Subtilitaet -- Vacuous Truth

Aussage "Für alle x in der leeren Menge gilt P(x)" ist immer wahr,
weil es kein Gegenbeispiel gibt. Darum `[]` → `True`.
