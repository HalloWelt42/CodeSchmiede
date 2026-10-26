---
schema_version: 1
id: w218-zwei-fassungen
revision: 1
titel: Zwei Fassungen
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
  notiz: Aufbaukurs CSS, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"kopf\">\n  <div class=\"logo\">Fischwagen</div>\n  <div class=\"menue\">Karte · Lage · Kontakt</div>\n\
  </div>\n<div class=\"inhalt\">\n  <div>Hering</div>\n  <div>Makrele</div>\n  <div>Sardine</div>\n</div>\n"
ziel_css: ".kopf {\n  padding: 10px;\n  background-color: #0b1d3a;\n}\n\n.logo {\n  color: #ffd166;\n  font-size: 20px;\n\
  }\n\n.inhalt {\n  display: grid;\n  gap: 6px;\n  margin-top: 6px;\n}\n\n.inhalt div {\n  padding: 12px;\n  background-color:\
  \ teal;\n}\n\n@media (min-width: 500px) {\n  .kopf {\n    display: flex;\n    justify-content: space-between;\n    align-items:\
  \ center;\n  }\n\n  .inhalt {\n    grid-template-columns: repeat(3, 1fr);\n  }\n}\n"
hints:
- kosten: 0
  text: 'Erst das Grundgerüst für schmale Fenster: alles untereinander. Dann in einer Media Query ab 500 Pixeln: Kopf als
    Flex-Reihe, Inhalt in drei Spalten.'
- kosten: 3
  text: 'Mobile First: die Media Query mit min-width kommt ans Ende.'
starter_code: '/* Erst schmal, dann breit */

  '
---

Alles aus dem Kapitel: eine Seite, die zuerst für schmale Fenster gebaut ist und ab 500 Pixeln breiter wird.

## Vorgaben

- `.kopf`: Polster `10px`, Hintergrund `#0b1d3a`
- `.logo`: Schrift `#ffd166`, `20px`
- `.inhalt`: Raster, Lücke `6px`, Außenabstand oben `6px`; Kästen darin Polster `12px`, Hintergrund `teal`
- ab `min-width: 500px`: `.kopf` als Flex-Behälter mit `space-between` und senkrecht mittig, `.inhalt` mit drei gleichen Spalten
