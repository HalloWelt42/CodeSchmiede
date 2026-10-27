---
schema_version: 1
id: b003-ueber-den-rand
revision: 1
titel: "Über den Rand"
sprache: maschine
task_type: kv
runner_type: server
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 15
tags: [schaltung, kv-diagramm]
voraussetzungen: []
quelle:
  url: null
  notiz: KV-Werkstatt, Level 3
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
  P = 
kv:
  eingaenge: ["A", "B", "C"]
  ausgaenge: ["P"]
  werte: {P: "10101011"}
---

# Über den Rand

Die Pumpe P soll laufen, wenn der Fühler C kein Wasser meldet, oder wenn A und B beide eingeschaltet sind.

Schau dir die Spalten 00 und 10 an: sie liegen am linken und am rechten Rand, unterscheiden sich aber nur in B. Sie sind Nachbarn. Ein Block darf deshalb über den Rand hinaus weitergehen und auf der anderen Seite wieder auftauchen, als hätte jemand das Raster zu einer Rolle gebogen.
