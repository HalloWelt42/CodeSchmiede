---
id: css-schatten
sprache: css
titel: Schatten und Verläufe
kurz: Schatten unter Kästen und Text, mehrere und innere Schatten, Farbverläufe gerade und rund.
fuehrt_ein: [box_shadow, text_shadow, verlauf]
lernziele:
  - Kästen mit box-shadow einen Schatten geben
  - Schatten mit Ausdehnung, innen und mehrfach zeichnen
  - Text mit text-shadow einen Schatten geben
  - einen geraden Farbverlauf mit linear-gradient als Hintergrund setzen
  - runde Verläufe und harte Streifen mit Farbhalten bauen
karte: Ich lasse Dinge schweben
bilder:
  - schluessel: karte_css_schatten
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin schwebt mit einem Schirm über einer Eisscholle und wirft einen weichen Schatten, der Himmel dahinter verläuft von Orange zu Blau
---

## Schatten unter Kästen

```alltag
text: Hält Pit eine Speisekarte über den Tresen, fällt ein Schatten darunter. Je höher er sie hält, desto weicher und weiter weg liegt der Schatten. Schatten sagen dem Auge, was über was schwebt.
zeichnung: schirm
```

`box-shadow` zeichnet einen Schatten unter einen Kasten. Die Werte der Reihe nach: Versatz nach rechts, Versatz nach unten, **Unschärfe** und Farbe. `box-shadow: 6px 6px 12px black` legt einen weichen schwarzen Schatten nach rechts unten. Negative Versätze schieben ihn nach links oder oben. Der Schatten folgt den runden Ecken und braucht keinen Platz.

```beispiel
id: schatten
html: |
  <div class="karte">Schwebt</div>
  <div class="karte hart">Klebt</div>
code: |
  .karte {
    width: 160px;
    padding: 20px;
    margin-bottom: 30px;
    background-color: #fbf4e2;
    color: #2b3442;
    border-radius: 8px;
    box-shadow: 8px 8px 16px black;
  }
  .hart {
    box-shadow: 4px 4px 0 gold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben ein weicher dunkler Schatten nach rechts unten, unten ein scharfer goldener Schatten, beide mit runden Ecken
      richtig: true
      erklaerung: Richtig. Unschärfe 0 gibt eine harte Kante, und der Schatten folgt der Form des Kastens.
    - text: Beide Schatten sind schwarz und weich
      erklaerung: Für .hart gilt die genauere Regel mit gold und Unschärfe 0.
    - text: Die Schatten schieben die Kästen auseinander
      erklaerung: Schatten brauchen keinen Platz, sie liegen nur unter dem Kasten.
```

```frage
frageart: auswahl
id: schatten-lesen
text: "Wohin fällt `box-shadow: -5px 10px 4px gray`?"
optionen:
  - text: Nach links unten
    richtig: true
    erklaerung: Richtig. Negativ nach rechts heißt links, positiv nach unten heißt unten.
  - text: Nach rechts oben
    erklaerung: Der erste Wert ist negativ, also nach links. Der zweite positiv, also nach unten.
  - text: Nur unscharf rundherum
    erklaerung: Die Versätze schieben ihn, rundherum wäre er bei 0 0.
```

## Mehr aus Schatten

Ein fünfter Wert vor der Farbe, die **Ausdehnung**, macht den Schatten größer als den Kasten. Mit dem Wort `inset` vorne fällt der Schatten **nach innen**, als wäre der Kasten eingedrückt. Und mehrere Schatten trennt man mit Komma; der erste liegt oben.

