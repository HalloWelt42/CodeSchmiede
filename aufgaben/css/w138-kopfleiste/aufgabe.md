---
schema_version: 1
id: w138-kopfleiste
revision: 1
titel: Die Kopfleiste
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
  notiz: Aufbaukurs CSS, Kapitel 13
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"kopf\">\n  <div class=\"logo\">Zum frostigen Hering</div>\n  <div class=\"menue\">\n    <div>Karte</div>\n\
  \    <div>Lage</div>\n    <div class=\"neu\">Neu</div>\n  </div>\n</div>\n"
ziel_css: ".kopf {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  height: 80px;\n  padding:\
  \ 0 16px;\n  background-color: #0b1d3a;\n}\n\n.logo {\n  font-size: 20px;\n  color: #ffd166;\n}\n\n.menue {\n  display:\
  \ flex;\n  gap: 6px;\n  align-items: flex-start;\n  height: 50px;\n}\n\n.menue div {\n  background-color: teal;\n  padding:\
  \ 10px;\n}\n\n.menue .neu {\n  align-self: flex-end;\n  background-color: crimson;\n}\n"
hints:
- kosten: 0
  text: 'Zwei Flex-Behälter: die Kopfleiste verteilt Logo und Menü, das Menü ordnet seine Einträge.'
- kosten: 3
  text: 'Die Kopfleiste: space-between und align-items center. Das Menü: Einträge oben (flex-start), nur Neu unten (align-self
    flex-end); damit sein Rot gegen .menue div gewinnt, schreib .menue .neu.'
starter_code: '/* Die Kopfleiste */

  '
---

Alles aus dem Kapitel in einer Kopfleiste.

## Vorgaben

- Klasse `kopf`: Flex-Behälter, Platz dazwischen (`space-between`), senkrecht mittig, Höhe `80px`, Polster `0 16px`, Hintergrund `#0b1d3a`
- Klasse `logo`: Schrift `20px`, `#ffd166`
- Klasse `menue`: Flex-Behälter, Lücke `6px`, Kinder oben (`flex-start`), Höhe `50px`
- Menüeinträge: Hintergrund `teal`, Polster `10px`
- Klasse `neu` im Menü (`.menue .neu`): selbst unten (`flex-end`), Hintergrund `crimson`
