---
id: css-verwandeln
sprache: css
titel: Verwandeln
kurz: Elemente mit transform verschieben, drehen und vergrößern, den Drehpunkt wählen und mit transition sanft wechseln lassen.
fuehrt_ein: [transform, grad, transform_origin, transition]
lernziele:
  - mit translate ein Element verschieben, ohne andere zu stören
  - mit rotate und der Einheit deg drehen
  - mit scale vergrößern und verkleinern
  - mehrere Verwandlungen verbinden und mit transform-origin den Drehpunkt wählen
  - erklären, was transition beim Wechsel eines Zustands tut
karte: Ich drehe und wende alles, wie ich will
bilder:
  - schluessel: karte_css_verwandeln
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin wirft eine Fischkiste hoch, die sich in der Luft dreht und dabei größer wird
---

## Verschieben mit translate

```alltag
text: "Wenn Pit ein Schild schief aufhängt, zieht er es zurecht, ohne dass die Schilder daneben verrutschen. transform verwandelt nur das Aussehen eines Elements: Für alle anderen bleibt es da, wo es war."
zeichnung: wirbel
```

`transform` verwandelt ein Element nur **im Bild**: Sein Platz im Fluss bleibt, wie er war, die Nachbarn merken nichts. `transform: translate(30px, 10px)` verschiebt es 30 Pixel nach rechts und 10 nach unten. Prozent beziehen sich hier auf das Element selbst: `translate(-50%, 0)` verschiebt um die halbe eigene Breite nach links.

```beispiel
id: translate
html: |
  <div class="a">Hering</div>
  <div class="b">Makrele</div>
  <div class="c">Sardine</div>
code: |
  div {
    width: 160px;
    padding: 8px;
    background-color: teal;
    margin-bottom: 4px;
  }
  .b {
    transform: translate(80px, 20px);
    background-color: crimson;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Makrele ist nach rechts unten verschoben und überdeckt die Sardine, die bleibt an ihrem Platz
      richtig: true
      erklaerung: Richtig. transform ändert nur das Bild, der Platz bleibt reserviert.
    - text: Makrele ist verschoben, und die Sardine rückt mit nach unten
      erklaerung: Bei transform merken die Nachbarn nichts.
    - text: Makrele ist doppelt so breit
      erklaerung: translate verschiebt nur, die Größe bleibt.
```

```frage
frageart: auswahl
id: translate-prozent
text: "Worauf bezieht sich `translate(50%, 0)`?"
optionen:
  - text: Auf die eigene Breite des Elements
    richtig: true
    erklaerung: Richtig, anders als bei width, wo Prozent am Elternelement hängen.
  - text: Auf die Breite der Eltern
    erklaerung: Das gilt für width. Bei translate zählt das Element selbst.
  - text: Auf die Bühne
    erklaerung: Bei translate zählt das Element selbst.
```

## Drehen mit rotate

`rotate()` dreht um den Mittelpunkt. Gemessen wird in **Grad** mit der Einheit `deg`: `rotate(90deg)` ist eine Vierteldrehung im Uhrzeigersinn, `rotate(-10deg)` ein klein wenig gegen den Uhrzeigersinn.

```beispiel
id: rotate
html: |
  <div class="schild">Geöffnet</div>
code: |
  .schild {
    width: 160px;
    margin: 40px;
    padding: 12px;
    text-align: center;
    background-color: #3fb950;
    color: #0b1d3a;
    transform: rotate(-12deg);
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Das Schild hängt leicht schief, rechts höher als links
      richtig: true
      erklaerung: Richtig. Negative Grad drehen gegen den Uhrzeigersinn, die rechte Seite hebt sich.
    - text: Das Schild steht senkrecht, um 90 Grad gedreht
      erklaerung: 12 Grad sind nur ein Kippen, keine Vierteldrehung.
    - text: Nur der Text ist schief, der grüne Kasten nicht
      erklaerung: transform dreht das ganze Element mit allem darin.
```

```frage
frageart: luecke
id: luecke-grad
text: Das Element soll um eine Vierteldrehung im Uhrzeigersinn gedreht werden. Ergänze den Wert.
code: |
  .pfeil {
    transform: rotate(___);
  }
antworten: [["90deg"]]
erklaerung: Richtig, 90 Grad.
hinweis: Eine ganze Drehung sind 360 Grad.
```

## Größer und kleiner mit scale

`scale(1.5)` vergrößert auf das Anderthalbfache, `scale(0.5)` verkleinert auf die Hälfte, mit allem darin, auch der Schrift. Mit zwei Werten, `scale(2, 1)`, wird nur in die Breite gezogen. Auch hier bleibt der Platz im Fluss unverändert.

