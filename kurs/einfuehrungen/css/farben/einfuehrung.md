---
id: css-farben
sprache: css
titel: Farben
kurz: Farben aus Rot, Grün und Blau mischen, als rgb und in Hex-Schreibweise, und Farben durchscheinen lassen.
fuehrt_ein: [rgb, hex, transparenz]
lernziele:
  - Farben mit rgb aus Rot, Grün und Blau mischen
  - Farben in Hex-Schreibweise lesen und schreiben, auch kurz mit drei Zeichen
  - Grautöne an gleichen Anteilen erkennen
  - Farben mit einem Alphawert durchscheinen lassen
  - mit opacity ein ganzes Element durchsichtig machen
karte: Ich mische jede Farbe, die ich will
bilder:
  - schluessel: karte_css_farben
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin gießt aus drei Farbeimern in Rot, Grün und Blau Licht auf eine Wand, wo sich die Farben mischen
---

## Mischen mit rgb

```alltag
text: Ein Bildschirm hat keine Farbeimer, nur winzige Lämpchen in Rot, Grün und Blau. Je heller jedes leuchtet, desto mehr trägt es bei. Alle drei voll ergibt Weiß, alle drei aus ergibt Schwarz. Pit mischt seine Lieblingsfarbe Lachsrosa also aus Licht.
zeichnung: farbeimer
```

Farbnamen wie `gold` sind bequem, aber es gibt nur gut 140 davon. Jede andere Farbe mischt man mit `rgb(rot, grün, blau)`: Jeder Anteil geht von 0 (aus) bis 255 (voll). `rgb(255, 0, 0)` ist reines Rot, `rgb(255, 255, 0)` Gelb (Rot und Grün zusammen, wie bei Licht), `rgb(255, 255, 255)` Weiß.

```beispiel
id: rgb
html: |
  <p class="eins">Rot</p>
  <p class="zwei">Rot und Grün</p>
  <p class="drei">Alles halb</p>
code: |
  .eins {
    background-color: rgb(255, 0, 0);
  }
  .zwei {
    background-color: rgb(255, 255, 0);
    color: black;
  }
  .drei {
    background-color: rgb(128, 128, 128);
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Ein roter, ein gelber und ein grauer Streifen
      richtig: true
      erklaerung: Richtig. Rot und Grün als Licht gemischt ergibt Gelb, alle drei halb ergibt Grau.
    - text: Ein roter, ein brauner und ein grauer Streifen
      erklaerung: Mit Farbeimern ergäbe Rot und Grün Braun. Licht mischt sich anders, zu Gelb.
    - text: Ein roter, ein gelber und ein weißer Streifen
      erklaerung: Weiß wäre alles voll, 255. Bei 128 leuchtet jedes Lämpchen nur halb, das ergibt Grau.
```

```frage
frageart: auswahl
id: welches-blau
text: "Welche Farbe ist `rgb(0, 0, 255)`?"
optionen:
  - text: Reines Blau
    richtig: true
    erklaerung: Richtig. Rot aus, Grün aus, Blau voll.
  - text: Schwarz, weil zwei Anteile 0 sind
    erklaerung: Schwarz wäre alles 0. Hier leuchtet Blau voll.
  - text: Reines Rot, die erste Zahl zählt
    erklaerung: Die Reihenfolge ist Rot, Grün, Blau. Die erste Zahl ist 0, Rot ist also aus.
```

## Hex-Schreibweise

Noch häufiger sieht man Farben wie `#ff8800`. Das ist dieselbe Mischung, nur kürzer: nach der Raute je zwei Zeichen für Rot, Grün und Blau, in **Hexadezimal**, also mit den Ziffern 0 bis 9 und den Buchstaben a bis f. `00` heißt 0, `ff` heißt 255, `80` ungefähr die Hälfte. `#ff8800` ist also Rot voll, Grün halb, Blau aus: Orange.

```beispiel
id: hex
html: |
  <h2>Hering</h2>
  <p>Frisch aus dem Eis</p>
code: |
  h2 {
    color: #ff8800;
  }
  p {
    background-color: #004466;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Eine orange Überschrift und ein Absatz auf dunklem Blaugrün
      richtig: true
      erklaerung: Richtig. ff8800 ist Rot voll, Grün halb. 004466 hat kein Rot und wenig Grün und Blau, also dunkles Blaugrün.
    - text: Eine rote Überschrift und ein Absatz auf hellem Blau
      erklaerung: Bei ff8800 ist Grün halb an, das macht Orange. Und 44 und 66 sind kleine Anteile, also dunkel.
    - text: Eine orange Überschrift und ein Absatz ohne Hintergrund, denn Hex geht nur bei color
      erklaerung: Hex-Farben gehen überall, wo eine Farbe stehen darf.
```

```frage
frageart: luecke
id: luecke-hex-weiss
text: Ergänze Weiß in Hex-Schreibweise.
code: |
  p {
    color: #___;
  }
antworten: [["ffffff", "FFFFFF", "fff", "FFF"]]
erklaerung: Richtig, alle drei Anteile voll.
hinweis: Voll heißt in Hex ff, und das dreimal.
```

```merke
text: "`rgb(rot, grün, blau)` mit Anteilen von 0 bis 255. `#rrggbb` ist dasselbe in Hex: `00` aus, `ff` voll."
```

## Kurz und grau

Sind bei jedem Anteil beide Zeichen gleich, geht es kürzer: `#ff8800` lässt sich als `#f80` schreiben, jedes Zeichen wird verdoppelt. Und eine Regel zum Merken: Sind alle drei Anteile gleich, ist die Farbe **grau**, von `#000` (Schwarz) über `#888` bis `#fff` (Weiß).

