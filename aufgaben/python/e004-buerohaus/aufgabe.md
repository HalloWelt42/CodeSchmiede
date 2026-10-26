---
schema_version: 1
id: e004-buerohaus
revision: 1
titel: Bürohaus
sprache: python
task_type: aufzug
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 50
schaetz_minuten: 30
tags: [aufzug, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Aufzugsteuerung, Level 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 20
hints:
  - kosten: 1
    text: "Im Bürohaus kommen die meisten unten an. Steht die Kabine ohne Arbeit irgendwo oben, ist der Weg zum Nächsten lang."
  - kosten: 1
    text: "Hat die Kabine nichts mehr zu tun und steht nicht im EG: \"runter\". Ein neuer Ruf unterwegs ändert die Richtung wie gewohnt."
starter_code: |
  def takt(lage):
      # zehn Etagen: 0 (EG) bis 9
      return "warten"
aufzug:
  haus: {etagen: 10, plaetze: 6}
  sensoren: [wartend, lichtschranke, voll]
  aufbauend_auf: e003-volle-kabine
  sichtbar:
    - name: Arbeitstag
      dauer: 240
      fahrgaeste:
        - {von: 0, nach: zufall, um: [2, 3, 15, 33, 34, 60, 95, 120, 140]}
        - {von: 0, nach: 8, um: [172]}
        - {von: zufall, nach: 0, um: [45, 80, 81, 130, 160]}
        - {von: 7, nach: 3, um: [100]}
  versteckt:
    - name: Morgens
      dauer: 200
      fahrgaeste:
        - {von: 0, nach: zufall, zufall: 0.05, bis: 150}
    - name: Abends
      dauer: 200
      fahrgaeste:
        - {von: zufall, nach: 0, zufall: 0.07, bis: 150}
    - name: Ruhiger Freitag
      dauer: 200
      fahrgaeste:
        - {von: 0, nach: 9, um: [5, 120]}
        - {von: 6, nach: 0, um: [60]}
  teilschritte:
    - titel: Alle kommen an
      text: "Wie bisher: sicher, niemand eingeklemmt, sammeln, niemand wartet länger als 120 s."
      regeln:
        - {art: tuer_sicher}
        - {art: kein_einklemmen}
        - {art: bedient, hoechstens: 120}
        - {art: mitnehmen}
        - {art: umkehren}
    - titel: Im Erdgeschoss parken
      text: "Hat die Kabine nichts zu tun, fährt sie ins Erdgeschoss und wartet dort."
      regeln:
        - {art: parken, etage: 0, nach: 10}
    - titel: Zügig
      text: "Die Tür steht höchstens 3 s offen, ohne dass jemand kommt oder geht; niemand wartet länger als 90 s."
      regeln:
        - {art: zuegig, sekunden: 3}
        - {art: bedient, hoechstens: 90}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: morgens, abends und ein ruhiger Freitag."
      ablaeufe: alle
  sterne: {warten: 20, zeichen: 560}
---

# Bürohaus

Zehn Etagen, und fast alle Wege führen über das Erdgeschoss: morgens rein und hoch, abends runter und raus. Ein Aufzug, der ohne Arbeit oben herumsteht, lässt die Leute unten unnötig warten.

Darum parkt ein guter Aufzug im Bürohaus im Erdgeschoss, sobald er nichts mehr zu tun hat. Der Rest ist Sammeln wie gehabt, nur höher.
