---
schema_version: 1
id: b006-ganze-anzeige
revision: 1
titel: "Die ganze Anzeige"
sprache: maschine
task_type: kv
runner_type: server
schwierigkeit: fortgeschritten
schwierigkeit_score: 70
schaetz_minuten: 45
tags: [schaltung, kv-diagramm]
voraussetzungen: []
quelle:
  url: null
  notiz: KV-Werkstatt, Level 6
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
  a = 
  b = 
  c = 
  d = 
  e = 
  f = 
  g = 
kv:
  eingaenge: ["A", "B", "C", "D"]
  ausgaenge: ["a", "b", "c", "d", "e", "f", "g"]
  werte: {a: "1011011111xxxxxx", b: "1111100111xxxxxx", c: "1101111111xxxxxx", d: "1011011011xxxxxx", e: "1010001010xxxxxx", f: "1000111011xxxxxx", g: "0011111011xxxxxx"}
  namen: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
---

# Die ganze Anzeige

Jetzt alle sieben Segmente a bis g: a oben, b rechts oben, c rechts unten, d unten, e links unten, f links oben, g in der Mitte. Jedes Segment ist ein eigenes KV-Diagramm; oben wählst du, welches du gerade bearbeitest.

Das ist der Dekoder aus jeder Digitaluhr. Die Egal-Felder 10 bis 15 helfen bei jedem Segment, und manche Blöcke kommen in mehreren Segmenten vor. Nimm dir Zeit, sieben Raster sind ein ordentliches Stück Arbeit.
