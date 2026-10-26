---
id: css-grid-bereiche
sprache: css
titel: Grid-Bereiche
kurz: Kinder über mehrere Spalten und Zeilen spannen, an Linien platzieren und das ganze Raster mit benannten Bereichen wie einen Plan zeichnen.
fuehrt_ein: [spannen, bereiche]
lernziele:
  - ein Kind mit span über mehrere Spalten oder Zeilen spannen
  - ein Kind mit Liniennummern genau platzieren
  - mit grid-template-areas ein Raster als Plan aus Namen zeichnen
  - Kinder mit grid-area in ihre Bereiche setzen
  - leere Fächer mit einem Punkt freilassen
karte: Ich zeichne Seiten wie einen Bauplan
bilder:
  - schluessel: karte_css_grid_bereiche
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin mit Bauhelm steht vor einem Bauplan aus farbigen Feldern und legt ein großes Brett über zwei Felder
---

## Über mehrere Spalten

```alltag
text: "Beim Fischfest baut Pit Tische aus Kisten. Meist steht eine Kiste in einem Feld, aber für die große Torte legt er ein Brett über zwei Kisten. So spannt sich ein Grid-Kind über mehrere Fächer."
zeichnung: bauplan
```

Normalerweise belegt jedes Kind genau ein Fach. Mit `grid-column: span 2` spannt es sich über **zwei Spalten**, mit `grid-row: span 2` über zwei Zeilen. Die übrigen Kinder rücken weiter, dorthin, wo noch Platz ist.

```beispiel
id: span
html: |
  <div class="fach">
    <div class="breit">Torte</div>
    <div>Hering</div><div>Lachs</div><div>Dorsch</div><div>Aal</div>
  </div>
code: |
  .fach {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 4px;
  }
  .fach div {
    background-color: teal;
    padding: 10px;
  }
  .fach .breit {
    grid-column: span 2;
    background-color: crimson;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben die Torte über zwei Spalten und daneben Hering, darunter Lachs, Dorsch und Aal
      richtig: true
      erklaerung: Richtig. Die Torte belegt zwei der drei Fächer der ersten Zeile, Hering passt noch daneben.
    - text: Die Torte allein in der ersten Zeile, alle anderen darunter
      erklaerung: Neben der Torte ist noch ein Fach frei, und das nimmt der Hering.
    - text: Die Torte ist so breit wie die anderen, span gilt nur für Zeilen
      erklaerung: grid-column span 2 spannt über Spalten.
```

```frage
frageart: luecke
id: luecke-span
text: Das Kind soll sich über drei Zeilen erstrecken. Ergänze.
code: |
  .hoch {
    grid-row: ___ 3;
  }
antworten: [["span"]]
erklaerung: Richtig, span 3 spannt über drei.
hinweis: Spannen heißt span.
```

## An Linien platzieren

Ein Raster hat **Linien**: Bei drei Spalten gibt es vier senkrechte Linien, von links gezählt 1 bis 4. `grid-column: 1 / 3` heißt von Linie 1 bis Linie 3, also über die ersten beiden Spalten. `grid-column: 1 / -1` reicht von der ersten bis zur letzten Linie, über die ganze Breite. Genauso `grid-row` für die waagerechten Linien.

```beispiel
id: linien
html: |
  <div class="plan">
    <div class="kopf">Kopf</div>
    <div class="seite">Seite</div>
    <div>A</div><div>B</div>
  </div>
code: |
  .plan {
    display: grid;
    grid-template-columns: 100px 1fr 1fr;
    grid-template-rows: 40px 80px 80px;
    gap: 4px;
  }
  .plan div {
    background-color: teal;
    padding: 8px;
  }
  .plan .kopf {
    grid-column: 1 / -1;
    background-color: crimson;
  }
  .plan .seite {
    grid-row: 2 / 4;
    background-color: purple;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Der Kopf über die ganze Breite, links darunter die Seite über zwei Zeilen hoch, A und B rechts daneben
      richtig: true
      erklaerung: Richtig. 1 / -1 reicht von der ersten bis zur letzten Linie, 2 / 4 über die Zeilen 2 und 3.
    - text: Der Kopf nur in der ersten Spalte
      erklaerung: -1 ist die letzte Linie, der Kopf reicht also über alle Spalten.
    - text: Die Seite ist nur eine Zeile hoch
      erklaerung: Von Linie 2 bis Linie 4 sind es zwei Zeilen.
```

```frage
frageart: auswahl
id: linien-zaehlen
text: "Über welche Spalten reicht `grid-column: 2 / 4`?"
optionen:
  - text: Über die zweite und dritte Spalte
    richtig: true
    erklaerung: Richtig. Von Linie 2 bis Linie 4 liegen die Spalten 2 und 3.
  - text: Über die zweite, dritte und vierte Spalte
    erklaerung: Gezählt werden Linien, nicht Spalten. Vor Linie 4 endet die dritte Spalte.
  - text: Über vier Spalten ab der zweiten
    erklaerung: 4 ist die End-Linie, keine Anzahl. Eine Anzahl schreibt man mit span.
```

