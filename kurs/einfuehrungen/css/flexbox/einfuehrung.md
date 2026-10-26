---
id: css-flexbox
sprache: css
titel: Flexbox
kurz: Mit display flex Kinder in eine Reihe oder Spalte stellen, Lücken mit gap, Richtung umkehren und umbrechen lassen.
fuehrt_ein: [flex, flex_richtung, gap, flex_wrap]
lernziele:
  - mit display flex die Kinder eines Elements nebeneinanderstellen
  - mit flex-direction Reihe und Spalte wählen und umkehren
  - mit gap gleichmäßige Lücken zwischen die Kinder legen
  - mit flex-wrap Kinder in die nächste Reihe umbrechen lassen
karte: Ich stelle Kästen in Reih und Glied
bilder:
  - schluessel: karte_css_flexbox
    art: sammelkarte
    sprache: css
    motiv: Pinguine stehen in einer ordentlichen Reihe auf einem gespannten Gummiband, das sich dehnt
---

## Ein flexibler Behälter

```alltag
text: "Für das Gruppenfoto stellt Pia alle Pinguine nebeneinander auf. Sie sagt nur einmal laut \"In eine Reihe!\", statt jedem einzeln zu sagen, wo er stehen soll. Genau das macht display flex: Die Regel steht beim Eltern-Element, und alle Kinder ordnen sich."
zeichnung: reihe
```

Bisher hat jedes Element selbst bestimmt, wie es sich anordnet. **Flexbox** dreht das um: `display: flex` steht beim **Behälter**, und seine direkten Kinder, die **Flex-Elemente**, stellen sich in eine Reihe, egal ob sie Blöcke oder inline sind. Sie sind dann so breit wie ihr Inhalt (oder ihr width) und so hoch wie die höchste in der Reihe.

```beispiel
id: flex
html: |
  <div class="reihe">
    <div class="p">Pit</div>
    <div class="p">Pia</div>
    <div class="p">Paul mit langem Namen</div>
  </div>
code: |
  .reihe {
    display: flex;
    background-color: #2b3442;
  }
  .p {
    background-color: teal;
    margin: 4px;
    padding: 8px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die drei Kästen stehen nebeneinander, jeder so breit wie sein Name, alle gleich hoch
      richtig: true
      erklaerung: Richtig. Im Flex-Behälter stehen auch div nebeneinander und nehmen nur so viel Breite, wie sie brauchen.
    - text: Die drei Kästen stehen untereinander über die ganze Breite
      erklaerung: Das wäre ohne display flex. Mit flex ordnet der Behälter seine Kinder in eine Reihe.
    - text: Nur der Behälter ändert sich, die Kinder bleiben Blöcke untereinander
      erklaerung: display flex wirkt gerade auf die Kinder, sie werden zu Flex-Elementen.
```

```frage
frageart: auswahl
id: wo-flex
text: Bei welchem Element steht display flex, damit die Listeneinträge nebeneinander stehen?
optionen:
  - text: Bei der ul, dem Behälter der Einträge
    richtig: true
    erklaerung: Richtig. flex gehört zum Eltern-Element, die Kinder ordnen sich.
  - text: Bei jedem li
    erklaerung: Dann würde jedes li seine eigenen Kinder ordnen, nicht sich selbst.
  - text: Beim body
    erklaerung: Dann stünden die direkten Kinder des body nebeneinander, nicht die Einträge.
```

## Reihe oder Spalte

`flex-direction` bestimmt die **Hauptachse**: `row` (die Voreinstellung) stellt die Kinder von links nach rechts, `column` von oben nach unten. Mit `row-reverse` und `column-reverse` geht es andersherum, ohne das HTML zu ändern.

```beispiel
id: richtung
html: |
  <div class="a">
    <div>1</div><div>2</div><div>3</div>
  </div>
  <div class="b">
    <div>1</div><div>2</div><div>3</div>
  </div>
code: |
  .a, .b {
    display: flex;
    margin-bottom: 12px;
  }
  .a div, .b div {
    background-color: teal;
    padding: 8px 16px;
    margin: 2px;
  }
  .a {
    flex-direction: row-reverse;
  }
  .b {
    flex-direction: column;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben 3 2 1 nebeneinander am rechten Rand, darunter 1 2 3 untereinander über die ganze Breite
      richtig: true
      erklaerung: Richtig. row-reverse beginnt rechts. In einer Spalte werden die Kinder so breit wie der Behälter.
    - text: Oben 3 2 1 am linken Rand, darunter 1 2 3 nebeneinander
      erklaerung: row-reverse beginnt am rechten Rand. Und column stellt sie untereinander.
    - text: Beide Behälter zeigen 1 2 3 nebeneinander
      erklaerung: flex-direction ändert Richtung und Reihenfolge.
```

