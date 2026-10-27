---
schema_version: 1
id: f005-lauflicht
revision: 1
titel: Lauflicht
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
  notiz: Schaltungen mit Takt, Level 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Weiterreichen ist einfach: Jedes Flipflop übernimmt das Licht links von ihm, `l1 = FF(l0)`."
  - kosten: 2
    text: "Ein neues Licht braucht L0 nur, wenn L0, L1 und L2 gerade alle dunkel sind: ein NOR über alle drei."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  l0 = FF(?) @ 330,20
  l1 = FF(?) @ 330,100
  l2 = FF(?) @ 330,180
  l3 = FF(?) @ 330,260
  L0 = l0
  L1 = l1
  L2 = l2
  L3 = l3
takt:
  ausgaenge: [L0, L1, L2, L3]
  bausteine: [FF, UND, ODER, XOR, NICHT, NOR]
  sichtbar:
    - name: Lauflicht
      takte: 10
      soll: {L0: "0100010001", L1: "0010001000", L2: "0001000100", L3: "0000100010"}
  versteckt:
    - name: Lange
      takte: 17
      soll: {L0: "01000100010001000", L1: "00100010001000100", L2: "00010001000100010", L3: "00001000100010001"}
  teilschritte:
    - titel: Ein Licht geht an
      text: "Nach dem Start ist alles dunkel; beim ersten Takt geht L0 an, und immer wenn das Licht hinten angekommen ist, wieder."
      ausgaenge: [L0]
    - titel: Weiterreichen
      text: "Bei jedem Takt wandert das Licht eins weiter: L0, L1, L2, L3."
      ausgaenge: alle
    - titel: Lange laufen
      text: "Zum Schluss ein längerer, versteckter Ablauf."
      ablaeufe: alle
  sterne: {bausteine: 2, tiefe: 2}
---

# Lauflicht

Vier Lämpchen, ein Licht, und es wandert: L0, L1, L2, L3, dann wieder von vorn. Das Weiterreichen erledigt eine Kette aus Flipflops, ein Schieberegister: Jedes übernimmt beim Takt, was das vorige gerade zeigt.

Bleibt die Frage, wo das Licht herkommt. Alle Flipflops beginnen bei 0, am Anfang ist also alles dunkel. Irgendetwas muss erkennen, wann ein neues Licht fällig ist. Und das am besten, ohne dass zwei Lichter gleichzeitig unterwegs sind.
