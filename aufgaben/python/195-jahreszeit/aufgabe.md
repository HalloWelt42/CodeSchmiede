---
schema_version: 1
id: 195-jahreszeit
revision: 1
titel: Jahreszeit aus Monatsnummer
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags: [datum, if-else, mapping]
pfade: []
voraussetzungen: []
quelle:
  url: null
  notiz: Klassische Verzweigungs-Aufgabe
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
funktion: jahreszeit
hints:
  - kosten: 0
    text: |
      Liefere die meteorologische Jahreszeit aus einer Monatsnummer:
      12,1,2 -> "winter"
      3,4,5 -> "frühling"
      6,7,8 -> "sommer"
      9,10,11 -> "herbst"
      Ungültige Monate (< 1 oder > 12) -> "ungültig".
  - kosten: 10
    text: |
      Liste mit 12 Eintraegen oder eine if-elif-Kette nach Bereichen.
      Achtung Dezember (12) liegt im Winter wie Januar/Februar.
tests_sichtbar:
  - input: [1]
    expected: "winter"
  - input: [4]
    expected: "fruehling"
  - input: [7]
    expected: "sommer"
  - input: [10]
    expected: "herbst"
tests_versteckt:
  - input: [12]
    expected: "winter"
  - input: [2]
    expected: "winter"
  - input: [3]
    expected: "fruehling"
  - input: [5]
    expected: "fruehling"
  - input: [8]
    expected: "sommer"
  - input: [11]
    expected: "herbst"
  - input: [0]
    expected: "ungueltig"
  - input: [13]
    expected: "ungueltig"
  - input: [-1]
    expected: "ungueltig"
starter_code: |
  def jahreszeit(monat: int) -> str:
      # Deine Lösung hier -- meteorologische Definition (Dez/Jan/Feb = Winter)
      pass
---

# Jahreszeit aus Monatsnummer

Schreibe `jahreszeit(monat)`, die für eine Monatsnummer die
**meteorologische Jahreszeit** liefert (im Gegensatz zur
astronomischen, die mit den Tag-und-Nacht-Gleichen wechselt).

| Monate     | Jahreszeit    |
|------------|---------------|
| 12, 1, 2   | `"winter"`    |
| 3, 4, 5    | `"frühling"` |
| 6, 7, 8    | `"sommer"`    |
| 9, 10, 11  | `"herbst"`    |

Ungültige Monate → `"ungültig"`.

## Beispiele

| Monat | Jahreszeit    |
|-------|---------------|
| `1`   | `"winter"`    |
| `4`   | `"frühling"` |
| `7`   | `"sommer"`    |
| `10`  | `"herbst"`    |
| `12`  | `"winter"`    |
| `0`   | `"ungültig"` |
| `13`  | `"ungültig"` |

## Hintergrund

Auf der **Südhalbkugel** sind Jahreszeiten umgekehrt -- in
Australien beginnt der Sommer im Dezember. Wer eine internationale
App baut, sollte Südhalbkugel-Logik einbauen.
