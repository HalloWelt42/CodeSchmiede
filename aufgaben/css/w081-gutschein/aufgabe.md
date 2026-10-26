---
schema_version: 1
id: w081-gutschein
revision: 1
titel: Zum Ausschneiden
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 3
schaetz_minuten: 2
tags:
- kurs
- border-style
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<p class="gutschein">Gutschein: ein Hering gratis</p>

  '
ziel_css: ".gutschein {\n  width: 280px;\n  padding: 16px;\n  border: 3px dashed gold;\n}\n"
hints:
- kosten: 0
  text: Tausche nur die Art des Randes.
- kosten: 2
  text: 'border: 3px dashed gold;'
starter_code: ".gutschein {\n  width: 280px;\n  padding: 16px;\n  border: 3px solid gold;\n}\n"
---

Ein Gutschein braucht einen gestrichelten Rand, sonst schneidet ihn keiner aus.

## Vorgaben

- Klasse `gutschein`: Rand `3px`, gestrichelt, `gold`
