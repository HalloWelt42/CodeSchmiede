---
schema_version: 1
id: f001-ein-bit-merken
revision: 1
titel: Ein Bit merken
sprache: maschine
task_type: takt
runner_type: server
schwierigkeit: anfaenger
schwierigkeit_score: 25
schaetz_minuten: 15
tags: [schaltung, takt]
voraussetzungen: []
quelle:
  url: null
  notiz: Schaltungen mit Takt, Level 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Ein Flipflop allein reicht für Durchreichen: `q = FF(E)` und `Q = q`."
  - kosten: 2
    text: "Halten heißt: wenn W 0 ist, bekommt das Flipflop seinen eigenen Wert zurück. Also D = (W UND E) ODER (NICHT W UND q)."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  q = FF(?) @ 410,80
  Q = q
takt:
  eingaenge: [E, W]
  ausgaenge: [Q]
  bausteine: [FF, UND, ODER, NICHT]
  sichtbar:
    - name: Durchreichen
      takte: 8
      eingaben: {E: "01101001", W: "11111111"}
      soll: {Q: "00110100"}
    - name: Halten
      takte: 8
      eingaben: {E: "11001010", W: "10001001"}
      soll: {Q: "01111111"}
  versteckt:
    - name: Morgens
      takte: 12
      eingaben: {E: "101100111010", W: "011010010110"}
      soll: {Q: "000110001101"}
    - name: Abends
      takte: 10
      eingaben: {E: "0011101100", W: "1100011011"}
      soll: {Q: "0000000110"}
  teilschritte:
    - titel: Durchreichen
      text: "Bei jedem Takt übernimmt Q, was an E anliegt: Q zeigt E einen Takt später."
      ausgaenge: alle
    - titel: Nur auf Befehl
      text: "Nur wenn W 1 ist, wird E übernommen; sonst hält Q seinen Wert."
      ablaeufe: [Halten]
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe."
      ablaeufe: alle
  sterne: {bausteine: 4, tiefe: 3}
---

# Ein Bit merken

Bisher hat jede Schaltung sofort gerechnet und sofort vergessen. Ein **Flipflop** (`FF`) merkt sich ein Bit: Bei jedem Takt übernimmt es, was an seinem Eingang D anliegt, und zeigt es bis zum nächsten Takt. Alle Flipflops beginnen bei 0 und hängen am selben Takt.

Erst reichst du nur durch: Q zeigt E, einen Takt später. Dann wird es ein richtiger Speicher: Nur wenn W (Schreiben) 1 ist, merkt er sich E, sonst hält er, was er hat. So steckt das in jedem Arbeitsspeicher, nur ein paar Milliarden Mal.

Rechts siehst du den Zeitverlauf: je Takt die Eingänge, darunter Soll (gestrichelt) und Ist. Ein Klick in den Verlauf springt zu diesem Takt, der Plan zeigt dann, was die Flipflops gerade gemerkt haben.
