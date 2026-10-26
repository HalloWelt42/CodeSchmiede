---
schema_version: 1
id: e005-zwei-aufzuege
revision: 1
titel: "Zwei Aufzüge: wer fährt?"
sprache: python
task_type: aufzug
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 60
schaetz_minuten: 40
tags: [aufzug, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Aufzugsteuerung, Level 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 25
hints:
  - kosten: 1
    text: "takt() wird jetzt für jede Kabine einzeln gefragt; lage.aufzug sagt, für welche. Merk dir die Richtung je Kabine in einem dict."
  - kosten: 1
    text: "lage.aufzuege zeigt beide Kabinen (etage, richtung, tuer, ziele, drin). Ein Ruf gehört der Kabine, die näher dran ist; bei Gleichstand der mit dem kleineren Namen."
  - kosten: 2
    text: "Ziele in der eigenen Kabine gehören immer ihr selbst. Nur die Rufe werden aufgeteilt."
starter_code: |
  def takt(lage):
      # zwei Kabinen: lage.aufzug ist "a" oder "b", lage.aufzuege zeigt beide
      return "warten"
aufzug:
  haus: {etagen: 8, aufzuege: [a, b], plaetze: 6}
  sensoren: [wartend, lichtschranke, voll, aufzuege]
  aufbauend_auf: e004-buerohaus
  sichtbar:
    - name: Hotel
      dauer: 200
      fahrgaeste:
        - {von: 0, nach: 6, um: [2]}
        - {von: 7, nach: 0, um: [3]}
        - {von: 3, nach: 0, um: [10]}
        - {von: 0, nach: 4, um: [18, 19]}
        - {von: 5, nach: 1, um: [30]}
        - {von: 2, nach: 7, um: [45]}
        - {von: 6, nach: 0, um: [52, 53]}
        - {von: 0, nach: 3, um: [70]}
        - {von: 7, nach: 2, um: [85]}
        - {von: 1, nach: 6, um: [100]}
        - {von: 4, nach: 0, um: [115]}
        - {von: 0, nach: 7, um: [130, 131]}
  versteckt:
    - name: Messe
      dauer: 220
      fahrgaeste:
        - {von: zufall, nach: zufall, zufall: 0.12, bis: 160}
    - name: Check-in
      dauer: 200
      fahrgaeste:
        - {von: 0, nach: zufall, zufall: 0.1, bis: 140}
        - {von: zufall, nach: 0, zufall: 0.04, bis: 140}
    - name: Nachtportier
      dauer: 200
      fahrgaeste:
        - {von: 0, nach: 5, um: [10]}
        - {von: 7, nach: 0, um: [90]}
  teilschritte:
    - titel: Beide Kabinen fahren
      text: "Jede Kabine fährt sicher, niemand wird eingeklemmt, jeder kommt an; niemand wartet länger als 90 s."
      regeln:
        - {art: tuer_sicher}
        - {art: kein_einklemmen}
        - {art: bedient, hoechstens: 90}
    - titel: Sammeln
      text: "Jede Kabine nimmt unterwegs mit, wer in ihre Richtung will, und kehrt erst um, wenn für sie nichts mehr in der Richtung liegt."
      regeln:
        - {art: mitnehmen}
    - titel: Gut aufgeteilt
      text: "Niemand wartet länger als 45 s: dafür müssen sich die beiden die Rufe teilen."
      regeln:
        - {art: bedient, hoechstens: 45}
        - {art: zuegig, sekunden: 3}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: eine Messe, der Check-in und der Nachtportier."
      ablaeufe: alle
  sterne: {warten: 10, zeichen: 900}
---

# Zwei Aufzüge: wer fährt?

Ein Hotel mit acht Etagen und zwei Kabinen, `"a"` und `"b"`. Dein `takt(lage)` wird jetzt für jede Kabine einzeln gefragt; `lage.aufzug` sagt, für welche. `lage.aufzuege["a"]` und `lage.aufzuege["b"]` zeigen, wo beide gerade sind (`etage`, `richtung`, `tuer`, `ziele`, `drin`).

Fahren beide zu jedem Ruf, ist eine umsonst unterwegs; fährt immer nur eine, wartet die Hälfte zu lang. Die Kunst ist, die Rufe zu teilen. Ziele in einer Kabine gehören natürlich der Kabine selbst.
