---
id: css-flex-ausrichten
sprache: css
titel: Flexbox ausrichten
kurz: Kinder entlang der Reihe verteilen, quer dazu ausrichten, einzelne aus der Reihe tanzen lassen und freien Platz mit flex-grow füllen.
fuehrt_ein: [justify_content, align_items, flex_grow]
lernziele:
  - mit justify-content Kinder auf der Hauptachse an den Anfang, die Mitte oder das Ende schieben
  - freien Platz mit space-between, space-around und space-evenly verteilen
  - mit align-items Kinder quer zur Hauptachse ausrichten
  - mit align-self ein einzelnes Kind anders ausrichten
  - mit flex-grow freien Platz an Kinder verteilen
karte: Ich verteile den Platz gerecht
bilder:
  - schluessel: karte_css_flex_ausrichten
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin schiebt auf einer langen Bank drei Fischkisten auseinander, sodass die Lücken gleich groß sind
---

## Entlang der Reihe: justify-content

```alltag
text: "Pit hat drei Kisten auf einer langen Bank. Er kann sie links zusammenschieben, in die Mitte stellen, nach rechts schieben oder gleichmäßig verteilen. Die Kisten bleiben gleich groß, nur der freie Platz wandert."
zeichnung: bank
```

`justify-content` beim Flex-Behälter verteilt den **freien Platz auf der Hauptachse**, bei einer Reihe also waagerecht: `flex-start` (die Voreinstellung) schiebt alles an den Anfang, `center` in die Mitte, `flex-end` ans Ende.

```beispiel
id: justify
html: |
  <div class="a"><div>1</div><div>2</div></div>
  <div class="b"><div>1</div><div>2</div></div>
code: |
  .a, .b {
    display: flex;
    gap: 6px;
    margin-bottom: 10px;
    background-color: #2b3442;
  }
  .a div, .b div {
    background-color: teal;
    padding: 8px 16px;
  }
  .a {
    justify-content: center;
  }
  .b {
    justify-content: flex-end;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben stehen beide Kästen in der Mitte, unten am rechten Rand
      richtig: true
      erklaerung: Richtig, nur der freie Platz wird anders verteilt.
    - text: Oben werden die Kästen breiter, bis sie die Reihe füllen
      erklaerung: justify-content ändert die Größe nicht, es verschiebt nur.
    - text: Unten stehen die Kästen in umgekehrter Reihenfolge
      erklaerung: Die Reihenfolge bleibt 1 2, nur rechtsbündig.
```

```frage
frageart: luecke
id: luecke-mitte
text: Die Kinder sollen waagerecht in der Mitte stehen. Ergänze den Wert.
code: |
  .reihe {
    display: flex;
    justify-content: ___;
  }
antworten: [["center"]]
erklaerung: Richtig.
hinweis: Mitte heißt center.
```

## Platz verteilen

Drei Werte verteilen den freien Platz **zwischen** die Kinder:

- `space-between`: das erste ganz links, das letzte ganz rechts, gleiche Lücken dazwischen
- `space-around`: jedes Kind bekommt links und rechts gleich viel Platz, am Rand also halb so viel wie dazwischen
- `space-evenly`: alle Lücken gleich, auch am Rand

`space-between` ist der Klassiker für Name links, Preis rechts.

```beispiel
id: verteilen
html: |
  <div class="zeile"><span>Hering im Eismantel</span><span>4,50</span></div>
  <div class="leiste"><div>A</div><div>B</div><div>C</div></div>
code: |
  .zeile, .leiste {
    display: flex;
    margin-bottom: 12px;
    background-color: #2b3442;
  }
  .zeile {
    justify-content: space-between;
  }
  .leiste {
    justify-content: space-evenly;
  }
  .leiste div {
    background-color: teal;
    padding: 6px 14px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben der Name ganz links, der Preis ganz rechts; unten drei Kästen mit gleich großen Lücken, auch zum Rand
      richtig: true
      erklaerung: Richtig. space-between drückt an die Ränder, space-evenly verteilt alle Lücken gleich.
    - text: Oben Name und Preis direkt nebeneinander
      erklaerung: space-between schiebt den freien Platz zwischen die beiden.
    - text: Unten stehen A und C direkt am Rand
      erklaerung: Das wäre space-between. space-evenly lässt auch am Rand eine gleich große Lücke.
```

```frage
frageart: auswahl
id: name-preis
text: Name links, Preis rechts in einer Zeile. Welcher Wert passt?
als_code: true
optionen:
  - text: "justify-content: space-between;"
    richtig: true
    erklaerung: Richtig, der Platz landet dazwischen.
  - text: "justify-content: center;"
    erklaerung: Beide stünden dicht beieinander in der Mitte.
  - text: "justify-content: flex-end;"
    erklaerung: Beide stünden dicht beieinander rechts.
```

## Quer zur Reihe: align-items

`align-items` richtet die Kinder **quer** zur Hauptachse aus, bei einer Reihe also senkrecht: `stretch` (die Voreinstellung) streckt sie auf die Höhe des Behälters, `flex-start` oben, `center` mittig, `flex-end` unten. Mit `justify-content: center` und `align-items: center` zusammen steht ein Kind genau in der Mitte, der bekannteste Trick der Flexbox.

