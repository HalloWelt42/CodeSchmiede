---
schema_version: 1
id: 059-monatstage
revision: 1
titel: Tage im Monat
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [zahlen, if-else, datum, listen]
pfade: [python_datum]
voraussetzungen: [058-schaltjahr]
quelle:
  url: null
  notiz: Klassisches Datums-Beispiel
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: tage_im_monat
hints:
  - kosten: 0
    text: |
      Lookup-Tabelle: Index = Monat (1-12), Wert = Tage. Februar
      separat behandeln, abhängig vom Schaltjahr.
  - kosten: 8
    text: |
      Wenn Monat außerhalb 1-12, gib 0 zurück (kein Crash).
tests_sichtbar:
  - input: [2024, 2]
    expected: 29
  - input: [2023, 2]
    expected: 28
  - input: [2026, 5]
    expected: 31
  - input: [2026, 4]
    expected: 30
tests_versteckt:
  - input: [2026, 12]
    expected: 31
  - input: [2026, 1]
    expected: 31
  - input: [2000, 2]
    expected: 29
  - input: [1900, 2]
    expected: 28
  - input: [2026, 0]
    expected: 0
  - input: [2026, 13]
    expected: 0
starter_code: |
  def tage_im_monat(jahr: int, monat: int) -> int:
      # Deine Lösung hier -- 0 bei ungueltigem Monat.
      pass
---

# Tage im Monat

Schreibe eine Funktion `tage_im_monat(jahr, monat)`, die die Anzahl
der Tage im gegebenen Monat zurückgibt.

| Monat                   | Tage     |
|-------------------------|----------|
| Januar, März, Mai, Juli, August, Oktober, Dezember | 31 |
| April, Juni, September, November                    | 30 |
| Februar (Schaltjahr)                                | 29 |
| Februar (sonst)                                     | 28 |

Bei einem Monat außerhalb von 1-12 gib `0` zurück.

## Beispiele

| Jahr  | Monat | Tage |
|-------|-------|------|
| 2024  | 2     | 29   |
| 2023  | 2     | 28   |
| 2026  | 5     | 31   |
| 2026  | 4     | 30   |
| 2026  | 13    | 0    |

## Idee

Liste mit den Standard-Tagen, dann Februar-Sonderfall. Schaltjahrs-
Logik kommt aus der vorherigen Aufgabe.
