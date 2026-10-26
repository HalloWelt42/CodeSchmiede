---
id: css-einheiten
sprache: css
titel: Einheiten
kurz: Größen relativ zur Schrift mit em und rem, zum Elternelement mit Prozent, zum Fenster mit vw und vh, und Grenzen mit min- und max-width.
fuehrt_ein: [em, rem, prozent, vw_vh, min_max]
lernziele:
  - Größen mit em relativ zur eigenen Schriftgröße angeben
  - mit rem Größen auf die Grundschrift der Seite beziehen
  - Breiten in Prozent des Elternelements angeben
  - mit vw und vh Größen auf das Fenster beziehen
  - mit max-width und min-width Grenzen setzen
karte: Ich messe mit dem passenden Maßband
bilder:
  - schluessel: karte_css_einheiten
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin misst mit drei verschiedenen Maßbändern einen Fisch, ein Küken und eine Eisscholle
---

## Relativ zur Schrift: em

```alltag
text: "Pit misst Fische nicht in Zentimetern, sondern in Pinguinflossen: Der Hering ist zwei Flossen lang. Bei Pia sind das andere Zentimeter als bei Pit, denn ihre Flossen sind kleiner. So funktioniert em: Das Maß hängt davon ab, wer misst."
zeichnung: massband
```

Pixel sind ein festes Maß. Oft ist es aber praktischer, relativ zu messen. `1em` ist so groß wie die **Schriftgröße des Elements selbst**. Ein Element mit `font-size: 20px` und `padding: 1em` hat also 20 Pixel Innenabstand. Wird die Schrift größer, wächst das Polster mit. Bei `font-size` selbst bezieht sich em auf die Schrift der **Eltern**: `font-size: 2em` heißt doppelt so groß wie bei den Eltern.

```beispiel
id: em
html: |
  <p class="klein">Hering</p>
  <p class="gross">Riesenhering</p>
code: |
  p {
    background-color: teal;
    padding: 0.5em 1em;
    width: 8em;
  }
  .klein {
    font-size: 12px;
  }
  .gross {
    font-size: 24px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Der zweite Kasten ist in allem doppelt so groß wie der erste, Polster und Breite inklusive
      richtig: true
      erklaerung: Richtig. em misst mit der eigenen Schriftgröße, also bei 24 Pixeln doppelt so viel wie bei 12.
    - text: Nur die Schrift ist verschieden, Polster und Breite sind gleich
      erklaerung: Polster und Breite stehen in em und wachsen mit der Schriftgröße.
    - text: Beide sind gleich groß, beide haben width 8em
      erklaerung: 8em sind beim ersten 96 Pixel, beim zweiten 192.
```

```frage
frageart: auswahl
id: em-rechnen
text: "Ein Absatz hat `font-size: 18px` und `margin-bottom: 2em`. Wie groß ist der Abstand?"
optionen:
  - text: 36 Pixel
    richtig: true
    erklaerung: Richtig, zweimal die eigene Schriftgröße.
  - text: 32 Pixel
    erklaerung: Gemessen wird mit der eigenen Schrift, 18 Pixel, nicht mit 16.
  - text: 2 Pixel
    erklaerung: em ist ein Vielfaches der Schriftgröße, kein Pixel.
```

## Relativ zur Seite: rem

em kann sich aufschaukeln: Ein Element mit `font-size: 1.2em` in einem anderen mit `1.2em` ist schon 1,44-mal so groß. `rem` (root em) misst dagegen immer mit der Schriftgröße der **Wurzel**, des Elements `html`, und die ist von Haus aus 16 Pixel. `2rem` ist also überall 32 Pixel, egal wie tief das Element steckt.

```beispiel
id: rem
html: |
  <div class="liste">
    <div class="liste">
      <p class="em">em</p>
      <p class="rem">rem</p>
    </div>
  </div>
code: |
  .liste {
    font-size: 1.5em;
  }
  .em {
    font-size: 1em;
  }
  .rem {
    font-size: 1rem;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: em erscheint groß, gut doppelt so groß wie rem, das in normaler Größe bleibt
      richtig: true
      erklaerung: Richtig. Die beiden Listen machen die Schrift erst 1,5-mal, dann noch einmal 1,5-mal so groß, also 36 Pixel. 1rem bleibt 16.
    - text: Beide sind gleich groß, 1em und 1rem sind dasselbe
      erklaerung: 1em erbt die vergrößerte Schrift der Eltern, 1rem bezieht sich immer auf html.
    - text: rem ist größer als em
      erklaerung: Andersherum. rem ignoriert die Vergrößerung der Eltern.
```

```frage
frageart: luecke
id: luecke-rem
text: Die Überschrift soll überall genau doppelt so groß wie die Grundschrift der Seite sein. Ergänze die Einheit.
code: |
  h2 {
    font-size: 2___;
  }
antworten: [["rem"]]
erklaerung: Richtig, rem misst immer mit der Schrift von html.
hinweis: Die Einheit, die sich auf die Wurzel bezieht.
```

## Prozent vom Elternelement

