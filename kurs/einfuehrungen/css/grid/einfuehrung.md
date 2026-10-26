---
id: css-grid
sprache: css
titel: Grid
kurz: Ein Raster aus Spalten und Zeilen mit display grid, Anteile mit fr, Wiederholung mit repeat und Lücken mit gap.
fuehrt_ein: [grid, grid_spuren, fr, repeat]
lernziele:
  - mit display grid und grid-template-columns ein Raster aus Spalten bauen
  - mit der Einheit fr den Platz in Anteilen verteilen
  - mit repeat gleiche Spalten kurz schreiben
  - Zeilenhöhen mit grid-template-rows festlegen und Lücken mit gap setzen
karte: Ich baue Raster wie ein Eiswürfelfach
bilder:
  - schluessel: karte_css_grid
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin füllt ein Eiswürfelfach, in jedem Fach liegt ein kleiner Fisch
---

## Ein Raster

```alltag
text: "Ein Eiswürfelfach hat feste Fächer in Reihen und Spalten. Pit legt in jedes Fach einen Fisch, der Reihe nach: erst die obere Reihe von links nach rechts, dann die nächste. Grid funktioniert genauso."
zeichnung: eiswuerfelfach
```

Flexbox ordnet in **einer** Richtung. **Grid** ordnet in zwei: Spalten und Zeilen zugleich. `display: grid` beim Behälter, dazu `grid-template-columns` mit einer Breite je Spalte. Die Kinder füllen die Fächer der Reihe nach, Zeile für Zeile; neue Zeilen entstehen von selbst.

```beispiel
id: raster
html: |
  <div class="fach">
    <div>1</div><div>2</div><div>3</div>
    <div>4</div><div>5</div>
  </div>
code: |
  .fach {
    display: grid;
    grid-template-columns: 100px 200px 100px;
  }
  .fach div {
    background-color: teal;
    border: 1px solid #2b3442;
    padding: 8px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben 1 2 3 in drei Spalten, die mittlere doppelt so breit, darunter 4 und 5 in den ersten beiden Spalten
      richtig: true
      erklaerung: Richtig. Drei Spalten sind festgelegt, die Kinder füllen Zeile für Zeile.
    - text: Alle fünf in einer Reihe
      erklaerung: Es gibt nur drei Spalten, das vierte Kind beginnt eine neue Zeile.
    - text: Drei Zeilen mit je zwei Kästen
      erklaerung: grid-template-columns legt die Spalten fest, nicht die Zeilen.
```

```frage
frageart: auswahl
id: wie-viele-spalten
text: "Wie viele Spalten hat `grid-template-columns: 80px 80px 80px 80px`?"
optionen:
  - text: vier
    richtig: true
    erklaerung: Richtig, ein Wert je Spalte.
  - text: eine, 320 Pixel breit
    erklaerung: Jeder Wert ist eine eigene Spalte.
  - text: "80"
    erklaerung: 80 ist die Breite, die Zahl der Werte ist die Zahl der Spalten.
```

## Anteile mit fr

Feste Breiten passen selten genau. Die Einheit `fr` (fraction, Anteil) verteilt den **freien Platz**: `1fr 2fr` teilt ihn eins zu zwei, `1fr 1fr 1fr` in drei gleiche Teile. Feste Breiten und Anteile lassen sich mischen: `120px 1fr` gibt der ersten Spalte 120 Pixel und der zweiten den ganzen Rest.

```beispiel
id: fr
html: |
  <div class="seite">
    <div>Menü</div>
    <div>Inhalt</div>
  </div>
  <div class="drittel">
    <div>A</div><div>B</div><div>C</div>
  </div>
code: |
  .seite, .drittel {
    display: grid;
    margin-bottom: 12px;
  }
  .seite {
    grid-template-columns: 120px 1fr;
  }
  .drittel {
    grid-template-columns: 1fr 2fr 1fr;
  }
  .seite div, .drittel div {
    background-color: teal;
    border: 1px solid #2b3442;
    padding: 8px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben ein schmales Menü links und der Inhalt über den ganzen Rest, unten B doppelt so breit wie A und C
      richtig: true
      erklaerung: Richtig. fr verteilt nur, was übrig bleibt, im angegebenen Verhältnis.
    - text: Oben zwei gleich breite Spalten
      erklaerung: Die erste ist fest 120 Pixel, die zweite bekommt den Rest.
    - text: Unten drei gleich breite Spalten
      erklaerung: 1fr 2fr 1fr gibt der mittleren den doppelten Anteil.
```

