---
schema_version: 1
id: w085-kreis
revision: 1
titel: Ein runder Knopf
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 5
schaetz_minuten: 4
tags:
- kurs
- border-radius
- kreis
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 8
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: '<div class="knopf">Los</div>

  '
ziel_css: ".knopf {\n  width: 60px;\n  height: 60px;\n  padding: 20px;\n  background-color: #e63946;\n  text-align: center;\n\
  \  border-radius: 50px;\n}\n"
hints:
- kosten: 0
  text: Mit dem Polster ist der Knopf größer als 60 Pixel. Rechne aus, wie groß er wirklich ist, und nimm die Hälfte.
- kosten: 2
  text: 60 + 2 × 20 = 100, also 50px
starter_code: ".knopf {\n  width: 60px;\n  height: 60px;\n  padding: 20px;\n  background-color: #e63946;\n  text-align: center;\n\
  \  border-radius: 30px;\n}\n"
---

Der Knopf soll kreisrund sein, ist aber nur ein Quadrat mit runden Ecken. Pit hat beim Radius das Polster vergessen.

## Vorgaben

- Klasse `knopf`: wie bisher, aber ein Kreis (der kleinste Radius, der ihn rund macht)
