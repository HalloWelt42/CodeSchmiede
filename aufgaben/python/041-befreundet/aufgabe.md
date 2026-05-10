---
schema_version: 1
id: 041-befreundet
revision: 1
titel: Befreundete Zahlen
sprache: python
task_type: code_schreiben
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 16
schaetz_minuten: 9
tags: [zahlen, teiler, hilfsfunktion]
pfade: [python_mathe2]
voraussetzungen: [040-perfekte-zahl]
quelle:
  url: https://de.wikipedia.org/wiki/Befreundete_Zahlen
  notiz: Klassische Zahlentheorie
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-10
zeitlimit_sekunden: 5
funktion: sind_befreundet
hints:
  - kosten: 0
    text: |
      Berechne die Summe der echten Teiler von a -- nenn das `s(a)`.
      Genauso `s(b)`. Die Zahlen sind befreundet, wenn `s(a) == b` und
      `s(b) == a` -- und beide verschieden sind.
  - kosten: 15
    text: |
      Hilfsfunktion `teiler_summe(n)` schreiben, dann zwei Aufrufe.
tests_sichtbar:
  - input: [220, 284]
    expected: true
  - input: [284, 220]
    expected: true
  - input: [10, 12]
    expected: false
  - input: [6, 6]
    expected: false
tests_versteckt:
  - input: [1184, 1210]
    expected: true
  - input: [2620, 2924]
    expected: true
  - input: [220, 285]
    expected: false
  - input: [1, 1]
    expected: false
  - input: [1, 2]
    expected: false
starter_code: |
  def sind_befreundet(a: int, b: int) -> bool:
      # Deine Loesung hier -- Hilfsfunktion fuer Teilersumme erlaubt.
      pass
---

# Befreundete Zahlen

Zwei Zahlen `a` und `b` heissen **befreundet**, wenn:

- `a != b`
- die Summe der echten Teiler von `a` **gleich** `b` ist
- die Summe der echten Teiler von `b` **gleich** `a` ist

Schreibe eine Funktion `sind_befreundet(a, b)`, die das prueft.

## Beispiele

| `a`   | `b`   | Befreundet? | Hintergrund                              |
|-------|-------|-------------|------------------------------------------|
| `220` | `284` | `True`      | klassisches Paar -- seit Pythagoras bekannt |
| `1184`| `1210`| `True`      | erst Anfang 19. Jh. entdeckt -- vom 16-Jaehrigen Niccolo Paganini! |
| `10`  | `12`  | `False`     |                                          |
| `6`   | `6`   | `False`     | gleich -- nicht erlaubt                  |

## Hintergrund

Das Paar `(220, 284)` war den Pythagoreern als Symbol der Freundschaft
bekannt -- sie sahen darin etwas Mystisches. Bis ins 18. Jh. waren nur
zwei oder drei Paare bekannt; heute sind es ueber **eine Milliarde**.
Niccolo Paganini (nicht der Geiger -- ein Sechzehnjaehriger) entdeckte
1866 das Paar `(1184, 1210)`, das jahrhundertelang allen entgangen war.

## Tipp

Eine Hilfsfunktion `teiler_summe(n)` fuer die Summe der echten Teiler
spart Tipparbeit -- ist aber kein Muss.
