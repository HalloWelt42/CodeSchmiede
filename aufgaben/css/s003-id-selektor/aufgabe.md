---
schema_version: 1
id: s003-id-selektor
revision: 1
titel: "Grundlagen 03: Nur ein Element per ID treffen"
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
  <section><p id="leitsatz">Wichtige Aussage</p><p>Anderer Text</p><p>Noch ein Text</p></section>
ziel_css: |
  #leitsatz {
    font-weight: 700;
    font-size: 24px;
  }
asserts:
  - selector: "#leitsatz"
    property: font-weight
    expected: "700"
  - selector: "#leitsatz"
    property: font-size
    expected: "24px"
hints:
  - kosten: 0
    text: |
      CSS wählt Elemente per **Selektor** und gibt ihnen Eigenschaften.
      Welcher Selektor zählt, regeln Spezifizitaet und Quellreihenfolge.
  - kosten: 3
    text: |
      `#leitsatz { font-weight: 700; font-size: 24px; }`
starter_code: |
  /* ID-Selektor: Raute + ID-Name */
---

# Grundlagen 03: Nur das Element mit der ID 'leitsatz' soll größer und fett werden

## Aufgabe

Nur das Element mit der ID 'leitsatz' soll größer und fett werden

## Aha

Der **ID-Selektor** beginnt mit `#`. IDs sind pro Seite eindeutig --
anders als Klassen darf jede ID nur EINMAL vorkommen. Sie haben hohe
Spezifizitaet und überschreiben Klassen-Stile.

## Wozu in der Praxis?

IDs werden eher selten zum Stylen genutzt -- meist für Anker-Links
(`<a href='#abschnitt'>`) und JavaScript-Hooks. Wegen ihrer harten
Spezifizitaet bevorzugt man Klassen, sie sind flexibler.