```frage
frageart: luecke
id: luecke-fr
text: Zwei Spalten sollen sich den Platz genau teilen. Ergänze.
code: |
  .zwei {
    display: grid;
    grid-template-columns: ___ ___;
  }
antworten: [["1fr"], ["1fr"]]
erklaerung: Richtig, zwei gleiche Anteile.
hinweis: Ein Anteil heißt 1fr.
```

## Kurz mit repeat

Bei vielen gleichen Spalten hilft `repeat(anzahl, breite)`: `repeat(4, 1fr)` ist dasselbe wie `1fr 1fr 1fr 1fr`. Und mit `minmax(min, max)` darf eine Spalte zwischen zwei Breiten wachsen; `repeat(3, minmax(100px, 1fr))` heißt drei Spalten, jede mindestens 100 Pixel, sonst gleich verteilt.

```beispiel
id: repeat
html: |
  <div class="fach">
    <div>1</div><div>2</div><div>3</div><div>4</div>
    <div>5</div><div>6</div><div>7</div><div>8</div>
  </div>
code: |
  .fach {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
  }
  .fach div {
    background-color: teal;
    border: 1px solid #2b3442;
    padding: 8px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Zwei Zeilen mit je vier gleich breiten Kästen über die ganze Breite
      richtig: true
      erklaerung: Richtig. Vier gleiche Anteile, acht Kinder, also zwei Zeilen.
    - text: Vier Zeilen mit je zwei Kästen
      erklaerung: repeat(4, ...) macht vier Spalten.
    - text: Eine Zeile mit acht Kästen
      erklaerung: Es gibt nur vier Spalten.
```

```frage
frageart: auswahl
id: repeat-lang
text: "Was ist dasselbe wie `repeat(3, 100px)`?"
als_code: true
optionen:
  - text: 100px 100px 100px
    richtig: true
    erklaerung: Richtig.
  - text: 300px
    erklaerung: Das wäre eine einzige breite Spalte.
  - text: 3px 100px
    erklaerung: Die erste Zahl ist die Anzahl, keine Breite.
```

## Zeilen und Lücken

`grid-template-rows` legt die Höhen der Zeilen fest, genauso wie die Spalten: `grid-template-rows: 60px 1fr` heißt erste Zeile 60 Pixel, die zweite den Rest der Höhe des Behälters. `gap` kennst du von Flexbox; im Grid legt es Lücken zwischen Spalten **und** Zeilen. Mit zwei Werten, `gap: 4px 16px`, erst zwischen den Zeilen, dann zwischen den Spalten.

```beispiel
id: zeilen
html: |
  <div class="plan">
    <div>Kopf</div><div>Kopf</div>
    <div>Links</div><div>Rechts</div>
  </div>
code: |
  .plan {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 50px 150px;
    gap: 10px;
  }
  .plan div {
    background-color: teal;
    padding: 8px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Zwei Spalten, oben eine flache Zeile von 50 Pixeln, darunter eine hohe von 150, mit 10 Pixeln Lücke überall dazwischen
      richtig: true
      erklaerung: Richtig. Die Zeilen haben feste Höhen, gap trennt Zeilen und Spalten.
    - text: Alle Kästen sind nur so hoch wie ihr Text
      erklaerung: grid-template-rows legt die Höhen fest, die Kästen füllen ihre Fächer.
    - text: Die Lücke gibt es nur zwischen den Spalten
      erklaerung: Im Grid wirkt gap in beide Richtungen.
```

```frage
frageart: auswahl
id: gap-zwei-werte
text: "Was heißt `gap: 20px 4px` im Grid?"
optionen:
  - text: 20 Pixel zwischen den Zeilen, 4 Pixel zwischen den Spalten
    richtig: true
    erklaerung: Richtig, erst Zeilen, dann Spalten.
  - text: 20 Pixel zwischen den Spalten, 4 zwischen den Zeilen
    erklaerung: Andersherum, der erste Wert gilt den Zeilen.
  - text: 20 Pixel Lücke und 4 Pixel Rand
    erklaerung: gap legt nur Lücken, keinen Rand.
```

```merke
text: "`display: grid` mit `grid-template-columns` (und `grid-template-rows`). `fr` verteilt den freien Platz in Anteilen, `repeat(n, breite)` wiederholt, `minmax(min, max)` setzt Grenzen, `gap` trennt Zeilen und Spalten."
```

```falle
titel: fr und feste Breiten
text: "fr verteilt nur, was **nach** den festen Breiten übrig bleibt. Bei `200px 1fr 1fr` auf 500 Pixeln bekommen die beiden Anteile je 150 Pixel, nicht je 250."
```

```augenzwinkern
text: Pia wollte die Fische nach Größe ins Raster legen. Grid füllt aber stur der Reihe nach. Jetzt liegt der Riesenhering zwischen zwei Sardinen und fühlt sich wohl.
```
