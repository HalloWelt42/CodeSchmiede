---
schema_version: 1
id: 254-tag-im-jahr
revision: 1
titel: Tag-Nummer im Jahr aus Datum
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 18
schaetz_minuten: 8
tags: [datum, mathematik, schaltjahr]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Datums-Berechnung
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: tag_im_jahr
hints:
  - kosten: 0
    text: |
      Bestimme den n-ten Tag des Jahres aus (jahr, monat, tag).
      1. Januar → 1. 31. Dezember (kein Schaltjahr) → 365.
      Schaltjahre bei Februar beachten!
      Ungültige Eingaben → 0.
  - kosten: 12
    text: |
      datetime.date(jahr, monat, tag).timetuple().tm_yday liefert es direkt.
      Manuell: Tage-pro-Monat-Liste, Schaltjahr für Februar +1.
tests_sichtbar:
  - input: [2026, 1, 1]
    expected: 1
  - input: [2026, 12, 31]
    expected: 365
  - input: [2024, 12, 31]
    expected: 366
  - input: [2026, 5, 11]
    expected: 131
tests_versteckt:
  - input: [2026, 2, 28]
    expected: 59
  - input: [2026, 3, 1]
    expected: 60
  - input: [2024, 2, 29]
    expected: 60
  - input: [2024, 3, 1]
    expected: 61
  - input: [2026, 7, 4]
    expected: 185
  - input: [2026, 11, 30]
    expected: 334
  - input: [2026, 13, 1]
    expected: 0
  - input: [2026, 0, 5]
    expected: 0
starter_code: |
  from datetime import date

  def tag_im_jahr(jahr: int, monat: int, tag: int) -> int:
      # Deine Lösung hier -- ungueltig → 0
      pass
---

# Tag-Nummer im Jahr aus Datum

Schreibe `tag_im_jahr(jahr, monat, tag)`, die für ein Datum die
**laufende Tag-Nummer im Jahr** zurückgibt (1.-365., bei
Schaltjahr 1.-366.).

Bei ungültigen Eingaben → `0`.

## Beispiele

| Datum      | Tag-Nr | Bemerkung           |
|------------|--------|---------------------|
| 2026-01-01 | `1`    | Neujahr             |
| 2026-05-11 | `131`  | heute               |
| 2026-12-31 | `365`  | Silvester (kein SJ) |
| 2024-12-31 | `366`  | Schaltjahr          |
| 2024-02-29 | `60`   | Schalttag           |
| 2024-03-01 | `61`   | nach Schalttag      |
| 2026-13-01 | `0`    | ungültiger Monat   |

## Idee mit `datetime`

`date(...)` validiert automatisch (z.B. `date(2026, 13, 1)` wirft
einen `ValueError`). `tm_yday` ist genau der "day of year".

## Idee ohne `datetime`

Komplizierter, aber lehrreich -- enthält die **Gregorianische
Schaltjahr-Regel** (Aufgabe 058).

## Anwendung

- Tag-genaue Daten-Indexierung in Zeitreihen.
- Astronomie: Julianisches Datum.
- Kalender-Apps: "Heute ist der x. Tag des Jahres".
