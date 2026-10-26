---
schema_version: 1
id: w127-kartenreihe
revision: 1
titel: Die Kartenreihe
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- flex
- flex-wrap
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 12
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"galerie\">\n  <div class=\"karte\">Pit</div>\n  <div class=\"karte\">Pia</div>\n  <div class=\"karte\"\
  >Paul</div>\n  <div class=\"karte\">Pauline</div>\n</div>\n"
ziel_css: ".galerie {\n  display: flex;\n  flex-wrap: wrap;\n  gap: 12px;\n  padding: 12px;\n  background-color: #2b3442;\n\
  }\n\n.karte {\n  width: 120px;\n  height: 140px;\n  padding: 8px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n  border-radius:\
  \ 8px;\n}\n"
hints:
- kosten: 0
  text: Die Galerie wird Flex-Behälter mit Umbruch, Lücken, Polster und dunklem Hintergrund.
- kosten: 2
  text: '.galerie: display flex, flex-wrap wrap, gap 12px, padding 12px, background-color #2b3442'
starter_code: ".karte {\n  width: 120px;\n  height: 140px;\n  padding: 8px;\n  background-color: #fbf4e2;\n  color: #2b3442;\n\
  \  border-radius: 8px;\n}\n"
---

Die Sammelkarten der Pinguine sollen nebeneinander in der Galerie liegen.

## Vorgaben

- Klasse `galerie`: Flex-Behälter mit Umbruch, Lücke `12px`, Polster `12px`, Hintergrund `#2b3442`
- Klasse `karte`: steht schon da
