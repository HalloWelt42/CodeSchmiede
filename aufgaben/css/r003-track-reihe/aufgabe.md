---
schema_version: 1
id: r003-track-reihe
revision: 1
titel: "Repro 03: Musik-Track-Zeile"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 10
tags: [repro, lernpfad, flexbox, musik]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="track"><div class="cover">🎵</div><div class="info"><div class="titel">Codeschmiede Theme</div><div class="kuenstler">Alpha & Crew</div></div><div class="dauer">3:42</div></div>
ziel_css: |
  .track {
    display: flex;
    align-items: center;
    gap: 12px;
    width: 480px;
    padding: 8px 12px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 6px;
  }
  .cover {
    width: 48px;
    height: 48px;
    border-radius: 4px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    flex-shrink: 0;
  }
  .info {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: 2px;
  }
  .titel {
    font-weight: 600;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .kuenstler {
    font-size: 13px;
    color: #9ca3af;
  }
  .dauer {
    font-family: monospace;
    font-size: 13px;
    color: #9ca3af;
    flex-shrink: 0;
  }
asserts:
  - selector: ".track"
    property: display
    expected: "flex"
  - selector: ".track"
    property: align-items
    expected: "center"
  - selector: ".cover"
    property: flex-shrink
    expected: "0"
  - selector: ".info"
    property: flex-grow
    expected: "1"
  - selector: ".titel"
    property: white-space
    expected: "nowrap"
  - selector: ".titel"
    property: text-overflow
    expected: "ellipsis"
hints:
  - kosten: 0
    text: |
      Drei Flex-Bereiche nebeneinander: Cover (fix), Info (waechst), Dauer (fix). Lange Titel müssen mit ... abgekürzt werden -- daher die Truncation-Kombo: white-space, overflow, text-overflow.
  - kosten: 6
    text: |
      `.info { flex: 1; min-width: 0; }` und `.titel { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }`
starter_code: |
  .track {
    /* flex-Zeile, vertikal zentriert, 12px gap */
    width: 480px;
    padding: 8px 12px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 6px;
  }
  .cover {
    width: 48px;
    height: 48px;
    border-radius: 4px;
    background-color: #2dd4bf;
    color: #1a1d23;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    /* nicht schrumpfen */
  }
  .info {
    /* fuellen, eigene flex-column mit min-width: 0 fuer Truncation */
  }
  .titel {
    font-weight: 600;
    /* Truncation: nowrap, hidden, ellipsis */
  }
  .kuenstler { font-size: 13px; color: #9ca3af; }
  .dauer {
    font-family: monospace;
    font-size: 13px;
    color: #9ca3af;
    /* nicht schrumpfen */
  }
---

# Repro 03: Musik-Track-Zeile

## Aufgabe

Eine kompakte Zeile für einen
Song: Cover-Bild links, in der Mitte Titel + Kuenstler, ganz rechts die Dauer.
Lange Titel werden mit '...' abgekürzt statt das Layout zu sprengen.

## Aha

Drei-Klassiker-Truncation: `white-space: nowrap` (kein Umbruch) + `overflow:
hidden` + `text-overflow: ellipsis`. Wichtig: das umgebende Flex-Item braucht
`min-width: 0`, sonst greift overflow nicht (Flex-Items haben einen impliziten
Default min-width: auto).

## Wozu in der Praxis?

Musik-Player, Dateilisten, Tabellen mit langen Texten, Adressbücher.
