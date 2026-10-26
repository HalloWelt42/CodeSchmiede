---
schema_version: 1
id: v008-sonderfaelle
revision: 1
titel: "Sonderfälle: Blaulicht, Nacht und Störung"
sprache: python
task_type: ampel
runner_type: docker_python
schwierigkeit: experte
schwierigkeit_score: 80
schaetz_minuten: 50
tags: [ampel, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Ampelschule, Level 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 25
hints:
  - kosten: 1
    text: "Meldet sich ein Einsatzfahrzeug an (lage.einsatz ist eine Gruppe), ist nur diese Gruppe dran, sofort und ohne Mindestgrün der anderen abzuwarten. Gelb und Räumzeit bleiben."
  - kosten: 1
    text: "Nachts: aus Grün über Gelb ins Blinken (\"gelb_blinkt\" für beide). Wenn die Nacht vorbei ist: erst alles Rot, dann Rot-Gelb und Grün für die Hauptstraße."
  - kosten: 2
    text: "Meldet lage.stoerung die Gruppe \"ow\", kann die Schleife dort nicht mehr melden. Dann bekommt Ost-West eben alle 25 s Grün, ob jemand wartet oder nicht."
starter_code: |
  def takt(lage):
      # lage.einsatz, lage.nacht und lage.stoerung sind neu
      return {"ns": "gruen", "ow": "rot"}
ampel:
  anlage:
    vorlage: kreuzung
    schleifen: true
    vorfahrt: [ns]
    zufahrten:
      nord: {spuren: [{wege: [gerade], gruppe: ns}]}
      sued: {spuren: [{wege: [gerade], gruppe: ns}]}
      ost: {spuren: [{wege: [gerade], gruppe: ow}]}
      west: {spuren: [{wege: [gerade], gruppe: ow}]}
  sensoren: [schleife, wartend, frei, einsatz, nacht, stoerung]
  aufbauend_auf: v004-kontaktschleifen
  sichtbar:
    - name: Alltag
      dauer: 120
      verkehr:
        - {zufahrt: nord, alle: 5}
        - {zufahrt: sued, ab: 2, alle: 5.5}
        - {zufahrt: ost, um: [15, 16.5, 70]}
        - {zufahrt: west, um: [40, 95, 96.5]}
    - name: Blaulicht
      dauer: 120
      verkehr:
        - {zufahrt: nord, alle: 5}
        - {zufahrt: sued, ab: 2, alle: 5.5}
        - {zufahrt: ost, um: [20, 75]}
        - {zufahrt: west, art: einsatz, um: [40]}
        - {zufahrt: west, um: [88, 89.5]}
        - {zufahrt: sued, art: einsatz, um: [100]}
    - name: Nacht
      dauer: 150
      nacht: [[20, 110]]
      verkehr:
        - {zufahrt: nord, zufall: 0.06}
        - {zufahrt: sued, zufall: 0.06}
        - {zufahrt: ost, um: [35, 60, 61.5, 90]}
        - {zufahrt: west, um: [48, 100, 130]}
    - name: Störung
      dauer: 150
      stoerung: {gruppe: ow, ab: 20}
      verkehr:
        - {zufahrt: nord, alle: 5}
        - {zufahrt: sued, ab: 2, alle: 5.5}
        - {zufahrt: ost, um: [10, 50, 51.5, 100]}
        - {zufahrt: west, um: [30, 80, 125]}
  versteckt:
    - name: Großeinsatz
      dauer: 150
      verkehr:
        - {zufahrt: nord, alle: 4.5}
        - {zufahrt: sued, ab: 1, alle: 5}
        - {zufahrt: ost, zufall: 0.08}
        - {zufahrt: west, zufall: 0.08}
        - {zufahrt: ost, art: einsatz, um: [30]}
        - {zufahrt: nord, art: einsatz, um: [70]}
        - {zufahrt: west, art: einsatz, um: [115]}
    - name: Nacht mit Störung
      dauer: 160
      nacht: [[0, 60]]
      stoerung: {gruppe: ow, ab: 75}
      verkehr:
        - {zufahrt: nord, zufall: 0.08}
        - {zufahrt: sued, zufall: 0.08}
        - {zufahrt: ost, zufall: 0.05}
        - {zufahrt: west, zufall: 0.05}
    - name: Feierabend
      dauer: 150
      verkehr:
        - {zufahrt: nord, alle: 3.5}
        - {zufahrt: sued, ab: 1, alle: 3.8}
        - {zufahrt: ost, alle: 9}
        - {zufahrt: west, ab: 4, alle: 10}
  teilschritte:
    - titel: Sicher nach Bedarf
      text: "Wie bei den Kontaktschleifen: sicher umschalten, Nord-Süd ruht auf Grün, niemand wartet länger als 60 s."
      regeln:
        - {art: feindlich}
        - {art: gelb, mindestens: 3}
        - {art: rotgelb, dauer: 1}
        - {art: raeumzeit, auto: 2}
        - {art: kein_unfall}
        - {art: ruhe, gruppe: ns}
        - {art: bedient, hoechstens: 60}
    - titel: Blaulicht
      text: "Meldet sich ein Einsatzfahrzeug an, bekommt seine Richtung rechtzeitig Grün: es hält nie an."
      regeln:
        - {art: einsatz, halt: 0}
      ablaeufe: [Blaulicht]
    - titel: Nachtbetrieb
      text: "Nachts blinken beide Ampeln gelb, spätestens 6 s nach Beginn der Nacht; Ost-West achtet dann selbst auf die Vorfahrt. Danach geht es sicher zurück in den Tag."
      regeln:
        - {art: nacht, wechsel: 6}
      ablaeufe: [Nacht]
    - titel: Störung
      text: "Fällt die Schleife von Ost-West aus, kommt Ost-West trotzdem dran: niemand wartet länger als 60 s."
      ablaeufe: [Störung]
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: ein Großeinsatz, eine Nacht mit Störung und Feierabendverkehr."
      ablaeufe: alle
  sterne: {autos: 6, zeichen: 1100}
---

# Sonderfälle: Blaulicht, Nacht und Störung

Die Kreuzung mit Kontaktschleifen bekommt drei Sonderfälle, jeder in einem eigenen Ablauf:

- **Blaulicht:** Ein Einsatzfahrzeug meldet sich gut zehn Sekunden vorher an; `lage.einsatz` nennt dann seine Gruppe. Es soll ohne anzuhalten durchkommen.
- **Nacht:** Solange `lage.nacht` gilt, blinken beide Ampeln gelb (`"gelb_blinkt"`). Nord-Süd hat Vorfahrt, Ost-West schaut selbst.
- **Störung:** Meldet `lage.stoerung` eine Gruppe, liefert deren Kontaktschleife nichts mehr. Wer nur auf die Schleife hört, lässt Ost-West ewig warten.

Das Programm von den Kontaktschleifen ist ein guter Anfang. Und falls jemand fragt: Ja, die Feuerwehr hat sich über die vielen Proben schon beschwert.