## Ein Plan aus Namen

Noch anschaulicher ist `grid-template-areas`: Man zeichnet das Raster als **Plan aus Namen**, je Zeile ein Text in Anführungszeichen, je Spalte ein Name. Steht derselbe Name in mehreren Fächern nebeneinander oder untereinander, bilden sie zusammen einen **Bereich**. Ein Punkt `.` lässt ein Fach leer.

```beispiel
id: bereiche
html: |
  <div class="seite">
    <div class="a">Kopf</div>
    <div class="b">Menü</div>
    <div class="c">Inhalt</div>
    <div class="d">Fuß</div>
  </div>
code: |
  .seite {
    display: grid;
    grid-template-columns: 120px 1fr;
    grid-template-rows: 50px 150px 40px;
    grid-template-areas:
      "kopf kopf"
      "menue inhalt"
      "fuss fuss";
    gap: 4px;
  }
  .seite div {
    background-color: teal;
    padding: 8px;
  }
  .a { grid-area: kopf; }
  .b { grid-area: menue; }
  .c { grid-area: inhalt; }
  .d { grid-area: fuss; }
vorhersage:
  art: auswahl
  optionen:
    - text: Ein Seitenplan mit Kopf über die ganze Breite, darunter Menü links und Inhalt rechts, unten ein Fuß über die ganze Breite
      richtig: true
      erklaerung: Richtig. Der Plan im CSS sieht schon aus wie das Ergebnis.
    - text: Vier gleich große Kästen in zwei Spalten
      erklaerung: Kopf und Fuß stehen im Plan je zweimal nebeneinander, sie spannen über beide Spalten.
    - text: Alle vier untereinander
      erklaerung: Der Plan hat zwei Spalten, Menü und Inhalt stehen nebeneinander.
```

```frage
frageart: auswahl
id: bereich-form
text: Welcher Plan ist ungültig?
als_code: true
optionen:
  - text: "\"a b\" \"b a\""
    richtig: true
    erklaerung: Richtig. Bereiche müssen Rechtecke sein, hier wären a und b über Kreuz verteilt.
  - text: "\"a a\" \"b c\""
    erklaerung: Gültig, a ist ein Rechteck über die erste Zeile.
  - text: "\"a .\" \"a b\""
    erklaerung: Gültig, a ist ein Rechteck über die erste Spalte, der Punkt lässt ein Fach leer.
```

## Kinder in ihre Bereiche

`grid-area: name` beim Kind setzt es in den Bereich mit diesem Namen, egal wo es im HTML steht. So bestimmt der Plan im CSS die Anordnung und nicht die Reihenfolge im HTML. Ein Fach mit Punkt bleibt frei.

```beispiel
id: grid-area
html: |
  <div class="theke">
    <div class="kasse">Kasse</div>
    <div class="fisch">Fisch</div>
    <div class="eis">Eis</div>
  </div>
code: |
  .theke {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 80px 80px;
    grid-template-areas:
      "eis fisch fisch"
      ". fisch fisch";
    gap: 4px;
  }
  .theke div {
    padding: 8px;
  }
  .kasse { display: none; }
  .fisch { grid-area: fisch; background-color: teal; }
  .eis { grid-area: eis; background-color: #38bdf8; }
vorhersage:
  art: auswahl
  optionen:
    - text: Eis oben links, der Fisch groß über zwei Spalten und zwei Zeilen rechts, unten links ein leeres Fach
      richtig: true
      erklaerung: Richtig. Der Plan entscheidet, das Fach mit Punkt bleibt frei, und die Kasse ist ausgeblendet.
    - text: Fisch oben links, Eis rechts, wie im HTML
      erklaerung: Mit grid-area zählt der Plan, nicht die Reihenfolge im HTML.
    - text: Drei gleich große Kästen nebeneinander
      erklaerung: fisch steht im Plan viermal, das ergibt einen großen Bereich.
```

```merke
text: "`grid-column: span 2` spannt, `grid-column: 1 / -1` reicht von Linie zu Linie. `grid-template-areas` zeichnet den Plan aus Namen (`.` für leer), `grid-area: name` setzt ein Kind hinein."
```

```falle
titel: Ungleich lange Zeilen
text: "Jede Zeile in grid-template-areas braucht gleich viele Namen. Hat eine Zeile drei und die andere zwei, ist der ganze Plan ungültig und fällt still weg."
```

```augenzwinkern
text: Pit hat den Plan seines Fischwagens in grid-template-areas gezeichnet. Der Bauamt-Pinguin hat ihn sofort verstanden. Das war das erste Mal.
```
