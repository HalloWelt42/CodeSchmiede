---
schema_version: 1
id: m011-mailadressen
revision: 1
titel: Einfache Mailadressen
sprache: javascript
task_type: muster_jagd
runner_type: docker_javascript
schwierigkeit: fortgeschritten
schwierigkeit_score: 9
schaetz_minuten: 8
tags: [muster-jagd, regex]
voraussetzungen: []
quelle:
  url: null
  notiz: Muster-Jagd, Level 11
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 2, text: "In eckigen Klammern ist der Punkt ein ganz normales Zeichen."}
muster:
  treffer: ["anna@beispiel.de", "max.muster@post.de", "kontakt@firma.com", "a1@b2.org"]
  nieten: ["anna@", "@beispiel.de", "anna beispiel.de", "anna@beispiel", "anna@@beispiel.de", "Mail: anna@beispiel.de"]
  treffer_versteckt: ["info@schmiede.de", "x.y.z@test.net"]
  nieten_versteckt: ["anna@beispiel.", "anna.beispiel.de"]
  sterne: {zwei: 22, drei: 17}
  spickzettel:
    - ["[\\w.]", "Wortzeichen oder Punkt"]
    - ["+", "einmal oder öfter"]
    - ["^ $", "die ganze Zeile"]
---

# Einfache Mailadressen

Fang Zeilen, die genau eine einfache Mailadresse sind: vor dem `@` Buchstaben, Ziffern und Punkte, dahinter ein Name, ein Punkt und eine Endung. Steht noch etwas anderes in der Zeile, ist sie eine Niete.
