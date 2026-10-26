---
schema_version: 1
id: w013-schild
revision: 1
titel: Ein Schild mit Hintergrund
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- background-color
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 1
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Geöffnet</h1>

  <p>Heute bis zum letzten Fisch.</p>

  '
ziel_css: "h1 {\n  color: navy;\n  background-color: skyblue;\n}\n"
hints:
- kosten: 0
  text: 'Dunkelblau auf der dunklen Bühne sieht man kaum. Gib der Überschrift einen hellen Hintergrund: eine zweite Angabe
    in derselben Regel.'
- kosten: 2
  text: 'background-color: skyblue;'
starter_code: "h1 {\n  color: navy;\n}\n"
---

Pit hat das Schild dunkelblau beschriftet, und jetzt kann es niemand lesen. Ein himmelblauer Hintergrund rettet das Schild.

## Vorgaben

- Überschrift (`h1`): Schriftfarbe `navy` (steht schon da), Hintergrundfarbe `skyblue`
