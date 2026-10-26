---
id: css-pseudoelemente
sprache: css
titel: Pseudoelemente
kurz: Mit ::before und ::after Text und Schmuck einfügen, ohne das HTML zu ändern, den ersten Buchstaben und die erste Zeile gestalten und Listenpunkte färben.
fuehrt_ein: [before_after, first_letter, marker]
lernziele:
  - mit ::before und ::after und content Text vor und hinter ein Element setzen
  - mit leerem content kleine Schmuckkästen bauen
  - mit ::first-letter und ::first-line den Anfang eines Textes gestalten
  - mit ::marker die Punkte einer Liste gestalten
karte: Ich schmücke, ohne das HTML anzufassen
bilder:
  - schluessel: karte_css_pseudoelemente
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin klebt mit einer Schablone kleine Sterne vor und hinter ein Holzschild, ohne das Schild selbst zu bemalen
---

## Etwas davor: ::before

```alltag
text: "Pit darf das Schild am Wagen nicht neu malen, der Schildermaler ist teuer. Aber er darf Sticker davor und dahinter kleben. Genau das machen ::before und ::after: Sie fügen etwas ein, ohne das HTML zu ändern."
zeichnung: schablone
```

Ein **Pseudoelement** ist ein Teil eines Elements, das im HTML nicht vorkommt und trotzdem gestaltet werden kann. Es steht mit **zwei Doppelpunkten** am Selektor. `::before` erzeugt einen neuen Kasten **am Anfang des Inhalts**, gefüllt mit dem, was in `content` steht, als Text in Anführungszeichen.

```beispiel
id: before
html: |
  <p class="tipp">Montags gibt es doppelt Eis.</p>
  <p>Heute mit Musik.</p>
code: |
  .tipp::before {
    content: "Tipp: ";
    font-weight: bold;
    color: gold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Vor dem ersten Satz steht ein fettes goldenes Tipp:, der zweite Absatz bleibt, wie er ist
      richtig: true
      erklaerung: Richtig. ::before fügt am Anfang ein, und nur beim Absatz mit der Klasse tipp.
    - text: 'Vor beiden Absätzen steht Tipp:'
      erklaerung: Der Selektor trifft nur .tipp.
    - text: Nichts ändert sich, im HTML steht kein Tipp
      erklaerung: Genau das ist der Witz. Der Text kommt aus content, nicht aus dem HTML.
```

```frage
frageart: luecke
id: luecke-content
text: Ergänze die Eigenschaft, ohne die ::before gar nicht erscheint.
code: |
  .neu::before {
    ___: "Neu! ";
  }
antworten: [["content"]]
erklaerung: Richtig. Ohne content gibt es kein Pseudoelement.
hinweis: Der Inhalt heißt auf Englisch content.
```

## Etwas danach: ::after

`::after` fügt am **Ende des Inhalts** ein. Beliebt für Einheiten und Zeichen, die immer dazugehören, etwa die Währung hinter jedem Preis: Im HTML steht nur die Zahl, das CSS hängt den Rest an.

```beispiel
id: after
html: |
  <p>Hering <span class="preis">4,50</span></p>
  <p>Makrele <span class="preis">3,80</span></p>
code: |
  .preis {
    color: gold;
  }
  .preis::after {
    content: " Euro";
    font-size: 12px;
    color: gray;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Hinter jedem goldenen Preis steht klein und grau Euro
      richtig: true
      erklaerung: Richtig. Das Pseudoelement gehört zu jedem Element mit der Klasse preis.
    - text: Hinter jedem Preis steht Euro, ebenfalls gold und groß
      erklaerung: Das Pseudoelement hat eigene Angaben, kleiner und grau.
    - text: Euro steht vor den Preisen
      erklaerung: Vor den Preisen wäre ::before.
```

```frage
frageart: auswahl
id: wohin-after
text: Wo landet der Inhalt von ::after?
optionen:
  - text: Am Ende des Inhalts des Elements, noch innerhalb des Elements
    richtig: true
    erklaerung: Richtig. Darum hat er auch den Hintergrund des Elements hinter sich.
  - text: Hinter dem Element, als neues Geschwister
    erklaerung: Pseudoelemente stecken im Element, nicht daneben.
  - text: Ganz am Ende der Seite
    erklaerung: Sie gehören zu ihrem Element.
```

## Schmuck aus leeren Kästen

`content` darf auch **leer** sein: `content: ""`. Dann entsteht ein Kasten ohne Text, den man mit `display`, Breite, Höhe und Hintergrund zu einem Schmuckstück macht, etwa einem Punkt, einer Linie oder einer Ecke.

