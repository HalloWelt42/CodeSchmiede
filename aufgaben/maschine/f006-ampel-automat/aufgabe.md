---
schema_version: 1
id: f006-ampel-automat
revision: 1
titel: Ampel als Automat
sprache: maschine
task_type: takt
runner_type: server
schwierigkeit: mittel
schwierigkeit_score: 45
schaetz_minuten: 20
tags: [schaltung, takt]
voraussetzungen: []
quelle:
  url: null
  notiz: Schaltungen mit Takt, Level 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Die vier Phasen sind die vier Stände des Zählers bis 3: 0 Rot, 1 Rot und Gelb, 2 Grün, 3 Gelb."
  - kosten: 2
    text: "Oben (Rot) leuchtet bei 0 und 1, also wenn Q1 0 ist. Die Mitte (Gelb) leuchtet bei 1 und 3, also wenn Q0 1 ist. Und unten (Grün) nur bei 2."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  # der Zähler bis 3 steht schon
  n0 = NICHT(f0) @ 130,40
  f0 = FF(n0) @ 260,40
  x1 = XOR(f0, f1) @ 130,170
  f1 = FF(x1) @ 260,170
  OBEN = ?
  MITTE = ?
  UNTEN = ?
takt:
  ausgaenge: [OBEN, MITTE, UNTEN]
  bausteine: [FF, UND, ODER, XOR, NICHT]
  sichtbar:
    - name: Ampel
      takte: 8
      soll: {OBEN: "11001100", MITTE: "01010101", UNTEN: "00100010"}
  versteckt:
    - name: Lange
      takte: 13
      soll: {OBEN: "1100110011001", MITTE: "0101010101010", UNTEN: "0010001000100"}
  teilschritte:
    - titel: Rot
      text: "Oben leuchtet Rot, in den ersten beiden von vier Phasen."
      ausgaenge: [OBEN]
    - titel: Gelb und Grün
      text: "Dann Rot und Gelb, dann Grün, dann Gelb, und wieder von vorn."
      ausgaenge: alle
    - titel: Lange laufen
      text: "Zum Schluss ein längerer, versteckter Ablauf."
      ablaeufe: alle
  sterne: {bausteine: 4, tiefe: 2}
---

# Ampel als Automat

In der Ampelschule hat ein Programm die Ampel gesteuert. Hier baust du sie in Hardware, wie in echten Ampelsteuerungen von früher: Rot, Rot und Gelb, Grün, Gelb, und wieder Rot. Vier Phasen, je ein Takt.

Vier Phasen, das klingt nach dem Zähler bis 3. Genau: Der Zähler aus dem dritten Level steht schon im Plan, du hängst nur noch an, welche Lampe in welcher Phase leuchtet. So ein Zähler mit Ausgabe heißt Automat: Er ist immer in einem Zustand, und der Takt schaltet ihn weiter.
