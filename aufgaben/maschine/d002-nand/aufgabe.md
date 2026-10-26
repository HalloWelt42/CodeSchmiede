---
schema_version: 1
id: d002-nand
revision: 1
titel: NAND selbst gebaut
sprache: maschine
task_type: schaltung
runner_type: server
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 10
tags: [schaltung]
voraussetzungen: []
quelle:
  url: null
  notiz: Digitale Schaltungen, Level 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Erst UND, dann das Ergebnis durch ein NICHT."
starter_code: |
  # name = ART(Eingang, Eingang) @ x,y   und   Ausgang = Signal
  Y = ?
schaltung:
  eingaenge: [A, B]
  ausgaenge: [Y]
  bausteine: [UND, NICHT]
  soll:
    Y: "1110"
  teilschritte:
    - titel: NICHT UND
      text: "Y ist nur dann 0, wenn A und B beide 1 sind."
      ausgaenge: alle
  sterne: {bausteine: 2, tiefe: 2}
---

# NAND selbst gebaut

Jetzt baust du selbst: Oben stehen die Bausteine, ein Klick setzt einen in den Plan, ziehen verschiebt ihn.

Gesucht ist NAND, das "nicht und": Y ist 1, außer wenn A und B beide 1 sind. Aus NAND allein lässt sich übrigens jede andere Schaltung bauen. Das kommt noch.
