---
schema_version: 1
id: e001-zwei-etagen
revision: 1
titel: Zwei Etagen
sprache: python
task_type: aufzug
runner_type: docker_python
schwierigkeit: anfaenger
schwierigkeit_score: 20
schaetz_minuten: 20
tags: [aufzug, bedingungen]
voraussetzungen: []
quelle:
  url: null
  notiz: Aufzugsteuerung, Level 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 15
hints:
  - kosten: 1
    text: "Erst die Tür: ist sie offen, \"warten\", solange jemand in der Tür steht oder hier noch jemand einsteigen will, sonst \"zu\"."
  - kosten: 1
    text: "Ist die Tür zu: will hier jemand rein oder raus (Ruf oder Ziel hier), \"auf\". Sonst hinfahren, wo ein Ruf oder Ziel ist."
starter_code: |
  def takt(lage):
      # lage.etage, lage.tuer, lage.rufe[1], lage.rufe[-1], lage.ziele, lage.lichtschranke
      return "warten"
aufzug:
  haus: {etagen: 2}
  sensoren: [lichtschranke]
  sichtbar:
    - name: Gartenhaus
      dauer: 90
      fahrgaeste:
        - {von: 0, nach: 1, um: [2, 30, 31, 62]}
        - {von: 1, nach: 0, um: [12, 45, 70]}
  versteckt:
    - name: Familienbesuch
      dauer: 120
      fahrgaeste:
        - {von: 0, nach: 1, um: [5, 5.5, 6, 6.5, 50]}
        - {von: 1, nach: 0, um: [20, 80, 80.5]}
    - name: Hin und her
      dauer: 120
      fahrgaeste:
        - {von: 0, nach: 1, zufall: 0.05}
        - {von: 1, nach: 0, zufall: 0.05}
  teilschritte:
    - titel: Hin und her
      text: "Wer ruft, wird abgeholt und an sein Ziel gebracht; niemand wartet länger als 30 s. Gefahren wird nur mit geschlossener Tür."
      regeln:
        - {art: tuer_sicher}
        - {art: bedient, hoechstens: 30}
    - titel: Niemand eingeklemmt
      text: "Die Tür geht erst zu, wenn niemand mehr in der Tür steht (lage.lichtschranke)."
      regeln:
        - {art: kein_einklemmen}
    - titel: Tür nicht länger offen als nötig
      text: "Sind alle drin, geht die Tür zu: höchstens 3 s offen, ohne dass jemand kommt oder geht."
      regeln:
        - {art: zuegig, sekunden: 3}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: Familienbesuch und ein Tag mit viel Hin und Her."
      ablaeufe: alle
  sterne: {warten: 6, zeichen: 300}
---

# Zwei Etagen

Ein kleiner Aufzug im Gartenhaus: Erdgeschoss und erster Stock. Leute rufen ihn, steigen ein, drücken ihr Ziel und wollen dort wieder raus.

Dein Programm ist die Funktion `takt(lage)`. Die Kabine fragt sie, sobald sie mit dem letzten Befehl fertig ist, und bekommt einen von fünf Befehlen zurück: `"hoch"`, `"runter"`, `"auf"`, `"zu"` oder `"warten"` (eine Sekunde). Bei offener Tür steigen erst alle aus, dann alle ein, einer nach dem anderen.

Was die Kabine weiß: `lage.etage` (0 ist das Erdgeschoss), `lage.tuer` (`"offen"` oder `"zu"`), die Rufe `lage.rufe[1]` (Etagen, an denen jemand nach oben will) und `lage.rufe[-1]` (nach unten), die gedrückten Ziele `lage.ziele` und `lage.lichtschranke` (jemand steht in der Tür).

Fahren mit offener Tür macht die Kabine übrigens nicht mit. Sie ist ja nicht lebensmüde.
