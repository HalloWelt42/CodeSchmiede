---
schema_version: 1
id: e006-stosszeit
revision: 1
titel: Stoßzeit am Morgen
sprache: python
task_type: aufzug
runner_type: docker_python
schwierigkeit: experte
schwierigkeit_score: 70
schaetz_minuten: 40
tags: [aufzug, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Aufzugsteuerung, Level 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 25
hints:
  - kosten: 1
    text: "Morgens kommen fast alle im EG an. Eine Kabine, die nichts zu tun hat, gehört dorthin."
  - kosten: 1
    text: "Das Programm aus dem Hotel ist ein guter Anfang; dazu das Parken aus dem Bürohaus, für jede Kabine."
starter_code: |
  def takt(lage):
      # zwei Kabinen, zehn Etagen, morgens um acht
      return "warten"
aufzug:
  haus: {etagen: 10, aufzuege: [a, b], plaetze: 8}
  sensoren: [wartend, lichtschranke, voll, aufzuege]
  aufbauend_auf: e005-zwei-aufzuege
  sichtbar:
    - name: Acht Uhr
      dauer: 270
      fahrgaeste:
        - {von: 0, nach: zufall, alle: 4, bis: 120}
        - {von: 0, nach: zufall, um: [150, 151, 152, 190]}
        - {von: 6, nach: 0, um: [60]}
        - {von: 9, nach: 2, um: [140]}
  versteckt:
    - name: Montag
      dauer: 240
      fahrgaeste:
        - {von: 0, nach: zufall, alle: 4.5, bis: 140}
        - {von: zufall, nach: 0, zufall: 0.02, bis: 160}
    - name: Brückentag
      dauer: 220
      fahrgaeste:
        - {von: 0, nach: zufall, zufall: 0.05, bis: 160}
  teilschritte:
    - titel: Alle kommen an
      text: "Beide Kabinen fahren sicher und sammeln, niemand wird eingeklemmt; niemand wartet länger als 90 s."
      regeln:
        - {art: tuer_sicher}
        - {art: kein_einklemmen}
        - {art: mitnehmen}
        - {art: bedient, hoechstens: 90}
    - titel: Im Erdgeschoss bereit
      text: "Wer nichts zu tun hat, fährt ins Erdgeschoss und wartet dort auf die Nächsten."
      regeln:
        - {art: parken, etage: 0, nach: 10}
    - titel: Zügig
      text: "Niemand wartet länger als 60 s; die Tür steht höchstens 3 s offen, ohne dass jemand kommt oder geht."
      regeln:
        - {art: bedient, hoechstens: 60}
        - {art: zuegig, sekunden: 3}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: ein Montag und ein Brückentag."
      ablaeufe: alle
  sterne: {warten: 18, zeichen: 920}
---

# Stoßzeit am Morgen

Acht Uhr im Bürohaus: alle paar Sekunden kommt jemand durch die Drehtür und will nach oben, jeder in eine andere Etage. Zwei Kabinen mit je acht Plätzen müssen das schaffen.

Was hilft: Kabinen, die nichts zu tun haben, stehen schon unten bereit, und die beiden teilen sich die Arbeit. Kaffee gibt es erst oben.
