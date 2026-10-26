---
schema_version: 1
id: e002-rufe-sammeln
revision: 1
titel: Rufe sammeln
sprache: python
task_type: aufzug
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 35
schaetz_minuten: 30
tags: [aufzug, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Aufzugsteuerung, Level 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 15
hints:
  - kosten: 1
    text: "Merk dir eine Richtung (1 hoch, -1 runter, 0 steht) außerhalb von takt(). Fahr in ihr weiter, solange dort noch ein Ruf oder Ziel liegt."
  - kosten: 1
    text: "Halten: wenn hier ein Ziel ist oder hier jemand in deine Richtung will. Erst wenn vor dir nichts mehr liegt, Richtung neu wählen, und dann auch die mitnehmen, die hier in die neue Richtung wollen."
  - kosten: 2
    text: "lage.rufe[richtung] geht nur für 1 und -1; bei richtung 0 hilft lage.rufe.get(richtung, set())."
starter_code: |
  def takt(lage):
      # sechs Etagen: 0 (EG) bis 5
      return "warten"
aufzug:
  haus: {etagen: 6}
  sensoren: [wartend, lichtschranke]
  aufbauend_auf: e001-zwei-etagen
  sichtbar:
    - name: Wohnhaus
      dauer: 150
      fahrgaeste:
        - {von: 0, nach: 4, um: [1]}
        - {von: 3, nach: 0, um: [4]}
        - {von: 5, nach: 2, um: [9]}
        - {von: 1, nach: 5, um: [14]}
        - {von: 4, nach: 1, um: [22]}
        - {von: 0, nach: 3, um: [35]}
        - {von: 2, nach: 0, um: [41]}
        - {von: 5, nach: 0, um: [58]}
        - {von: 3, nach: 5, um: [66]}
        - {von: 0, nach: 2, um: [80]}
        - {von: 4, nach: 0, um: [88]}
        - {von: 1, nach: 3, um: [101]}
  versteckt:
    - name: Feierabend
      dauer: 160
      fahrgaeste:
        - {von: 0, nach: zufall, zufall: 0.06}
        - {von: zufall, nach: 0, zufall: 0.04}
    - name: Durcheinander
      dauer: 180
      fahrgaeste:
        - {von: zufall, nach: zufall, zufall: 0.08, bis: 130}
    - name: Hochhausblick
      dauer: 140
      fahrgaeste:
        - {von: 0, nach: 5, um: [2, 40, 41]}
        - {von: 5, nach: 0, um: [20, 21, 75]}
        - {von: 2, nach: 4, um: [24]}
        - {von: 3, nach: 1, um: [30]}
  teilschritte:
    - titel: Alle kommen an
      text: "Jeder Ruf wird bedient, jedes Ziel erreicht; niemand wartet länger als 90 s. Tür sicher, niemand eingeklemmt."
      regeln:
        - {art: tuer_sicher}
        - {art: kein_einklemmen}
        - {art: bedient, hoechstens: 90}
    - titel: Unterwegs mitnehmen
      text: "Fährt die Kabine an einer Etage vorbei, an der jemand in ihre Richtung will, hält sie und nimmt ihn mit."
      regeln:
        - {art: mitnehmen}
    - titel: Erst umkehren, wenn alles erledigt ist
      text: "Die Richtung wechselt erst, wenn in ihr niemand mehr wartet und kein Ziel mehr liegt."
      regeln:
        - {art: umkehren}
    - titel: Zügig
      text: "Die Tür steht höchstens 3 s offen, ohne dass jemand kommt oder geht; niemand wartet länger als 60 s."
      regeln:
        - {art: zuegig, sekunden: 3}
        - {art: bedient, hoechstens: 60}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: Feierabend, Durcheinander und ein Blick vom Hochhaus."
      ablaeufe: alle
  sterne: {warten: 18, zeichen: 450}
---

# Rufe sammeln

Jetzt hat das Haus sechs Etagen, und es rufen viele durcheinander. Ein guter Aufzug fährt nicht kreuz und quer, sondern sammelt: er fährt in einer Richtung, hält unterwegs für alle, die dorthin wollen oder aussteigen, und kehrt erst um, wenn in dieser Richtung nichts mehr zu tun ist.

`lage.rufe[1]` sind die Etagen, an denen jemand nach oben will, `lage.rufe[-1]` die nach unten. `lage.wartend` zählt je Etage, wie viele dort stehen.

Kleiner Trost für alle, die an der falschen Etage einsteigen: steigt jemand ein, der eigentlich in die andere Richtung will, fährt er eben eine Runde mit. Ist im Aufzug ja warm.
