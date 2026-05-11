---
schema_version: 1
id: l010-modal-dialog
revision: 1
titel: "Layout 10: Modal-Dialog mit Backdrop"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 16
schaetz_minuten: 10
tags: [layout, lernpfad, modal, flexbox]
pfade: []
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe -- CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="backdrop"><div class="dialog"><h3 class="dtitel">Bestaetigung</h3><p class="dtext">Wirklich loeschen?</p><div class="dknopfe"><button class="kn">Abbrechen</button><button class="kn primaer">Loeschen</button></div></div></div>
ziel_css: |
  .backdrop {
    width: 500px;
    height: 320px;
    background-color: rgba(0, 0, 0, 0.6);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .dialog {
    width: 320px;
    padding: 24px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 8px;
    box-shadow: 0px 12px 32px rgba(0, 0, 0, 0.5);
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .dtitel { margin: 0; color: #e7ecf1; }
  .dtext { margin: 0; color: #9ca3af; }
  .dknopfe { display: flex; justify-content: flex-end; gap: 8px; }
  .kn {
    background-color: transparent;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
  }
  .primaer {
    background-color: #ef4444;
    color: #ffffff;
    border-color: #ef4444;
  }
asserts:
  - selector: ".backdrop"
    property: background-color
    expected: "rgba(0, 0, 0, 0.6)"
  - selector: ".backdrop"
    property: display
    expected: "flex"
  - selector: ".backdrop"
    property: justify-content
    expected: "center"
  - selector: ".backdrop"
    property: align-items
    expected: "center"
  - selector: ".dialog"
    property: box-shadow
    expected: "rgba(0, 0, 0, 0.5) 0px 12px 32px 0px"
  - selector: ".dknopfe"
    property: justify-content
    expected: "flex-end"
hints:
  - kosten: 0
    text: |
      Backdrop ist halbtransparent (rgba mit 0.6 Alpha) und zentriert den Dialog per flex. Der Dialog selbst ist eine flex-column, die Action-Buttons unten rechts liegen.
  - kosten: 6
    text: |
      Backdrop: `background: rgba(0,0,0,0.6); display: flex; justify-content: center; align-items: center;`
      Dialog: `box-shadow: 0 12px 32px rgba(0,0,0,0.5);`
      Button-Reihe: `display: flex; justify-content: flex-end; gap: 8px;`
starter_code: |
  .backdrop {
    width: 500px;
    height: 320px;
    /* halbtransparenter dunkler Backdrop, Dialog mittig */
  }
  .dialog {
    width: 320px;
    padding: 24px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 8px;
    /* Schatten + vertikales Layout mit Abstaenden */
  }
  .dtitel { margin: 0; color: #e7ecf1; }
  .dtext { margin: 0; color: #9ca3af; }
  .dknopfe { /* Buttons rechts ausrichten */ }
  .kn {
    background-color: transparent;
    color: #e7ecf1;
    border: 1px solid #3a4049;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
  }
  .primaer {
    background-color: #ef4444;
    color: #ffffff;
    border-color: #ef4444;
  }
---

# Layout 10: Modal-Dialog

## Aufgabe

Klassischer Bestaetigungs-Dialog: halbtransparenter Backdrop überlagert
die Seite, der Dialog sitzt mittig mit Schatten. Action-Buttons stehen
unten rechts -- die destruktive Action ist rot hervorgehoben.

## Aha

Drei verschachtelte Flex-Container: 1) Backdrop zentriert den Dialog,
2) Dialog ist flex-column für den Inhalts-Stack, 3) Knopf-Reihe ist
flex mit justify-content: flex-end. Jedes Mal trifft Flex die jeweils
passende Stelle.

rgba mit Alpha unter 1 ergibt Transparenz. 0.6 ist
der typische Wert für Modal-Backdrops -- hell genug um zu erkennen
dass etwas dahinter liegt, dunkel genug damit der Dialog im Fokus steht.

## Wozu in der Praxis?

Lösch-Bestaetigung, Login-Modal, Image-Lightbox,
Konfigurations-Dialog -- ein universelles Pattern.
