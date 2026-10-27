---
schema_version: 1
id: b002-mehrheit
revision: 1
titel: "Mehrheit aus drei"
sprache: maschine
task_type: kv
runner_type: server
schwierigkeit: anfaenger
schwierigkeit_score: 25
schaetz_minuten: 15
tags: [schaltung, kv-diagramm]
voraussetzungen: []
quelle:
  url: null
  notiz: KV-Werkstatt, Level 2
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
  M = 
kv:
  eingaenge: ["A", "B", "C"]
  ausgaenge: ["M"]
  werte: {M: "00010111"}
---

# Mehrheit aus drei

Drei Leute stimmen ab, A, B und C, und M zeigt, ob die Mehrheit dafür ist: also mindestens zwei von dreien.

Jetzt sind es acht Felder in zwei Zeilen. Die Spalten heißen 00, 01, 11, 10, damit Nachbarn sich in genau einem Eingang unterscheiden. Blöcke dürfen sich überlappen: jede 1 darf in mehreren Blöcken liegen, wenn sie dadurch größer werden.
