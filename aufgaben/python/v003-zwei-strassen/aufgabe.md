---
schema_version: 1
id: v003-zwei-strassen
revision: 1
titel: Zwei Straßen, ein Umlauf
sprache: python
task_type: ampel
runner_type: docker_python
schwierigkeit: mittel
schwierigkeit_score: 30
schaetz_minuten: 20
tags: [ampel, modulo]
voraussetzungen: []
quelle:
  url: null
  notiz: Ampelschule, Level 3
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-26
zeitlimit_sekunden: 15
hints:
  - kosten: 1
    text: "Derselbe Trick wie beim festen Takt: ein Umlauf als Liste von Phasen, lage.sekunde % Umlauf sagt, wo du bist."
  - kosten: 1
    text: "Jede Phase braucht jetzt zwei Signale, eins für \"ns\" und eins für \"ow\". Zwischen den Richtungen: Gelb, Räumzeit mit allem Rot, Rot-Gelb."
starter_code: |
  def takt(lage):
      # zwei Gruppen: "ns" (Nord und Süd) und "ow" (Ost und West)
      return {"ns": "gruen", "ow": "rot"}
ampel:
  anlage:
    vorlage: kreuzung
    zufahrten:
      nord: {spuren: [{wege: [gerade], gruppe: ns}]}
      sued: {spuren: [{wege: [gerade], gruppe: ns}]}
      ost: {spuren: [{wege: [gerade], gruppe: ow}]}
      west: {spuren: [{wege: [gerade], gruppe: ow}]}
  sichtbar:
    - name: Mittag
      dauer: 120
      verkehr:
        - {zufahrt: nord, alle: 6}
        - {zufahrt: sued, ab: 2, alle: 7}
        - {zufahrt: ost, ab: 1, alle: 5}
        - {zufahrt: west, ab: 3, alle: 6.5}
  versteckt:
    - name: Stoßzeit Nord-Süd
      dauer: 120
      verkehr:
        - {zufahrt: nord, alle: 2.6}
        - {zufahrt: sued, ab: 1, alle: 2.9}
        - {zufahrt: ost, zufall: 0.12}
        - {zufahrt: west, zufall: 0.12}
    - name: Stoßzeit Ost-West
      dauer: 120
      verkehr:
        - {zufahrt: ost, alle: 2.7}
        - {zufahrt: west, ab: 1, alle: 3}
        - {zufahrt: nord, zufall: 0.12}
        - {zufahrt: sued, zufall: 0.12}
    - name: Sonntag
      dauer: 150
      verkehr:
        - {zufahrt: nord, zufall: 0.05}
        - {zufahrt: sued, zufall: 0.05}
        - {zufahrt: ost, zufall: 0.05}
        - {zufahrt: west, zufall: 0.05}
  teilschritte:
    - titel: Abwechselnd Grün
      text: "Nord-Süd und Ost-West bekommen abwechselnd Grün, nie beide zugleich. Niemand wartet länger als 40 s."
      regeln:
        - {art: feindlich}
        - {art: bedient, hoechstens: 40}
    - titel: Gelb und Rot-Gelb
      text: "Vor Rot mindestens 3 s Gelb, vor Grün 1 s Rot-Gelb, für beide Richtungen."
      regeln:
        - {art: gelb, mindestens: 3}
        - {art: rotgelb, dauer: 1}
    - titel: Räumzeit
      text: "Zwischen dem Rot der einen und dem Rot-Gelb der anderen Richtung 2 s alles Rot, damit die Kreuzung leer ist. Kein Blechschaden."
      regeln:
        - {art: raeumzeit, auto: 2}
        - {art: kein_unfall}
    - titel: Alle Abläufe
      text: "Zum Schluss die versteckten Abläufe: Stoßzeit in beiden Richtungen und ein stiller Sonntag."
      ablaeufe: alle
  sterne: {autos: 8, zeichen: 380}
---

# Zwei Straßen, ein Umlauf

Jetzt kreuzen sich zwei Straßen. Nord und Süd fahren gemeinsam (Gruppe `"ns"`), Ost und West auch (Gruppe `"ow"`); ihre Wege kreuzen sich in der Mitte. Fußgänger gibt es hier noch keine, dafür kann jetzt Blech auf Blech treffen.

Gesucht ist eine Umschaltautomatik: ein fester Umlauf, der beide Richtungen abwechselnd fahren lässt, mit Gelb, Rot-Gelb und einer Räumzeit dazwischen.

Gleiche Signale wie bisher: `"gruen"`, `"gelb"`, `"rot"`, `"rotgelb"`.
