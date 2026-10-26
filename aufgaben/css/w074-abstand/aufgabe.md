---
schema_version: 1
id: w074-abstand
revision: 1
titel: Abstand halten
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- margin
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="kiste">Hering</div>

  <div class="kiste">Makrele</div>

  <div class="kiste">Sardinen</div>

  '
ziel_css: ".kiste {\n  background-color: #c98c55;\n  color: #222;\n  padding: 10px;\n  margin-bottom: 20px;\n  width: 160px;\n\
  }\n"
hints:
- kosten: 0
  text: Zwischen die Kisten kommt Außenabstand nach unten, und jede Kiste wird 160 Pixel breit.
- kosten: 2
  text: "margin-bottom: 20px;\n  width: 160px;"
starter_code: ".kiste {\n  background-color: #c98c55;\n  color: #222;\n  padding: 10px;\n}\n"
---

Die Kisten stehen eng aneinander und sind viel zu breit. Mach sie 160 Pixel breit und lass unter jeder 20 Pixel Luft.

## Vorgaben

- Klasse `kiste`: wie bisher, dazu Breite `160px` und Außenabstand unten `20px`
