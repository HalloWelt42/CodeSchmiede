---
schema_version: 1
id: d007-xor-aus-nand
revision: 1
titel: XOR nur aus NAND
sprache: maschine
task_type: schaltung
runner_type: server
schwierigkeit: fortgeschritten
schwierigkeit_score: 40
schaetz_minuten: 25
tags: [schaltung]
voraussetzungen: []
quelle:
  url: null
  notiz: Digitale Schaltungen, Level 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Fang mit NAND(A, B) an und füttere das Ergebnis zusammen mit A und mit B in zwei weitere NAND."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  X = ?
schaltung:
  eingaenge: [A, B]
  ausgaenge: [X]
  bausteine: [NAND]
  soll:
    X: "0110"
  teilschritte:
    - titel: Nur NAND
      text: "X ist 1, wenn genau einer von A und B 1 ist, gebaut nur aus NAND."
      ausgaenge: alle
  sterne: {bausteine: 4, tiefe: 3}
---

# XOR nur aus NAND

NAND ist ein Alleskönner: aus ihm allein lässt sich jede Schaltung bauen. Hier das XOR, mit nichts als NAND-Bausteinen.

Mit vier geht es. Wer es mit weniger schafft, hat einen Fehler in der Wahrheitstabelle.
