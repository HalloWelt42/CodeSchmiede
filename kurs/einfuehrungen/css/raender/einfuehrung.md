---
id: css-raender
sprache: css
titel: Ränder und Ecken
kurz: Gestrichelte und doppelte Ränder, einzelne Seiten, runde Ecken bis zum Kreis und Umrisse, die keinen Platz brauchen.
fuehrt_ein: [rahmenart, rahmenseite, ecken, outline]
lernziele:
  - Ränder gestrichelt, gepunktet oder doppelt zeichnen
  - nur einzelne Seiten mit einem Rand versehen
  - Ecken mit border-radius abrunden, bis zur Pille und zum Kreis
  - einzelne Ecken verschieden rund machen
  - mit outline einen Umriss zeichnen, der keinen Platz einnimmt
karte: Ich runde jede Ecke ab
bilder:
  - schluessel: karte_css_raender
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin schleift mit einer Feile die Ecken einer Eisscholle rund, daneben liegt eine kreisrunde Scholle
---

## Arten von Rändern

```alltag
text: 'Am Fischwagen hängen Schilder mit allen möglichen Rändern: Das Angebot hat einen gestrichelten zum Ausschneiden, die Urkunde einen doppelten Goldrand, und die Eisscholle ist rund geschliffen, damit sich niemand stößt.'
zeichnung: feile
```

Die Art des Randes, die zweite Angabe in `border`, bestimmt sein Aussehen: `solid` (durchgezogen), `dashed` (gestrichelt), `dotted` (gepunktet) oder `double` (doppelt, braucht mindestens 3 Pixel Breite, damit zwei Linien und eine Lücke hineinpassen).

```beispiel
id: arten
html: |
  <p class="a">Gutschein zum Ausschneiden</p>
  <p class="b">Urkunde für den besten Hering</p>
  <p class="c">Kleingedrucktes</p>
code: |
  p {
    padding: 8px;
  }
  .a {
    border: 3px dashed gold;
  }
  .b {
    border: 6px double gold;
  }
  .c {
    border: 3px dotted gray;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Ein gestrichelter, ein doppelter und ein gepunkteter Rand
      richtig: true
      erklaerung: Richtig, drei Arten, drei Bilder.
    - text: Drei durchgezogene Ränder in verschiedenen Farben
      erklaerung: Die Art steht zwischen Breite und Farbe, und keiner ist solid.
    - text: Nur der erste Absatz hat einen Rand, die anderen Arten gibt es nicht
      erklaerung: double und dotted gibt es genauso wie dashed.
```

```frage
frageart: luecke
id: luecke-gestrichelt
text: Ergänze die Art für einen gestrichelten Rand.
code: |
  .gutschein {
    border: 2px ___ black;
  }
antworten: [["dashed"]]
erklaerung: Richtig, dashed heißt gestrichelt.
hinweis: Ein Strich heißt auf Englisch dash.
```

## Einzelne Seiten

Statt rundum geht ein Rand auch nur an einer Seite: `border-top`, `border-right`, `border-bottom` und `border-left` nehmen dieselben drei Angaben wie `border`. So entstehen Unterstreichungen über die ganze Breite oder ein farbiger Balken am Rand.

```beispiel
id: seiten
html: |
  <h2>Speisekarte</h2>
  <p class="tipp">Tipp: Montags gibt es doppelt Eis.</p>
code: |
  h2 {
    border-bottom: 3px solid gold;
  }
  .tipp {
    border-left: 6px solid teal;
    padding-left: 10px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Unter der Überschrift eine goldene Linie über die ganze Breite, links neben dem Tipp ein türkiser Balken
      richtig: true
      erklaerung: Richtig. Die Überschrift ist so breit wie die Bühne, also auch ihre Linie.
    - text: Die Überschrift ist nur unter den Buchstaben unterstrichen
      erklaerung: Der Rand gehört zum Kasten, und der ist so breit wie die Bühne.
    - text: Beide bekommen einen Rand rundherum
      erklaerung: border-bottom und border-left zeichnen nur ihre eine Seite.
```

```frage
frageart: auswahl
id: welche-seite
text: Welche Angabe zieht eine Linie über einem Element?
als_code: true
optionen:
  - text: "border-top: 1px solid white;"
    richtig: true
    erklaerung: Richtig, top ist oben.
  - text: "border-bottom: 1px solid white;"
    erklaerung: bottom ist unten.
  - text: "border-over: 1px solid white;"
    erklaerung: Die Seiten heißen top, right, bottom und left.
```

## Runde Ecken

`border-radius` rundet die Ecken eines Kastens ab, mit oder ohne Rand: Der Hintergrund wird mit abgerundet. Der Wert ist der Radius der Rundung. Ein sehr großer Wert wie `999px` macht aus einem flachen Kasten eine **Pille**, und ist ein Kasten quadratisch, wird er mit dem halben Seitenmaß zum **Kreis**.

```beispiel
id: rund
html: |
  <div class="karte">Karte</div>
  <div class="pille">Pille</div>
  <div class="kreis">Kreis</div>
code: |
  div {
    background-color: teal;
    margin-bottom: 10px;
    padding: 8px;
  }
  .karte {
    width: 200px;
    border-radius: 6px;
  }
  .pille {
    width: 200px;
    border-radius: 999px;
  }
  .kreis {
    width: 64px;
    height: 64px;
    border-radius: 40px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Ein Kasten mit leicht runden Ecken, eine Pille mit halbrunden Enden und ein Kreis
      richtig: true
      erklaerung: Richtig. Der Kreis ist samt Polster 80 Pixel groß, und 40 ist die Hälfte.
    - text: Drei gleiche Kästen, border-radius geht nur mit einem Rand
      erklaerung: Gerundet wird der Kasten selbst, auch der Hintergrund, mit oder ohne Rand.
    - text: Die Pille ist ein riesiger Kreis von 999 Pixeln
      erklaerung: Größer als halb so hoch wie der Kasten kann die Rundung nicht werden, darum bleibt es eine Pille.
```

