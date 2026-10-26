---
schema_version: 1
id: d003-halbaddierer
revision: 1
titel: Halbaddierer
sprache: maschine
task_type: schaltung
runner_type: server
schwierigkeit: anfaenger
schwierigkeit_score: 20
schaetz_minuten: 15
tags: [schaltung]
voraussetzungen: []
quelle:
  url: null
  notiz: Digitale Schaltungen, Level 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "XOR ist 1, wenn genau einer seiner Eingänge 1 ist: genau die Einerstelle."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  x1 = XOR(?, ?) @ 230,40
  u1 = UND(?, ?) @ 230,170
  S = ?
  C = ?
schaltung:
  eingaenge: [A, B]
  ausgaenge: [S, C]
  bausteine: [UND, ODER, XOR, NICHT]
  vorgabe:
    - {name: x1, art: XOR, x: 230, y: 40}
    - {name: u1, art: UND, x: 230, y: 170}
  soll:
    S: "0110"
    C: "0001"
  teilschritte:
    - titel: Die Summe S
      text: "S ist 1, wenn genau eins von A und B 1 ist."
      ausgaenge: [S]
    - titel: Der Übertrag C
      text: "C ist 1, wenn A und B beide 1 sind."
      ausgaenge: alle
  sterne: {bausteine: 2, tiefe: 1}
---

# Halbaddierer

Zwei Bits A und B sollen addiert werden. Das Ergebnis hat zwei Stellen: S ist die Einerstelle, C der Übertrag. 1 + 1 ergibt also S = 0 und C = 1, binär 10.

Die Bausteine stehen schon, du verdrahtest sie nur.
