---
schema_version: 1
id: m009-doppelte-woerter
revision: 1
titel: Doppelte Wörter
sprache: javascript
task_type: muster_jagd
runner_type: docker_javascript
schwierigkeit: mittel
schwierigkeit_score: 8
schaetz_minuten: 6
tags: [muster-jagd, regex]
voraussetzungen: []
quelle:
  url: null
  notiz: Muster-Jagd, Level 9
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-10-25
zeitlimit_sekunden: 5
hints:
  - {kosten: 2, text: "Eine Gruppe merkt sich, was sie getroffen hat; mit \\1 verlangst du denselben Text noch einmal."}
muster:
  treffer: ["das das ist falsch", "Ich bin bin müde", "und und so weiter", "Es war war einmal"]
  nieten: ["das ist richtig", "bin ich müde", "Haus Hausboot", "der Herr Herrmann"]
  treffer_versteckt: ["Er sagte ja ja", "bis bis morgen"]
  nieten_versteckt: ["Kind Kinder", "an anderer Stelle"]
  sterne: {zwei: 16, drei: 13}
  spickzettel:
    - ["\\w", "Buchstabe, Ziffer oder _ (ohne Umlaute)"]
    - ["(...)", "Gruppe, merkt sich den Treffer"]
    - ["\\1", "derselbe Text wie Gruppe 1"]
---

# Doppelte Wörter

Beim Tippen rutscht oft ein Wort doppelt hinein. Fang die Zeilen, in denen dasselbe Wort zweimal hintereinander steht, getrennt durch ein Leerzeichen.