```beispiel
id: grau
html: |
  <p class="dunkel">Kohle</p>
  <p class="mittel">Möwe</p>
  <p class="hell">Nebel</p>
code: |
  .dunkel {
    background-color: #333;
  }
  .mittel {
    background-color: #888;
  }
  .hell {
    background-color: #ccc;
    color: #000;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Drei graue Streifen von dunkel nach hell, der letzte mit schwarzer Schrift
      richtig: true
      erklaerung: Richtig. Gleiche Anteile sind grau, je größer, desto heller.
    - text: Drei Streifen in Rot, Grün und Blau
      erklaerung: Die drei Zeichen stehen für Rot, Grün und Blau, aber sie sind jeweils gleich. Das ergibt Grau.
    - text: Drei graue Streifen von hell nach dunkel
      erklaerung: 3 ist wenig, c ist viel. Also wird es von oben nach unten heller.
```

```frage
frageart: auswahl
id: kurzform
text: "Welche lange Form gehört zu `#0af`?"
als_code: true
optionen:
  - text: "#00aaff"
    richtig: true
    erklaerung: Richtig, jedes Zeichen verdoppelt.
  - text: "#0a0f00"
    erklaerung: Verdoppelt wird jedes Zeichen für sich, nicht mit Nullen aufgefüllt.
  - text: "#000aff"
    erklaerung: Jedes der drei Zeichen steht für einen Anteil und wird verdoppelt.
```

## Durchscheinend

Eine vierte Zahl macht eine Farbe durchscheinend: `rgb(255 255 255 / 0.2)` ist Weiß, das nur zu 20 Prozent deckt; der Rest des Hintergrunds scheint durch. Diese Schreibweise trennt die Anteile mit Leerzeichen und den **Alphawert** mit einem Schrägstrich. Alpha 1 deckt ganz, 0 ist unsichtbar. Ältere Stylesheets schreiben dafür `rgba(255, 255, 255, 0.2)`.

```beispiel
id: alpha
html: |
  <div class="wasser">
    <p class="eis">Eisscholle</p>
    <p class="fest">Felsen</p>
  </div>
code: |
  .wasser {
    background-color: rgb(0, 80, 160);
  }
  .eis {
    background-color: rgb(255 255 255 / 0.3);
  }
  .fest {
    background-color: rgb(255 255 255 / 1);
    color: black;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die Eisscholle ist hellblau, weil das Blau durchscheint, der Felsen reinweiß
      richtig: true
      erklaerung: Richtig. 30 Prozent Weiß über Blau ergibt ein helleres Blau. Alpha 1 deckt ganz.
    - text: Beide Streifen sind reinweiß
      erklaerung: Bei der Eisscholle deckt das Weiß nur zu 30 Prozent, das Blau dahinter scheint durch.
    - text: Die Eisscholle ist unsichtbar, der Felsen weiß
      erklaerung: Unsichtbar wäre Alpha 0. Bei 0.3 bleibt etwas Weiß.
```

```frage
frageart: auswahl
id: alpha-null
text: "Wie sieht `background-color: rgb(255 0 0 / 0)` aus?"
optionen:
  - text: Gar nicht, der Hintergrund ist völlig durchsichtig
    richtig: true
    erklaerung: Richtig, Alpha 0 deckt überhaupt nicht.
  - text: Kräftig rot
    erklaerung: Rot wäre es mit Alpha 1. Bei 0 ist nichts davon zu sehen.
  - text: Schwarz, weil 0
    erklaerung: Die 0 steht hinter dem Schrägstrich, das ist die Deckkraft, keine Farbe.
```

## Alles durchsichtig mit opacity

Der Alphawert gilt nur für die eine Farbe. `opacity` dagegen macht das **ganze Element** durchsichtig, mit Text, Hintergrund und allem, was darin steckt: `opacity: 0.4` lässt nur 40 Prozent übrig. Praktisch für Dinge, die gerade nicht zählen, etwa ausverkaufte Gerichte.

```beispiel
id: opacity
html: |
  <ul>
    <li class="da">Hering</li>
    <li class="weg">Eisscholle</li>
  </ul>
code: |
  li {
    background-color: teal;
  }
  .weg {
    opacity: 0.4;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die Eisscholle ist samt Schrift, Hintergrund und Punkt blass, der Hering kräftig
      richtig: true
      erklaerung: Richtig. opacity gilt für das ganze Element, mit allem darin.
    - text: Nur die Schrift der Eisscholle ist blass, ihr Hintergrund bleibt kräftig
      erklaerung: Das wäre eine Farbe mit Alphawert bei color. opacity macht alles durchsichtig.
    - text: Beide Einträge werden blass, die Regel gilt für die ganze Liste
      erklaerung: opacity steht in der Regel für .weg, und die Klasse trägt nur die Eisscholle.
```

```falle
titel: Komma oder Schrägstrich
text: "In der neuen Schreibweise trennen Leerzeichen die Anteile und ein Schrägstrich den Alphawert: `rgb(255 255 255 / 0.5)`. Mischt man das mit Kommas, etwa `rgb(255, 255, 255 / 0.5)`, ist die Farbe ungültig und fällt still weg."
```

```augenzwinkern
text: Pit hat seinen Fischwagen in rgb(255, 160, 122) gestrichen. Er sagt Lachs, Pia sagt Garnele. Der Bildschirm sagt nur drei Zahlen.
```
