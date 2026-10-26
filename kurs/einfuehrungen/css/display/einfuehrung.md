---
id: css-display
sprache: css
titel: display
kurz: Blöcke, die eine ganze Zeile nehmen, Inline-Elemente mitten im Text, das Beste aus beiden mit inline-block, und Elemente, die ganz verschwinden.
fuehrt_ein: [display_block, display_inline, display_inline_block, display_none]
lernziele:
  - Block- und Inline-Elemente an ihrem Verhalten erkennen
  - mit display block ein Element eine eigene Zeile nehmen lassen
  - mit display inline Elemente in eine Zeile holen
  - mit inline-block Kästen mit fester Breite nebeneinanderstellen
  - mit display none ein Element ganz ausblenden
karte: Ich bestimme, wer eine eigene Zeile bekommt
bilder:
  - schluessel: karte_css_display
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin räumt ein Regal ein, große Kisten stehen je in einer eigenen Reihe, kleine Dosen nebeneinander
---

## Block und inline

```alltag
text: "Im Regal des Fischwagens gibt es zwei Sorten Dinge: Große Kisten bekommen jede ein ganzes Brett für sich. Kleine Dosen stellt Pit nebeneinander, so viele, wie aufs Brett passen. Für CSS sind das Block- und Inline-Elemente."
zeichnung: regal
```

Jedes Element hat eine Art, sich anzuordnen, die Eigenschaft `display`:

- **Block-Elemente** wie `div`, `p`, `h1`, `ul` und `li` beginnen eine neue Zeile, nehmen die ganze Breite ein und gehorchen `width`, `height` und allen Abständen
- **Inline-Elemente** wie `span`, `strong` und `em` stehen mitten im Text, sind nur so breit wie ihr Inhalt und ignorieren `width` und `height`; Abstände nach oben und unten verschieben nichts

```beispiel
id: block-inline
html: |
  <span class="a">Hering</span>
  <span class="a">Makrele</span>
  <div class="b">Sardine</div>
  <div class="b">Thunfisch</div>
code: |
  .a, .b {
    background-color: teal;
    width: 120px;
    margin: 4px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Hering und Makrele nebeneinander, nur so breit wie ihre Wörter, darunter Sardine und Thunfisch untereinander, je 120 Pixel breit
      richtig: true
      erklaerung: Richtig. span ist inline und ignoriert width, div ist ein Block und nimmt eine eigene Zeile.
    - text: Alle vier stehen untereinander, je 120 Pixel breit
      erklaerung: Die beiden span sind Inline-Elemente. Sie stehen nebeneinander und kümmern sich nicht um width.
    - text: Alle vier stehen nebeneinander
      erklaerung: div beginnt immer eine neue Zeile, solange display nichts anderes sagt.
```

```frage
frageart: auswahl
id: welche-inline
text: Welches Element ist von Haus aus inline?
als_code: true
optionen:
  - text: span
    richtig: true
    erklaerung: Richtig, span steht mitten im Text.
  - text: p
    erklaerung: Ein Absatz ist ein Block und beginnt eine neue Zeile.
  - text: li
    erklaerung: Listeneinträge stehen untereinander, sie sind Blöcke.
```

## Die Art wechseln

`display` lässt sich ändern. `display: inline` holt Blöcke in eine Zeile, zum Beispiel Listeneinträge für eine Leiste. `display: block` macht ein Inline-Element zum Block: Es bekommt eine eigene Zeile und gehorcht `width` und `height`.

```beispiel
id: wechseln
html: |
  <ul class="leiste">
    <li>Fisch</li>
    <li>Getränke</li>
    <li>Eis</li>
  </ul>
  <span class="schild">Geöffnet</span>
code: |
  .leiste li {
    display: inline;
    margin-right: 20px;
  }
  .schild {
    display: block;
    width: 150px;
    background-color: teal;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Fisch, Getränke und Eis stehen nebeneinander ohne Punkte, darunter ein 150 Pixel breiter Kasten Geöffnet
      richtig: true
      erklaerung: Richtig. Als inline verlieren die Einträge ihre Punkte und rücken in eine Zeile, der span wird zum Block.
    - text: Die Liste bleibt untereinander, nur der span ändert sich
      erklaerung: display inline holt die Einträge in eine Zeile.
    - text: Der span bleibt nur so breit wie sein Wort
      erklaerung: Als Block gehorcht er width.
```

