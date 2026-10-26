---
id: css-kaskade
sprache: css
titel: Kaskade und Vererbung
kurz: Welche Regel gewinnt, wenn sich zwei streiten, und was Elemente von ihren Eltern erben.
fuehrt_ein: [kaskade, spezifitaet, vererbung]
lernziele:
  - sagen, welche von zwei gleich genauen Regeln gewinnt
  - die Genauigkeit eines Selektors abschätzen (id vor Klasse vor Element)
  - nutzen, dass Kinder die Schriftfarbe ihrer Eltern erben
  - mit inherit eine Eigenschaft ausdrücklich erben lassen
  - erklären, warum eine eigene Regel jede geerbte Farbe schlägt
karte: Ich weiß, wer am Ende gewinnt
bilder:
  - schluessel: karte_css_kaskade
    art: sammelkarte
    sprache: css
    motiv: Ein großer Pinguin legt einem Küken einen gestreiften Schal um, daneben streiten zwei Pinguine um einen Farbeimer
---

## Wenn sich Regeln streiten

```alltag
text: Pit schreibt morgens auf die Tafel "Heute Hering". Mittags schreibt Pia darunter "Heute Makrele". Was gilt? Das, was zuletzt dasteht. So hält es auch CSS, solange die Regeln gleich genau sind.
zeichnung: schal
```

Oft treffen mehrere Regeln dasselbe Element und wollen dieselbe Eigenschaft setzen. Dann entscheidet die **Kaskade**, wer gewinnt. Die einfachste Stufe: Sind beide Selektoren gleich genau, gewinnt die Regel, die **später** im CSS steht. Angaben, um die sich niemand streitet, gelten weiter.

```beispiel
id: reihenfolge
html: |
  <p>Hering mit Eis</p>
code: |
  p {
    color: gold;
    background-color: navy;
  }
  p {
    color: tomato;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Tomatenrote Schrift auf dunkelblauem Grund
      richtig: true
      erklaerung: Richtig. Bei color gewinnt die spätere Regel, den Hintergrund setzt nur die erste, er bleibt also.
    - text: Goldene Schrift auf dunkelblauem Grund
      erklaerung: Beide Regeln sind gleich genau, da gewinnt die spätere. Und die sagt tomato.
    - text: Tomatenrote Schrift ohne Hintergrund
      erklaerung: Die zweite Regel überschreibt nur color. Um den Hintergrund streitet sich niemand, er bleibt.
```

```frage
frageart: auswahl
id: wer-gewinnt
text: Welche Farbe hat der Absatz?
code: |
  p { color: skyblue; }
  p { color: lightgreen; }
  p { color: gold; }
optionen:
  - text: gold
    richtig: true
    erklaerung: Richtig, die letzte von drei gleich genauen Regeln.
  - text: skyblue
    erklaerung: Die erste Regel wird zweimal überschrieben.
  - text: Eine Mischung aus allen dreien
    erklaerung: Farben mischen sich hier nicht, eine Regel gewinnt ganz.
```

## Genauer gewinnt

Sind die Selektoren **unterschiedlich genau**, zählt die Reihenfolge nicht mehr: Der genauere Selektor gewinnt, egal wo er steht. Diese Genauigkeit heißt **Spezifität**. Grob gilt:

- eine **id** wiegt am meisten
- dann zählen **Klassen**
- dann **Elemente**

Gezählt wird von oben: Wer mehr ids hat, gewinnt. Bei gleich vielen ids entscheiden die Klassen, dann die Elemente. `.karte p` (eine Klasse, ein Element) schlägt also `p` (ein Element), und `#tagesangebot` schlägt jede Regel nur mit Klassen.

```beispiel
id: genauer
html: |
  <ul class="karte">
    <li id="tagesangebot">Makrele am Stiel</li>
    <li class="neu">Sardinen</li>
  </ul>
code: |
  #tagesangebot {
    color: gold;
  }
  .karte li {
    color: skyblue;
  }
  li {
    color: tomato;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Makrele am Stiel wird gold, Sardinen himmelblau
      richtig: true
      erklaerung: Richtig. Die id schlägt alles, und .karte li ist genauer als li, obwohl li zuletzt steht.
    - text: Beide werden tomatenrot
      erklaerung: Die Reihenfolge zählt nur bei gleich genauen Selektoren. li ist der ungenaueste von allen.
    - text: Makrele am Stiel wird himmelblau, Sardinen tomatenrot
      erklaerung: Für die Makrele gibt es eine Regel mit id, und die wiegt am meisten.
```

```frage
frageart: auswahl
id: genauester
text: Welcher Selektor ist am genauesten?
als_code: true
optionen:
  - text: "#karte li"
    richtig: true
    erklaerung: Richtig, er hat eine id. Die wiegt mehr als jede Menge Klassen.
  - text: ".karte .liste li"
    erklaerung: Zwei Klassen und ein Element, aber keine id.
  - text: "ul li span"
    erklaerung: Drei Elemente, aber keine Klasse und keine id. Das ist der ungenaueste.
```

```merke
text: "Bei gleicher Genauigkeit gewinnt die spätere Regel. Sonst gewinnt die genauere: erst zählen ids, dann Klassen, dann Elemente."
```

## Vererbung