```frage
frageart: luecke
id: luecke-spalte
text: Die Kinder sollen untereinander stehen. Ergänze den Wert.
code: |
  .liste {
    display: flex;
    flex-direction: ___;
  }
antworten: [["column"]]
erklaerung: Richtig, column heißt Spalte.
hinweis: Eine Säule, auf Englisch column.
```

## Lücken mit gap

Abstände zwischen Flex-Elementen gehen mit margin, einfacher aber mit `gap` am Behälter: Es legt die Lücke nur **zwischen** die Kinder, nicht an den Rand. `gap: 12px` heißt 12 Pixel zwischen je zwei Kindern.

```beispiel
id: gap
html: |
  <div class="reihe">
    <div>Hering</div><div>Makrele</div><div>Sardine</div>
  </div>
code: |
  .reihe {
    display: flex;
    gap: 20px;
    background-color: #2b3442;
  }
  .reihe div {
    background-color: teal;
    padding: 8px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Drei Kästen mit je 20 Pixeln Lücke dazwischen, außen bündig mit dem Behälter
      richtig: true
      erklaerung: Richtig. gap legt Lücken nur zwischen die Kinder.
    - text: Drei Kästen mit 20 Pixeln Abstand auch zum Rand des Behälters
      erklaerung: Am Rand gibt gap keinen Abstand, dafür wäre padding da.
    - text: Kein Unterschied, gap wirkt nur in Tabellen
      erklaerung: gap wirkt bei Flexbox und Grid.
```

```frage
frageart: auswahl
id: gap-wo
text: Wo steht gap?
optionen:
  - text: Beim Flex-Behälter
    richtig: true
    erklaerung: Richtig, wie display flex.
  - text: Bei jedem Kind
    erklaerung: Die Kinder kennen ihre Nachbarn nicht. Die Lücken verteilt der Behälter.
  - text: Beim body
    erklaerung: Nur beim Behälter, dessen Kinder Lücken bekommen sollen.
```

## Umbrechen mit flex-wrap

Von Haus aus quetscht Flexbox alle Kinder in **eine** Reihe, notfalls schmaler, als ihre Breite sagt. Mit `flex-wrap: wrap` dürfen sie in die nächste Reihe **umbrechen**, wenn der Platz nicht reicht. gap gilt dann auch zwischen den Reihen.

```beispiel
id: wrap
html: |
  <div class="a">
    <div>1</div><div>2</div><div>3</div><div>4</div>
  </div>
  <div class="b">
    <div>1</div><div>2</div><div>3</div><div>4</div>
  </div>
code: |
  .a, .b {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
  }
  .a div, .b div {
    width: 200px;
    height: 40px;
    background-color: teal;
  }
  .b {
    flex-wrap: wrap;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben vier gestauchte Kästen in einer Reihe, unten zwei Reihen mit je zwei Kästen von 200 Pixeln
      richtig: true
      erklaerung: Richtig. Ohne wrap wird gestaucht, mit wrap bricht es um.
    - text: Beide Behälter brechen in zwei Reihen um
      erklaerung: Umbrechen nur mit flex-wrap wrap. Oben wird gestaucht.
    - text: Oben ragen die Kästen über den Rand hinaus
      erklaerung: Flex-Elemente dürfen schrumpfen, darum werden sie gestaucht, statt hinauszuragen.
```

```frage
frageart: luecke
id: luecke-wrap
text: Die Kacheln sollen in die nächste Reihe umbrechen dürfen. Ergänze den Wert.
code: |
  .kacheln {
    display: flex;
    flex-wrap: ___;
  }
antworten: [["wrap"]]
erklaerung: Richtig, wrap heißt umbrechen.
hinweis: Umwickeln, auf Englisch wrap.
```

```merke
text: "`display: flex` beim Behälter stellt seine Kinder in eine Reihe. `flex-direction` (`row`, `column`, `-reverse`), `gap` für Lücken dazwischen, `flex-wrap: wrap` zum Umbrechen."
```

```falle
titel: flex beim falschen Element
text: "`li { display: flex; }` stellt nicht die Einträge nebeneinander, sondern ordnet den Inhalt jedes Eintrags. Für eine Reihe von Einträgen gehört flex zur `ul`."
```

```augenzwinkern
text: Pit hat einmal flex-direction column-reverse für die Schlange vor dem Wagen ausprobiert. Seitdem bekommt der Letzte zuerst, und alle stellen sich hinten an.
```
