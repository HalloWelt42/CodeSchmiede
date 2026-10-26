---
schema_version: 1
id: e007-sonderfaelle
revision: 1
titel: "Sonderfälle: Überlast und Feueralarm"
sprache: python
task_type: aufzug
runner_type: docker_python
schwierigkeit: experte
schwierigkeit_score: 70
schaetz_minuten: 35
tags: [aufzug, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Aufzugsteuerung, Level 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 20
hints:
  - kosten: 1
    text: "Bei lage.ueberlast bleibt die Tür offen: wer zuletzt einstieg, steigt von selbst wieder aus, wenn du wartest."
  - kosten: 1
    text: "Bei lage.feuer zählt nur noch eins: Tür zu (wenn niemand drinsteht), ohne Halt ins EG, dort \"auf\" und dann nur noch \"warten\"."
starter_code: |
  def takt(lage):
      # neu: lage.ueberlast und lage.feuer
      return "warten"
aufzug:
  haus: {etagen: 6, plaetze: 6, last: 500}
  sensoren: [wartend, lichtschranke, voll, ueberlast, feuer]
  aufbauend_auf: e003-volle-kabine
  sichtbar:
    - name: Alltag
      dauer: 150
      fahrgaeste:
        - {von: 0, nach: 3, um: [2, 50]}
        - {von: 4, nach: 0, um: [20]}
        - {von: 2, nach: 5, um: [70]}
        - {von: 5, nach: 1, um: [95]}
    - name: Umzug
      dauer: 180
      fahrgaeste:
        - {von: 0, nach: 4, um: [2, 2.5]}
        - {von: 0, nach: 4, um: [3], gewicht: 380}
        - {von: 0, nach: 4, um: [40], gewicht: 380}
        - {von: 4, nach: 0, um: [90, 90.5]}
    - name: Feueralarm
      dauer: 150
      feuer: 40
      fahrgaeste:
        - {von: 0, nach: 5, um: [30]}
        - {von: 3, nach: 0, um: [38]}
        - {von: 2, nach: 4, um: [60]}
  versteckt:
    - name: Klavierlieferung
      dauer: 200
      fahrgaeste:
        - {von: 0, nach: 5, um: [5, 5.5, 6, 6.5]}
        - {von: 0, nach: 5, um: [7], gewicht: 420}
        - {von: zufall, nach: zufall, zufall: 0.03, bis: 140}
    - name: Alarm in der Stoßzeit
      dauer: 150
      feuer: 25
      fahrgaeste:
        - {von: 0, nach: zufall, alle: 3, bis: 60}
  teilschritte:
    - titel: Alltag
      text: "Wie bisher: sicher, niemand eingeklemmt, sammeln, jeder kommt an; niemand wartet länger als 90 s."
      regeln:
        - {art: tuer_sicher}
        - {art: kein_einklemmen}
        - {art: mitnehmen}
        - {art: bedient, hoechstens: 90}
    - titel: Überlast
      text: "Ist die Kabine zu schwer (lage.ueberlast), bleibt die Tür offen, bis wieder genug ausgestiegen sind."
      regeln:
        - {art: ueberlast}
      ablaeufe: [Umzug]
    - titel: Feueralarm
      text: "Bei Feueralarm (lage.feuer) ohne Halt ins Erdgeschoss, dort öffnen und stehen bleiben, binnen 30 s."
      regeln:
        - {art: feuer, sekunden: 30}
      ablaeufe: [Feueralarm]
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: eine Klavierlieferung und ein Alarm mitten in der Stoßzeit."
      ablaeufe: alle
  sterne: {warten: 6, zeichen: 740}
---

# Sonderfälle: Überlast und Feueralarm

Die Kabine trägt höchstens 500 kg. Normalerweise reicht das für sechs Leute, aber heute ist Umzug, und jemand schiebt ein Klavier herein. Meldet `lage.ueberlast`, darf die Tür nicht zugehen; wer zuletzt kam, steigt dann von selbst wieder aus.

Und wenn `lage.feuer` meldet, gibt es nur noch eins: ohne Halt ins Erdgeschoss, Tür auf, stehen bleiben. Eingestiegen wird da nicht mehr.

Jeder Sonderfall hat seinen eigenen sichtbaren Ablauf. Das Klavier ist übrigens unversichert.
