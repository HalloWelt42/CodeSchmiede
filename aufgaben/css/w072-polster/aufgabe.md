---
schema_version: 1
id: w072-polster
revision: 1
titel: Etwas Polster
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 3
tags:
- kurs
- padding
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 7
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="preis">Hering 4,50</p>

  '
ziel_css: ".preis {\n  background-color: #1f6f8b;\n  padding: 12px 24px;\n}\n"
hints:
- kosten: 0
  text: Mit zwei Werten gilt der erste oben und unten, der zweite links und rechts.
- kosten: 2
  text: 'padding: 12px 24px;'
starter_code: ".preis {\n  background-color: #1f6f8b;\n}\n"
---

Der Text klebt am Rand seines Streifens. Gib ihm oben und unten 12, links und rechts 24 Pixel Innenabstand.

## Vorgaben

- Klasse `preis`: Hintergrund `#1f6f8b` (steht schon da), Innenabstand `12px 24px`
