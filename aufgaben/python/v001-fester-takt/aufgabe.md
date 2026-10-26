---
schema_version: 1
id: v001-fester-takt
revision: 1
titel: Fußgängerampel im festen Takt
sprache: python
task_type: ampel
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 20
schaetz_minuten: 20
tags: [ampel, modulo]
voraussetzungen: []
quelle:
  url: null
  notiz: Ampelschule, Level 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 15
hints:
  - kosten: 1
    text: "lage.sekunde % 30 läuft immer wieder von 0 bis 29: so wiederholt sich ein Umlauf von 30 Sekunden von selbst."
  - kosten: 1
    text: "Schreib den Umlauf als Liste von Phasen (Dauer, Signal Autos, Signal Fußgänger) und zähl in takt() ab, in welcher Phase die Sekunde liegt."
starter_code: |
  def takt(lage):
      # lage.sekunde: Sekunden seit dem Start
      return {"auto": "gruen", "fuss": "rot"}
ampel:
  anlage: {vorlage: ueberweg}
  sichtbar:
    - name: Vormittag
      dauer: 90
      verkehr:
        - {zufahrt: west, alle: 4}
        - {zufahrt: ost, ab: 2, alle: 5}
        - {ueberweg: mitte, ab: 3, alle: 7}
  versteckt:
    - name: Schulschluss
      dauer: 120
      verkehr:
        - {zufahrt: west, alle: 5}
        - {zufahrt: ost, ab: 1, alle: 6}
        - {ueberweg: mitte, zufall: 0.3}
    - name: Berufsverkehr
      dauer: 120
      verkehr:
        - {zufahrt: west, alle: 2.5}
        - {zufahrt: ost, ab: 1, alle: 2.8}
        - {ueberweg: mitte, zufall: 0.08}
    - name: Sonntag
      dauer: 120
      verkehr:
        - {zufahrt: west, zufall: 0.08}
        - {zufahrt: ost, zufall: 0.06}
        - {ueberweg: mitte, um: [15, 70]}
  teilschritte:
    - titel: Abwechselnd Grün
      text: "Autos und Fußgänger bekommen abwechselnd Grün, nie beide zugleich. Niemand wartet länger als 45 s."
      regeln:
        - {art: feindlich}
        - {art: bedient, hoechstens: 45}
    - titel: Gelb vor Rot
      text: "Zwischen Grün und Rot zeigt die Autoampel mindestens 3 s Gelb."
      regeln:
        - {art: gelb, mindestens: 3}
    - titel: Räumzeit
      text: "Nach Gelb 2 s alles Rot, bevor die Fußgänger gehen; nach dem Grün der Fußgänger 3 s, bevor die Autos anfahren. Niemand wird überfahren."
      regeln:
        - {art: raeumzeit, auto: 2, fuss: 3}
        - {art: kein_unfall}
    - titel: Rot-Gelb vor Grün
      text: "Bevor die Autos Grün bekommen, zeigt ihre Ampel 1 s Rot-Gelb."
      regeln:
        - {art: rotgelb, dauer: 1}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: Schulschluss, Berufsverkehr und ein ruhiger Sonntag."
      ablaeufe: alle
  sterne: {fuss: 30, autos: 9, zeichen: 300}
---

# Fußgängerampel im festen Takt

Eine Fußgängerampel über eine zweispurige Straße, ganz ohne Taster: sie schaltet stur im Kreis, wie eine Uhr. Erst haben die Autos Grün, dann die Fußgänger, dann wieder die Autos.

Dein Programm ist die Funktion `takt(lage)`. Sie läuft jede Sekunde und gibt für jede Gruppe ein Signal zurück: für `"auto"` eins von `"gruen"`, `"gelb"`, `"rot"`, `"rotgelb"`, für `"fuss"` eins von `"gruen"`, `"rot"`. Mehr als `lage.sekunde` brauchst du hier nicht.

Ein Ziel nach dem anderen: klappt ein Teilschritt, kommt der nächste dazu. Mit "Ablauf" siehst du den Verkehr, mit "Prüfen" zählt es. Und keine Sorge: die Fußgänger sind nur Punkte. Trotzdem wäre es nett, sie heil rüberzubringen.
