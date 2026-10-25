---
schema_version: 1
id: r002-chat-zweispaltig
revision: 3
titel: "Repro 02: Chat-Dialog mit eigener und fremder Nachricht"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: mittel
schwierigkeit_score: 14
schaetz_minuten: 10
tags: [repro, lernpfad, chat, flexbox]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="chat"><div class="zeile fremd"><div class="avatar">A</div><div class="bubble">Wie war dein Tag?</div></div><div class="zeile eigen"><div class="bubble selber">Lang - aber gut.</div></div></div>
ziel_css: |
  .chat {
    display: flex;
    flex-direction: column;
    gap: 12px;
    width: 480px;
    padding: 16px;
    background-color: #1a1d23;
  }
  .zeile {
    display: flex;
    gap: 8px;
  }
  .zeile.eigen {
    justify-content: flex-end;
  }
  .avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background-color: #fb923c;
    color: #1a1d23;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    flex-shrink: 0;
  }
  .bubble {
    padding: 8px 12px;
    background-color: #22262d;
    color: #e7ecf1;
    border-radius: 12px 12px 12px 4px;
    max-width: 240px;
  }
  .bubble.selber {
    background-color: #a78bfa;
    color: #1a1d23;
    border-radius: 12px 12px 4px 12px;
  }
hints:
  - kosten: 0
    text: |
      Chat als flex-column. Jede Zeile ist eine Flex-Reihe mit Avatar + Bubble. Eigene Nachrichten haben justify-content: flex-end (Bubble rechts), fremde links. Die Bubble-Ecken sind asymmetrisch - die 'Spitze' zeigt zum jeweiligen Avatar.
  - kosten: 6
    text: |
      fremd-Bubble: `border-radius: 12px 12px 12px 4px;` (spitze unten links)
      eigene Bubble: `border-radius: 12px 12px 4px 12px;` (spitze unten rechts) + justify-content: flex-end auf der Zeile
starter_code: |
  .chat {
    display: flex;
    flex-direction: column;
    gap: 12px;
    width: 480px;
    padding: 16px;
    background-color: #1a1d23;
  }
  .zeile {
    display: flex;
    gap: 8px;
  }
  .zeile.eigen {
    /* eigene Nachricht rechts ausrichten */
  }
  .avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background-color: #fb923c;
    color: #1a1d23;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 700;
    /* schrumpfschutz */
  }
  .bubble {
    padding: 8px 12px;
    background-color: #22262d;
    color: #e7ecf1;
    max-width: 240px;
    /* asymmetrischer Border-Radius: oben gerundet, unten links spitz */
  }
  .bubble.selber {
    background-color: #a78bfa;
    color: #1a1d23;
    /* spitz unten rechts */
  }
---

# Repro 02: Chat-Dialog

## Aufgabe

Zwei Nachrichten in einem Chat-Layout.
Die fremde Nachricht (links) hat einen Avatar daneben und Bubble in Grau, die
eigene (rechts) ist Lavendel ohne Avatar. Die untere Bubble-Ecke zeigt jeweils
zum Sender - bei fremd unten links spitz, bei eigen unten rechts.

## Aha

Border-radius akzeptiert vier Werte (im Uhrzeigersinn ab oben links). Mit
asymmetrischen Werten gibst du Bubbles die typische Sprech-Form. Plus:
`flex-shrink: 0` auf dem Avatar schützt ihn davor, bei langen Nachrichten
zu schrumpfen.

## Wozu in der Praxis?

Messenger, Kunden-Chat-Widgets, KI-Assistenten.
