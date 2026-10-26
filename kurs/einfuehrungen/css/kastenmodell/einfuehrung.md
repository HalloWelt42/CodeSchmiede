---
id: css-kastenmodell
sprache: css
titel: Das Kastenmodell
kurz: Jedes Element ist ein Kasten aus Inhalt, Innenabstand, Rand und Außenabstand; wie breit er wirklich ist und wie box-sizing hilft.
fuehrt_ein: [breite_hoehe, padding, border, margin, box_sizing]
lernziele:
  - Breite und Höhe eines Kastens mit width und height setzen
  - Innenabstand, Rand und Außenabstand mit padding, border und margin geben
  - ausrechnen, wie breit ein Kasten von Rand zu Rand ist
  - mit box-sizing border-box die Breite einschließlich Innenabstand und Rand festlegen
  - erklären, warum sich Außenabstände übereinander schlucken
karte: Ich weiß, wie groß jeder Kasten wirklich ist
bilder:
  - schluessel: karte_css_kastenmodell
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin hängt ein Bild im Rahmen mit breitem Passepartout an eine Eiswand, mit Abstand zum Nachbarbild
---

## Jedes Element ist ein Kasten

Für den Browser ist jedes Element ein rechteckiger **Kasten**. Überschriften, Absätze und `div` nehmen von sich aus die ganze verfügbare Breite ein und sind so hoch wie ihr Inhalt. Mit `width` und `height` legt man Breite und Höhe selbst fest. Den Kasten sieht man am besten mit einem Hintergrund.

```beispiel
id: kasten
html: |
  <div class="schild">Pinguin-Ausweis</div>
  <div class="streifen">Ganz breit</div>
code: |
  .schild {
    width: 200px;
    height: 80px;
    background-color: teal;
  }
  .streifen {
    background-color: purple;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben ein Rechteck 200 mal 80 Pixel, darunter ein lila Streifen über die ganze Breite, nur so hoch wie seine Zeile
      richtig: true
      erklaerung: Richtig. Ohne width nimmt ein div die ganze Breite, ohne height ist es so hoch wie sein Inhalt.
    - text: Beide Kästen sind 200 Pixel breit
      erklaerung: width steht nur in der Regel für das Schild. Der Streifen bleibt so breit wie die Bühne.
    - text: Das Schild ist nur so breit wie das Wort Pinguin-Ausweis
      erklaerung: width setzt die Breite fest, egal wie lang der Text ist.
```

```frage
frageart: auswahl
id: wie-breit-div
text: Wie breit ist ein Absatz ohne width?
optionen:
  - text: So breit wie der Platz in seinem Elternelement
    richtig: true
    erklaerung: Richtig. Absätze, Überschriften und div füllen die Breite aus.
  - text: So breit wie sein Text
    erklaerung: So verhält sich ein span. Ein Absatz nimmt die ganze Breite ein.
  - text: Genau 100 Pixel
    erklaerung: Eine feste Vorgabe gibt es nicht. Er füllt die verfügbare Breite.
```

## Innen, Rand, außen

```alltag
text: "Ein Foto im Bilderrahmen: Um das Foto liegt ein weißer Karton, das Passepartout. Dann kommt der Rahmen. Und damit es nicht am Nachbarbild klebt, hängt es mit etwas Abstand an der Wand."
zeichnung: bilderrahmen
```

Jedes HTML-Element ist so ein Bild im Rahmen. Der **Inhalt** in der Mitte, darum der Innenabstand `padding`, dann der Rand `border`, ganz außen der Außenabstand `margin`.