```frage
frageart: auswahl
id: kreis
text: "Ein Kasten ist 60 mal 60 Pixel groß (ohne Polster und Rand). Welcher Radius macht ihn zum Kreis?"
optionen:
  - text: 30px
    richtig: true
    erklaerung: Richtig, die Hälfte der Seite.
  - text: 15px
    erklaerung: Das ergibt ein Quadrat mit runden Ecken. Für den Kreis braucht es die halbe Seite.
  - text: 6px
    erklaerung: Das rundet nur die Ecken ein wenig ab.
```

## Ecken einzeln

Mit vier Werten bekommt jede Ecke ihre eigene Rundung, wieder im Uhrzeigersinn, diesmal von **oben links**: `border-radius: 20px 0 20px 0` rundet oben links und unten rechts, die anderen Ecken bleiben spitz. Mit zwei Werten gilt der erste für oben links und unten rechts, der zweite für die anderen beiden.

```beispiel
id: einzeln
html: |
  <p class="blase">Frischer Fisch!</p>
code: |
  .blase {
    width: 200px;
    padding: 12px;
    background-color: gold;
    color: black;
    border-radius: 20px 20px 20px 0;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Eine Sprechblase, nur die Ecke unten links ist spitz
      richtig: true
      erklaerung: Richtig. Die vierte Angabe gehört zur Ecke unten links.
    - text: Nur die Ecke oben links ist spitz
      erklaerung: Gezählt wird von oben links im Uhrzeigersinn, die 0 steht an vierter Stelle, also unten links.
    - text: Alle Ecken sind gleich rund
      erklaerung: Mit vier Werten bekommt jede Ecke ihren eigenen.
```

```frage
frageart: luecke
id: luecke-ecken
text: Nur die beiden oberen Ecken sollen 10 Pixel rund sein, wie bei einem Reiter. Ergänze die fehlenden Werte.
code: |
  .reiter {
    border-radius: 10px 10px ___ ___;
  }
antworten: [["0", "0px"], ["0", "0px"]]
erklaerung: Richtig. Oben links, oben rechts, unten rechts, unten links.
hinweis: Die unteren Ecken bleiben spitz, also null.
```

## Umrisse mit outline

`outline` sieht aus wie ein Rand und nimmt dieselben drei Angaben, braucht aber **keinen Platz**: Der Umriss wird außen um den Kasten gezeichnet, ohne etwas zu verschieben. Mit `outline-offset` rückt man ihn ein Stück nach außen. Browser nutzen Umrisse zum Beispiel, um zu zeigen, welches Element gerade bedient wird.

```beispiel
id: outline
html: |
  <p class="a">Mit Rand</p>
  <p class="b">Mit Umriss</p>
  <p>Darunter</p>
code: |
  .a, .b {
    width: 200px;
    background-color: teal;
  }
  .a {
    border: 8px solid gold;
  }
  .b {
    outline: 8px solid gold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Der erste Kasten wird durch den Rand größer, der Umriss des zweiten ragt in die Umgebung hinein, ohne etwas zu verschieben
      richtig: true
      erklaerung: Richtig. Der Rand zählt zum Kasten, der Umriss liegt nur darüber.
    - text: Beide sehen völlig gleich aus und stehen gleich weit auseinander
      erklaerung: Der Rand macht den ersten Kasten 16 Pixel breiter und höher. Der Umriss braucht keinen Platz.
    - text: Der Umriss ist unsichtbar, weil outline nur beim Anklicken erscheint
      erklaerung: Eine Regel mit outline zeichnet den Umriss immer.
```

```frage
frageart: auswahl
id: outline-platz
text: Ein Kasten bekommt statt eines Randes von 5 Pixeln einen Umriss von 5 Pixeln. Was passiert mit dem Absatz darunter?
optionen:
  - text: Er rückt 10 Pixel nach oben, denn der Umriss braucht keinen Platz
    richtig: true
    erklaerung: Richtig. Oben und unten fallen je 5 Pixel Rand weg, der Umriss nimmt keinen Platz ein.
  - text: Er bleibt, wo er ist
    erklaerung: Der Rand hat Platz gebraucht, der Umriss braucht keinen. Also rückt der Absatz nach.
  - text: Er rückt 10 Pixel nach unten
    erklaerung: Der Umriss macht nichts größer, eher im Gegenteil.
```

```merke
text: "`border` mit `solid`, `dashed`, `dotted`, `double`; einzelne Seiten mit `border-top` und Verwandten; `border-radius` für runde Ecken, vier Werte von oben links im Uhrzeigersinn; `outline` zeichnet ohne Platz zu brauchen."
```

```falle
titel: Kreis mit Polster
text: "Ein Kasten mit `width: 60px; height: 60px; padding: 10px;` ist ohne box-sizing 80 Pixel groß. Für einen Kreis braucht er dann 40 Pixel Radius. Mit 30 bleibt ein Quadrat mit runden Ecken."
```

```augenzwinkern
text: Pit hat die Ecken des Wagens so rund geschliffen, dass er jetzt rollt. Seitdem steht der Fischwagen jeden Tag woanders.
```
