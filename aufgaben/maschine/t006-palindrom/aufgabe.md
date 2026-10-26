---
schema_version: 1
id: t006-palindrom
revision: 1
titel: Palindrom
sprache: maschine
task_type: turing
runner_type: server
schwierigkeit: fortgeschritten
schwierigkeit_score: 50
schaetz_minuten: 30
tags: [turingmaschine]
voraussetzungen: []
quelle:
  url: null
  notiz: Turingmaschine, Level 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Für jedes gemerkte Zeichen einen eigenen Zustand: hat0 und hat1."
  - kosten: 2
    text: "Wer vorne und hinten je ein Zeichen löscht, macht das Band kürzer, bis nichts mehr übrig ist."
starter_code: |
  # Zustand liest -> schreibt geht danach
  start 0 -> _ R hat0
turing:
  zeichen: ["0", "1"]
  start: start
  ende: [ja, nein]
  kopf: anfang
  grenze: 2000
  sichtbar:
    - {band: "0110", soll_zustand: ja}
    - {band: "011", soll_zustand: nein}
    - {band: "10101", soll_zustand: ja}
  versteckt:
    - {band: "", name: "leer", soll_zustand: ja}
    - {band: "1", soll_zustand: ja}
    - {band: "10", soll_zustand: nein}
    - {band: "1001001", soll_zustand: ja}
    - {band: "110100", soll_zustand: nein}
    - {band: "0000", soll_zustand: ja}
  teilschritte:
    - titel: Außen vergleichen
      text: "0110 liest sich rückwärts gleich: ja."
    - titel: Ungleich
      text: "011 rückwärts ist 110: nein."
      baender: ["011"]
    - titel: Ungerade Länge
      text: "Bei 10101 bleibt in der Mitte ein Zeichen übrig: ja."
      baender: ["10101"]
    - titel: Alle Bänder
      text: "Zum Schluss die versteckten Bänder, auch ein leeres."
      baender: alle
  sterne: {zustaende: 6, zeilen: 18}
---

# Palindrom

Ein Palindrom liest sich vorwärts und rückwärts gleich, wie OTTO oder 0110. Die Maschine soll in `ja` halten, wenn das Band eins ist, sonst in `nein`.

Sie kann nur ein Zeichen auf einmal sehen. Aber sie kann vorne eins wegnehmen, es sich im Zustand merken, nach hinten laufen und dort vergleichen.