- `padding: 16px` gibt rundum 16 Pixel Innenabstand; mit zwei Werten `padding: 8px 24px` oben und unten 8, links und rechts 24; mit drei Werten oben, seitlich, unten; mit vier Werten im Uhrzeigersinn oben, rechts, unten, links; einzelne Seiten gehen mit `padding-left` und Verwandten
- `border: 6px solid gold` zieht einen 6 Pixel breiten, durchgezogenen, goldenen Rand: Breite, Art, Farbe
- `margin` funktioniert wie `padding`, nur nach außen; der Wert `auto` links und rechts, etwa `margin: 0 auto`, teilt den freien Platz gleich auf und stellt einen Kasten mit fester Breite in die Mitte

Die Werkbank zeigt das Kastenmodell jedes Elements: Zeige auf ein Element der Bühne, und die vier Schichten leuchten in ihren Farben auf.

```beispiel
id: schichten
html: |
  <div class="karte">Pinguin-Ausweis</div>
code: |
  .karte {
    width: 200px;
    background-color: teal;
    padding: 16px;
    border: 6px solid #ec6aa8;
    margin: 24px;
  }
vorhersage:
  art: auswahl
  frage: Der Inhalt ist 200px breit. Wie breit ist der Kasten von Rand zu Rand, mit padding 16px und border 6px?
  optionen:
    - text: 200px
      erklaerung: Das ist nur der Inhalt. padding und border legen sich außen herum.
    - text: 222px
      erklaerung: "Fast: 200 + 16 + 6. Aber padding und border gibt es links und rechts, also je doppelt."
    - text: 244px
      richtig: true
      erklaerung: "Richtig: 200 + 2 × 16 + 2 × 6. Links und rechts zählen beide."
    - text: 292px
      erklaerung: Da ist der Außenabstand schon mitgezählt. Der liegt aber außerhalb des Randes.
```

```merke
text: "`padding` gehört zum Kasten und bekommt seine Hintergrundfarbe. `margin` ist Abstand nach draußen und bleibt immer durchsichtig."
```

```frage
frageart: luecke
id: luecke-rand
text: Der Kasten soll einen 2 Pixel breiten, durchgezogenen, schwarzen Rand bekommen. Ergänze die Art des Randes.
code: |
  .kasten {
    border: 2px ___ black;
  }
antworten: [["solid"]]
erklaerung: Richtig. Ohne Art zeichnet der Browser gar keinen Rand.
hinweis: Durchgezogen heißt auf Englisch solid.
```

## Wie breit ist der Kasten wirklich?

Von Haus aus gilt `width` nur für den **Inhalt**. Innenabstand und Rand kommen außen dazu. Ein Kasten mit `width: 200px`, `padding: 20px` und `border: 5px solid` ist also von Rand zu Rand 200 + 40 + 10 = 250 Pixel breit. Das überrascht viele: Zwei Kästen mit gleichem width können verschieden breit aussehen.

```beispiel
id: wirklich
html: |
  <div class="a">Ohne Polster</div>
  <div class="b">Mit Polster</div>
code: |
  .a, .b {
    width: 200px;
    background-color: teal;
    margin-bottom: 8px;
  }
  .b {
    padding: 0 50px;
    border: 4px solid gold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Der zweite Kasten ist deutlich breiter als der erste, 308 statt 200 Pixel
      richtig: true
      erklaerung: "Richtig: 200 + 2 × 50 + 2 × 4 = 308. width gilt nur für den Inhalt."
    - text: Beide sind gleich breit, beide haben width 200px
      erklaerung: width zählt nur den Inhalt. padding und border kommen beim zweiten noch dazu.
    - text: Der zweite ist schmaler, weil das Polster Platz wegnimmt
      erklaerung: Von Haus aus nimmt das Polster nichts weg, es kommt außen dazu.
```

```frage
frageart: auswahl
id: rechnen
text: "Wie breit ist ein Kasten mit `width: 100px; padding: 10px; border: 2px solid;` von Rand zu Rand?"
optionen:
  - text: 124px
    richtig: true
    erklaerung: "Richtig: 100 + 2 × 10 + 2 × 2."
  - text: 112px
    erklaerung: padding und border gibt es auf beiden Seiten.
  - text: 100px
    erklaerung: Das wäre so mit box-sizing border-box, davon gleich mehr.
```

