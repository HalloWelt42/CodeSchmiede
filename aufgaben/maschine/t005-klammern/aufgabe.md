---
schema_version: 1
id: t005-klammern
revision: 1
titel: Klammern prüfen
sprache: maschine
task_type: turing
runner_type: server
schwierigkeit: fortgeschritten
schwierigkeit_score: 45
schaetz_minuten: 30
tags: [turingmaschine]
voraussetzungen: []
quelle:
  url: null
  notiz: Turingmaschine, Level 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 5
hints:
  - kosten: 1
    text: "Such die erste schließende Klammer, streich sie (X) und lauf nach links zur nächsten öffnenden; die streichst du auch."
  - kosten: 2
    text: "Gibt es keine schließende mehr, lauf zurück und schau, ob noch eine öffnende übrig ist."
starter_code: |
  # Zustand liest -> schreibt geht danach
  such ( -> ( R such
turing:
  zeichen: ["(", ")", "X"]
  start: such
  ende: [ja, nein]
  kopf: anfang
  grenze: 2000
  sichtbar:
    - {band: "(())", soll_zustand: ja}
    - {band: "(()", soll_zustand: nein}
    - {band: ")(", soll_zustand: nein}
  versteckt:
    - {band: "()()(())", soll_zustand: ja}
    - {band: "", name: "leer", soll_zustand: ja}
    - {band: "(()))(", soll_zustand: nein}
    - {band: "((((()))))", soll_zustand: ja}
    - {band: "())", soll_zustand: nein}
    - {band: "(", soll_zustand: nein}
  teilschritte:
    - titel: Paare streichen
      text: "Zu jeder schließenden Klammer gehört eine öffnende davor: (()) hält in ja."
    - titel: Übrige öffnende
      text: "Bleibt eine öffnende übrig wie bei ((), hält die Maschine in nein."
      baender: ["(()"]
    - titel: Zu früh geschlossen
      text: "Bei )( fehlt die öffnende vor der schließenden: nein."
      baender: [")("]
    - titel: Alle Bänder
      text: "Zum Schluss die versteckten Bänder, auch ein leeres."
      baender: alle
  sterne: {zustaende: 3, zeilen: 10}
---

# Klammern prüfen

Stimmen die Klammern? `(())` und `()()` ja, `(()` und `)(` nein. Die Maschine hält in `ja` oder `nein`.

Neu ist das Zeichen `X`: die Maschine darf es schreiben, um sich zu merken, welche Klammern schon erledigt sind. Auf den Bändern steht es am Anfang nie.
