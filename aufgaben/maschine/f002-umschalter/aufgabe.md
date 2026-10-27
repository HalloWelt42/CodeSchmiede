---
schema_version: 1
id: f002-umschalter
revision: 1
titel: Umschalter
sprache: maschine
task_type: takt
runner_type: server
schwierigkeit: anfaenger
schwierigkeit_score: 25
schaetz_minuten: 10
tags: [schaltung, takt]
voraussetzungen: []
quelle:
  url: null
  notiz: Schaltungen mit Takt, Level 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Das Flipflop soll beim Takt das Gegenteil von sich selbst übernehmen, aber nur, wenn K 1 ist."
  - kosten: 1
    text: "XOR mit 1 dreht um, XOR mit 0 lässt stehen. Ein Baustein reicht."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  l = FF(?) @ 360,60
  L = l
takt:
  eingaenge: [K]
  ausgaenge: [L]
  bausteine: [FF, UND, ODER, XOR, NICHT]
  sichtbar:
    - name: Dauertaste
      takte: 8
      eingaben: {K: "11111111"}
      soll: {L: "01010101"}
    - name: Ab und zu
      takte: 8
      eingaben: {K: "10110010"}
      soll: {L: "01101110"}
  versteckt:
    - name: Flur
      takte: 12
      eingaben: {K: "011100100110"}
      soll: {L: "001011100010"}
    - name: Keller
      takte: 10
      eingaben: {K: "0000110001"}
      soll: {L: "0000010000"}
  teilschritte:
    - titel: Bei jedem Takt
      text: "Solange K gedrückt ist, wechselt das Licht bei jedem Takt."
      ausgaenge: alle
    - titel: Nur mit Taste
      text: "Ohne K bleibt das Licht, wie es ist."
      ablaeufe: [Ab und zu]
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe."
      ablaeufe: alle
  sterne: {bausteine: 1, tiefe: 1}
---

# Umschalter

Im Treppenhaus schaltet ein Druck auf den Taster das Licht an, der nächste wieder aus. Dein Licht L soll das auch können: Ist K beim Takt gedrückt, wechselt L, sonst bleibt es, wie es ist.

Neu ist die Rückkopplung: Das Flipflop bekommt an D etwas, das von seinem eigenen Q abhängt. Ohne Flipflop wäre das ein Kreis, der nie zur Ruhe kommt; mit Flipflop rechnet die Schaltung bis zum Takt mit dem alten Wert und übernimmt erst dann den neuen.
