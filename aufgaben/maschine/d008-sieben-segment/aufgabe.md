---
schema_version: 1
id: d008-sieben-segment
revision: 1
titel: 7-Segment-Anzeige von 0 bis 3
sprache: maschine
task_type: schaltung
runner_type: server
schwierigkeit: fortgeschritten
schwierigkeit_score: 50
schaetz_minuten: 30
tags: [schaltung]
voraussetzungen: []
quelle:
  url: null
  notiz: Digitale Schaltungen, Level 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Schreib dir für jedes Segment auf, bei welchen Ziffern es leuchtet. Einige sind gleich, andere ganz einfach."
  - kosten: 2
    text: "e leuchtet bei 0 und 2: genau dann, wenn B = 0 ist."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  a = ?
  b = ?
  c = ?
  d = ?
  e = ?
  f = ?
  g = ?
schaltung:
  eingaenge: [A, B]
  ausgaenge: [a, b, c, d, e, f, g]
  bausteine: [UND, ODER, NICHT, NOR]
  soll:
    a: "1011"
    b: "1111"
    c: "1101"
    d: "1011"
    e: "1010"
    f: "1000"
    g: "0011"
  teilschritte:
    - titel: Rechts die Eins
      text: "Für die 1 leuchten b und c; b leuchtet sogar immer."
      ausgaenge: [b, c]
    - titel: Oben und unten
      text: "a und d leuchten bei 0, 2 und 3."
      ausgaenge: [a, d]
    - titel: Alle Segmente
      text: "Dazu e, f und g: die Ziffern 0 bis 3 stehen richtig da."
      ausgaenge: alle
  sterne: {bausteine: 5, tiefe: 2}
---

# 7-Segment-Anzeige von 0 bis 3

Eine 7-Segment-Anzeige setzt Ziffern aus sieben Strichen zusammen: a oben, b rechts oben, c rechts unten, d unten, e links unten, f links oben, g in der Mitte. A und B bilden eine Zahl von 0 bis 3, und die Anzeige soll sie zeigen.

Neu: ein Ausgang darf auch fest an 1 oder 0 hängen (`b = 1`), und ein Segment darf direkt an einem Eingang hängen. Wer genau hinsieht, braucht erstaunlich wenige Bausteine.
