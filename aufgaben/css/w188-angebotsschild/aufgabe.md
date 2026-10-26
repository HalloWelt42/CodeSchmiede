---
schema_version: 1
id: w188-angebotsschild
revision: 1
titel: Das Angebotsschild
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
  notiz: Aufbaukurs CSS, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"schild\">\n  <p class=\"name\">Makrele am Stiel</p>\n  <p class=\"preis\">3,80</p>\n</div>\n"
ziel_css: ".schild {\n  position: relative;\n  width: 260px;\n  margin: 30px;\n  padding: 16px;\n  background-color: #fbf4e2;\n\
  \  color: #2b3442;\n}\n\n.schild::before {\n  content: \"Angebot\";\n  position: absolute;\n  top: -12px;\n  left: 12px;\n\
  \  padding: 2px 8px;\n  background-color: crimson;\n  color: white;\n}\n\n.name::first-letter {\n  font-size: 28px;\n  color:\
  \ crimson;\n}\n\n.preis::after {\n  content: \" €\";\n}\n"
hints:
- kosten: 0
  text: Das Schild ist Bezugsrahmen für ein Pseudoelement, das wie ein Etikett oben auf dem Rand sitzt.
- kosten: 3
  text: .schild::before mit content "Angebot" und position absolute; .name::first-letter groß und rot; .preis::after mit dem
    Euro-Zeichen
starter_code: '/* Das Angebotsschild */

  '
---

Alles aus dem Kapitel auf einem Angebotsschild.

## Vorgaben

- Klasse `schild`: Bezugsrahmen (`position: relative`), Breite `260px`, Außenabstand `30px`, Polster `16px`, Hintergrund `#fbf4e2`, Schrift `#2b3442`
- `.schild::before`: Inhalt `"Angebot"`, absolut bei `top: -12px` und `left: 12px`, Polster `2px 8px`, Hintergrund `crimson`, Schrift `white`
- `.name::first-letter`: Schrift `28px`, `crimson`
- `.preis::after`: Inhalt `" €"`