```beispiel
id: align
html: |
  <div class="buehne">
    <div class="klein">klein</div>
    <div class="gross">groß</div>
  </div>
code: |
  .buehne {
    display: flex;
    gap: 8px;
    height: 160px;
    background-color: #2b3442;
    align-items: center;
  }
  .klein, .gross {
    background-color: teal;
    padding: 8px;
  }
  .gross {
    height: 100px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Beide Kästen stehen senkrecht in der Mitte, der kleine ist nur so hoch wie sein Text
      richtig: true
      erklaerung: Richtig. Mit center wird nicht mehr gestreckt, sondern mittig ausgerichtet.
    - text: Beide sind 160 Pixel hoch
      erklaerung: Das wäre stretch, die Voreinstellung. center streckt nicht.
    - text: Beide kleben oben
      erklaerung: Das wäre flex-start.
```

```frage
frageart: auswahl
id: genau-mitte
text: Wie steht ein einzelnes Kind genau in der Mitte eines Flex-Behälters?
optionen:
  - text: Mit justify-content center und align-items center beim Behälter
    richtig: true
    erklaerung: Richtig, eins für jede Achse.
  - text: Mit text-align center beim Kind
    erklaerung: Das richtet nur den Text im Kind aus.
  - text: Mit align-items center allein
    erklaerung: Das zentriert nur senkrecht.
```

## Einer tanzt aus der Reihe: align-self

`align-self` steht bei einem **Kind** und überschreibt für dieses eine die Ausrichtung quer zur Achse, mit denselben Werten wie `align-items`.

```beispiel
id: self
html: |
  <div class="reihe">
    <div>Pit</div>
    <div class="huepft">Pia</div>
    <div>Paul</div>
  </div>
code: |
  .reihe {
    display: flex;
    gap: 8px;
    height: 120px;
    align-items: flex-end;
    background-color: #2b3442;
  }
  .reihe div {
    background-color: teal;
    padding: 10px;
  }
  .huepft {
    align-self: flex-start;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Pit und Paul stehen unten, Pia oben
      richtig: true
      erklaerung: Richtig, Pia hüpft mit align-self aus der Reihe.
    - text: Alle drei stehen oben
      erklaerung: align-self gilt nur für Pia, die anderen folgen align-items.
    - text: Pia steht ganz links oben, die anderen rücken nach
      erklaerung: align-self ändert nur die Höhe, die Reihenfolge bleibt.
```

```frage
frageart: auswahl
id: self-wo
text: Wo steht align-self?
optionen:
  - text: Bei dem einen Kind, das anders stehen soll
    richtig: true
    erklaerung: Richtig. align-items gilt für alle, align-self für eines.
  - text: Beim Flex-Behälter
    erklaerung: Dort steht align-items für alle Kinder zugleich.
  - text: Beim body
    erklaerung: align-self wirkt nur bei einem Flex-Element selbst.
```

## Wachsen mit flex-grow

`flex-grow` bei einem Kind sagt, wie viel vom **freien Platz** es bekommt. Mit `flex-grow: 1` bei einem Kind nimmt dieses allen restlichen Platz. Haben zwei Kinder 1 und 2, teilen sie den freien Platz eins zu zwei. Die Kurzform `flex: 1` macht dasselbe und ist sehr verbreitet.

```beispiel
id: grow
html: |
  <div class="leiste">
    <div class="logo">Fisch</div>
    <div class="suche">Suchen ...</div>
    <div class="knopf">Los</div>
  </div>
code: |
  .leiste {
    display: flex;
    gap: 8px;
  }
  .leiste div {
    background-color: teal;
    padding: 8px;
  }
  .leiste .suche {
    flex-grow: 1;
    background-color: #e3f1f8;
    color: #555;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Fisch und Los bleiben schmal, das Suchfeld füllt den ganzen Platz dazwischen
      richtig: true
      erklaerung: Richtig. Nur das Suchfeld darf wachsen, es bekommt den gesamten freien Platz.
    - text: Alle drei werden gleich breit
      erklaerung: Dafür bräuchten alle drei flex-grow.
    - text: Das Suchfeld schiebt Los aus dem Behälter hinaus
      erklaerung: Es bekommt nur den freien Platz, Los bleibt drin.
```

```frage
frageart: luecke
id: luecke-grow
text: Das mittlere Kind soll allen freien Platz bekommen. Ergänze den Wert.
code: |
  .mitte {
    flex-grow: ___;
  }
antworten: [["1"]]
erklaerung: Richtig. Solange kein anderes Kind wächst, bekommt es den ganzen freien Platz.
hinweis: Eine kleine ganze Zahl reicht.
```

```merke
text: "Beim Behälter: `justify-content` entlang der Achse (`flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly`), `align-items` quer dazu (`stretch`, `flex-start`, `center`, `flex-end`). Beim Kind: `align-self`, `flex-grow`."
```

```falle
titel: Achsen vertauscht
text: "Bei `flex-direction: column` dreht sich alles: justify-content wirkt dann senkrecht, align-items waagerecht. Wer in einer Spalte waagerecht zentrieren will, braucht `align-items: center`."
```

```augenzwinkern
text: Pit hat seinem Lieblingsfisch flex-grow 999 gegeben. Der Hering nimmt jetzt die ganze Speisekarte ein, und Pia sucht seitdem die Makrele.
```
