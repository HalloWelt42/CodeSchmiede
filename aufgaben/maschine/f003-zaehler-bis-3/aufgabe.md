---
schema_version: 1
id: f003-zaehler-bis-3
revision: 1
titel: Zähler bis 3
sprache: maschine
task_type: takt
runner_type: server
schwierigkeit: mittel
schwierigkeit_score: 40
schaetz_minuten: 20
tags: [schaltung, takt]
voraussetzungen: []
quelle:
  url: null
  notiz: Schaltungen mit Takt, Level 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Q0 kippt bei jedem Takt: D0 ist das Gegenteil von Q0."
  - kosten: 2
    text: "Q1 kippt genau dann, wenn Q0 gerade 1 ist. Das ist der Umschalter aus dem letzten Level, mit Q0 als Taste."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  f0 = FF(?) @ 260,40
  f1 = FF(?) @ 260,170
  Q0 = f0
  Q1 = f1
takt:
  ausgaenge: [Q1, Q0]
  bausteine: [FF, UND, ODER, XOR, NICHT]
  zahl: [Q1, Q0]
  sichtbar:
    - name: Zählen
      takte: 8
      soll: {Q1: "00110011", Q0: "01010101"}
  versteckt:
    - name: Lange
      takte: 14
      soll: {Q1: "00110011001100", Q0: "01010101010101"}
  teilschritte:
    - titel: Q0 kippt
      text: "Bei jedem Takt wechselt Q0: 0, 1, 0, 1."
      ausgaenge: [Q0]
    - titel: Der Übertrag
      text: "Q1 wechselt genau dann, wenn Q0 gerade 1 ist."
      ausgaenge: alle
    - titel: Lange zählen
      text: "Zum Schluss ein längerer, versteckter Ablauf."
      ablaeufe: alle
  sterne: {bausteine: 2, tiefe: 1}
---

# Zähler bis 3

Zwei Flipflops, und die Schaltung kann zählen. Q1 und Q0 sind zusammen eine Binärzahl: 00 ist 0, 01 ist 1, 10 ist 2, 11 ist 3. Bei jedem Takt soll sie eins weiter zählen und nach 3 wieder bei 0 anfangen.

Kein Eingang, nur der Takt. Schau auf die Einerstelle: die wechselt immer. Und die Zweierstelle? Wechselt genau dann, wenn es einen Übertrag gibt. Klingt nach schriftlichem Addieren, ist es auch.
