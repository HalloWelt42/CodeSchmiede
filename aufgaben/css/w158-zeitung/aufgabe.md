---
schema_version: 1
id: w158-zeitung
revision: 1
titel: Die Fischzeitung
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 7
schaetz_minuten: 6
tags:
- kurs
- kurztest
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 15
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"zeitung\">\n  <div class=\"titel\">Fischblatt</div>\n  <div class=\"aufmacher\">Riesenhering gefangen!</div>\n\
  \  <div class=\"wetter\">Eisig</div>\n  <div class=\"anzeige\">Fischwagen sucht Hilfe</div>\n  <div class=\"kurz\">Kurz\
  \ notiert</div>\n</div>\n"
ziel_css: ".zeitung {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  grid-template-rows: 50px 120px 80px;\n\
  \  grid-template-areas:\n    \"titel titel titel\"\n    \"aufmacher aufmacher wetter\"\n    \"anzeige kurz kurz\";\n  gap:\
  \ 6px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n  padding: 6px;\n}\n\n.zeitung div {\n  border: 1px solid #2b3442;\n\
  \  padding: 6px;\n}\n\n.titel { grid-area: titel; font-family: serif; font-size: 24px; }\n.aufmacher { grid-area: aufmacher;\
  \ }\n.wetter { grid-area: wetter; }\n.anzeige { grid-area: anzeige; background-color: #ffd166; }\n.kurz { grid-area: kurz;\
  \ }\n"
hints:
- kosten: 0
  text: Ein Plan mit drei Zeilen und drei Spalten, dann bekommt jedes Kind seinen Bereich.
- kosten: 3
  text: '"titel titel titel" "aufmacher aufmacher wetter" "anzeige kurz kurz"'
starter_code: '/* Die Fischzeitung */

  '
---

Alles aus dem Kapitel: die Titelseite der Fischzeitung.

## Vorgaben

- Klasse `zeitung`: drei gleiche Spalten, Zeilen `50px 120px 80px`, Plan `"titel titel titel" "aufmacher aufmacher wetter" "anzeige kurz kurz"`, Lücke `6px`, Hintergrund `#fbf4e2`, Schrift `#2b3442`, Polster `6px`
- alle Kästen (`.zeitung div`): Rand `1px solid #2b3442`, Polster `6px`
- `.titel`: Bereich titel, Schrift `serif`, `24px`
- `.aufmacher`, `.wetter`, `.kurz`: ihre Bereiche
- `.anzeige`: Bereich anzeige, Hintergrund `#ffd166`
