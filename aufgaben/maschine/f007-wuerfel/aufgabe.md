---
schema_version: 1
id: f007-wuerfel
revision: 1
titel: Würfel auf der 7-Segment-Anzeige
sprache: maschine
task_type: takt
runner_type: server
schwierigkeit: experte
schwierigkeit_score: 85
schaetz_minuten: 50
tags: [schaltung, takt]
voraussetzungen: []
quelle:
  url: null
  notiz: Schaltungen mit Takt, Level 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Sechs Zustände mit drei Flipflops, die nacheinander kippen: 000, 001, 011, 111, 110, 100. D0 ist NICHT q2, D1 ist q0, D2 ist q1."
  - kosten: 2
    text: "Halten: wenn W 0 ist, bekommt jedes Flipflop seinen eigenen Wert zurück. Wie beim Bit merken, nur dreimal."
  - kosten: 2
    text: "Anzeige: f leuchtet genau bei 4, 5 und 6, das ist q2. a und d leuchten, wenn q0 und q2 verschieden sind. g leuchtet überall außer bei der 1."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  q0 = FF(?) @ 250,20
  q1 = FF(?) @ 250,110
  q2 = FF(?) @ 250,200
  a = ?
  b = ?
  c = ?
  d = ?
  e = ?
  f = ?
  g = ?
takt:
  eingaenge: [W]
  ausgaenge: [a, b, c, d, e, f, g]
  bausteine: [FF, UND, ODER, XOR, NICHT, NAND, NOR]
  sichtbar:
    - name: Rollen
      takte: 8
      eingaben: {W: "11111111"}
      soll: {a: "01101101", b: "11110011", c: "10111110", d: "01101101", e: "01000101", f: "00011100", g: "01111101"}
    - name: Anhalten
      takte: 10
      eingaben: {W: "1110001100"}
      soll: {a: "0110000111", b: "1111111000", c: "1011111111", d: "0110000111", e: "0100000011", f: "0001111111", g: "0111111111"}
  versteckt:
    - name: Langer Wurf
      takte: 12
      eingaben: {W: "111111111100"}
      soll: {a: "011011011011", b: "111100111100", c: "101111101111", d: "011011011011", e: "010001010000", f: "000111000111", g: "011111011111"}
    - name: Zögern
      takte: 13
      eingaben: {W: "0101100111001"}
      soll: {a: "0011100011000", b: "1111111100111", c: "1100111111111", d: "0011100011000", e: "0011000001000", f: "0000011111000", g: "0011111111000"}
  teilschritte:
    - titel: Rollen
      text: "Solange W gedrückt ist, zeigt die Anzeige bei jedem Takt die nächste Zahl: 1, 2, 3, 4, 5, 6, 1."
      ausgaenge: alle
    - titel: Anhalten
      text: "Lässt man W los, bleibt die Zahl stehen."
      ablaeufe: [Anhalten]
    - titel: Alle Würfe
      text: "Zum Schluss die versteckten Abläufe."
      ablaeufe: alle
  sterne: {bausteine: 17, tiefe: 3}
---

# Würfel auf der 7-Segment-Anzeige

Ein elektronischer Würfel: Solange du W drückst, zählt er im Takt 1, 2, 3, 4, 5, 6 und wieder 1, viel zu schnell zum Mitlesen. Lässt du los, bleibt die Zahl stehen, und die 7-Segment-Anzeige zeigt, was gewürfelt wurde.

Zwei Hälften: ein Zähler mit sechs Zuständen, der anhalten kann, und eine Anzeige, die aus dem Zustand die Segmente a bis g macht. Mit drei Flipflops gibt es acht Zustände, du brauchst nur sechs. Welche du nimmst, ist deine Sache; manche Wahl macht die Anzeige verblüffend einfach.

Die Segmente: a oben, b rechts oben, c rechts unten, d unten, e links unten, f links oben, g in der Mitte.
