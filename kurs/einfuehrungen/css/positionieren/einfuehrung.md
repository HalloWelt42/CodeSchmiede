---
id: css-positionieren
sprache: css
titel: Positionieren
kurz: Elemente ein Stück verschieben, frei auf eine Fläche setzen, den Bezugsrahmen wählen und bestimmen, was oben liegt.
fuehrt_ein: [position_relative, position_absolute, versatz, z_index]
lernziele:
  - mit position relative ein Element verschieben, ohne die anderen zu stören
  - mit position absolute ein Element frei platzieren
  - mit position relative bei den Eltern den Bezugsrahmen festlegen
  - mit top, right, bottom, left und inset die Lage angeben
  - mit z-index bestimmen, was oben liegt
karte: Ich setze Dinge genau dahin, wo ich will
bilder:
  - schluessel: karte_css_positionieren
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin klebt einen runden roten Aufkleber schräg in die Ecke einer Speisekarte an einer Pinnwand
---

## Ein Stück verschieben: relative

```alltag
text: "Pit hat die Speisekarte an die Pinnwand gehängt. Jetzt klebt er einen roten Aufkleber Neu! in die obere rechte Ecke. Der Aufkleber verdrängt nichts, er liegt einfach obendrauf. Genau dafür ist position da."
zeichnung: aufkleber
```

Bisher hat der Browser jedes Element an seine Stelle im Fluss gesetzt, eins nach dem anderen. Mit `position: relative` und einem **Versatz** wie `top: 10px` oder `left: 20px` verschiebt man ein Element von seiner Stelle aus. Wichtig: Sein **Platz bleibt reserviert**, die anderen merken nichts von der Verschiebung. `top: 10px` heißt 10 Pixel Abstand von oben, also nach unten; `left: 20px` nach rechts.

```beispiel
id: relative
html: |
  <p class="a">Hering</p>
  <p class="b">Makrele</p>
  <p class="c">Sardine</p>
code: |
  p {
    background-color: teal;
    width: 200px;
  }
  .b {
    position: relative;
    top: 24px;
    left: 40px;
    background-color: crimson;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Makrele ist nach rechts unten verrutscht und überdeckt ein Stück der Sardine, die bleibt, wo sie war
      richtig: true
      erklaerung: Richtig. Der Platz von Makrele bleibt frei, darum rückt die Sardine nicht nach.
    - text: Makrele rückt nach rechts unten, und die Sardine rutscht mit nach unten
      erklaerung: Mit relative merken die anderen nichts. Die Sardine bleibt an ihrer Stelle.
    - text: Makrele springt in die linke obere Ecke der Bühne
      erklaerung: relative verschiebt von der eigenen Stelle aus, nicht von der Bühne.
```

```frage
frageart: auswahl
id: wohin-left
text: "In welche Richtung verschiebt `position: relative; left: 30px`?"
optionen:
  - text: Nach rechts, 30 Pixel Abstand von links
    richtig: true
    erklaerung: Richtig. left ist der Abstand zur linken Kante, mehr Abstand heißt weiter rechts.
  - text: Nach links
    erklaerung: Nach links ginge es mit einem negativen Wert oder mit right.
  - text: Gar nicht, left gilt nur für Text
    erklaerung: left verschiebt das Element, sobald es positioniert ist.
```

## Frei auf der Fläche: absolute

`position: absolute` nimmt ein Element **aus dem Fluss**: Sein Platz verschwindet, die anderen rücken nach, als gäbe es es nicht. Mit `top`, `right`, `bottom` und `left` setzt man es dann frei auf die Fläche. `top: 0; right: 0` heißt: in die obere rechte Ecke.

