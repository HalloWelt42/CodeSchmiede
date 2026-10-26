---
id: css-klassen
sprache: css
titel: Klassen und ids
kurz: Elemente mit Attributen benennen und mit dem Punkt eine Klasse, mit der Raute eine id wählen.
fuehrt_ein: [klasse, id]
lernziele:
  - Attribute im Starttag lesen
  - Elementen mit class eine oder mehrere Klassen geben und sie mit dem Punkt wählen
  - ein einzelnes Element mit seiner id und der Raute wählen
  - Element und Klasse in einem Selektor verbinden
karte: Ich rufe Elemente beim Namen
bilder:
  - schluessel: karte_css_klassen
    art: sammelkarte
    sprache: css
    motiv: Drei Pinguine mit farbigen Namensschildern stehen in einer Reihe, einer trägt zusätzlich einen goldenen Orden
---

## Attribute und Klassen

```alltag
text: Am Fischwagen tragen alle Pinguine Namensschilder. Die Grünen machen die Kasse, die Blauen braten. Ruft Pit "Alle Grünen zur Kasse!", wissen sofort alle, wer gemeint ist. Und Pia trägt dazu einen goldenen Orden, den gibt es nur einmal.
zeichnung: namensschilder
```

Ein Starttag kann **Attribute** tragen: zusätzliche Angaben in der Form `name="wert"`, nach dem Namen des Elements. Das wichtigste für CSS ist `class`. Es gibt einem Element eine **Klasse**, einen frei gewählten Namen wie ein Namensschild. Viele Elemente dürfen dieselbe Klasse tragen, auch ganz verschiedene Elemente.

Im CSS wählt ein **Punkt** vor dem Namen alle Elemente mit dieser Klasse: `.preis` heißt "alles mit der Klasse preis".

```beispiel
id: klasse
html: |
  <p>Hering <span class="preis">4,50</span></p>
  <p>Makrele <span class="preis">3,80</span></p>
  <p>Heute: <span>mit Eis</span></p>
code: |
  .preis {
    color: gold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die beiden Preise werden gold, mit Eis bleibt hell
      richtig: true
      erklaerung: Richtig. Nur die beiden span mit der Klasse preis sind gemeint.
    - text: Alle drei span werden gold
      erklaerung: Der dritte span trägt keine Klasse. .preis wählt nur Elemente mit class="preis".
    - text: Nichts wird gold, preis ist doch gar kein Element
      erklaerung: Genau dafür ist der Punkt da. Er sagt, dass preis eine Klasse ist, kein Element.
```

```frage
frageart: auswahl
id: wer-ist-gemeint
text: "Welche Elemente wählt `.neu`?"
code: |
  <h2 class="neu">Makrele</h2>
  <p>Hering</p>
  <p class="neu">Sardine</p>
optionen:
  - text: Die Überschrift Makrele und den Absatz Sardine
    richtig: true
    erklaerung: Richtig. Die Klasse zählt, nicht die Art des Elements.
  - text: Nur den Absatz Sardine
    erklaerung: Auch die Überschrift trägt die Klasse neu. Eine Klasse kann an verschiedenen Elementen hängen.
  - text: Gar keins, es gibt kein Element namens neu
    erklaerung: Der Punkt macht aus neu einen Klassennamen, kein Element.
```

```falle
titel: Punkt vergessen
text: "Ohne Punkt sucht `preis { color: gold; }` nach einem Element namens preis. Das gibt es nicht, also passiert nichts, und der Browser beschwert sich auch nicht."
```

## Mehrere Klassen

Ein Element darf mehrere Klassen tragen, durch Leerzeichen getrennt: `class="preis angebot"` heißt, das Element hat die Klasse preis **und** die Klasse angebot. Dann gelten die Regeln beider Klassen.

