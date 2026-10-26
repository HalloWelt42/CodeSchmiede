---
schema_version: 1
id: w067-luftig
revision: 1
titel: Luft zwischen den Zeilen
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 6
schaetz_minuten: 4
tags:
- kurs
- line-height
- letter-spacing
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 6
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<h2>Speisekarte</h2>

  <p>Hering im Eismantel, dazu ein Klecks Remoulade, frisches Brot vom Bäcker nebenan und ein Becher Eiswasser zum Nachspülen.</p>

  '
ziel_css: "h2 {\n  letter-spacing: 8px;\n}\n\np {\n  line-height: 1.8;\n}\n"
hints:
- kosten: 0
  text: Zwischen die Buchstaben der Überschrift kommt letter-spacing, zwischen die Zeilen des Absatzes line-height.
- kosten: 2
  text: 'h2 { letter-spacing: 8px; } und p { line-height: 1.8; }'
starter_code: '/* Mehr Luft */

  '
---

Der Text ist zu gedrängt. Gib der Überschrift Abstand zwischen den Buchstaben und dem Absatz mehr Platz zwischen den Zeilen.

## Vorgaben

- `h2`: Buchstabenabstand `8px`
- Absatz: Zeilenhöhe `1.8`