```beispiel
id: mehr-schatten
html: |
  <div class="schale">Eisschale</div>
  <div class="glow">Leuchtfisch</div>
code: |
  div {
    width: 160px;
    padding: 20px;
    margin: 24px;
    background-color: #1f6f8b;
    border-radius: 12px;
  }
  .schale {
    box-shadow: inset 0 0 12px black;
  }
  .glow {
    box-shadow: 0 0 0 4px gold, 0 0 20px 8px orange;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die Schale wirkt nach innen gewölbt, der Leuchtfisch hat einen goldenen Ring und einen orangen Schein
      richtig: true
      erklaerung: Richtig. inset zeichnet nach innen, und zwei Schatten mit Komma liegen übereinander.
    - text: Beide haben einen dunklen Schatten unter sich
      erklaerung: inset wirft den Schatten nach innen, und der zweite Kasten hat zwei bunte Schatten ohne Versatz.
    - text: Der goldene Ring liegt unter dem orangen Schein und ist nicht zu sehen
      erklaerung: Der erste Schatten liegt oben, der goldene Ring ist also vorn.
```

```frage
frageart: luecke
id: luecke-inset
text: Der Kasten soll eingedrückt aussehen. Ergänze das Wort.
code: |
  .feld {
    box-shadow: ___ 0 2px 6px black;
  }
antworten: [["inset"]]
erklaerung: Richtig, inset wirft den Schatten nach innen.
hinweis: Innen heißt in, eingesetzt inset.
```

## Schatten unter Text

`text-shadow` funktioniert wie `box-shadow`, nur für die Buchstaben: Versatz rechts, Versatz unten, Unschärfe, Farbe. Ohne Unschärfe gibt es harte Doppelbuchstaben, mit viel Unschärfe ein Leuchten. Ausdehnung und inset gibt es bei Text nicht.

```beispiel
id: textschatten
html: |
  <h1 class="leuchten">Fischfest</h1>
  <h1 class="kante">Fischfest</h1>
code: |
  .leuchten {
    color: white;
    text-shadow: 0 0 12px gold;
  }
  .kante {
    color: gold;
    text-shadow: 3px 3px 0 crimson;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben weiße Buchstaben mit goldenem Leuchten, unten goldene Buchstaben mit einer harten roten Kante rechts unten
      richtig: true
      erklaerung: Richtig. Ohne Versatz und mit Unschärfe leuchtet es, mit Versatz und ohne Unschärfe gibt es eine Kante.
    - text: Beide Überschriften haben einen Kasten mit Schatten
      erklaerung: text-shadow wirft den Schatten der Buchstaben, nicht des Kastens.
    - text: Oben ist nichts zu sehen, weil der Schatten keinen Versatz hat
      erklaerung: Mit Unschärfe ragt der Schatten auch ohne Versatz rundum heraus und leuchtet.
```

```frage
frageart: auswahl
id: textschatten-eigenschaft
text: Welche Eigenschaft gibt Buchstaben einen Schatten?
als_code: true
optionen:
  - text: text-shadow
    richtig: true
    erklaerung: Richtig.
  - text: box-shadow
    erklaerung: box-shadow wirft den Schatten des ganzen Kastens.
  - text: font-shadow
    erklaerung: Die gibt es nicht. Der Schatten von Text heißt text-shadow.
```

## Farbverläufe

Ein **Farbverlauf** ist ein Bild, das der Browser selbst malt. Darum steht er nicht bei `background-color`, sondern bei `background-image` oder kurz `background`: `background: linear-gradient(to right, gold, crimson)` verläuft von links nach rechts von Gold zu Rot. Die Richtung beginnt mit `to`: `to bottom` (die Voreinstellung), `to right`, `to top`, `to left`, auch schräg wie `to bottom right`. Es dürfen beliebig viele Farben folgen.

