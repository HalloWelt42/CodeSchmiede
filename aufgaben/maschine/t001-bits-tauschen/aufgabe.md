---
schema_version: 1
id: t001-bits-tauschen
revision: 1
titel: Bits tauschen
sprache: maschine
task_type: turing
runner_type: server
schwierigkeit: anfaenger
schwierigkeit_score: 10
schaetz_minuten: 10
tags: [turingmaschine]
voraussetzungen: []
quelle:
  url: null
  notiz: Turingmaschine, Level 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Am Ende der Folge liest der Kopf `_`. Dafür braucht es eine eigene Zeile, die nach `fertig` führt."
starter_code: |
  # Zustand liest -> schreibt geht danach
  tauschen 0 -> 1 R tauschen
turing:
  zeichen: ["0", "1"]
  start: tauschen
  ende: [fertig]
  kopf: anfang
  grenze: 200
  sichtbar:
    - {band: "0110", soll: "1001"}
    - {band: "1", soll: "0"}
  versteckt:
    - {band: "000", soll: "111"}
    - {band: "1010101", soll: "0101010"}
    - {band: "", name: "leer", soll: ""}
  teilschritte:
    - titel: Tauschen und weiter
      text: "Aus 0 wird 1, aus 1 wird 0, dann ein Feld nach rechts."
    - titel: Alle Bänder
      text: "Zum Schluss die versteckten Bänder, auch ein leeres."
      baender: alle
  sterne: {zustaende: 1, zeilen: 3}
---

# Bits tauschen

Die erste Maschine: Auf dem Band steht eine Folge aus 0 und 1, der Kopf steht auf dem ersten Zeichen. Die Maschine soll jede 0 zur 1 machen und jede 1 zur 0 und am Ende im Zustand `fertig` anhalten.

Eine Turingmaschine hat keine Variablen und keine Schleifen, nur eine Tabelle. Jede Zeile sagt: Wenn ich im Zustand X bin und das Zeichen Y lese, dann schreibe ich Z, gehe nach links (`L`), rechts (`R`) oder bleibe (`N`) und bin danach im Zustand W. `_` ist ein leeres Feld.

Klingt wenig? Damit kann man alles ausrechnen, was ein Computer ausrechnen kann. Nur eben sehr, sehr geduldig.