```frage
frageart: luecke
id: luecke-block
text: Der span soll eine eigene Zeile bekommen und 200 Pixel breit werden. Ergänze den Wert.
code: |
  span {
    display: ___;
    width: 200px;
  }
antworten: [["block"]]
erklaerung: Richtig, als Block gehorcht er width.
hinweis: Das Gegenteil von inline.
```

## Das Beste aus beiden: inline-block

`display: inline-block` stellt Elemente **nebeneinander** wie inline, lässt sie aber Breite, Höhe und alle Abstände annehmen wie einen Block. So entstehen Kacheln, Knöpfe und Marken, die in einer Reihe stehen. Passt keine mehr in die Zeile, rutscht die nächste in die nächste Zeile.

```beispiel
id: inline-block
html: |
  <div class="kachel">Hering</div>
  <div class="kachel">Makrele</div>
  <div class="kachel">Sardine</div>
  <div class="kachel">Thunfisch</div>
code: |
  .kachel {
    display: inline-block;
    width: 200px;
    height: 60px;
    margin: 4px;
    background-color: teal;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Zwei Reihen mit je zwei Kacheln von 200 mal 60 Pixeln
      richtig: true
      erklaerung: Richtig. Drei Kacheln mit Abständen passen nicht auf die 576 Pixel breite Fläche, also rutscht die dritte in die nächste Reihe.
    - text: Vier Kacheln untereinander
      erklaerung: inline-block stellt sie nebeneinander, solange Platz ist.
    - text: Alle vier in einer Reihe, schmaler gedrückt
      erklaerung: Die Breite bleibt 200 Pixel. Was nicht passt, rutscht in die nächste Reihe.
```

```frage
frageart: auswahl
id: warum-inline-block
text: Warum nimmt man für Knöpfe in einer Reihe inline-block statt inline?
optionen:
  - text: Weil inline-block auch Breite, Höhe und Polster nach oben und unten richtig annimmt
    richtig: true
    erklaerung: Richtig. Nebeneinander wie inline, gestaltbar wie ein Block.
  - text: Weil inline-Elemente nicht nebeneinander stehen
    erklaerung: Doch, das tun sie. Sie ignorieren nur width und height.
  - text: Weil inline-block schneller lädt
    erklaerung: Mit der Ladezeit hat das nichts zu tun.
```

## Ganz weg: display none

`display: none` blendet ein Element **ganz** aus: Es ist nicht zu sehen und nimmt auch keinen Platz mehr ein, als gäbe es es nicht. Alle Kinder verschwinden mit. Anders `opacity: 0`: Das Element wird unsichtbar, sein Platz bleibt aber frei.

```beispiel
id: none
html: |
  <p>Hering</p>
  <p class="weg">Eisscholle</p>
  <p class="durchsichtig">Makrele</p>
  <p>Sardinen</p>
code: |
  p {
    background-color: teal;
  }
  .weg {
    display: none;
  }
  .durchsichtig {
    opacity: 0;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Hering, dann eine Lücke in der Größe eines Streifens, dann Sardinen
      richtig: true
      erklaerung: Richtig. Die Eisscholle ist ganz weg, die Makrele unsichtbar, aber ihr Platz bleibt.
    - text: Hering und Sardinen direkt untereinander
      erklaerung: Die Makrele mit opacity 0 hält ihren Platz frei.
    - text: Zwei Lücken, wo die beiden verschwundenen Streifen waren
      erklaerung: Mit display none ist die Eisscholle samt Platz verschwunden.
```

```frage
frageart: auswahl
id: platz-bleibt
text: Ein Element soll unsichtbar sein, aber seinen Platz behalten. Was passt?
als_code: true
optionen:
  - text: "opacity: 0;"
    richtig: true
    erklaerung: Richtig. Unsichtbar, aber der Platz bleibt frei.
  - text: "display: none;"
    erklaerung: Damit verschwindet auch der Platz.
  - text: "display: inline;"
    erklaerung: Das ändert nur die Anordnung, sichtbar bleibt es.
```

```merke
text: "`display: block` eigene Zeile, volle Breite. `inline` mitten im Text, ohne width und height. `inline-block` nebeneinander, aber gestaltbar. `none` ganz weg, auch ohne Platz."
```

```falle
titel: width bei inline
text: "`span { width: 200px; }` bewirkt nichts, Inline-Elemente ignorieren Breite und Höhe. Erst mit `display: inline-block` oder `block` gehorcht der span."
```

```augenzwinkern
text: Pit wollte die Rechnung mit display none verschwinden lassen. Pia hat im HTML nachgesehen. Da stand sie noch.
```