```beispiel
id: absolute
html: |
  <p>Hering</p>
  <p class="stempel">Neu!</p>
  <p>Makrele</p>
code: |
  p {
    background-color: teal;
    width: 200px;
  }
  .stempel {
    position: absolute;
    top: 0;
    right: 0;
    margin: 0;
    background-color: crimson;
    width: 80px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Hering und Makrele stehen direkt untereinander, Neu! sitzt in der oberen rechten Ecke der Bühne
      richtig: true
      erklaerung: Richtig. Der Stempel ist aus dem Fluss genommen, darum rückt Makrele nach.
    - text: Zwischen Hering und Makrele bleibt eine Lücke für Neu!
      erklaerung: Bei absolute verschwindet der Platz. Nur bei relative bleibt er frei.
    - text: Neu! steht in der oberen rechten Ecke über dem Hering
      erklaerung: right 0 heißt rechter Rand der Bühne, nicht rechts vom Hering.
```

```frage
frageart: auswahl
id: platz-weg
text: Was passiert mit dem Platz eines Elements mit position absolute?
optionen:
  - text: Er verschwindet, die anderen rücken nach
    richtig: true
    erklaerung: Richtig, das Element ist aus dem Fluss genommen.
  - text: Er bleibt frei, wie bei relative
    erklaerung: Das gilt nur für relative.
  - text: Er wird doppelt so groß
    erklaerung: Mit Größe hat position nichts zu tun.
```

## Der Bezugsrahmen

Woran misst `absolute` seine Lage? Am nächsten Vorfahren, der **selbst positioniert** ist, also etwa `position: relative` trägt. Gibt es keinen, gilt das ganze Fenster. Darum der Klassiker: Der Behälter bekommt `position: relative` (ohne Versatz, er bleibt also, wo er ist), und das Kind mit `absolute` richtet sich nach ihm.

```beispiel
id: bezug
html: |
  <div class="karte">
    <p>Hering</p>
    <p>Makrele</p>
    <span class="stempel">Neu!</span>
  </div>
code: |
  .karte {
    position: relative;
    width: 260px;
    margin: 30px;
    padding: 10px;
    background-color: #2b3442;
  }
  .stempel {
    position: absolute;
    top: -12px;
    right: -12px;
    background-color: crimson;
    padding: 4px 8px;
    border-radius: 999px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Der Stempel sitzt schräg über der oberen rechten Ecke der Karte und ragt ein Stück über sie hinaus
      richtig: true
      erklaerung: Richtig. Die Karte ist der Bezugsrahmen, und die negativen Werte schieben den Stempel über ihre Ecke hinaus.
    - text: Der Stempel sitzt in der oberen rechten Ecke der Bühne
      erklaerung: Die Karte ist positioniert, also misst der Stempel an ihr, nicht an der Bühne.
    - text: Der Stempel steht unter Makrele im Fluss
      erklaerung: absolute nimmt ihn aus dem Fluss.
```

```frage
frageart: luecke
id: luecke-bezug
text: Das Kind mit position absolute soll sich nach der Kiste richten. Ergänze den Wert bei der Kiste.
code: |
  .kiste {
    position: ___;
  }
antworten: [["relative"]]
erklaerung: Richtig, relative ohne Versatz macht die Kiste zum Bezugsrahmen, ohne sie zu bewegen.
hinweis: Der Wert, bei dem das Element an seiner Stelle bleibt.
```

## Was liegt oben: z-index

Überdecken sich positionierte Elemente, liegt normalerweise das spätere im HTML oben. `z-index` ändert das: Wer die **größere Zahl** hat, liegt oben. Das wirkt nur bei positionierten Elementen.

