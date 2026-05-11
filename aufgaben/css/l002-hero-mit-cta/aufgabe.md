---
schema_version: 1
id: l002-hero-mit-cta
revision: 1
titel: "Layout 02: Hero-Sektion mit Headline und CTA"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 12
schaetz_minuten: 7
tags: [layout, lernpfad, hero, flexbox]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <section class="hero"><h1 class="ueberschrift">Willkommen</h1><p class="lead">Lerne CSS auf die didaktische Art.</p><button class="cta">Loslegen</button></section>
ziel_css: |
  .hero {
    width: 480px;
    height: 280px;
    background-color: #22262d;
    color: #e7ecf1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 16px;
    padding: 24px;
  }
  .ueberschrift { margin: 0; font-size: 32px; color: #2dd4bf; }
  .lead { margin: 0; color: #9ca3af; font-size: 16px; }
  .cta {
    background-color: #2dd4bf;
    color: #1a1d23;
    border: none;
    padding: 12px 28px;
    border-radius: 999px;
    font-weight: 700;
    cursor: pointer;
  }
asserts:
  - selector: ".hero"
    property: display
    expected: "flex"
  - selector: ".hero"
    property: flex-direction
    expected: "column"
  - selector: ".hero"
    property: justify-content
    expected: "center"
  - selector: ".hero"
    property: align-items
    expected: "center"
  - selector: ".hero"
    property: gap
    expected: "16px"
  - selector: ".cta"
    property: border-radius
    expected: "999px"
hints:
  - kosten: 0
    text: |
      Hero-Container als flex-column mit zentrierter Ausrichtung in beiden Richtungen. Gap für den Vertikal-Abstand zwischen den drei Elementen, kein margin nötig.
  - kosten: 4
    text: |
      Auf .hero: `display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 16px;`
starter_code: |
  .hero {
    width: 480px;
    height: 280px;
    background-color: #22262d;
    color: #e7ecf1;
    padding: 24px;
    /* hier: flex-column, vertikal+horizontal zentrieren, 16px gap */
  }
  .ueberschrift { margin: 0; font-size: 32px; color: #2dd4bf; }
  .lead { margin: 0; color: #9ca3af; font-size: 16px; }
  .cta {
    background-color: #2dd4bf;
    color: #1a1d23;
    border: none;
    padding: 12px 28px;
    border-radius: 999px;
    font-weight: 700;
    cursor: pointer;
  }
---

# Layout 02: Hero-Sektion

## Aufgabe

Vertikal gestapelt und in beiden Achsen zentriert:
- Petrolfarbene Headline
- Gedämpfter Lead-Text
- Pill-Button (CTA) als Action

## Aha

Flex-column + justify-center + align-center ist die
einfachste Centering-Kombination für einen ganzen Block. Mit gap
verteilst du die Abstaende, ohne margin schreiben zu müssen.

## Wozu in der Praxis?

Landing-Pages, Onboarding-Slides, Empty-
States -- alle nutzen diese Anordnung.