```beispiel
id: verlauf
html: |
  <div class="himmel">Sonnenuntergang</div>
  <div class="meer">Meer</div>
code: |
  div {
    height: 80px;
    padding: 10px;
  }
  .himmel {
    background: linear-gradient(to bottom, orange, crimson, #2b1a4a);
  }
  .meer {
    background: linear-gradient(to right, #0b4f8a, #38bdf8);
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben von Orange über Rot zu Dunkellila nach unten, darunter von Dunkelblau links zu Hellblau rechts
      richtig: true
      erklaerung: Richtig. Drei Farben verteilen sich gleichmäßig, die Richtung steht vorne.
    - text: Beide verlaufen von oben nach unten
      erklaerung: Beim Meer steht to right, es verläuft von links nach rechts.
    - text: Nur die erste und die letzte Farbe sind zu sehen
      erklaerung: Alle Farben kommen vor, gleichmäßig verteilt.
```

```frage
frageart: luecke
id: luecke-verlauf
text: Der Verlauf soll von links nach rechts gehen. Ergänze die Richtung.
code: |
  .streifen {
    background: linear-gradient(___, white, teal);
  }
antworten: [["to right"]]
erklaerung: Richtig, to right heißt nach rechts.
hinweis: Zwei Wörter, das erste ist to.
```

## Runde Verläufe und Streifen

`radial-gradient` verläuft **kreisförmig** von der Mitte nach außen. Und hinter jede Farbe darf eine Stelle in Prozent, ein **Farbhalt**: `linear-gradient(to right, gold 50%, teal 50%)` heißt Gold bis zur Hälfte, dann sofort Teal. Zwei Farben an derselben Stelle ergeben eine harte Kante statt eines Übergangs, so entstehen Streifen.

```beispiel
id: rund-und-streifen
html: |
  <div class="sonne">Sonne</div>
  <div class="markise">Markise</div>
code: |
  div {
    height: 90px;
    padding: 10px;
    color: #2b3442;
  }
  .sonne {
    background: radial-gradient(gold, orange, #0b1d3a);
  }
  .markise {
    background: linear-gradient(to right, white 25%, crimson 25%, crimson 50%, white 50%, white 75%, crimson 75%);
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben ein goldenes Leuchten in der Mitte, das nach außen dunkel wird, unten vier harte Streifen weiß und rot im Wechsel
      richtig: true
      erklaerung: Richtig. Gleiche Stellen für zwei Farben geben harte Kanten.
    - text: Unten ein weicher Übergang von Weiß zu Rot
      erklaerung: Die Farbhalte liegen paarweise auf derselben Stelle, darum gibt es keinen Übergang, sondern Kanten.
    - text: Oben ein Verlauf von links nach rechts
      erklaerung: radial-gradient verläuft von der Mitte nach außen.
```

```frage
frageart: auswahl
id: harte-kante
text: "Wie sieht `linear-gradient(to right, gold 30%, teal 30%)` aus?"
optionen:
  - text: Links ein goldenes Drittel, dann mit scharfer Kante Teal
    richtig: true
    erklaerung: Richtig. Beide Farben an derselben Stelle geben eine harte Kante.
  - text: Ein weicher Übergang von Gold nach Teal über die ganze Breite
    erklaerung: Ohne Farbhalte wäre es weich. Hier liegen beide auf 30 Prozent.
  - text: Nur Teal, Gold wird überdeckt
    erklaerung: Gold reicht bis 30 Prozent, erst danach beginnt Teal.
```

```merke
text: "`box-shadow: x y unschärfe [ausdehnung] farbe` (mit `inset` innen, mehrere mit Komma), `text-shadow: x y unschärfe farbe`, Verläufe als `background: linear-gradient(to right, a, b)` oder `radial-gradient(a, b)`, Farbhalte in Prozent."
```

```falle
titel: Verlauf bei background-color
text: "`background-color: linear-gradient(...)` ist ungültig und fällt still weg. Ein Verlauf ist ein Bild, er gehört zu `background` oder `background-image`."
```

```augenzwinkern
text: Pit hat dem Fischwagen einen Schatten mit 200 Pixeln Unschärfe gegeben. Jetzt sieht es aus, als würde er schweben, und die Kundschaft fragt, ob er auch fliegen kann.
```
