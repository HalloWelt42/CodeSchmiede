---
schema_version: 1
id: m012-preise
revision: 1
titel: Preise in Euro
sprache: javascript
task_type: muster_jagd
runner_type: docker_javascript
schwierigkeit: fortgeschritten
schwierigkeit_score: 8
schaetz_minuten: 6
tags: [muster-jagd, regex]
voraussetzungen: []
quelle:
  url: null
  notiz: Muster-Jagd, Level 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 2, text: "Bei 12,9 € darf die 9 allein nicht als Preis zählen: was steht davor?"}
muster:
  treffer: ["Nur 12,99 €", "3 € pro Stück", "Summe: 1500,00 €", "0,50 €"]
  nieten: ["12 Euro", "€ 12", "12,99€", "12,9 €", "EUR 5"]
  treffer_versteckt: ["Eintritt 8 €", "99,95 € Rabatt"]
  nieten_versteckt: ["Preis: zwölf €", "5,5€", "1,999 €"]
  sterne: {zwei: 22, drei: 18}
  spickzettel:
    - ["+", "einmal oder öfter"]
    - ["(...)?", "die ganze Gruppe darf fehlen"]
    - ["(^| )", "Zeilenanfang oder Leerzeichen"]
---

# Preise in Euro

Fang Preise: eine Zahl, wahlweise mit Komma und genau zwei Nachkommastellen, dann ein Leerzeichen und das Zeichen €. Vor der Zahl steht nichts oder ein Leerzeichen.
