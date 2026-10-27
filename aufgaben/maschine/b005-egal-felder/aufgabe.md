---
schema_version: 1
id: b005-egal-felder
revision: 1
titel: "Egal-Felder als Joker"
sprache: maschine
task_type: kv
runner_type: server
schwierigkeit: mittel
schwierigkeit_score: 40
schaetz_minuten: 20
tags: [schaltung, kv-diagramm]
voraussetzungen: []
quelle:
  url: null
  notiz: KV-Werkstatt, Level 5
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
  e = 
kv:
  eingaenge: ["A", "B", "C", "D"]
  ausgaenge: ["e"]
  werte: {e: "1010001010xxxxxx"}
  namen: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
---

# Egal-Felder als Joker

Die 7-Segment-Anzeige bekommt eine Ziffer von 0 bis 9 als vier Bits A B C D. Segment e, links unten, leuchtet bei 0, 2, 6 und 8.

Die Belegungen 10 bis 15 kommen nie vor. Dort steht x: egal. Ein x darfst du in einen Block nehmen, wenn er dadurch größer wird, musst aber nicht. Mit den richtigen Jokern wird die Formel verblüffend kurz.
