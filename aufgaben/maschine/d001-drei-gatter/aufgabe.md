---
schema_version: 1
id: d001-drei-gatter
revision: 1
titel: Drei Gatter
sprache: maschine
task_type: schaltung
runner_type: server
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 10
tags: [schaltung]
voraussetzungen: []
quelle:
  url: null
  notiz: Digitale Schaltungen, Level 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Jeder Eingang eines Bausteins braucht genau eine Leitung, jedes Lämpchen auch."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  u1 = UND(?, ?) @ 220,30
  o1 = ODER(?, ?) @ 220,120
  n1 = NICHT(?) @ 220,210
  U = ?
  O = ?
  N = ?
schaltung:
  eingaenge: [A, B]
  ausgaenge: [U, O, N]
  bausteine: [UND, ODER, NICHT]
  vorgabe:
    - {name: u1, art: UND, x: 220, y: 30}
    - {name: o1, art: ODER, x: 220, y: 120}
    - {name: n1, art: NICHT, x: 220, y: 210}
  soll:
    U: "0001"
    O: "0111"
    N: "1100"
  teilschritte:
    - titel: UND
      text: "U ist 1, wenn A und B beide 1 sind: verbinde A und B mit u1 und u1 mit U."
      ausgaenge: [U]
    - titel: ODER
      text: "O ist 1, wenn mindestens einer 1 ist."
      ausgaenge: [O]
    - titel: NICHT
      text: "N ist das Gegenteil von A."
      ausgaenge: alle
  sterne: {bausteine: 3, tiefe: 1}
---

# Drei Gatter

Die drei Grundbausteine der Digitaltechnik: UND, ODER und NICHT. Sie stehen schon im Plan, du ziehst nur die Leitungen.

So geht es: Klick auf einen Ausgang (den Punkt rechts an A, B oder einem Baustein), dann auf einen Eingang (links an einem Baustein oder an einem Lämpchen). Klickst du auf einen belegten Eingang, ist die Leitung wieder weg.

Die Wahrheitstabelle rechts rechnet bei jeder Änderung neu. Ein Klick auf eine Zeile zeigt, welche Leitungen dann 1 führen.
