---
id: css-media
sprache: css
titel: Media Queries
kurz: Regeln, die nur bei bestimmten Fensterbreiten gelten, vom Telefon bis zum großen Bildschirm, und wie man Seiten zuerst für schmale Fenster baut.
fuehrt_ein: [media_query]
lernziele:
  - mit @media und min-width Regeln ab einer Fensterbreite gelten lassen
  - mit max-width Regeln bis zu einer Fensterbreite gelten lassen
  - eine Seite zuerst für schmale Fenster bauen und für breite erweitern
  - Bedingungen mit and verbinden und die Ausrichtung des Fensters abfragen
  - erklären, warum die Reihenfolge auch bei Media Queries zählt
karte: Meine Seiten passen auf jeden Bildschirm
bilder:
  - schluessel: karte_css_media
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin hält dieselbe Speisekarte einmal auf einem kleinen Telefon und einmal auf einer großen Tafel, beide ordentlich angeordnet
---

## Regeln mit Bedingung

```alltag
text: "Pit hat zwei Speisekarten: eine große Tafel neben dem Wagen und einen kleinen Zettel für die Hand. Gleicher Inhalt, andere Anordnung. Webseiten müssen das auch können, denn sie landen auf Telefonen und auf großen Bildschirmen."
zeichnung: zwei-karten
```

Eine **Media Query** ist eine Bedingung um eine Gruppe von Regeln: `@media (min-width: 500px) { ... }` heißt, die Regeln darin gelten nur, wenn das Fenster **mindestens** 500 Pixel breit ist. Unsere Bühne ist ein Fenster von 600 mal 400 Pixeln. Eine Bedingung mit `min-width: 500px` ist hier also erfüllt, eine mit `min-width: 800px` nicht.

```beispiel
id: media
html: |
  <h1>Fischwagen</h1>
  <p>Heute frisch</p>
code: |
  h1 {
    color: white;
  }
  @media (min-width: 500px) {
    h1 {
      color: gold;
    }
  }
  @media (min-width: 800px) {
    p {
      color: tomato;
    }
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die Überschrift ist gold, der Absatz bleibt hell
      richtig: true
      erklaerung: Richtig. Die Bühne ist 600 Pixel breit, also gilt die erste Bedingung und die zweite nicht.
    - text: Die Überschrift ist weiß, der Absatz tomatenrot
      erklaerung: Mindestens 500 Pixel sind erfüllt, mindestens 800 nicht. Es ist genau andersherum.
    - text: Beides gilt, die Überschrift ist gold und der Absatz rot
      erklaerung: 600 Pixel sind weniger als 800, die zweite Bedingung ist nicht erfüllt.
```

```frage
frageart: auswahl
id: gilt-sie
text: "Gilt `@media (min-width: 700px)` auf unserer 600 Pixel breiten Bühne?"
optionen:
  - text: Nein, das Fenster ist schmaler als 700 Pixel
    richtig: true
    erklaerung: Richtig.
  - text: Ja, 600 ist nah genug dran
    erklaerung: Die Bedingung ist streng. Mindestens 700 heißt mindestens 700.
  - text: Nur, wenn man scrollt
    erklaerung: Scrollen ändert die Fensterbreite nicht.
```

## Höchstens: max-width

`max-width` dreht die Bedingung um: `@media (max-width: 500px)` gilt nur, wenn das Fenster **höchstens** 500 Pixel breit ist, also auf Telefonen. Auf unserer Bühne ist sie nicht erfüllt.

```beispiel
id: max
html: |
  <p class="hinweis">Tipp: Dreh dein Telefon quer.</p>
  <p>Speisekarte</p>
code: |
  .hinweis {
    display: none;
  }
  @media (max-width: 500px) {
    .hinweis {
      display: block;
      color: gold;
    }
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Nur Speisekarte ist zu sehen, der Tipp bleibt verborgen
      richtig: true
      erklaerung: Richtig. Höchstens 500 Pixel trifft auf die 600 Pixel breite Bühne nicht zu.
    - text: Der Tipp erscheint in Gold über der Speisekarte
      erklaerung: Das passiert erst in einem Fenster bis 500 Pixel Breite.
    - text: Beide Absätze sind gold
      erklaerung: Die Regel im @media gilt hier gar nicht.
```

```frage
frageart: luecke
id: luecke-max
text: Die Regeln sollen nur in Fenstern bis 400 Pixel Breite gelten. Ergänze die Bedingung.
code: |
  @media (___: 400px) {
    h1 { font-size: 24px; }
  }
antworten: [["max-width"]]
erklaerung: Richtig, höchstens 400 Pixel.
hinweis: Höchstens heißt maximal.
```

## Zuerst für schmale Fenster

Bewährt hat sich **Mobile First**: Erst baut man die Seite für schmale Fenster, einfach und untereinander. Dann erweitert man sie mit `min-width` für breitere Fenster, etwa mit mehr Spalten. So bekommt jedes Gerät das Grundgerüst, und große Bildschirme bekommen etwas dazu.