## box-sizing rettet den Tag

Mit `box-sizing: border-box` gilt `width` für den ganzen Kasten **einschließlich** Innenabstand und Rand. Der Inhalt wird dann eben schmaler. Das rechnet sich viel leichter, darum setzen viele Stylesheets es gleich zu Beginn für alle Elemente: `* { box-sizing: border-box; }`.

```beispiel
id: border-box
html: |
  <div class="a">Ohne Polster</div>
  <div class="b">Mit Polster</div>
code: |
  .a, .b {
    width: 200px;
    background-color: teal;
    margin-bottom: 8px;
    box-sizing: border-box;
  }
  .b {
    padding: 0 50px;
    border: 4px solid gold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Beide Kästen sind von Rand zu Rand genau 200 Pixel breit, beim zweiten ist der Inhalt schmaler
      richtig: true
      erklaerung: "Richtig. Mit border-box zählt width den ganzen Kasten, für den Inhalt bleiben 200 - 100 - 8 = 92 Pixel."
    - text: Der zweite ist wieder 308 Pixel breit
      erklaerung: Genau das verhindert border-box. Polster und Rand werden innen abgezogen.
    - text: Der zweite verschwindet, weil kein Platz mehr bleibt
      erklaerung: Es bleiben 92 Pixel für den Inhalt. Eng, aber sichtbar.
```

```frage
frageart: luecke
id: luecke-box-sizing
text: Alle Elemente sollen width einschließlich Innenabstand und Rand rechnen. Ergänze.
code: |
  * {
    box-sizing: ___;
  }
antworten: [["border-box"]]
erklaerung: Richtig, border-box zählt bis zum Rand.
hinweis: Der Kasten reicht bis zur Grenze, englisch border.
```

## Außenabstände, die sich schlucken

Eine Eigenart von `margin`: Stoßen zwei Außenabstände **übereinander** zusammen, addieren sie sich nicht. Nur der größere zählt, der kleinere wird geschluckt. Zwei Absätze mit `margin: 20px` stehen also 20 Pixel auseinander, nicht 40. Nebeneinander passiert das nicht, und bei padding nie.

```beispiel
id: schlucken
html: |
  <p class="oben">Oben</p>
  <p class="unten">Unten</p>
code: |
  p {
    background-color: teal;
  }
  .oben {
    margin-bottom: 30px;
  }
  .unten {
    margin-top: 10px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Zwischen den Streifen liegen 30 Pixel
      richtig: true
      erklaerung: Richtig. Der größere Außenabstand gewinnt, der kleinere wird geschluckt.
    - text: Zwischen den Streifen liegen 40 Pixel
      erklaerung: Übereinander addieren sich Außenabstände nicht. Nur der größere zählt.
    - text: Zwischen den Streifen liegen 10 Pixel
      erklaerung: Es gewinnt der größere, nicht der kleinere.
```

```frage
frageart: auswahl
id: nebeneinander
text: "Zwei Absätze untereinander haben `margin-bottom: 12px` und `margin-top: 12px`. Wie groß ist der Abstand?"
optionen:
  - text: 12 Pixel
    richtig: true
    erklaerung: Richtig. Gleich große Außenabstände übereinander schlucken sich bis auf einen.
  - text: 24 Pixel
    erklaerung: Übereinander werden Außenabstände nicht addiert.
  - text: 0 Pixel, sie heben sich auf
    erklaerung: Aufgehoben wird nichts, der größere bleibt.
```

```falle
titel: Rand ohne Art
text: "`border: 4px gold` zeichnet nichts. Die Art des Randes fehlt, und ohne sie ist der Rand unsichtbar. Richtig: `border: 4px solid gold`."
```

```augenzwinkern
text: "Rechnen in CSS: die einzige Mathematik, bei der man links und rechts doppelt zählt."
```
