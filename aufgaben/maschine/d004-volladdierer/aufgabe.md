---
schema_version: 1
id: d004-volladdierer
revision: 1
titel: Volladdierer
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
  notiz: Digitale Schaltungen, Level 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Zwei Halbaddierer hintereinander: erst A und B, dann das Ergebnis mit Ci."
  - kosten: 2
    text: "Einen Übertrag gibt es, wenn einer der beiden Halbaddierer einen hat: ein ODER."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  S = ?
  Co = ?
schaltung:
  eingaenge: [A, B, Ci]
  ausgaenge: [S, Co]
  bausteine: [UND, ODER, XOR]
  soll:
    S: "01101001"
    Co: "00010111"
  teilschritte:
    - titel: Die Summe
      text: "S ist die Einerstelle von A + B + Ci."
      ausgaenge: [S]
    - titel: Der Übertrag
      text: "Co ist 1, wenn mindestens zwei der drei Eingänge 1 sind."
      ausgaenge: alle
  sterne: {bausteine: 5, tiefe: 3}
---

# Volladdierer

Der Volladdierer addiert drei Bits: A, B und den Übertrag Ci aus der Stelle davor. Heraus kommen die Summe S und der neue Übertrag Co. Hängt man vier davon hintereinander, addiert die Schaltung ganze Zahlen.

Diesmal stehen keine Bausteine bereit.
