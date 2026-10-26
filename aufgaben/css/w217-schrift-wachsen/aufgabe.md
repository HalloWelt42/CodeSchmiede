---
schema_version: 1
id: w217-schrift-wachsen
revision: 1
titel: Mitwachsende Schrift
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- media
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 21
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Zum frostigen Hering</h1>

  <p>Fisch, so frisch wie die Antarktis</p>

  '
ziel_css: "h1 {\n  font-size: 24px;\n}\n\np {\n  font-size: 14px;\n}\n\n@media (min-width: 400px) {\n  h1 {\n    font-size:\
  \ 32px;\n  }\n}\n\n@media (min-width: 550px) {\n  h1 {\n    font-size: 44px;\n    text-align: center;\n  }\n\n  p {\n  \
  \  font-size: 18px;\n    text-align: center;\n  }\n}\n"
hints:
- kosten: 0
  text: Zwei Media Queries hintereinander. Die zweite kommt später und gewinnt bei breiten Fenstern.
- kosten: 3
  text: '@media (min-width: 400px) mit h1 32px, dann @media (min-width: 550px) mit h1 44px mittig und p 18px mittig'
starter_code: "h1 {\n  font-size: 24px;\n}\n\np {\n  font-size: 14px;\n}\n"
---

Die Schrift wächst mit dem Fenster in zwei Stufen.

## Vorgaben

- Grundgerüst: `h1` `24px`, `p` `14px` (steht schon da)
- ab `400px`: `h1` `32px`
- ab `550px`: `h1` `44px` und mittig, `p` `18px` und mittig
