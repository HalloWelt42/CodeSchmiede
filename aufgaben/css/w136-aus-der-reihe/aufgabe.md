---
schema_version: 1
id: w136-aus-der-reihe
revision: 1
titel: Aus der Reihe
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- align-self
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"reihe\">\n  <div>Pit</div>\n  <div class=\"huepft\">Pia</div>\n  <div>Paul</div>\n  <div>Pauline</div>\n\
  </div>\n"
ziel_css: ".reihe {\n  display: flex;\n  gap: 8px;\n  height: 140px;\n  align-items: flex-end;\n  background-color: #2b3442;\n\
  }\n\n.reihe div {\n  background-color: teal;\n  padding: 10px;\n}\n\n.reihe .huepft {\n  align-self: flex-start;\n  background-color:\
  \ crimson;\n}\n"
hints:
- kosten: 0
  text: Alle stehen unten (beim Behälter), Pia oben (bei ihr selbst).
- kosten: 3
  text: 'align-items: flex-end beim Behälter, align-self: flex-start und ein roter Hintergrund bei .reihe .huepft (genauer
    als .reihe div)'
starter_code: ".reihe {\n  display: flex;\n  gap: 8px;\n  height: 140px;\n  background-color: #2b3442;\n}\n\n.reihe div {\n\
  \  background-color: teal;\n  padding: 10px;\n}\n"
---

Alle Pinguine stehen unten auf dem Eis, nur Pia hüpft gerade, oben und in Rot.

## Vorgaben

- Klasse `reihe`: Kinder unten ausgerichtet (`flex-end`)
- Klasse `huepft` in der Reihe (`.reihe .huepft`): selbst oben (`flex-start`), Hintergrund `crimson`
