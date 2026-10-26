---
schema_version: 1
id: d005-multiplexer
revision: 1
titel: Multiplexer
sprache: maschine
task_type: schaltung
runner_type: server
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 20
tags: [schaltung]
voraussetzungen: []
quelle:
  url: null
  notiz: Digitale Schaltungen, Level 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "A darf nur durch, wenn W = 0 ist: UND mit NICHT W. Für B entsprechend mit W."
  - kosten: 2
    text: "Am Ende beide Wege mit ODER zusammenführen."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  Y = ?
schaltung:
  eingaenge: [W, A, B]
  ausgaenge: [Y]
  bausteine: [UND, ODER, NICHT]
  soll:
    Y: "00110101"
  teilschritte:
    - titel: Die Weiche
      text: "Ist W = 0, kommt A durch, ist W = 1, kommt B durch."
      ausgaenge: alle
  sterne: {bausteine: 4, tiefe: 3}
---

# Multiplexer

Ein Multiplexer ist eine Weiche für Bits: der Wahleingang W entscheidet, welcher der beiden Eingänge A und B am Ausgang Y ankommt. So sucht ein Rechenwerk aus, mit welchen Daten es weiterrechnet.