```beispiel
id: z-index
html: |
  <div class="stapel">
    <div class="a">Pit</div>
    <div class="b">Pia</div>
    <div class="c">Paul</div>
  </div>
code: |
  .stapel {
    position: relative;
    height: 180px;
  }
  .stapel div {
    position: absolute;
    width: 120px;
    height: 80px;
    padding: 6px;
  }
  .stapel .a { top: 0; left: 0; background-color: teal; z-index: 3; }
  .stapel .b { top: 30px; left: 50px; background-color: crimson; }
  .stapel .c { top: 60px; left: 100px; background-color: purple; z-index: 2; }
vorhersage:
  art: auswahl
  optionen:
    - text: Pit liegt ganz oben, dann Paul, Pia liegt unten
      richtig: true
      erklaerung: Richtig. Pit hat 3, Paul 2, Pia gar keinen z-index und damit den kleinsten.
    - text: Paul liegt oben, er steht zuletzt im HTML
      erklaerung: Die Reihenfolge im HTML zählt nur ohne z-index. Pit hat die größte Zahl.
    - text: Alle liegen nebeneinander ohne Überdeckung
      erklaerung: Die Versätze sind kleiner als die Kästen, sie überdecken sich.
```

```frage
frageart: auswahl
id: z-wer-oben
text: "Zwei positionierte Kästen überdecken sich. A hat `z-index: 1`, B hat `z-index: 5`. Welcher liegt oben?"
optionen:
  - text: B
    richtig: true
    erklaerung: Richtig, die größere Zahl liegt oben.
  - text: A
    erklaerung: Die kleinere Zahl liegt weiter unten.
  - text: Der spätere im HTML, egal welche Zahl
    erklaerung: Das gilt nur, wenn kein z-index gesetzt ist oder beide gleich sind.
```

## Festnageln mit inset

Setzt man gegenüberliegende Seiten zugleich, etwa `top: 0; bottom: 0`, wird das Element dazwischen **aufgespannt**. Die Kurzform `inset` setzt alle vier: `inset: 0` füllt den ganzen Bezugsrahmen, `inset: 10px` lässt rundum 10 Pixel frei. Praktisch für Schleier und Rahmen über einem Bild.

```beispiel
id: inset
html: |
  <div class="bild">
    Riesenhering
    <div class="schleier"></div>
  </div>
code: |
  .bild {
    position: relative;
    height: 160px;
    background-color: #38bdf8;
    padding: 10px;
  }
  .schleier {
    position: absolute;
    inset: 20px;
    border: 3px dashed white;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Ein weißer gestrichelter Rahmen mit 20 Pixeln Abstand rundum im blauen Feld
      richtig: true
      erklaerung: Richtig. inset 20px hält zu allen vier Seiten 20 Pixel Abstand.
    - text: Der Rahmen ist unsichtbar, weil das div keinen Inhalt hat
      erklaerung: Mit allen vier Seiten festgenagelt bekommt es seine Größe vom Bezugsrahmen, auch ohne Inhalt.
    - text: Der Rahmen umschließt nur das Wort Riesenhering
      erklaerung: Der Schleier richtet sich nach dem Bild, nicht nach dem Text.
```

```frage
frageart: luecke
id: luecke-inset
text: Der Schleier soll den ganzen Bezugsrahmen ausfüllen. Ergänze den Wert.
code: |
  .schleier {
    position: absolute;
    inset: ___;
  }
antworten: [["0", "0px"]]
erklaerung: Richtig, null Abstand zu allen vier Seiten.
hinweis: Kein Abstand zu keiner Seite.
```

```merke
text: "`position: relative` verschiebt, der Platz bleibt. `position: absolute` nimmt aus dem Fluss und misst am nächsten positionierten Vorfahren. Lage mit `top`, `right`, `bottom`, `left` oder `inset`, Stapel mit `z-index`."
```

```falle
titel: absolute ohne Bezugsrahmen
text: "Fehlt beim Behälter `position: relative`, misst ein absolut positioniertes Kind am ganzen Fenster. Der Aufkleber landet dann in der Ecke der Seite statt in der Ecke der Karte."
```

```augenzwinkern
text: Pit hat den Aufkleber mit z-index 9999 festgeklebt. Seitdem liegt er über allem, auch über der Rechnung. Die Kundschaft findet das gut.
```
