---
schema_version: 1
id: f004-zaehler-bis-9
revision: 1
titel: Zähler bis 9 mit Rücksetzen
sprache: maschine
task_type: takt
runner_type: server
schwierigkeit: fortgeschritten
schwierigkeit_score: 70
schaetz_minuten: 40
tags: [schaltung, takt]
voraussetzungen: []
quelle:
  url: null
  notiz: Schaltungen mit Takt, Level 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Ohne R: wie der Zähler bis 3, nur mit vier Stellen. Jede Stelle kippt, wenn alle Stellen darunter 1 sind."
  - kosten: 2
    text: "Nach 9 (1001) kommt 0: Q1 darf dann nicht kippen, Q3 muss auf 0. Q3 bleibt 1 nur, wenn Q0 noch 0 ist (von 8 nach 9)."
  - kosten: 1
    text: "R: Jeder Eingang D bekommt zum Schluss ein UND mit NICHT R. NOR(f0, R) ist dabei schon D0."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  f0 = FF(?) @ 470,20
  f1 = FF(?) @ 470,110
  f2 = FF(?) @ 470,200
  f3 = FF(?) @ 470,290
  Q0 = f0
  Q1 = f1
  Q2 = f2
  Q3 = f3
takt:
  eingaenge: [R]
  ausgaenge: [Q3, Q2, Q1, Q0]
  bausteine: [FF, UND, ODER, XOR, NICHT, NOR]
  zahl: [Q3, Q2, Q1, Q0]
  sichtbar:
    - name: Bis 9
      takte: 12
      soll: {Q3: "000000001100", Q2: "000011110000", Q1: "001100110000", Q0: "010101010101"}
    - name: Zurück auf 0
      takte: 16
      eingaben: {R: "0000100000100000"}
      soll: {Q3: "0000000000000000", Q2: "0000100001100001", Q1: "0011000110000110", Q0: "0101001010101010"}
  versteckt:
    - name: Zweimal ganz
      takte: 22
      soll: {Q3: "0000000011000000001100", Q2: "0000111100000011110000", Q1: "0011001100001100110000", Q0: "0101010101010101010101"}
    - name: Mitten drin
      takte: 18
      eingaben: {R: "000000010010000001"}
      soll: {Q3: "000000000000000000", Q2: "000011110000000111", Q1: "001100110010011001", Q0: "010101010100101010"}
  teilschritte:
    - titel: Bis 7
      text: "Die drei unteren Stellen zählen wie ein Binärzähler: Q2 Q1 Q0 von 0 bis 7."
      ausgaenge: [Q2, Q1, Q0]
    - titel: Nach 9 kommt 0
      text: "Q3 dazu: nach 8 kommt 9, nach 9 wieder 0."
      ausgaenge: alle
    - titel: Rücksetzen
      text: "Ist R beim Takt 1, steht der Zähler danach auf 0."
      ablaeufe: [Zurück auf 0]
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe."
      ablaeufe: alle
  sterne: {bausteine: 12, tiefe: 4}
---

# Zähler bis 9 mit Rücksetzen

Ein Zähler, wie er in jeder Digitaluhr steckt: Er zählt von 0 bis 9 und fängt dann wieder bei 0 an. Vier Flipflops, Q3 ist die höchste Stelle. Dazu kommt ein Knopf R: Ist er beim Takt gedrückt, steht der Zähler danach auf 0, egal wo er war.

Der Trick ist die 9. Ein gewöhnlicher Binärzähler würde nach 1001 bei 1010 weitermachen. Deiner muss an genau dieser Stelle auf 0000 springen, und dafür musst du herausfinden, welche Stellen sich dann anders verhalten als sonst.