```beispiel
id: mehrere
html: |
  <p>Hering <span class="preis">4,50</span></p>
  <p>Makrele <span class="preis angebot">3,00</span></p>
code: |
  .preis {
    color: gold;
  }
  .angebot {
    background-color: tomato;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Beide Preise sind gold, der Preis der Makrele steht zusätzlich auf rotem Grund
      richtig: true
      erklaerung: Richtig. Der zweite Preis hat beide Klassen und bekommt beide Regeln.
    - text: Der Preis der Makrele ist nur rot hinterlegt, aber nicht gold
      erklaerung: Er trägt auch die Klasse preis, also gilt die goldene Schrift ebenfalls.
    - text: Der Preis der Makrele bleibt hell, weil zwei Klassen sich gegenseitig aufheben
      erklaerung: Klassen heben sich nicht auf, sie sammeln sich. Jede Regel trägt ihren Teil bei.
```

```frage
frageart: luecke
id: luecke-zwei-klassen
text: Das Element soll die Klassen fisch und neu tragen. Ergänze das Attribut.
code: |
  <li class="___">Sardine</li>
antworten: [["fisch neu", "neu fisch"]]
erklaerung: Richtig. Mehrere Klassen stehen durch Leerzeichen getrennt im selben Attribut.
hinweis: Beide Namen in die Anführungszeichen, dazwischen ein Leerzeichen.
```

## Einzigartig mit id

Das Attribut `id` gibt einem Element einen Namen, den es auf der ganzen Seite **nur einmal** geben darf, wie Pias Orden. Im CSS wählt die **Raute** `#` das Element mit dieser id: `#tagesangebot`.

```beispiel
id: id
html: |
  <ul>
    <li>Hering</li>
    <li id="tagesangebot">Makrele am Stiel</li>
    <li>Sardinen</li>
  </ul>
code: |
  #tagesangebot {
    color: black;
    background-color: gold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Nur Makrele am Stiel steht schwarz auf goldenem Streifen
      richtig: true
      erklaerung: Richtig. Die Raute wählt das eine Element mit id="tagesangebot".
    - text: Alle Einträge stehen schwarz auf gold
      erklaerung: Nur ein Eintrag trägt die id. Die anderen sind nicht gemeint.
    - text: Nichts ändert sich, denn ids wählt man mit dem Punkt
      erklaerung: Der Punkt ist für Klassen. Für ids steht die Raute.
```

```merke
text: "`.name` wählt alle Elemente mit `class=\"name\"`, `#name` das eine Element mit `id=\"name\"`. Klassen dürfen sich wiederholen, ids nicht."
```

## Element und Klasse zusammen

Schreibt man Element und Klasse **ohne Leerzeichen** zusammen, müssen beide passen: `li.neu` wählt nur Listeneinträge mit der Klasse neu, aber keine Überschrift mit derselben Klasse. Das geht auch mit ids und mit mehreren Klassen: `.preis.angebot` wählt nur, was beide Klassen trägt.

```beispiel
id: zusammen
html: |
  <h2 class="neu">Neu auf der Karte</h2>
  <ul>
    <li class="neu">Makrele am Stiel</li>
    <li>Hering</li>
  </ul>
code: |
  li.neu {
    color: lightgreen;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Nur Makrele am Stiel wird hellgrün
      richtig: true
      erklaerung: Richtig. li.neu verlangt beides, ein li und die Klasse neu. Die Überschrift ist kein li.
    - text: Die Überschrift und Makrele am Stiel werden hellgrün
      erklaerung: Das wäre .neu allein. Mit li davor muss das Element auch ein li sein.
    - text: Alle Listeneinträge werden hellgrün
      erklaerung: Hering trägt die Klasse neu nicht, also passt li.neu nicht.
```

```frage
frageart: auswahl
id: zusammen-oder-nicht
text: "Welcher Selektor wählt nur Absätze mit der Klasse hinweis?"
als_code: true
optionen:
  - text: p.hinweis
    richtig: true
    erklaerung: Richtig, Element und Klasse ohne Leerzeichen zusammen.
  - text: .hinweis
    erklaerung: Das wählt alles mit der Klasse hinweis, auch Überschriften oder Listeneinträge.
  - text: hinweis.p
    erklaerung: Erst kommt das Element, dann die Klasse mit Punkt.
```

```augenzwinkern
text: Pit wollte sich die id chef geben, zweimal, für Montag und Dienstag. Der Browser hat beide bedient, aber die Kollegen haben nur einen Chef anerkannt.
```
