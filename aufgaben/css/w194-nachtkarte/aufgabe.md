---
schema_version: 1
id: w194-nachtkarte
revision: 1
titel: Die Nachtkarte
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- variablen
- bereich
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 19
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="karte">Tageskarte</div>

  <div class="karte nacht">Nachtkarte</div>

  '
ziel_css: ":root {\n  --grund: #fbf4e2;\n  --schrift: #2b3442;\n}\n\n.karte {\n  padding: 20px;\n  margin-bottom: 10px;\n\
  \  background-color: var(--grund);\n  color: var(--schrift);\n}\n\n.nacht {\n  --grund: #0b1d3a;\n  --schrift: #ffd166;\n\
  }\n"
hints:
- kosten: 0
  text: Setz die beiden Variablen für .nacht neu, die Regel .karte bleibt unverändert.
- kosten: 2
  text: ".nacht {\n  --grund: #0b1d3a;\n  --schrift: #ffd166;\n}"
starter_code: ":root {\n  --grund: #fbf4e2;\n  --schrift: #2b3442;\n}\n\n.karte {\n  padding: 20px;\n  margin-bottom: 10px;\n\
  \  background-color: var(--grund);\n  color: var(--schrift);\n}\n"
---

Die Nachtkarte soll dunkel sein, ohne die Regel `.karte` anzufassen. Setz dafür die Variablen für `.nacht` neu.

## Vorgaben

- `.nacht`: `--grund` `#0b1d3a`, `--schrift` `#ffd166`
