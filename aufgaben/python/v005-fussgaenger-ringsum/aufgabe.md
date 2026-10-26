---
schema_version: 1
id: v005-fussgaenger-ringsum
revision: 1
titel: Kreuzung mit Fußgängern ringsum
sprache: python
task_type: ampel
runner_type: docker_python
schwierigkeit: fortgeschritten
schwierigkeit_score: 55
schaetz_minuten: 40
tags: [ampel, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Ampelschule, Level 5
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 20
hints:
  - kosten: 1
    text: "Fußgänger gehen mit dem Verkehr, dessen Weg sie nicht kreuzen: \"fuss_ow\" (Überwege Ost und West) zusammen mit Nord-Süd, \"fuss_ns\" zusammen mit Ost-West."
  - kosten: 1
    text: "Gib jeder Fußgängergruppe einen eigenen Zähler für ihr Grün. Die Autophase darf erst wechseln, wenn ihre Fußgänger wieder Rot haben."
  - kosten: 2
    text: "Ein Lkw braucht für die Kreuzung länger als Gelb und Räumzeit. Frag lage.frei[...] für die Gruppe, die als Nächste öffnen will."
starter_code: |
  def takt(lage):
      # neue Gruppen: "fuss_ns" (Überwege Nord und Süd), "fuss_ow" (Überwege Ost und West)
      return {"ns": "gruen", "ow": "rot", "fuss_ns": "rot", "fuss_ow": "rot"}
ampel:
  anlage:
    vorlage: kreuzung
    schleifen: true
    zufahrten:
      nord: {spuren: [{wege: [gerade], gruppe: ns}]}
      sued: {spuren: [{wege: [gerade], gruppe: ns}]}
      ost: {spuren: [{wege: [gerade], gruppe: ow}]}
      west: {spuren: [{wege: [gerade], gruppe: ow}]}
    ueberwege: {nord: fuss_ns, sued: fuss_ns, ost: fuss_ow, west: fuss_ow}
  sensoren: [taster, schleife, wartend, frei]
  aufbauend_auf: v004-kontaktschleifen
  sichtbar:
    - name: Wohnviertel
      dauer: 150
      verkehr:
        - {zufahrt: nord, alle: 5}
        - {zufahrt: sued, ab: 2, alle: 5.5}
        - {zufahrt: ost, um: [20, 21.5, 70, 112]}
        - {zufahrt: west, um: [45, 100, 101.5]}
        - {ueberweg: nord, um: [8, 60, 61, 120]}
        - {ueberweg: sued, um: [30, 95]}
        - {ueberweg: ost, um: [15, 50, 51, 105]}
        - {ueberweg: west, um: [75, 130]}
  versteckt:
    - name: Schulweg
      dauer: 150
      verkehr:
        - {zufahrt: nord, alle: 6}
        - {zufahrt: sued, ab: 3, alle: 6}
        - {zufahrt: ost, zufall: 0.06}
        - {zufahrt: west, zufall: 0.06}
        - {ueberweg: nord, zufall: 0.08}
        - {ueberweg: sued, zufall: 0.08}
        - {ueberweg: ost, zufall: 0.08}
        - {ueberweg: west, zufall: 0.08}
    - name: Lieferverkehr
      dauer: 180
      verkehr:
        - {zufahrt: nord, alle: 7}
        - {zufahrt: sued, art: lkw, ab: 5, alle: 23}
        - {zufahrt: ost, art: lkw, ab: 11, alle: 29}
        - {zufahrt: west, zufall: 0.05}
        - {ueberweg: nord, ab: 4, alle: 13}
        - {ueberweg: ost, ab: 9, alle: 17}
        - {ueberweg: west, ab: 2, alle: 19}
    - name: Abendruhe
      dauer: 150
      verkehr:
        - {zufahrt: nord, zufall: 0.05}
        - {zufahrt: sued, zufall: 0.05}
        - {ueberweg: ost, um: [40]}
        - {ueberweg: sued, um: [90]}
  teilschritte:
    - titel: Fußgänger gehen mit
      text: "Alle vier Überwege bekommen Grün, nie zugleich mit Verkehr, der ihren Weg kreuzt. Niemand wartet länger als 60 s, niemand wird überfahren."
      regeln:
        - {art: feindlich}
        - {art: bedient, hoechstens: 60}
        - {art: kein_unfall}
    - titel: Sicher umschalten
      text: "Gelb vor Rot, Rot-Gelb vor Grün. Räumzeit: 2 s nach Autos, 3 s nach Fußgängern."
      regeln:
        - {art: gelb, mindestens: 3}
        - {art: rotgelb, dauer: 1}
        - {art: raeumzeit, auto: 2, fuss: 3}
    - titel: Nur auf Knopfdruck
      text: "Fußgänger bekommen Grün nur, wenn an ihrem Überweg jemand gedrückt hat."
      regeln:
        - {art: nur_bei_bedarf, gruppen: [fuss_ns, fuss_ow]}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: Schulweg, Lieferverkehr mit langsamen Lkw und Abendruhe."
      ablaeufe: alle
  sterne: {fuss: 30, autos: 6, zeichen: 1050}
---

# Kreuzung mit Fußgängern ringsum

Jetzt hat jede Zufahrt einen Überweg mit Taster. Wer über die Nord- oder Südzufahrt geht, kreuzt den Verkehr Nord-Süd (Gruppe `"fuss_ns"`); wer über Ost oder West geht, kreuzt Ost-West (Gruppe `"fuss_ow"`).

Das Schöne: Fußgänger dürfen zusammen mit dem Verkehr gehen, der ihren Weg nicht kreuzt. Haben Nord und Süd Grün, können die Überwege Ost und West gleich mitgehen. Abbieger gibt es hier noch keine, die kommen bald.

Vier Gruppen wollen versorgt sein, also vier Signale: `"ns"`, `"ow"`, `"fuss_ns"`, `"fuss_ow"`.
