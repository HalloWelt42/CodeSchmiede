---
schema_version: 1
id: v006-linksabbieger
revision: 1
titel: Linksabbieger mit eigener Phase
sprache: python
task_type: ampel
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 60
schaetz_minuten: 40
tags: [ampel, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Ampelschule, Level 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 20
hints:
  - kosten: 1
    text: "Denk in Übergängen statt in einer festen Reihe: wer hat Grün, und wer ist als Nächstes dran? Dazwischen immer Gelb, Räumzeit und Rot-Gelb."
  - kosten: 1
    text: "Merk dir einen Zustand (\"gruen\", \"gelb\", \"raeumen\", \"an\"), die Gruppe mit Grün und das Ziel des Übergangs. Ein Dict je Gruppe mit \"rot\" ist der Anfang jedes Rückgabewerts."
  - kosten: 2
    text: "Die Linksabbieger kommen nur dran, wenn ihre Schleife meldet. Vor jedem Rot-Gelb: lage.frei[ziel], damit kein Lkw mehr in der Kreuzung steht."
starter_code: |
  def takt(lage):
      # "ns_links": Linksabbieger aus Nord und Süd, eigene Spur, eigene Ampel
      return {"ns": "gruen", "ns_links": "rot", "ow": "rot"}
ampel:
  anlage:
    vorlage: kreuzung
    schleifen: true
    zufahrten:
      nord: {spuren: [{wege: [links], gruppe: ns_links}, {wege: [gerade, rechts], gruppe: ns}]}
      sued: {spuren: [{wege: [links], gruppe: ns_links}, {wege: [gerade, rechts], gruppe: ns}]}
      ost: {spuren: [{wege: [gerade, rechts], gruppe: ow}]}
      west: {spuren: [{wege: [gerade, rechts], gruppe: ow}]}
  sensoren: [schleife, wartend, frei]
  sichtbar:
    - name: Ortsdurchfahrt
      dauer: 150
      verkehr:
        - {weg: nord_gerade, alle: 6}
        - {weg: sued_gerade, ab: 2, alle: 6.5}
        - {weg: nord_rechts, ab: 4, alle: 19}
        - {weg: sued_rechts, ab: 9, alle: 23}
        - {weg: nord_links, um: [14, 15.5, 70, 118]}
        - {weg: sued_links, um: [40, 41.5, 43, 97]}
        - {zufahrt: ost, um: [25, 80, 81.5, 130]}
        - {zufahrt: west, um: [55, 105, 106.5]}
  versteckt:
    - name: Einkaufszentrum
      dauer: 150
      verkehr:
        - {weg: nord_gerade, alle: 5}
        - {weg: sued_gerade, ab: 2, alle: 5.5}
        - {weg: nord_links, zufall: 0.12}
        - {weg: sued_links, zufall: 0.12}
        - {zufahrt: ost, zufall: 0.08}
        - {zufahrt: west, zufall: 0.08}
    - name: Baustellenverkehr
      dauer: 180
      verkehr:
        - {weg: nord_gerade, alle: 8}
        - {weg: sued_links, art: lkw, ab: 6, alle: 47}
        - {zufahrt: ost, art: lkw, ab: 25, alle: 53}
        - {zufahrt: west, ab: 3, alle: 9}
        - {weg: nord_links, zufall: 0.05}
    - name: Ruhige Nacht
      dauer: 150
      verkehr:
        - {weg: nord_gerade, zufall: 0.05}
        - {weg: sued_links, um: [60]}
        - {zufahrt: west, um: [100]}
  teilschritte:
    - titel: Alle kommen dran
      text: "Linksabbieger kreuzen den Gegenverkehr: nie zugleich mit Nord-Süd geradeaus, nie zugleich mit Ost-West. Kein Blechschaden, und niemand wartet länger als 60 s."
      regeln:
        - {art: feindlich}
        - {art: kein_unfall}
        - {art: bedient, hoechstens: 60}
    - titel: Sicher umschalten
      text: "Gelb vor Rot, Rot-Gelb vor Grün, 2 s Räumzeit."
      regeln:
        - {art: gelb, mindestens: 3}
        - {art: rotgelb, dauer: 1}
        - {art: raeumzeit, auto: 2}
    - titel: Linkspfeil nur bei Bedarf
      text: "Die Linksabbieger und Ost-West bekommen Grün nur, wenn auf ihrer Schleife jemand steht; sonst ruht die Kreuzung auf Nord-Süd."
      regeln:
        - {art: nur_bei_bedarf, gruppen: [ns_links, ow]}
        - {art: ruhe, gruppe: ns}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: Einkaufszentrum, Baustellenverkehr mit Lkw und eine ruhige Nacht."
      ablaeufe: alle
  sterne: {autos: 11, zeichen: 850}
---

# Linksabbieger mit eigener Phase

Nord und Süd haben jetzt zwei Spuren: links eine für Linksabbieger, rechts eine für geradeaus und rechts. Wer links abbiegt, kreuzt den Gegenverkehr. Darum bekommen die Linksabbieger eine eigene Ampel (Gruppe `"ns_links"`) mit einer eigenen Phase.

Drei Gruppen also: `"ns"`, `"ns_links"`, `"ow"`. Die Pfeile auf der Fahrbahn zeigen, welche Spur wohin darf. Rechts abbiegen geht zusammen mit geradeaus; die Wege, die sich dabei treffen, kennt die Anlage selbst.
