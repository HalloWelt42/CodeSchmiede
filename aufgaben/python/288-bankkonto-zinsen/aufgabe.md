---
schema_version: 1
id: 288-bankkonto-zinsen
revision: 1
titel: Bankkonto mit Zinsbuchung
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 28
schaetz_minuten: 12
tags: [oop, klassen, geld, runden]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: OOP mit zwei Methoden + Zustand
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: jahres_endsaldi
hints:
  - kosten: 0
    text: |
      Klasse Bankkonto: start-Saldo, jaehrlicher Zinssatz (in Prozent).
      Methoden: einzahlen(b), abheben(b), zinsen_buchen() (Zinsen auf
      aktuellen Saldo addieren).
      Funktion jahres_endsaldi(start, zins, jahre) → Liste der
      Endsaldi nach jedem Jahr (nur Zinsen, keine Bewegungen).
      Auf 2 Nachkommastellen.
  - kosten: 20
    text: |
      Konto-Klasse implementieren, dann Funktion wrappen:
      Pro Jahr zinsen_buchen aufrufen, runden, sammeln.
tests_sichtbar:
  - input: [1000, 5, 1]
    expected: [1050.0]
  - input: [1000, 5, 2]
    expected: [1050.0, 1102.5]
  - input: [1000, 0, 3]
    expected: [1000.0, 1000.0, 1000.0]
  - input: [0, 5, 5]
    expected: [0.0, 0.0, 0.0, 0.0, 0.0]
tests_versteckt:
  - input: [100, 10, 5]
    expected: [110.0, 121.0, 133.1, 146.41, 161.05]
  - input: [10000, 3, 4]
    expected: [10300.0, 10609.0, 10927.27, 11255.09]
  - input: [500, 2.5, 3]
    expected: [512.5, 525.31, 538.45]
  - input: [1000, 100, 4]
    expected: [2000.0, 4000.0, 8000.0, 16000.0]
  - input: [1000, 5, 0]
    expected: []
  - input: [1000, -5, 2]
    expected: [950.0, 902.5]
starter_code: |
  def jahres_endsaldi(start: float, zinssatz_prozent: float, jahre: int) -> list[float]:
      # Tipp: Bankkonto-Klasse mit zinsen_buchen-Methode intern
      pass
---

# Bankkonto mit Zinsbuchung

Implementiere `jahres_endsaldi(start, zinssatz_prozent, jahre)` --
ein Bankkonto startet mit `start` Euro, wird **jaehrlich** mit
`zinssatz_prozent` verzinst. Liefere den **Endsaldo nach jedem Jahr**
als Liste, **auf 2 Nachkommastellen** gerundet.

Bei `jahre <= 0` → `[]`. Negative Zinsen funktionieren (Strafzinsen).

## Beispiele

| Start | Zins | Jahre | Endsaldi                                |
|-------|------|-------|------------------------------------------|
| 1000  | 5%   | 1     | `[1050.0]`                              |
| 1000  | 5%   | 2     | `[1050.0, 1102.5]`                      |
| 100   | 10%  | 5     | `[110, 121, 133.1, 146.41, 161.05]`     |
| 1000  | 100% | 4     | `[2000, 4000, 8000, 16000]`             |
| 1000  | 0%   | 3     | `[1000, 1000, 1000]`                    |
| 1000  | -5%  | 2     | `[950, 902.5]`                          |

## Idee -- Klasse mit Zinsen-Methode

```python
class Bankkonto:
    def __init__(self, saldo, zinssatz):
        self.saldo = saldo
        self.zinssatz = zinssatz / 100  # in Dezimal

    def zinsen_buchen(self):
        self.saldo += self.saldo * self.zinssatz
        return self.saldo


def jahres_endsaldi(start, zinssatz_prozent, jahre):
    konto = Bankkonto(start, zinssatz_prozent)
    return [round(konto.zinsen_buchen(), 2) for _ in range(jahre)]
```

## Vergleich mit Aufgabe 160

Aufgabe **160-zinseszins** liefert nur den **End-Wert** nach n Jahren.
Hier liefern wir die **Verlaufs-Liste** -- gut für Charts und
"Was-wenn"-Simulationen.

## Erweiterung -- Mit Bewegungen

Eine echte Bankkonto-Klasse haette zusaetzlich `einzahlen(betrag)`
und `abheben(betrag)`. Mit der Liste der Bewegungen könnte man
realistische Zins-Verlaeufe simulieren -- ist aber Stoff für eine
eigene, komplexere Aufgabe.

## Hintergrund -- Banker's Rounding

`round(1102.5, 0)` ist in Python `1102` (zur **geraden** Zahl). Bei
**.50**-Cent-Rundungen kann das zu Verwirrung fuehren. In der
realen Bank-Mathematik nimmt man oft `decimal.Decimal` mit
explizitem Rounding-Modus.
