---
schema_version: 1
id: v007-grosse-kreuzung
revision: 1
titel: Die große Kreuzung
sprache: python
task_type: ampel
runner_type: docker_python
schwierigkeit: experte
schwierigkeit_score: 75
schaetz_minuten: 50
tags: [ampel, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Ampelschule, Level 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 25
hints:
  - kosten: 1
    text: "Fünf Gruppen, eine Reihe: Nord-Süd, Linksabbieger Nord-Süd, Ost-West, Linksabbieger Ost-West, Fußgänger. Dran ist der Nächste in der Reihe, bei dem jemand wartet; Nord-Süd wartet immer."
  - kosten: 1
    text: "Rechtsabbieger kreuzen jeden Überweg. Darum gehen die Fußgänger in einer eigenen Phase, in der alle Autos Rot haben, dafür über alle vier Überwege zugleich."
  - kosten: 2
    text: "Nach den Fußgängern braucht die Räumzeit 3 s statt 2 s. Und vor jedem Rot-Gelb: lage.frei[ziel]."
starter_code: |
  def takt(lage):
      # Gruppen: "ns", "ns_links", "ow", "ow_links", "fuss"
      return {"ns": "gruen", "ns_links": "rot", "ow": "rot", "ow_links": "rot", "fuss": "rot"}
ampel:
  anlage:
    vorlage: kreuzung
    schleifen: true
    zufahrten:
      nord: {spuren: [{wege: [links], gruppe: ns_links}, {wege: [gerade, rechts], gruppe: ns}]}
      sued: {spuren: [{wege: [links], gruppe: ns_links}, {wege: [gerade, rechts], gruppe: ns}]}
      ost: {spuren: [{wege: [links], gruppe: ow_links}, {wege: [gerade, rechts], gruppe: ow}]}
      west: {spuren: [{wege: [links], gruppe: ow_links}, {wege: [gerade, rechts], gruppe: ow}]}
    ueberwege: {nord: fuss, sued: fuss, ost: fuss, west: fuss}
  sensoren: [taster, schleife, wartend, frei]
  aufbauend_auf: v006-linksabbieger
  sichtbar:
    - name: Innenstadt
      dauer: 180
      verkehr:
        - {weg: nord_gerade, alle: 7}
        - {weg: sued_gerade, ab: 2, alle: 7.5}
        - {weg: nord_rechts, ab: 5, alle: 21}
        - {weg: sued_rechts, ab: 11, alle: 25}
        - {weg: nord_links, um: [18, 19.5, 95, 150]}
        - {weg: sued_links, um: [50, 51.5, 120]}
        - {weg: ost_gerade, ab: 3, alle: 13}
        - {weg: west_gerade, ab: 8, alle: 14}
        - {weg: ost_rechts, um: [33, 110]}
        - {weg: west_links, um: [60, 61.5, 140]}
        - {weg: ost_links, um: [85]}
        - {ueberweg: nord, um: [25, 100]}
        - {ueberweg: ost, um: [40, 41, 130]}
        - {ueberweg: sued, um: [75]}
        - {ueberweg: west, um: [155]}
  versteckt:
    - name: Messe
      dauer: 180
      verkehr:
        - {zufahrt: nord, alle: 4.5}
        - {zufahrt: sued, ab: 1, alle: 5}
        - {zufahrt: ost, ab: 2, alle: 8}
        - {zufahrt: west, ab: 3, alle: 8.5}
        - {ueberweg: nord, zufall: 0.03}
        - {ueberweg: sued, zufall: 0.03}
        - {ueberweg: ost, zufall: 0.03}
        - {ueberweg: west, zufall: 0.03}
    - name: Lieferverkehr
      dauer: 200
      verkehr:
        - {zufahrt: nord, alle: 9}
        - {weg: sued_links, art: lkw, ab: 7, alle: 51}
        - {weg: ost_rechts, art: lkw, ab: 20, alle: 57}
        - {weg: west_gerade, art: lkw, ab: 33, alle: 61}
        - {zufahrt: ost, ab: 2, alle: 15}
        - {ueberweg: ost, ab: 10, alle: 29}
        - {ueberweg: nord, ab: 25, alle: 37}
    - name: Nachts um drei
      dauer: 180
      verkehr:
        - {zufahrt: nord, zufall: 0.03}
        - {zufahrt: west, zufall: 0.02}
        - {ueberweg: sued, um: [80]}
  teilschritte:
    - titel: Alle kommen dran
      text: "Was sich kreuzt, ist nie zugleich offen; das gilt auch für Rechtsabbieger und Überwege. Kein Unfall, und niemand wartet länger als 90 s, auch die Fußgänger nicht."
      regeln:
        - {art: feindlich}
        - {art: kein_unfall}
        - {art: bedient, hoechstens: 90}
    - titel: Sicher umschalten
      text: "Gelb vor Rot, Rot-Gelb vor Grün, Räumzeit 2 s nach Autos und 3 s nach Fußgängern."
      regeln:
        - {art: gelb, mindestens: 3}
        - {art: rotgelb, dauer: 1}
        - {art: raeumzeit, auto: 2, fuss: 3}
    - titel: Nur bei Bedarf
      text: "Linksabbieger, Ost-West und Fußgänger bekommen Grün nur, wenn dort jemand wartet; sonst ruht die Kreuzung auf Nord-Süd."
      regeln:
        - {art: nur_bei_bedarf, gruppen: [ns_links, ow, ow_links, fuss]}
        - {art: ruhe, gruppe: ns}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: Messe, Lieferverkehr mit Lkw und nachts um drei."
      ablaeufe: alle
  sterne: {fuss: 50, autos: 18, zeichen: 1000}
---

# Die große Kreuzung

Jetzt alles auf einmal: vier Zufahrten mit je zwei Spuren, eigene Linksabbieger in beide Richtungen, Rechtsabbieger und Überwege an allen vier Seiten. Fünf Gruppen: `"ns"`, `"ns_links"`, `"ow"`, `"ow_links"` und `"fuss"` für alle Überwege zusammen.

Die Rechtsabbieger kreuzen jeden Überweg, an dem sie vorbeimüssen. Darum gehen die Fußgänger hier in einer eigenen Phase, in der alle Autos stehen; dafür dürfen sie dann über alle vier Überwege zugleich.

Das Programm aus der Kreuzung mit Linksabbiegern ist ein guter Anfang. Viel Glück, und ein Tipp vom Straßenbauamt: lieber ein paar Sekunden länger Rot als einmal Blechschaden.