```beispiel
id: schmuck
html: |
  <h2>Speisekarte</h2>
code: |
  h2::after {
    content: "";
    display: block;
    width: 60px;
    height: 4px;
    margin-top: 6px;
    background-color: gold;
    border-radius: 2px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Unter der Überschrift liegt ein kurzer goldener Strich, 60 Pixel lang
      richtig: true
      erklaerung: Richtig. Ein leerer Kasten, als Block in eine eigene Zeile gesetzt.
    - text: Die Überschrift ist gold unterstrichen, über die ganze Breite
      erklaerung: Der Kasten ist nur 60 Pixel breit.
    - text: Es erscheint nichts, weil content leer ist
      erklaerung: Leer ist nicht fehlend. Ein leerer content erzeugt einen Kasten ohne Text.
```

```frage
frageart: auswahl
id: leer-oder-fehlt
text: "Was ist der Unterschied zwischen `content: \"\"` und gar keinem content?"
optionen:
  - text: Leerer content erzeugt einen leeren Kasten, ohne content gibt es gar keinen
    richtig: true
    erklaerung: Richtig.
  - text: Es gibt keinen Unterschied
    erklaerung: Ohne content erscheint das Pseudoelement überhaupt nicht.
  - text: Leerer content ist ungültig
    erklaerung: Leer ist gültig und sehr verbreitet für Schmuck.
```

## Der erste Buchstabe

`::first-letter` gestaltet den **ersten Buchstaben** eines Absatzes, wie die großen verzierten Anfangsbuchstaben in alten Büchern. `::first-line` gestaltet die **erste Zeile**, wie lang die auch gerade ist.

```beispiel
id: first-letter
html: |
  <p class="geschichte">Es war einmal ein Hering, der wollte nicht in die Pfanne. Also schwamm er bis zum Eisberg und eröffnete dort einen Fischwagen.</p>
code: |
  .geschichte::first-letter {
    font-size: 40px;
    font-family: serif;
    color: gold;
  }
  .geschichte::first-line {
    font-weight: bold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Ein großes goldenes E mit Füßchen am Anfang, die erste Zeile fett, der Rest normal
      richtig: true
      erklaerung: Richtig, zwei Pseudoelemente am selben Absatz.
    - text: Jedes Wort beginnt mit einem großen goldenen Buchstaben
      erklaerung: first-letter gilt nur für den allerersten Buchstaben des Absatzes.
    - text: Der ganze Absatz ist fett
      erklaerung: first-line trifft nur die erste Zeile.
```

```frage
frageart: luecke
id: luecke-first-letter
text: Der erste Buchstabe soll groß werden. Ergänze das Pseudoelement.
code: |
  p::___ {
    font-size: 32px;
  }
antworten: [["first-letter"]]
erklaerung: Richtig.
hinweis: Erster Buchstabe heißt first letter, mit Bindestrich.
```

## Listenpunkte mit ::marker

Die Punkte und Nummern einer Liste sind selbst ein Pseudoelement: `::marker`. Man kann ihnen eine Farbe und Größe geben oder mit `content` ein anderes Zeichen einsetzen.

```beispiel
id: marker
html: |
  <ul class="liste">
    <li>Hering</li>
    <li>Makrele</li>
  </ul>
code: |
  .liste li::marker {
    content: "> ";
    color: gold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Vor jedem Eintrag steht ein goldenes Größerzeichen statt eines Punktes
      richtig: true
      erklaerung: Richtig, der Marker bekommt einen neuen Inhalt und eine Farbe.
    - text: Die Punkte bleiben, und die Einträge werden gold
      erklaerung: Die Angaben gelten nur für den Marker, nicht für den Text.
    - text: Die Einträge verschwinden
      erklaerung: Nur der Marker ändert sich.
```

```frage
frageart: auswahl
id: marker-was
text: Was gestaltet li::marker?
optionen:
  - text: Den Punkt oder die Nummer vor dem Eintrag
    richtig: true
    erklaerung: Richtig.
  - text: Den ganzen Eintrag
    erklaerung: Dafür reicht li allein.
  - text: Den letzten Eintrag
    erklaerung: Das wäre li:last-child.
```

```merke
text: "Pseudoelemente mit zwei Doppelpunkten: `::before` und `::after` brauchen `content` (auch leer `\"\"` für Schmuck), `::first-letter` und `::first-line` gestalten den Anfang, `::marker` die Listenpunkte."
```

```falle
titel: content vergessen
text: "`.preis::after { color: gray; }` zeigt nichts. Ohne content entsteht kein Pseudoelement, ganz egal, was sonst in der Regel steht."
```

```augenzwinkern
text: "Pit hat mit ::after hinter jeden Preis ein \"nur heute\" gehängt. Das steht jetzt seit drei Jahren da."
```
