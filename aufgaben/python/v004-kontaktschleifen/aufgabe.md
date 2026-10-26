---
schema_version: 1
id: v004-kontaktschleifen
revision: 1
titel: "Kontaktschleifen: Grün nur bei Bedarf"
sprache: python
task_type: ampel
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 40
schaetz_minuten: 30
tags: [ampel, zustandsautomat]
voraussetzungen: []
quelle:
  url: null
  notiz: Ampelschule, Level 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 15
hints:
  - kosten: 1
    text: "Ein fester Umlauf reicht nicht mehr: merk dir die Phase und seit wann sie läuft (global), und wechsle erst, wenn die Mindestdauer um ist und es einen Grund gibt."
  - kosten: 1
    text: "Grund für Ost-West ist lage.schleife[\"ow\"]. Solange dort weiter Autos auf der Schleife stehen, darf Ost-West Grün behalten, aber nicht ewig."
  - kosten: 2
    text: "Eine Tabelle je Phase mit beiden Signalen und der Mindestdauer, dazu eine zweite, welche Phase danach kommt, hält takt() kurz."
starter_code: |
  def takt(lage):
      # lage.schleife["ow"]: ein Auto steht vor der Haltlinie von Ost oder West
      return {"ns": "gruen", "ow": "rot"}
ampel:
  anlage:
    vorlage: kreuzung
    schleifen: true
    zufahrten:
      nord: {spuren: [{wege: [gerade], gruppe: ns}]}
      sued: {spuren: [{wege: [gerade], gruppe: ns}]}
      ost: {spuren: [{wege: [gerade], gruppe: ow}]}
      west: {spuren: [{wege: [gerade], gruppe: ow}]}
  sensoren: [schleife, wartend]
  aufbauend_auf: v003-zwei-strassen
  sichtbar:
    - name: Landstraße
      dauer: 150
      verkehr:
        - {zufahrt: nord, alle: 4.5}
        - {zufahrt: sued, ab: 2, alle: 5}
        - {zufahrt: ost, um: [12, 13.5, 60, 95, 96, 97.5, 130]}
        - {zufahrt: west, um: [30, 75, 110]}
  versteckt:
    - name: Nachtruhe
      dauer: 150
      verkehr:
        - {zufahrt: nord, zufall: 0.06}
        - {zufahrt: sued, zufall: 0.06}
        - {zufahrt: ost, um: [70]}
    - name: Stoßzeit Ost-West
      dauer: 150
      verkehr:
        - {zufahrt: nord, alle: 4}
        - {zufahrt: sued, ab: 1, alle: 4.5}
        - {zufahrt: ost, alle: 3.5}
        - {zufahrt: west, ab: 2, alle: 4}
    - name: Feldweg
      dauer: 150
      verkehr:
        - {zufahrt: nord, alle: 3}
        - {zufahrt: sued, ab: 1, alle: 3.2}
        - {zufahrt: west, zufall: 0.05}
        - {zufahrt: ost, zufall: 0.05}
  teilschritte:
    - titel: Jeder kommt dran
      text: "Nie beide zugleich offen, kein Blechschaden, und niemand wartet länger als 45 s."
      regeln:
        - {art: feindlich}
        - {art: kein_unfall}
        - {art: bedient, hoechstens: 45}
    - titel: Sicher umschalten
      text: "Wie bisher: Gelb vor Rot, Rot-Gelb vor Grün, 2 s Räumzeit."
      regeln:
        - {art: gelb, mindestens: 3}
        - {art: rotgelb, dauer: 1}
        - {art: raeumzeit, auto: 2}
    - titel: Die Hauptstraße ruht auf Grün
      text: "Wartet an Ost und West niemand, hat Nord-Süd Grün. Ost-West öffnet nur, wenn dort ein Auto auf der Schleife steht."
      regeln:
        - {art: ruhe, gruppe: ns}
        - {art: nur_bei_bedarf, gruppen: [ow]}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: Nachtruhe, Stoßzeit Ost-West und ein Feldweg, auf dem kaum einer kommt."
      ablaeufe: alle
  sterne: {autos: 5, zeichen: 600}
---

# Kontaktschleifen: Grün nur bei Bedarf

Die Hauptstraße Nord-Süd ist viel befahren, die Nebenstraße Ost-West kaum. Ein fester Umlauf lässt die Hauptstraße ständig vor einer leeren Kreuzung warten. Besser: Nord-Süd hat Grün, bis an Ost oder West wirklich jemand steht.

Dafür liegen vor den Haltlinien Kontaktschleifen (gestrichelt). Steht ein Auto darauf, meldet `lage.schleife["ow"]` (oder `["ns"]`) `True`; `lage.wartend["ow"]` zählt, wie viele dort vor Rot stehen.

Klingt einfach, ist es auch fast. Nur darf die Nebenstraße nicht verhungern, wenn auf der Hauptstraße Stoßzeit ist.
