---
schema_version: 1
id: w196-abstand-mal-zwei
revision: 1
titel: Ein Abstand für alles
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- calc
- var
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"kasten\">\n  <h2>Hering</h2>\n  <p>Frisch aus dem Eis</p>\n</div>\n"
ziel_css: ":root {\n  --abstand: 12px;\n}\n\n.kasten {\n  padding: calc(var(--abstand) * 2);\n  background-color: #1f6f8b;\n\
  \  border-radius: var(--abstand);\n}\n\n.kasten h2 {\n  margin: 0 0 var(--abstand);\n}\n\n.kasten p {\n  margin: 0;\n  padding:\
  \ var(--abstand);\n  background-color: #2b3442;\n}\n"
hints:
- kosten: 0
  text: 'Alle Abstände leiten sich von --abstand ab: außen das Doppelte, sonst einfach.'
- kosten: 3
  text: '.kasten: padding calc(var(--abstand) * 2), border-radius var(--abstand); h2: margin 0 0 var(--abstand); p: padding
    var(--abstand)'
starter_code: ":root {\n  --abstand: 12px;\n}\n\n.kasten {\n  background-color: #1f6f8b;\n}\n\n.kasten p {\n  margin: 0;\n\
  \  background-color: #2b3442;\n}\n"
---

Alle Abstände des Kastens hängen an einer einzigen Variable.

## Vorgaben

- `.kasten`: Polster `calc(var(--abstand) * 2)`, Eckenradius `var(--abstand)`
- `.kasten h2`: Außenabstand `0 0 var(--abstand)`
- `.kasten p`: Polster `var(--abstand)`
