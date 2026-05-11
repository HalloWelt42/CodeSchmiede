---
schema_version: 1
id: r005-einstellungs-reihe
revision: 1
titel: "Repro 05: Einstellungs-Zeile mit Toggle-Switch"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 10
tags: [repro, lernpfad, settings, flexbox]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="reihe"><div class="text"><div class="ttitel">Benachrichtigungen</div><div class="tsub">Bei neuen Aufgaben informieren</div></div><label class="schalter"><span class="schiene"><span class="knopf"></span></span></label></div>
ziel_css: |
  .reihe {
    display: flex;
    align-items: center;
    gap: 16px;
    width: 480px;
    padding: 14px 16px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 8px;
  }
  .text {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 2px;
  }
  .ttitel { font-weight: 600; }
  .tsub { font-size: 13px; color: #9ca3af; }
  .schalter { display: inline-block; flex-shrink: 0; }
  .schiene {
    display: block;
    width: 44px;
    height: 24px;
    background-color: #2dd4bf;
    border-radius: 999px;
    position: relative;
  }
  .knopf {
    position: absolute;
    top: 2px;
    left: 22px;
    width: 20px;
    height: 20px;
    background-color: #ffffff;
    border-radius: 50%;
  }
asserts:
  - selector: ".reihe"
    property: display
    expected: "flex"
  - selector: ".text"
    property: flex-grow
    expected: "1"
  - selector: ".schiene"
    property: border-radius
    expected: "999px"
  - selector: ".schiene"
    property: background-color
    expected: "rgb(45, 212, 191)"
  - selector: ".knopf"
    property: border-radius
    expected: "50%"
  - selector: ".knopf"
    property: left
    expected: "22px"
hints:
  - kosten: 0
    text: |
      Zwei-Spalten-Layout: Text-Stack links (flex: 1 für den Platz), Toggle-Switch rechts (flex-shrink: 0). Der Switch besteht aus Schiene + absolut positioniertem Knopf -- bei 'an' steht der Knopf rechts.
  - kosten: 6
    text: |
      .schiene: `width: 44px; height: 24px; border-radius: 999px; position: relative;` -- .knopf: `position: absolute; top: 2px; left: 22px; width: 20px; height: 20px; border-radius: 50%;`
starter_code: |
  .reihe {
    /* flex, vertikal zentriert, 16px gap */
    width: 480px;
    padding: 14px 16px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 8px;
  }
  .text {
    /* fuellt den linken Platz, vertikale Stack */
  }
  .ttitel { font-weight: 600; }
  .tsub { font-size: 13px; color: #9ca3af; }
  .schalter { display: inline-block; flex-shrink: 0; }
  .schiene {
    display: block;
    width: 44px;
    height: 24px;
    background-color: #2dd4bf;
    /* pillenrund + position-Kontext fuer den Knopf */
  }
  .knopf {
    width: 20px;
    height: 20px;
    background-color: #ffffff;
    /* absolut positionieren, oben 2px, links 22px, Kreis-Form */
  }
---

# Repro 05: Einstellungs-Zeile

## Aufgabe

Eine Reihe in einem
Einstellungs-Menue: links Titel + Erklaerung, rechts ein iOS-ähnlicher
Toggle-Switch im 'an'-Zustand.

## Aha

Der Knopf des Toggle liegt
**absolut** positioniert innerhalb der Schiene. Die Schiene braucht dafür
`position: relative`, damit der Knopf sich an ihrer Position orientiert,
nicht an der ganzen Seite.

## Wozu in der Praxis?

Settings-Apps, Filter-Panels, Feature-Flag-UIs.
