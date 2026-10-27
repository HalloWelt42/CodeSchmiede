---
schema_version: 1
id: b007-vom-block-zum-schaltplan
revision: 1
titel: "Vom Block zum Schaltplan"
sprache: maschine
task_type: kv
runner_type: server
schwierigkeit: fortgeschritten
schwierigkeit_score: 60
schaetz_minuten: 30
tags: [schaltung, kv-diagramm]
voraussetzungen: []
quelle:
  url: null
  notiz: KV-Werkstatt, Level 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-27
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Erst die großen Blöcke: suche Rechtecke aus 4 oder 8 Feldern, die keine 0 erwischen. Dann die Einsen, die noch übrig sind."
  - kosten: 2
    text: "Eine 1, die nur in einen einzigen größten Block passt, gibt diesen Block vor. Fang mit solchen Einsen an."
starter_code: |
  S = 
  Co = 
kv:
  eingaenge: ["A", "B", "C"]
  ausgaenge: ["S", "Co"]
  werte: {S: "01101001", Co: "00010111"}
---

# Vom Block zum Schaltplan

Der Volladdierer aus den Schaltungen: A und B und der Übertrag C von der Stelle davor. S ist die Summe, Co der neue Übertrag. Rechts siehst du, welchen Schaltplan deine Formel ergibt, mit UND, ODER und NICHT.

Co wird schön klein. Und S? Ein Schachbrett: keine zwei Einsen sind Nachbarn, kein Block geht größer als ein Feld. Das KV-Diagramm sagt dir damit ehrlich, dass es hier nicht weiterhilft. Wer XOR kennt, braucht für S nur zwei Bausteine; das KV-Diagramm kennt XOR nicht. Gut zu wissen, wann ein Werkzeug passt.
