---
schema_version: 1
id: s012-margin-aussenabstand
revision: 1
titel: "Grundlagen 12: Margin -- Aussenabstand zwischen Boxen"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: anfaenger
schwierigkeit_score: 8
schaetz_minuten: 4
tags: [grundlagen, lernpfad]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="block">Erste</div><div class="block">Zweite</div>
ziel_css: |
  .block {
    margin: 16px 0;
    padding: 12px;
    background-color: #2dd4bf;
    color: #1a1d23;
    width: 200px;
  }
asserts:
  - selector: ".block"
    property: margin-top
    expected: "16px"
  - selector: ".block"
    property: margin-bottom
    expected: "16px"
  - selector: ".block"
    property: margin-left
    expected: "0px"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `margin: 16px 0;`
starter_code: |
  .block {
    padding: 12px;
    background-color: #2dd4bf;
    color: #1a1d23;
    width: 200px;
    /* hier 16px Margin oben+unten, 0 links+rechts */
  }
---

# Grundlagen 12: Beide Boxen haben 16px Margin oben und unten -- dadurch entsteht Luft zwischen ihnen

## Aufgabe

Beide Boxen haben 16px Margin oben und unten -- dadurch entsteht Luft zwischen ihnen

## Aha

**Margin** ist der Abstand AUSSERHALB einer Box. Anders als Padding
ist Margin nicht Teil der sichtbaren Box -- die Hintergrundfarbe der
Box endet vor dem Margin. Vertikale Margins benachbarter Boxen
**kollabieren** überraschenderweise (es gewinnt der größere).

## Wozu in der Praxis?

Margin trennt Boxen voneinander. Klassische Faustregel: Padding für
Innen-Luft, Margin für Aussen-Abstand. Mit `margin: 0 auto` kann
man eine Box mit fester Breite horizontal zentrieren.