```beispiel
id: scale
html: |
  <div class="reihe">
    <div>Hering</div>
    <div class="gross">Makrele</div>
    <div>Sardine</div>
  </div>
code: |
  .reihe {
    display: flex;
    gap: 30px;
    margin: 30px;
  }
  .reihe div {
    padding: 10px;
    background-color: teal;
  }
  .reihe .gross {
    transform: scale(1.5);
    background-color: crimson;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Makrele ist anderthalbmal so groß und ragt über ihren Platz hinaus, die Nachbarn bleiben an ihrem Ort
      richtig: true
      erklaerung: Richtig, vergrößert wird nur das Bild.
    - text: Makrele ist größer, und Hering und Sardine rücken zur Seite
      erklaerung: Die Nachbarn merken nichts von transform.
    - text: Nur die Schrift von Makrele ist größer
      erklaerung: scale vergrößert das ganze Element.
```

```frage
frageart: auswahl
id: halb
text: Welche Angabe macht ein Element halb so groß?
als_code: true
optionen:
  - text: "transform: scale(0.5);"
    richtig: true
    erklaerung: Richtig.
  - text: "transform: scale(-2);"
    erklaerung: Negative Werte spiegeln. Das wäre gespiegelt und doppelt so groß.
  - text: "transform: scale(50);"
    erklaerung: Das wäre fünfzigmal so groß.
```

## Mehrere auf einmal und der Drehpunkt

Mehrere Verwandlungen stehen mit Leerzeichen hintereinander: `transform: translate(20px, 0) rotate(10deg) scale(1.2)`. Gedreht und vergrößert wird um den **Mittelpunkt**. `transform-origin` verlegt diesen Punkt, etwa `transform-origin: top left` für die obere linke Ecke: Dann schwingt ein Schild wie an einem Nagel.

```beispiel
id: origin
html: |
  <div class="schild mitte">Mitte</div>
  <div class="schild ecke">Ecke</div>
code: |
  .schild {
    width: 140px;
    margin: 30px 60px;
    padding: 12px;
    background-color: #ffd166;
    color: #2b3442;
    transform: rotate(20deg);
  }
  .ecke {
    transform-origin: top left;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Beide sind gleich stark gedreht, das obere um seine Mitte, das untere hängt an seiner oberen linken Ecke und schwingt nach rechts unten
      richtig: true
      erklaerung: Richtig. Der Drehpunkt bestimmt, wohin sich ein gedrehtes Element bewegt.
    - text: Das untere ist gar nicht gedreht
      erklaerung: Es ist genauso um 20 Grad gedreht, nur um einen anderen Punkt.
    - text: Das untere ist doppelt so stark gedreht
      erklaerung: Der Winkel ist gleich, nur der Drehpunkt ist ein anderer.
```

```frage
frageart: luecke
id: luecke-origin
text: Das Schild soll sich um seine untere Mitte drehen. Ergänze die Eigenschaft.
code: |
  .schild {
    transform: rotate(5deg);
    ___: bottom center;
  }
antworten: [["transform-origin"]]
erklaerung: Richtig.
hinweis: Der Ursprung der Verwandlung, auf Englisch origin.
```

## Sanft wechseln mit transition

Ändert sich ein Wert, etwa bei `:hover`, springt er sofort. Mit `transition` gleitet er: `transition: transform 0.3s` lässt jede Änderung von transform in 0,3 Sekunden ablaufen. Die Bühne zeigt nur Standbilder, aber in der Werkbank kannst du zeigen und zusehen.

```beispiel
id: transition
html: |
  <div class="knopf">Zeig auf mich</div>
code: |
  .knopf {
    width: 160px;
    margin: 40px;
    padding: 12px;
    text-align: center;
    background-color: teal;
    transition: transform 0.3s;
  }
  .knopf:hover {
    transform: scale(1.2) rotate(-3deg);
  }
vorhersage:
  art: auswahl
  frage: Wie sieht der Knopf aus, solange niemand auf ihn zeigt?
  optionen:
    - text: Gerade und in normaler Größe
      richtig: true
      erklaerung: Richtig. Erst unter dem Zeiger wächst und kippt er, sanft in 0,3 Sekunden. Probier es in der Werkbank aus.
    - text: Vergrößert und schief
      erklaerung: Das gilt nur unter dem Zeiger.
    - text: Er wackelt ständig hin und her
      erklaerung: transition läuft nur, wenn sich ein Wert ändert.
```

```merke
text: "`transform` mit `translate(x, y)`, `rotate(20deg)`, `scale(f)`, auch hintereinander; der Platz im Fluss bleibt. `transform-origin` wählt den Drehpunkt. `transition: eigenschaft dauer` lässt Wechsel gleiten."
```

```falle
titel: Zweites transform überschreibt das erste
text: "Steht `transform: rotate(10deg)` in einer Regel und `transform: scale(2)` in einer genaueren, gilt nur scale. transform ist eine einzige Eigenschaft. Wer beides will, schreibt beides in eine Angabe."
```

```augenzwinkern
text: Pit hat dem Schild Geöffnet ein rotate(180deg) gegeben, um zu sehen, ob es jemand merkt. Drei Kunden haben den Kopf gedreht und trotzdem bestellt.
```