Manche Eigenschaften geben Elemente an ihre Kinder weiter, wie Eltern ihre Augenfarbe. Das heißt **Vererbung**. Die Schriftfarbe `color` gehört dazu: Färbst du ein `div`, wird alles darin mitgefärbt, solange keine eigene Regel etwas anderes sagt. Darum hatte bisher alles helle Schrift: Der Grundstil der Bühne setzt `color` beim body, und alle erben.

```beispiel
id: vererbung
html: |
  <div class="karte">
    <h2>Speisekarte</h2>
    <p>Heute mit <strong>doppelt</strong> Eis</p>
  </div>
  <p>Draußen</p>
code: |
  .karte {
    color: lightgreen;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Überschrift, Absatz und doppelt in der Karte werden hellgrün, Draußen bleibt hell
      richtig: true
      erklaerung: Richtig. Die Karte vererbt ihre Schriftfarbe an alles, was in ihr steckt.
    - text: Nichts ändert sich, denn die Karte selbst enthält keinen Text
      erklaerung: Die Farbe der Karte wandert zu ihren Kindern und Enkeln. Der Text darin wird also hellgrün.
    - text: Nur die Überschrift wird hellgrün, sie ist das erste Kind
      erklaerung: Vererbt wird an alle Kinder, auch an Enkel wie strong.
```

```frage
frageart: auswahl
id: wer-erbt
text: "Welche Farbe hat das Wort Eis bei `.kiste { color: gold; }`?"
code: |
  <div class="kiste">
    <p>Hering mit <em>Eis</em></p>
  </div>
optionen:
  - text: gold, geerbt über p von der Kiste
    richtig: true
    erklaerung: Richtig. Die Farbe wird von Generation zu Generation weitergereicht.
  - text: hell wie vorher, denn em ist ein Enkel und erbt nicht
    erklaerung: Vererbt wird an alle Nachfahren, nicht nur an Kinder.
  - text: gold, aber nur, weil em schräg ist
    erklaerung: Mit der Schrägschrift hat das nichts zu tun.
```

## Nicht alles wird vererbt

Längst nicht jede Eigenschaft wird vererbt. `background-color` zum Beispiel nicht: Ein Kind hat zunächst gar keinen Hintergrund, es ist durchsichtig. Darum **sieht** man den Hintergrund der Eltern durch das Kind hindurch, geerbt ist er aber nicht.

Will man eine Eigenschaft ausdrücklich von den Eltern übernehmen, schreibt man als Wert `inherit`. Das hilft auch, wenn eine andere Regel einem Element eine eigene Farbe gegeben hat und es doch die der Eltern tragen soll.

```beispiel
id: inherit
html: |
  <p class="hinweis">Achtung, <span>heißer</span> Fisch!</p>
code: |
  .hinweis {
    color: black;
    background-color: gold;
  }
  span {
    color: tomato;
  }
  .hinweis span {
    color: inherit;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Der ganze Satz ist schwarz auf gold, auch heißer
      richtig: true
      erklaerung: Richtig. .hinweis span ist genauer als span und sagt inherit, also übernimmt das Wort die Farbe des Absatzes.
    - text: Schwarz auf gold, nur heißer ist tomatenrot
      erklaerung: Die Regel span verliert gegen die genauere Regel .hinweis span, und die sagt inherit.
    - text: heißer ist schwarz auf eigenem goldenen Kasten, der Rest des Satzes ohne Hintergrund
      erklaerung: Der goldene Hintergrund gehört zum Absatz, er liegt hinter dem ganzen Satz.
```

```frage
frageart: luecke
id: luecke-inherit
text: Die Preise sollen dieselbe Schriftfarbe haben wie ihre Eltern. Ergänze den Wert.
code: |
  .preis {
    color: ___;
  }
antworten: [["inherit"]]
erklaerung: Richtig, inherit übernimmt den Wert der Eltern.
hinweis: Erben heißt auf Englisch inherit.
```

## Geerbt verliert immer

Eine geerbte Farbe hat keine Genauigkeit. Sobald irgendeine Regel das Element **selbst** trifft, gewinnt diese, und sei ihr Selektor noch so schlicht. Selbst eine id bei den Eltern hilft nicht: Die Kinder erben nur, wenn niemand ihnen etwas anderes sagt.

```beispiel
id: geerbt-verliert
html: |
  <div id="karte">
    <h2>Speisekarte</h2>
    <p>Hering</p>
  </div>
code: |
  #karte {
    color: gold;
  }
  p {
    color: skyblue;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die Überschrift wird gold, der Absatz himmelblau
      richtig: true
      erklaerung: Richtig. Der Absatz hat eine eigene Regel, die schlägt jede geerbte Farbe, auch die von einer id.
    - text: Beide werden gold, die id ist genauer
      erklaerung: Die id trifft das div, nicht den Absatz. Beim Absatz kommt die Farbe nur geerbt an, und Geerbtes verliert gegen jede eigene Regel.
    - text: Beide werden himmelblau
      erklaerung: Die Regel für p trifft nur den Absatz. Die Überschrift erbt weiter Gold.
```

```falle
titel: Die Klasse kommt nicht durch
text: "Steht `.karte li { color: white; }` im CSS, wird `.ausverkauft { color: gray; }` beim Listeneintrag nichts ändern: Eine Klasse und ein Element sind genauer als eine Klasse allein. Abhilfe: genauer werden, etwa `.karte .ausverkauft`."
```

```augenzwinkern
text: Pit hat einmal versucht, einen Streit mit Pia per Spezifität zu gewinnen. Er hat verloren. Pia hatte eine id.
```
