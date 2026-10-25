---
schema_version: 1
id: h006-zwei-tone-kreis
revision: 3
titel: "Challenge 06: Zweifarbiger Kreis (oben/unten halbiert)"
sprache: css
task_type: css_klon
runner_type: iframe_css
schwierigkeit: fortgeschritten
schwierigkeit_score: 18
schaetz_minuten: 10
tags: [challenge, lernpfad, gradient, kreis]
voraussetzungen: []
quelle:
  notiz: Eigene Aufgabe - CSS-Klon-Generator.
lizenz: eigen
autor: HalloWelt42
erstellt_am: 2026-05-11
zeitlimit_sekunden: 5
ziel_html: |
  <div class="kreis"></div>
ziel_css: |
  .kreis {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background-image: linear-gradient(180deg, #a78bfa 50%, #fb923c 50%);
  }
hints:
  - kosten: 0
    text: |
      Trick: ein linear-gradient mit hartem Übergang (gleicher Prozent-Wert in beiden Stops) erzeugt eine scharfe Linie statt eines Verlaufs. Plus border-radius: 50% macht aus der Box einen Kreis - fertig ist die Halbierung.
  - kosten: 6
    text: |
      `linear-gradient(180deg, #a78bfa 50%, #fb923c 50%)` mit `border-radius: 50%`
starter_code: |
  .kreis {
    width: 120px;
    height: 120px;
    /* Kreis-Form */
    /* zweifarbiger Gradient mit scharfem 50%-Uebergang */
  }
---

# Challenge 06: Zweifarbiger Kreis

## Ziel

Ein 120px-Kreis, dessen obere Hälfte lavendelfarben und untere orange ist. Mit
scharfem Übergang (keine Verlaufs-Mischung).

## Aha

Wenn zwei aufeinanderfolgende color-stops in einem linear-gradient den
GLEICHEN Prozentwert haben, gibt es keine Interpolation - die Farben
treffen mit scharfer Kante aufeinander. Damit kann man Streifen, Halbierungen
oder Drittel-Teilungen präzise erzeugen. Kombiniert mit border-radius: 50%
entsteht aus der Box ein Kreis, der nur zwei Farbflächen zeigt.

## Wozu in der Praxis?

Status-Icons mit zwei Zuständen, dekorative Indikatoren, Logo-Bausteine,
Donut-Chart-Caps.
