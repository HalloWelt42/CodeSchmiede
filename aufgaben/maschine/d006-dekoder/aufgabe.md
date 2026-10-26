---
schema_version: 1
id: d006-dekoder
revision: 1
titel: Dekoder
sprache: maschine
task_type: schaltung
runner_type: server
schwierigkeit: mittel
schwierigkeit_score: 35
schaetz_minuten: 20
tags: [schaltung]
voraussetzungen: []
quelle:
  url: null
  notiz: Digitale Schaltungen, Level 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "NOR ist 1, wenn beide Eingänge 0 sind: genau Y0."
  - kosten: 2
    text: "Für Y1 brauchst du NICHT A und B."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  Y0 = ?
  Y1 = ?
  Y2 = ?
  Y3 = ?
schaltung:
  eingaenge: [A, B]
  ausgaenge: [Y0, Y1, Y2, Y3]
  bausteine: [UND, NICHT, NOR]
  soll:
    Y0: "1000"
    Y1: "0100"
    Y2: "0010"
    Y3: "0001"
  teilschritte:
    - titel: Die Ränder
      text: "Y0 leuchtet bei A = 0, B = 0, Y3 bei A = 1, B = 1."
      ausgaenge: [Y0, Y3]
    - titel: Dazwischen
      text: "Y1 bei 01, Y2 bei 10: immer genau ein Lämpchen."
      ausgaenge: alle
  sterne: {bausteine: 6, tiefe: 2}
---

# Dekoder

A und B bilden zusammen eine Zahl von 0 bis 3 (A ist die Zweierstelle). Der Dekoder hat vier Ausgänge Y0 bis Y3, und es leuchtet immer genau der, dessen Nummer anliegt. So wählt ein Speicher aus, welche Zelle gemeint ist.
