---
schema_version: 1
id: w068-plakat
revision: 1
titel: Das Plakat
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
  notiz: Aufbaukurs CSS, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h1>Fischfest</h1>

  <p class="wann">Samstag ab zehn</p>

  <p class="klein">Bei Regen fällt es ins Wasser, also wie immer.</p>

  '
ziel_css: "h1 {\n  font-size: 56px;\n  font-family: serif;\n  text-align: center;\n  text-transform: uppercase;\n  letter-spacing:\
  \ 4px;\n}\n\n.wann {\n  font-size: 24px;\n  font-weight: bold;\n  text-align: center;\n}\n\n.klein {\n  font-size: 12px;\n\
  \  font-style: italic;\n  text-align: right;\n}\n"
hints:
- kosten: 0
  text: Drei Regeln mit mehreren Angaben. Geh die Vorgaben Zeile für Zeile durch.
- kosten: 3
  text: 'Die Überschrift hat fünf Angaben: Größe, Familie, Ausrichtung, Großbuchstaben, Buchstabenabstand.'
starter_code: '/* Das Plakat für das Fischfest */

  '
---

Alles aus dem Kapitel auf einem Plakat.

## Vorgaben

- `h1`: Größe `56px`, Schriftart `serif`, mittig, Großbuchstaben, Buchstabenabstand `4px`
- Klasse `wann`: Größe `24px`, fett, mittig
- Klasse `klein`: Größe `12px`, schräg, rechts
