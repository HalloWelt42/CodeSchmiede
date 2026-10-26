---
schema_version: 1
id: t004-unaer-addieren
revision: 1
titel: Unär addieren
sprache: maschine
task_type: turing
runner_type: server
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 20
tags: [turingmaschine]
voraussetzungen: []
quelle:
  url: null
  notiz: Turingmaschine, Level 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Das Plus wird einfach zur 1. Dann ist eine 1 zu viel auf dem Band; die letzte muss weg."
starter_code: |
  # Zustand liest -> schreibt geht danach
  a 1 -> 1 R a
turing:
  zeichen: ["1", "+"]
  start: a
  ende: [fertig]
  kopf: anfang
  grenze: 500
  sichtbar:
    - {band: "111+11", soll: "11111"}
    - {band: "1+1", soll: "11"}
    - {band: "+111", soll: "111"}
  versteckt:
    - {band: "11+", soll: "11"}
    - {band: "+", name: "nur plus", soll: ""}
    - {band: "1111111+1", soll: "11111111"}
    - {band: "1+11111", soll: "111111"}
  teilschritte:
    - titel: Zusammenschieben
      text: "Aus 111+11 wird 11111: so viele Einsen wie links und rechts zusammen."
    - titel: Kleine Summen
      text: "Auch 1+1 ergibt 11."
      baender: ["1+1"]
    - titel: Null vorn
      text: "+111 ist null plus drei."
      baender: ["+111"]
    - titel: Alle Bänder
      text: "Zum Schluss die versteckten Bänder, auch null plus null."
      baender: alle
  sterne: {zustaende: 3, zeilen: 5}
---

# Unär addieren

Unär schreibt man Zahlen wie auf einem Bierdeckel: drei ist 111, zwei ist 11. Auf dem Band steht eine Aufgabe wie `111+11`, und am Ende soll dort nur die Summe stehen: `11111`.

Der Kopf steht am Anfang. Es gibt einen schönen Trick, der fast nichts verschieben muss.
