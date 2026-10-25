---
schema_version: 1
id: h004-sprechblase
revision: 3
titel: "Challenge 04: Sprechblase mit ::after-Spitze"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 12
tags: [challenge, lernpfad, pseudo-element, after]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="blase">Hallo!</div>
ziel_css: |
  .blase {
    position: relative;
    display: inline-block;
    padding: 10px 16px;
    background-color: #fbbf24;
    color: #1a1d23;
    border-radius: 12px;
    font-weight: 600;
  }
  .blase::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 20px;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-top: 8px solid #fbbf24;
  }
hints:
  - kosten: 0
    text: |
      Sprechblase = abgerundete Box + Dreieck unten dran. Das Dreieck baust du mit ::after-Pseudölement (content: ''!) und dem Border-Trick aus h002. Position: absolute relativ zur Blase, top: 100% setzt es genau unter die Box.
  - kosten: 8
    text: |
      `.blase { position: relative; }` - `.blase::after { content: ''; position: absolute; top: 100%; left: 20px; width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-top: 8px solid #fbbf24; }`
starter_code: |
  .blase {
    /* Blase: Hintergrund #fbbf24, Schrift #1a1d23 halbfett, Innenabstand 10px 16px, Ecken 12px */
    /* position: relative - damit das ::after sich daran orientieren kann */
  }
  .blase::after {
    content: "";
    /* Dreieck unten an der Blase, per Border-Trick + absolute */
  }
---

# Challenge 04: Sprechblase mit Spitze

## Ziel

Eine goldfarbene Sprechblase mit kleinem Dreieck am unteren Rand -
ohne zusätzliches HTML, nur per ::after-Pseudölement.

## Aha

Pseudölemente `::before` und `::after` sind 'gefakte' Kindelemente, die
rein in CSS leben. Sie brauchen ZWINGEND `content: ""` (auch leerer
String reicht), sonst rendern sie nicht. Mit position: absolute innerhalb
eines position: relative-Containers landen sie genau wo man sie haben will.

Kombiniert mit dem Border-Triangle-Trick aus der vorigen Challenge entsteht
die Sprechblasen-Spitze - ohne ein einziges zusätzliches DOM-Element.

## Wozu in der Praxis?

Tooltips, Chat-Bubbles, Notification-Popups, Help-Tags.
