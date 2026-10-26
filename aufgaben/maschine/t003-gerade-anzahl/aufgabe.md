---
schema_version: 1
id: t003-gerade-anzahl
revision: 1
titel: Gerade Anzahl
sprache: maschine
task_type: turing
runner_type: server
schwierigkeit: mittel
schwierigkeit_score: 25
schaetz_minuten: 15
tags: [turingmaschine]
voraussetzungen: []
quelle:
  url: null
  notiz: Turingmaschine, Level 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Zwei Zustände reichen: `gerade` und `ungerade`. Jede 1 wechselt vom einen zum anderen."
starter_code: |
  # Zustand liest -> schreibt geht danach
  gerade 0 -> 0 R gerade
turing:
  zeichen: ["0", "1"]
  start: gerade
  ende: [ja, nein]
  kopf: anfang
  grenze: 300
  sichtbar:
    - {band: "0110", soll_zustand: ja}
    - {band: "1011", soll_zustand: nein}
    - {band: "", name: "leer", soll_zustand: ja}
  versteckt:
    - {band: "1", soll_zustand: nein}
    - {band: "111111", soll_zustand: ja}
    - {band: "100000001", soll_zustand: ja}
    - {band: "0001000", soll_zustand: nein}
  teilschritte:
    - titel: Zählen ohne Zahlen
      text: "Steht eine gerade Anzahl Einsen auf dem Band, hält die Maschine in ja."
    - titel: Auch ungerade
      text: "Bei ungerader Anzahl hält sie in nein."
      baender: ["1011"]
    - titel: Leeres Band
      text: "Null Einsen sind auch eine gerade Anzahl."
      baender: ["leer"]
    - titel: Alle Bänder
      text: "Zum Schluss die versteckten Bänder."
      baender: alle
  sterne: {zustaende: 2, zeilen: 6}
---

# Gerade Anzahl

Diese Maschine rechnet nichts aus, sie entscheidet: Steht auf dem Band eine gerade Anzahl Einsen, hält sie im Zustand `ja`, sonst in `nein`. Was am Ende auf dem Band steht, ist egal.

Zählen kann sie nicht, sie hat ja keine Zahlen. Aber sie kann sich in ihrem Zustand merken, ob es bisher gerade oder ungerade viele waren.
