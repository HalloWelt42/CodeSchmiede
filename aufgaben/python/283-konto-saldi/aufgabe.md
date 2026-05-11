---
schema_version: 1
id: 283-konto-saldi
revision: 1
titel: Konto-Saldi nach jeder Buchung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 6
tags: [oop, klassen, listen, schleifen]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: OOP-Klasse intern, API liefert Daten
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: konto_saldi
hints:
  - kosten: 0
    text: |
      Liefere die Liste der Saldi nach jeder Buchung.
      start = Anfangs-Saldo, buchungen = Liste von Betraegen (+/-).
      Beispiel: start=100, buchungen=[10, -30, 50] → [110, 80, 130].
      Bei buchungen == [] → [].
  - kosten: 15
    text: |
      Klasse Konto mit __init__(saldo) und buchen(betrag).
      Funktion erzeugt Konto, ruft für jede Buchung buchen() auf,
      sammelt saldo nach jeder Buchung.
tests_sichtbar:
  - input: [100, [10, -30, 50]]
    expected: [110, 80, 130]
  - input: [0, []]
    expected: []
  - input: [50, [-50]]
    expected: [0]
  - input: [0, [100]]
    expected: [100]
tests_versteckt:
  - input: [1000, [100, 100, 100]]
    expected: [1100, 1200, 1300]
  - input: [-50, [100]]
    expected: [50]
  - input: [0, [1, 2, 3, 4, 5]]
    expected: [1, 3, 6, 10, 15]
  - input: [500, [-100, -100, -100, -100, -100]]
    expected: [400, 300, 200, 100, 0]
  - input: [1000000, [-1]]
    expected: [999999]
  - input: [0, [0, 0, 0]]
    expected: [0, 0, 0]
starter_code: |
  def konto_saldi(start: int, buchungen: list[int]) -> list[int]:
      # Tipp: nutze intern eine Konto-Klasse
      pass
---

# Konto-Saldi nach jeder Buchung

Schreibe `konto_saldi(start, buchungen)`, die für einen Anfangs-
Saldo und eine Liste von Buchungen (positiv = Einzahlung, negativ =
Auszahlung) den **Saldo nach jeder einzelnen Buchung** liefert.

Bei leerer Buchungsliste → `[]`.

## Beispiele

| start | buchungen        | Saldi             |
|-------|------------------|-------------------|
| 100   | `[10, -30, 50]`  | `[110, 80, 130]`  |
| 0     | `[1, 2, 3, 4, 5]`| `[1, 3, 6, 10, 15]` |
| 50    | `[-50]`          | `[0]`             |
| 1000  | `[100, 100, 100]`| `[1100, 1200, 1300]` |

## Idee -- mit interner Klasse

Die Klasse haelt den Zustand (`self.saldo`), die Methode mutiert
ihn und liefert den neuen Wert -- das ist klassisches OOP.

## Idee -- ohne Klasse (procedural)

Genauso korrekt, kürzer. Die OOP-Variante zeigt aber, wie man
**Zustand kapseln** kann -- was bei mehreren Konten oder zusaetzlichen
Methoden (Zinsen, Sperre, Limit) sehr schnell hilfreich wird.

## Pattern -- Akkumulator als Klasse

Wenn du in den nächsten Aufgaben **mehrere Operationen** auf dem
gleichen Zustand brauchst, ist eine Klasse fast immer der bessere
Container als lose Variablen.
