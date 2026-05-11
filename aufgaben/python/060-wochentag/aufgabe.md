---
schema_version: 1
id: 060-wochentag
revision: 1
titel: Wochentag mit Zeller-Formel
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 22
schaetz_minuten: 15
tags: [zahlen, datum, formel]
pfade: [python_datum]
voraussetzungen: [059-monatstage]
quelle:
  url: https://de.wikipedia.org/wiki/Zellers_Kongruenz
  notiz: Klassische Datums-Formel von Christian Zeller, 1882
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: wochentag
hints:
  - kosten: 0
    text: |
      Zeller-Formel: ein direkter Weg zum Wochentag. Zählweise:
      0 = Sonntag, 1 = Montag, ..., 6 = Samstag.
  - kosten: 15
    text: |
      Trick: Januar und Februar zählen als Monat 13 und 14 des
      **Vorjahres**.

      ```
      if monat < 3:
          monat += 12
          jahr -= 1
      k = jahr % 100
      j = jahr // 100
      h = (tag + (13*(monat+1))//5 + k + k//4 + j//4 + 5*j) % 7
      ```

      `h = 0` ist Samstag in Zellers Original. Wir wandeln in
      0=So..6=Sa um: `(h + 6) % 7`.
tests_sichtbar:
  - input: [2026, 5, 10]
    expected: 0
  - input: [2024, 1, 1]
    expected: 1
  - input: [2000, 2, 29]
    expected: 2
  - input: [1969, 7, 20]
    expected: 0
tests_versteckt:
  - input: [2025, 12, 25]
    expected: 4
  - input: [2026, 1, 1]
    expected: 4
  - input: [1989, 11, 9]
    expected: 4
  - input: [1582, 10, 15]
    expected: 5
starter_code: |
  def wochentag(jahr: int, monat: int, tag: int) -> int:
      # Deine Lösung hier -- 0=Sonntag, 1=Montag, ..., 6=Samstag.
      pass
---

# Wochentag mit Zeller-Formel

Schreibe eine Funktion `wochentag(jahr, monat, tag)`, die den Wochentag
für ein Datum im Gregorianischen Kalender zurückgibt.

Konvention: **`0 = Sonntag, 1 = Montag, ..., 6 = Samstag`**.

## Beispiele

| Datum         | Wochentag     | Code |
|---------------|---------------|------|
| 10. Mai 2026  | Sonntag       | `0`  |
| 1. Jan 2024   | Montag        | `1`  |
| 25. Dez 2025  | Donnerstag    | `4`  |
| 9. Nov 1989   | Donnerstag    | `4`  |
| 20. Juli 1969 | Sonntag       | `0`  |
| 15. Okt 1582  | Freitag       | `5`  |

## Zellers Formel

Ein eleganter Trick von Christian Zeller (1882): Januar und Februar
behandelt man als 13. und 14. Monat des **Vorjahres**.

$$
h = \left(q + \left\lfloor \tfrac{13(m+1)}{5} \right\rfloor + K + \left\lfloor \tfrac{K}{4} \right\rfloor + \left\lfloor \tfrac{J}{4} \right\rfloor + 5J \right) \mod 7
$$

mit $q$ = Tag, $m$ = (gezogener) Monat, $K = \text{jahr} \mod 100$,
$J = \text{jahr} \div 100$.

In Zellers Konvention ist $h = 0$ Samstag. Wir wollen Sonntag = 0,
also `(h + 6) % 7`.

## Hintergrund

Pythons `datetime.date(jahr, monat, tag).weekday()` macht das natuerlich
auch -- liefert aber `0 = Montag`. Hier geht es darum, die Formel
selbst zu programmieren.
