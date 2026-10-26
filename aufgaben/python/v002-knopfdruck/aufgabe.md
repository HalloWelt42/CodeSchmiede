---
schema_version: 1
id: v002-knopfdruck
revision: 1
titel: Fußgänger auf Knopfdruck
sprache: python
task_type: ampel
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 25
tags: [ampel, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Ampelschule, Level 2
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 15
hints:
  - kosten: 1
    text: "Merk dir in einer Variablen außerhalb von takt(), in welcher Phase du bist und seit wie vielen Sekunden. Mit global darf takt() sie ändern."
  - kosten: 1
    text: "Eine Tabelle hilft: je Phase die beiden Signale und die Mindestdauer, dazu, welche Phase danach kommt."
  - kosten: 2
    text: "Bevor die Fußgänger Grün bekommen, frag lage.frei[\"fuss\"]: ein langsamer Lkw braucht für den Überweg länger als Gelb und Räumzeit."
starter_code: |
  def takt(lage):
      # lage.taster: jemand wartet am Überweg
      return {"auto": "gruen", "fuss": "rot"}
ampel:
  anlage: {vorlage: ueberweg}
  sensoren: [taster, frei]
  aufbauend_auf: v001-fester-takt
  sichtbar:
    - name: Feierabend
      dauer: 90
      verkehr:
        - {zufahrt: west, alle: 3.5}
        - {zufahrt: ost, ab: 1.7, alle: 4.5}
        - {ueberweg: mitte, um: [6, 9, 41, 47, 78]}
  versteckt:
    - name: Stoßzeit
      dauer: 120
      verkehr:
        - {zufahrt: west, alle: 2.6}
        - {zufahrt: ost, ab: 1, alle: 2.9}
        - {ueberweg: mitte, zufall: 0.07}
    - name: Lieferverkehr
      dauer: 150
      verkehr:
        - {zufahrt: west, art: lkw, ab: 1, alle: 10}
        - {zufahrt: ost, art: lkw, ab: 4, alle: 13}
        - {zufahrt: ost, ab: 2, alle: 6}
        - {ueberweg: mitte, ab: 2, alle: 9}
    - name: ruhiger Abend
      dauer: 120
      verkehr:
        - {zufahrt: west, alle: 9}
        - {zufahrt: ost, ab: 4, alle: 11}
        - {ueberweg: mitte, um: [20, 65, 100]}
  teilschritte:
    - titel: Grün, bis jemand drückt
      text: "Die Autos haben Grün. Drückt jemand den Taster, nehmen sie es spätestens nach 30 s zurück; wartet niemand, bleibt es Grün."
      regeln:
        - {art: ruhe, gruppe: auto}
        - {art: reagiert, gruppe: auto, binnen: 30}
    - titel: Gelb vor Rot
      text: "Zwischen Grün und Rot zeigt die Autoampel mindestens 3 s Gelb."
      regeln:
        - {art: gelb, mindestens: 3}
    - titel: Fußgänger gehen
      text: "Bei Rot für die Autos bekommen die Fußgänger Grün, nie beide zugleich. Niemand wartet länger als 60 s, und niemand wird überfahren."
      regeln:
        - {art: feindlich}
        - {art: bedient, gruppen: [fuss], hoechstens: 60}
        - {art: kein_unfall}
    - titel: Räumzeit
      text: "Nach Gelb 2 s alles Rot, bevor die Fußgänger gehen; nach dem Grün der Fußgänger 3 s, bevor die Autos wieder anfahren."
      regeln:
        - {art: raeumzeit, auto: 2, fuss: 3}
    - titel: Zurück zu den Autos
      text: "Vor dem Grün der Autos 1 s Rot-Gelb."
      regeln:
        - {art: rotgelb, dauer: 1}
    - titel: Mindestgrün
      text: "Die Autos behalten mindestens 20 s Grün am Stück, auch wenn ständig jemand drückt."
      regeln:
        - {art: mindestgruen, sekunden: 20, gruppen: [auto]}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: Stoßzeit, Lieferverkehr mit langsamem Lkw und ein ruhiger Abend."
      ablaeufe: alle
  sterne: {fuss: 25, autos: 6, zeichen: 600}
---

# Fußgänger auf Knopfdruck

Eine Fußgängerampel über eine zweispurige Straße. Die Autos haben Grün, bis jemand den Taster drückt. Dann schaltet die Ampel sicher um, lässt die Fußgänger gehen und gibt den Autos wieder Grün.

Dein Programm ist die Funktion `takt(lage)`. Sie läuft jede Sekunde, bekommt in `lage` die Sensoren und gibt für jede Gruppe ein Signal zurück: für `"auto"` eins von `"gruen"`, `"gelb"`, `"rot"`, `"rotgelb"`, für `"fuss"` eins von `"gruen"`, `"rot"`.

Ein Ziel nach dem anderen: klappt ein Teilschritt, kommt der nächste dazu, und dein Programm wächst mit. Wer sich traut, schaltet auf "Alles auf einmal". Unfälle sieht man übrigens sofort. Der Straßenreinigung zuliebe: lieber nicht.