Eine Breite in **Prozent** bezieht sich auf die Breite des **Elternelements**, genauer auf den Platz für seinen Inhalt. `width: 50%` ist halb so breit wie die Eltern. Ändert sich deren Breite, passt sich das Kind an.

```beispiel
id: prozent
html: |
  <div class="wagen">
    <p class="halb">Halb</p>
    <p class="viertel">Viertel</p>
  </div>
code: |
  .wagen {
    width: 400px;
    background-color: #2b3442;
  }
  .halb {
    width: 50%;
    background-color: teal;
  }
  .viertel {
    width: 25%;
    background-color: purple;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Im 400 Pixel breiten Wagen ein Streifen von 200 und einer von 100 Pixeln
      richtig: true
      erklaerung: Richtig. Prozent beziehen sich auf den Wagen, nicht auf die Bühne.
    - text: Ein Streifen von 300 und einer von 150 Pixeln, halb und viertel der Bühne
      erklaerung: Die Prozent beziehen sich auf das Elternelement, und das ist der Wagen mit 400 Pixeln.
    - text: Beide Streifen sind so breit wie der Wagen
      erklaerung: width 50% und 25% machen sie schmaler.
```

```frage
frageart: auswahl
id: prozent-wovon
text: "Worauf bezieht sich `width: 30%`?"
optionen:
  - text: Auf die Breite des Elternelements
    richtig: true
    erklaerung: Richtig, genauer auf den Platz für dessen Inhalt.
  - text: Immer auf die Breite des Fensters
    erklaerung: Das wäre vw. Prozent hängen am Elternelement.
  - text: Auf die Schriftgröße
    erklaerung: Das wäre em.
```

## Relativ zum Fenster: vw und vh

`vw` und `vh` messen am **Fenster**: `1vw` ist ein Hundertstel der Fensterbreite, `1vh` ein Hundertstel der Fensterhöhe, egal wie tief ein Element steckt. Auf unserer Bühne, 600 mal 400 Pixel, ist `1vw` also 6 Pixel und `1vh` 4 Pixel. `height: 50vh` ist die halbe Bühnenhöhe.

```beispiel
id: vw
html: |
  <div class="schild">Halbe Bühne</div>
code: |
  .schild {
    width: 50vw;
    height: 50vh;
    background-color: teal;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Ein Kasten 300 mal 200 Pixel, halb so breit und halb so hoch wie die Bühne
      richtig: true
      erklaerung: Richtig. 50vw sind die Hälfte von 600, 50vh die Hälfte von 400.
    - text: Ein Quadrat von 50 mal 50 Pixeln
      erklaerung: vw und vh sind Hundertstel des Fensters, keine Pixel.
    - text: Ein Kasten, der die ganze Bühne füllt
      erklaerung: Das wären 100vw und 100vh.
```

```frage
frageart: auswahl
id: vh-buehne
text: "Wie hoch ist `height: 25vh` auf unserer 400 Pixel hohen Bühne?"
optionen:
  - text: 100 Pixel
    richtig: true
    erklaerung: Richtig, ein Viertel von 400.
  - text: 25 Pixel
    erklaerung: vh sind Hundertstel der Fensterhöhe, keine Pixel.
  - text: 150 Pixel
    erklaerung: Das wäre ein Viertel der Breite, 25vw.
```

## Grenzen setzen

Relative Breiten können zu breit oder zu schmal werden. `max-width` setzt eine **Obergrenze**, `min-width` eine **Untergrenze**. `width: 80%; max-width: 300px` heißt: 80 Prozent, aber nie mehr als 300 Pixel. Genauso gibt es `min-height` und `max-height`.

```beispiel
id: grenzen
html: |
  <p class="a">Mit Obergrenze</p>
  <p class="b">Ohne Obergrenze</p>
code: |
  p {
    width: 80%;
    background-color: teal;
  }
  .a {
    max-width: 300px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Der erste Streifen ist 300 Pixel breit, der zweite deutlich breiter
      richtig: true
      erklaerung: Richtig. 80 Prozent der Bühne wären über 450 Pixel, die Obergrenze kappt beim ersten auf 300.
    - text: Beide sind gleich breit, width gewinnt
      erklaerung: max-width begrenzt width, wenn es größer würde.
    - text: Der erste ist 80 Pixel breit
      erklaerung: 80% heißt 80 Prozent des Elternelements, nicht 80 Pixel.
```

```merke
text: "`em`: eigene Schriftgröße (bei font-size die der Eltern). `rem`: Schrift von html. `%`: Breite der Eltern. `vw`/`vh`: Hundertstel des Fensters. `max-width` und `min-width` setzen Grenzen."
```

```falle
titel: em, das sich aufschaukelt
text: "`li { font-size: 1.2em; }` sieht harmlos aus. Steckt aber eine Liste in einer Liste, wird jede Ebene noch einmal 1,2-mal größer. Mit `rem` passiert das nicht."
```

```augenzwinkern
text: Pia hat einmal 100vw als Breite für ihr Handtuch bestellt. Geliefert wurde ein Handtuch genau so breit wie ihr Bildschirm.
```
