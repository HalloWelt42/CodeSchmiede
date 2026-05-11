---
schema_version: 1
id: r001-repo-karte
revision: 1
titel: "Repro 01: Repository-Karte (Code-Hosting-Stil)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 10
tags: [repro, lernpfad, card, flexbox]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <article class="repo"><header class="kopf"><span class="emoji">📦</span><span class="name">codeschmiede</span><span class="sichtbar">public</span></header><p class="bschr">Gamifizierter Programmier-Trainer mit didaktischen Lernpfaden.</p><footer class="meta"><span class="sprache"><span class="punkt"></span>Python</span><span class="zahl">★ 1.2k</span><span class="zahl">⑂ 84</span></footer></article>
ziel_css: |
  .repo {
    width: 480px;
    padding: 16px;
    background-color: #22262d;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .kopf {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .name {
    color: #2dd4bf;
    font-weight: 600;
    font-size: 16px;
    margin-right: auto;
  }
  .sichtbar {
    font-size: 11px;
    padding: 2px 8px;
    border: 1px solid #3a4049;
    border-radius: 999px;
    color: #9ca3af;
    text-transform: uppercase;
  }
  .bschr {
    margin: 0;
    color: #9ca3af;
    font-size: 14px;
  }
  .meta {
    display: flex;
    gap: 16px;
    font-size: 13px;
    color: #9ca3af;
  }
  .sprache {
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .punkt {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #fbbf24;
    display: inline-block;
  }
asserts:
  - selector: ".repo"
    property: display
    expected: "flex"
  - selector: ".repo"
    property: flex-direction
    expected: "column"
  - selector: ".kopf"
    property: display
    expected: "flex"
  - selector: ".name"
    property: margin-right
    expected: "auto"
  - selector: ".sichtbar"
    property: border-radius
    expected: "999px"
  - selector: ".punkt"
    property: border-radius
    expected: "50%"
hints:
  - kosten: 0
    text: |
      Karte als flex-column mit drei Sektionen (Header, Beschreibung, Footer-Meta). Im Header sorgt margin-right: auto auf dem Namen dafür, dass das public-Label nach rechts wandert.
  - kosten: 6
    text: |
      Auf .repo: `display: flex; flex-direction: column; gap: 12px;` -- auf .kopf: `display: flex; gap: 8px;` -- auf .name: `margin-right: auto;`
starter_code: |
  .repo {
    width: 480px;
    padding: 16px;
    background-color: #22262d;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    border-radius: 8px;
    /* vertikale Anordnung mit 12px Abstand */
  }
  .kopf { /* flex-Zeile, 8px gap */ }
  .name {
    color: #2dd4bf;
    font-weight: 600;
    font-size: 16px;
    /* nach links wachsen, Folge-Items nach rechts schieben */
  }
  .sichtbar {
    font-size: 11px;
    padding: 2px 8px;
    border: 1px solid #3a4049;
    color: #9ca3af;
    text-transform: uppercase;
    /* Pill-Form */
  }
  .bschr { margin: 0; color: #9ca3af; font-size: 14px; }
  .meta { display: flex; gap: 16px; font-size: 13px; color: #9ca3af; }
  .sprache { display: inline-flex; align-items: center; gap: 6px; }
  .punkt {
    width: 10px; height: 10px;
    background-color: #fbbf24;
    display: inline-block;
    /* Kreis-Form */
  }
---

# Repro 01: Repository-Karte

## Aufgabe

Bau eine Karte im Stil typischer
Code-Hosting-Plattformen: Emoji + Name + Visibility-Badge oben, Beschreibung
in der Mitte, Sprache + Sterne + Forks im Footer.

## Aha

`margin-right: auto` auf einem Flex-Item ist der elegante Push-Trick: alles
links bleibt links, alles rechts wandert ganz nach rechts, ohne dass du
justify-content auf dem Container ändern musst. Sehr nützlich für
asymmetrische Anordnungen.

## Wozu in der Praxis?

Project-Listings, Repo-Browser, Suchergebnisse mit Metadaten.
