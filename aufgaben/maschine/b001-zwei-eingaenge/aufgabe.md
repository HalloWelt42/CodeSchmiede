---
schema_version: 1
id: b001-zwei-eingaenge
revision: 1
titel: "Zwei Eingänge"
sprache: maschine
task_type: kv
runner_type: server
schwierigkeit: anfaenger
schwierigkeit_score: 15
schaetz_minuten: 10
tags: [schaltung, kv-diagramm]
voraussetzungen: []
quelle:
  url: null
  notiz: KV-Werkstatt, Level 1
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
  L = 
kv:
  eingaenge: ["A", "B"]
  ausgaenge: ["L"]
  werte: {L: "0111"}
---

# Zwei Eingänge

Das erste KV-Diagramm ist winzig: zwei Eingänge, vier Felder. Das Licht L im Flur brennt, wenn der Schalter an der Tür (A) oder der an der Treppe (B) an ist, oder beide.

Zieh Blöcke über die Felder mit 1. Ein Block hat 1, 2 oder 4 Felder und ist ein Rechteck. Was im Block gleich bleibt, steht in seinem Term, was wechselt, fällt weg. Ein Block über die ganze untere Zeile ist also einfach A.
