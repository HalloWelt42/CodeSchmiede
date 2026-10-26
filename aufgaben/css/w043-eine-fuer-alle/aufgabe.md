---
schema_version: 1
id: w043-eine-fuer-alle
revision: 1
titel: Eine für alle
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 4
schaetz_minuten: 3
tags:
- kurs
- vererbung
voraussetzungen: []
quelle:
  notiz: Aufbaukurs CSS, Kapitel 4
lizenz: eigen
autor: HalloWelt42
erstellt_am: '2026-10-26'
zeitlimit_sekunden: 5
ziel_html: "<div class=\"karte\">\n  <h2>Speisekarte</h2>\n  <p>Hering mit <em>viel</em> Eis</p>\n  <ul>\n    <li>Makrele</li>\n\
  \    <li>Sardinen</li>\n  </ul>\n</div>\n"
ziel_css: ".karte {\n  color: lightgreen;\n}\n"
hints:
- kosten: 0
  text: Die Schriftfarbe wird vererbt. Färbe die Karte selbst, dann erben alle Elemente darin.
- kosten: 2
  text: ".karte {\n  color: lightgreen;\n}"
starter_code: '/* Eine einzige Regel genügt */

  '
---

Alles in der Karte soll hellgrün werden. Statt jedes Element einzeln zu färben, nutze die Vererbung: eine Regel, ein Selektor.

## Vorgaben

- alles im Element mit der Klasse `karte`: Schriftfarbe `lightgreen`, mit einer einzigen Regel
