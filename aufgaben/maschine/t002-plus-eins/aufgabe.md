---
schema_version: 1
id: t002-plus-eins
revision: 1
titel: Plus eins
sprache: maschine
task_type: turing
runner_type: server
schwierigkeit: anfaenger
schwierigkeit_score: 20
schaetz_minuten: 15
tags: [turingmaschine]
voraussetzungen: []
quelle:
  url: null
  notiz: Turingmaschine, Level 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Eine 1 am Ende wird 0, und der Übertrag wandert nach links. Eine 0 (oder ein leeres Feld) wird 1, dann ist Schluss."
starter_code: |
  # Zustand liest -> schreibt geht danach
  plus 1 -> 0 L plus
turing:
  zeichen: ["0", "1"]
  start: plus
  ende: [fertig]
  kopf: ende
  grenze: 200
  sichtbar:
    - {band: "0", soll: "1"}
    - {band: "1011", soll: "1100"}
    - {band: "111", soll: "1000"}
  versteckt:
    - {band: "1", soll: "10"}
    - {band: "10", soll: "11"}
    - {band: "1111111", soll: "10000000"}
    - {band: "100111", soll: "101000"}
  teilschritte:
    - titel: Aus 0 wird 1
      text: "Endet die Zahl auf 0: eine 1 schreiben und anhalten."
    - titel: Überträge
      text: "Aus 1011 wird 1100: jede 1 am Ende wird 0, die erste 0 davor wird 1."
      baender: ["1011"]
    - titel: Eine Stelle mehr
      text: "Aus 111 wird 1000: links vom Band ist leer (_), dort kommt die neue 1 hin."
      baender: ["111"]
    - titel: Alle Bänder
      text: "Zum Schluss die versteckten Bänder."
      baender: alle
  sterne: {zustaende: 1, zeilen: 3}
---

# Plus eins

Auf dem Band steht eine Binärzahl, der Kopf steht diesmal auf ihrer letzten Ziffer. Die Maschine soll die Zahl um eins erhöhen und dann im Zustand `fertig` anhalten.

Wie beim schriftlichen Addieren: von hinten anfangen, und wo ein Übertrag entsteht, weiter nach links.
