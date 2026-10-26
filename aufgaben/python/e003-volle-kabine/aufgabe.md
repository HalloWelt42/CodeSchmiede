---
schema_version: 1
id: e003-volle-kabine
revision: 1
titel: Volle Kabine
sprache: python
task_type: aufzug
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 40
schaetz_minuten: 25
tags: [aufzug, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Aufzugsteuerung, Level 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 15
hints:
  - kosten: 1
    text: "Ist die Kabine voll (lage.voll), steigt niemand mehr ein. Wer bei offener Tür auf die Wartenden wartet, wartet dann ewig."
  - kosten: 1
    text: "Eine volle Kabine braucht auch nicht für Rufe zu halten, nur für Ziele."
starter_code: |
  def takt(lage):
      # neu: lage.voll, lage.drin (wie viele in der Kabine sind)
      return "warten"
aufzug:
  haus: {etagen: 6, plaetze: 4}
  sensoren: [wartend, lichtschranke, voll]
  aufbauend_auf: e002-rufe-sammeln
  sichtbar:
    - name: Schulklasse
      dauer: 180
      fahrgaeste:
        - {von: 0, nach: 4, um: [2, 2.5, 3, 3.5, 4, 4.5, 5]}
        - {von: 2, nach: 4, um: [8]}
        - {von: 4, nach: 0, um: [40, 40.5, 41, 41.5, 42, 42.5]}
        - {von: 3, nach: 0, um: [50]}
        - {von: 5, nach: 1, um: [95, 95.5]}
        - {von: 1, nach: 5, um: [110]}
  versteckt:
    - name: Reisegruppe
      dauer: 200
      fahrgaeste:
        - {von: 0, nach: 5, um: [3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6]}
        - {von: 5, nach: 0, um: [70, 70.5, 71, 71.5, 72, 72.5]}
        - {von: zufall, nach: zufall, zufall: 0.03, bis: 150}
    - name: Hausfest
      dauer: 200
      fahrgaeste:
        - {von: 0, nach: 3, alle: 4, bis: 60}
        - {von: 3, nach: 0, alle: 5, ab: 80, bis: 150}
  teilschritte:
    - titel: Alle kommen an
      text: "Auch wenn nicht alle in die Kabine passen: jeder kommt an, niemand wartet länger als 120 s. Tür sicher, niemand eingeklemmt."
      regeln:
        - {art: tuer_sicher}
        - {art: kein_einklemmen}
        - {art: bedient, hoechstens: 120}
    - titel: Sammeln wie bisher
      text: "Unterwegs mitnehmen, wer in die Fahrtrichtung will und noch Platz hat; erst umkehren, wenn alles erledigt ist."
      regeln:
        - {art: mitnehmen}
        - {art: umkehren}
    - titel: Zügig
      text: "Die Tür steht höchstens 3 s offen, ohne dass jemand kommt oder geht, auch bei voller Kabine."
      regeln:
        - {art: zuegig, sekunden: 3}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: eine Reisegruppe und ein Hausfest."
      ablaeufe: alle
  sterne: {warten: 20, zeichen: 520}
---

# Volle Kabine

Die Kabine hat jetzt nur vier Plätze, und es kommen Gruppen: eine ganze Schulklasse will auf einmal nach oben. Wer nicht mehr hineinpasst, bleibt stehen und wartet auf die nächste Fahrt.

`lage.voll` sagt, ob noch jemand hineinpasst, `lage.drin`, wie viele in der Kabine sind. Eine Kabine, die bei offener Tür auf Leute wartet, die gar nicht mehr hineinpassen, steht bis zum Sankt-Nimmerleins-Tag.
