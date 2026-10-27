---
schema_version: 1
id: b004-vier-eingaenge
revision: 1
titel: "Vier Eingänge: Primzahlen"
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
  notiz: KV-Werkstatt, Level 4
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
  eingaenge: ["A", "B", "C", "D"]
  ausgaenge: ["P"]
  werte: {P: "0011010100010100"}
  namen: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
---

# Vier Eingänge: Primzahlen

Vier Bits A B C D sind eine Zahl von 0 bis 15, A ist die höchste Stelle. P soll 1 sein, wenn die Zahl eine Primzahl ist: 2, 3, 5, 7, 11, 13.

Jetzt ist das Raster vier mal vier, und beide Achsen laufen 00, 01, 11, 10. Oben und unten sind auch Nachbarn, und die vier Ecken gehören zusammen. Primzahlen sind übrigens nicht besonders ordentlich verteilt; ganz klein wird die Formel hier nicht. Aber kleiner als 6 Terme mit je 4 Buchstaben.