```beispiel
id: mobile-first
html: |
  <div class="karten">
    <div>Hering</div><div>Makrele</div><div>Sardine</div>
  </div>
code: |
  .karten {
    display: grid;
    gap: 6px;
  }
  .karten div {
    padding: 12px;
    background-color: teal;
  }
  @media (min-width: 500px) {
    .karten {
      grid-template-columns: repeat(3, 1fr);
    }
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Drei Kästen nebeneinander in drei Spalten
      richtig: true
      erklaerung: Richtig. Auf der 600 Pixel breiten Bühne gilt die Erweiterung, auf einem Telefon stünden sie untereinander.
    - text: Drei Kästen untereinander
      erklaerung: So sähe es in einem Fenster unter 500 Pixeln aus. Die Bühne ist breiter.
    - text: Ein Kasten pro Zeile, aber nur halb so breit
      erklaerung: Bei 600 Pixeln gelten die drei Spalten.
```

```frage
frageart: auswahl
id: warum-mobile-first
text: Was heißt Mobile First?
optionen:
  - text: Erst die Regeln für schmale Fenster schreiben, dann mit min-width für breite erweitern
    richtig: true
    erklaerung: Richtig.
  - text: Die Seite gibt es nur für Telefone
    erklaerung: Es gibt sie für alle, nur der Aufbau beginnt beim schmalen Fenster.
  - text: Telefone laden die Seite schneller
    erklaerung: Mit der Ladezeit hat der Begriff nichts zu tun.
```

## Mehrere Bedingungen

Bedingungen lassen sich mit `and` verbinden: `@media (min-width: 500px) and (max-width: 900px)` gilt nur dazwischen. Außer der Breite lässt sich zum Beispiel die **Ausrichtung** abfragen: `(orientation: landscape)` ist ein Fenster, das breiter als hoch ist, `portrait` eines, das höher als breit ist. Unsere Bühne liegt quer.

```beispiel
id: and
html: |
  <p class="a">Tablet</p>
  <p class="b">Quer</p>
code: |
  @media (min-width: 500px) and (max-width: 900px) {
    .a {
      background-color: purple;
    }
  }
  @media (orientation: portrait) {
    .b {
      background-color: teal;
    }
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Tablet ist lila hinterlegt, Quer bleibt ohne Hintergrund
      richtig: true
      erklaerung: Richtig. 600 liegt zwischen 500 und 900, aber die Bühne ist quer, nicht hochkant.
    - text: Beide sind hinterlegt
      erklaerung: Die Bühne ist 600 breit und 400 hoch, also landscape. portrait trifft nicht zu.
    - text: Keiner ist hinterlegt, and verlangt zu viel
      erklaerung: Beide Teile der ersten Bedingung sind erfüllt.
```

```frage
frageart: auswahl
id: hochkant
text: Ein Telefon wird hochkant gehalten. Welche Bedingung ist erfüllt?
als_code: true
optionen:
  - text: "(orientation: portrait)"
    richtig: true
    erklaerung: Richtig, höher als breit.
  - text: "(orientation: landscape)"
    erklaerung: landscape heißt quer, breiter als hoch.
  - text: "(min-width: 2000px)"
    erklaerung: So breit ist kein Telefon.
```

## Die Reihenfolge zählt

Eine Media Query macht Regeln **nicht genauer**. Steht eine Regel im `@media` **vor** einer gleich genauen Regel außerhalb, gewinnt die spätere, auch wenn die Bedingung erfüllt ist. Darum gehören Media Queries meist ans Ende des CSS.

```beispiel
id: reihenfolge
html: |
  <h2>Speisekarte</h2>
code: |
  @media (min-width: 500px) {
    h2 {
      color: gold;
    }
  }
  h2 {
    color: skyblue;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die Überschrift ist himmelblau
      richtig: true
      erklaerung: Richtig. Beide Regeln sind gleich genau, die spätere gewinnt, die Bedingung macht nichts genauer.
    - text: Die Überschrift ist gold, die Bedingung ist ja erfüllt
      erklaerung: Erfüllt heißt nur, dass die Regel mitspielt. Gewinnen muss sie trotzdem nach den Regeln der Kaskade.
    - text: Die Überschrift ist gold und himmelblau gestreift
      erklaerung: Eine Angabe gewinnt ganz.
```

```frage
frageart: fehlerstelle
id: reihenfolge-fehler
text: Die Überschrift soll auf breiten Fenstern gold sein, bleibt aber weiß. In welcher Zeile steht die Regel, die gewinnt?
code: |
  @media (min-width: 500px) {
    h1 { color: gold; }
  }
  h1 { color: white; }
zeile: 4
erklaerung: Genau. Sie steht später und ist gleich genau, darum gewinnt sie. Die Media Query gehört ans Ende.
hinweis: Gleich genau heißt, die spätere gewinnt.
```

```merke
text: "`@media (min-width: 500px)` gilt ab einer Breite, `(max-width: 500px)` bis zu einer Breite, mit `and` verbunden, dazu `(orientation: landscape)` oder `portrait`. Mobile First: erst schmal, dann mit min-width erweitern. Media Queries machen nichts genauer, darum ans Ende."
```

```falle
titel: Leerzeichen und Klammern
text: "`@media min-width: 500px { ... }` ohne Klammern ist ungültig, und alle Regeln darin fallen weg. Die Bedingung steht immer in runden Klammern: `@media (min-width: 500px)`."
```

```augenzwinkern
text: Pit hat seine Webseite auf seinem alten Telefon getestet. Es ist so schmal, dass die Speisekarte nur ein Wort pro Zeile zeigt. Pit sagt, das sei Lyrik.
```
