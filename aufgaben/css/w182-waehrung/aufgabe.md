---
schema_version: 1
id: w182-waehrung
revision: 1
titel: Die Währung dahinter
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- after
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 18
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p>Hering <span class="preis">4,50</span></p>

  <p>Makrele <span class="preis">3,80</span></p>

  <p>Sardine <span class="preis">2,90</span></p>

  '
ziel_css: ".preis {\n  color: gold;\n}\n\n.preis::after {\n  content: \" €\";\n}\n"
hints:
- kosten: 0
  text: Hinter jeden Preis kommt ein Leerzeichen und das Euro-Zeichen.
- kosten: 2
  text: ".preis::after {\n  content: \" €\";\n}"
starter_code: ".preis {\n  color: gold;\n}\n"
---

Im HTML stehen nur Zahlen. Hänge hinter jeden Preis ein Leerzeichen und ein Euro-Zeichen.

## Vorgaben

- `.preis::after`: Inhalt `" €"`
