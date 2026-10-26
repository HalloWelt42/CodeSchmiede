---
schema_version: 1
id: t007-kopieren
revision: 1
titel: Kopieren
sprache: maschine
task_type: turing
runner_type: server
schwierigkeit: experte
schwierigkeit_score: 60
schaetz_minuten: 40
tags: [turingmaschine]
voraussetzungen: []
quelle:
  url: null
  notiz: Turingmaschine, Level 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Erst das | ans Ende. Dann: zurück zur ersten unmarkierten Ziffer, markieren, im Zustand merken (trage0, trage1), ans Ende tragen."
  - kosten: 2
    text: "Liest das Nehmen das |, ist alles kopiert: dann nach links und A und B zurückverwandeln."
starter_code: |
  # Zustand liest -> schreibt geht danach
  start 0 -> 0 R start
turing:
  zeichen: ["0", "1", "|", "A", "B"]
  start: start
  ende: [fertig]
  kopf: anfang
  grenze: 3000
  sichtbar:
    - {band: "1", soll: "1|1"}
    - {band: "10", soll: "10|10"}
    - {band: "0110", soll: "0110|0110"}
  versteckt:
    - {band: "", name: "leer", soll: "|"}
    - {band: "111", soll: "111|111"}
    - {band: "00100", soll: "00100|00100"}
    - {band: "1010", soll: "1010|1010"}
  teilschritte:
    - titel: Ein Zeichen
      text: "Aus 1 wird 1|1: erst ein Trennzeichen ans Ende, dann die Kopie dahinter."
    - titel: Mehrere Zeichen
      text: "Aus 10 wird 10|10; schon kopierte Zeichen markierst du mit A und B."
      baender: ["10"]
    - titel: Aufräumen
      text: "Am Ende stehen links wieder 0 und 1, keine Markierungen."
      baender: ["0110"]
    - titel: Alle Bänder
      text: "Zum Schluss die versteckten Bänder, auch ein leeres."
      baender: alle
  sterne: {zustaende: 6, zeilen: 23}
---

# Kopieren

Aus `0110` soll `0110#0110` werden: erst ein Trennzeichen `#`, dahinter dieselbe Folge noch einmal.

Die Maschine trägt ein Zeichen nach dem anderen nach hinten. Damit sie weiß, wie weit sie schon ist, markiert sie kopierte Zeichen: eine 0 wird `A`, eine 1 wird `B`. Am Ende werden die Markierungen wieder zu 0 und 1.
