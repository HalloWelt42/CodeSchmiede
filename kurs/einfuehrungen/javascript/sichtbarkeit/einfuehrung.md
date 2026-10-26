---
id: js-sichtbarkeit
sprache: javascript
titel: Sichtbarkeit und Closures
kurz: Wo ein Name gilt, Blöcke und Funktionen als eigene Bereiche, gleiche Namen innen und außen, Funktionen, die sich an ihre Umgebung erinnern, und die alte Art var.
fuehrt_ein: [var]
lernziele:
  - wissen, dass let und const nur in ihrem Block gelten
  - Parameter und Namen in Funktionen von Namen außerhalb unterscheiden
  - verstehen, was passiert, wenn innen ein Name von außen überdeckt wird
  - mit einer Closure eine Funktion bauen, die sich etwas merkt
  - var erkennen und wissen, warum man heute let und const nimmt
karte: Ich weiß, wo ein Name gilt
bilder:
  - schluessel: karte_js_sichtbarkeit
    art: sammelkarte
    sprache: javascript
    motiv: Eine große Schneekugel enthält eine kleinere Schneekugel, in beiden sitzt ein Pinguin, der kleine schaut nach draußen
---

## Wo ein Name gilt

```alltag
text: Pit hat eine große Schneekugel, und darin steht eine kleinere. Wer in der kleinen sitzt, sieht durch das Glas alles in der großen. Wer in der großen sitzt, sieht aber nicht, was in der kleinen versteckt ist. So sind die Bereiche in JavaScript ineinandergesteckt.
zeichnung: schneekugel
```

Ein Name, der mit `let` oder `const` angelegt wird, gilt in dem Block, in dem er steht, also zwischen den geschweiften Klammern, und in allen Blöcken darin. Außerhalb gibt es ihn nicht. Das gilt für if, Schleifen und Funktionen gleichermaßen. Spiel das Beispiel ab und sieh im Speicher, wann `rabatt` auftaucht und wieder verschwindet.

```beispiel
id: block
code: |
  const summe = 24;
  if (summe >= 20) {
    const rabatt = summe / 10;
    console.log("Rabatt:", rabatt);
  }
  console.log("Summe:", summe);
  console.log(typeof rabatt);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Rabatt: 2.4
        Summe: 24
        undefined
      richtig: true
      erklaerung: Richtig. rabatt gibt es nur im Block des if. Außerhalb kennt JavaScript den Namen nicht, typeof meldet undefined.
    - text: |-
        Rabatt: 2.4
        Summe: 24
        number
      erklaerung: Mit der schließenden Klammer endet der Block, und rabatt verschwindet mit ihm.
    - text: |-
        Rabatt: 2.4
        Summe: 2.4
        undefined
      erklaerung: summe wurde nie verändert. rabatt ist ein eigener Name im Block.
```

```falle
titel: Draußen unbekannt
text: "Ohne typeof bricht der Zugriff von außen ab: `console.log(rabatt);` hinter dem Block meldet `ReferenceError: rabatt is not defined`. Brauchst du einen Wert nach dem Block, leg den Namen vorher außen an, etwa `let rabatt = 0;`, und gib ihm im Block den Wert."
```

```frage
frageart: fehlerstelle
id: fehler-block
text: Das Programm bricht ab. In welcher Zeile?
code: |
  for (let i = 0; i < 3; i++) {
    const doppelt = i * 2;
  }
  console.log(doppelt);
zeile: 4
erklaerung: Genau. doppelt lebt nur im Block der Schleife.
hinweis: Wo endet der Block, in dem doppelt angelegt wurde?
```

## Funktionen haben ihren eigenen Bereich

Parameter und Namen, die in einer Funktion angelegt werden, gehören der Funktion; jeder Aufruf bekommt frische. Von innen sieht die Funktion aber auch alle Namen außen herum. Legt sie innen einen Namen an, den es außen schon gibt, überdeckt der innere den äußeren, solange die Funktion läuft. Draußen ändert sich nichts.

```beispiel
id: ueberdecken
code: |
  const fisch = "Hering";
  let zaehler = 0;
  function angebot(preis) {
    const fisch = "Makrele";
    zaehler++;
    return `${fisch} für ${preis} Euro`;
  }
  console.log(angebot(3));
  console.log(fisch, zaehler);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Makrele für 3 Euro
        Hering 1
      richtig: true
      erklaerung: Richtig. Innen überdeckt Makrele den Hering, draußen bleibt er. zaehler gibt es nur außen, die Funktion zählt ihn hoch.
    - text: |-
        Makrele für 3 Euro
        Makrele 1
      erklaerung: Der innere Name fisch ist ein eigener. Der äußere bleibt Hering.
    - text: |-
        Hering für 3 Euro
        Hering 0
      erklaerung: Innen gilt zuerst der eigene Name, Makrele. Und zaehler++ ändert den äußeren zaehler.
```

```merke
text: "let und const gelten im Block ihrer Klammern und allen Blöcken darin. Innen sieht man nach außen, außen nicht nach innen. Ein gleicher Name innen überdeckt den äußeren nur innen."
```

## Funktionen mit Gedächtnis

Eine Funktion, die in einer anderen entsteht, nimmt die Namen ihrer Umgebung mit, auch wenn die äußere Funktion längst fertig ist. So eine Funktion mit Gedächtnis heißt Closure. Damit baut man Zähler, die niemand von außen verstellen kann.

```beispiel
id: closure
code: |
  function nummernGeber(start) {
    let naechste = start;
    return () => {
      const nummer = naechste;
      naechste++;
      return nummer;
    };
  }
  const bonNummer = nummernGeber(100);
  const losNummer = nummernGeber(1);
  console.log(bonNummer(), bonNummer(), losNummer(), bonNummer());
vorhersage:
  art: auswahl
  optionen:
    - text: 100 101 1 102
      richtig: true
      erklaerung: Richtig. Jeder Geber hat sein eigenes naechste und merkt es sich zwischen den Aufrufen.
    - text: 100 100 1 100
      erklaerung: naechste wird bei jedem Aufruf hochgezählt und bleibt erhalten, denn die Pfeilfunktion hält es fest.
    - text: 100 101 102 103
      erklaerung: losNummer ist ein eigener Geber mit eigenem naechste, der bei 1 beginnt.
```

```frage
frageart: auswahl
id: was-ist-closure
text: Was ist eine Closure?
optionen:
  - text: Eine Funktion, die sich die Namen ihrer Umgebung merkt, auch nachdem die äußere Funktion fertig ist
    richtig: true
    erklaerung: Richtig. Sie trägt ihren Rucksack mit den äußeren Namen immer mit sich.
  - text: Eine Funktion, die sich selbst schließt und nur einmal laufen kann
    erklaerung: Eine Closure kann beliebig oft laufen; sie behält ihre Umgebung.
  - text: Ein Block mit geschweiften Klammern
    erklaerung: Ein Block ist ein Bereich, eine Closure eine Funktion mit Gedächtnis.
```

## Die alte Art var

Früher gab es nur `var`. Ein var-Name gilt nicht im Block, sondern in der ganzen Funktion (oder überall, wenn er außerhalb steht), und JavaScript kennt ihn schon vor seiner Zeile, dort mit dem Wert undefined. Beides führt leicht zu Fehlern, die niemand bemerkt. Du wirst var in älterem Code sehen; schreib selbst let und const.

```beispiel
id: var
code: |
  console.log(alt);
  var alt = "var";
  if (true) {
    var drinnen = "aus dem Block entwischt";
  }
  console.log(alt, drinnen);
vorhersage:
  art: eintippen
  erklaerung: "alt ist in Zeile 1 schon bekannt, hat aber noch keinen Wert: undefined. Und drinnen entwischt aus dem if, weil var den Block nicht beachtet. Mit let gäbe es an beiden Stellen einen ReferenceError, und der wäre ehrlicher."
```

```frage
frageart: ordnen
id: ordnen-closure
text: Bring die Zeilen in Reihenfolge, damit ein Zähler entsteht, der 1 und dann 2 ausgibt.
zeilen:
  - function zaehlerBauen() {
  - '  let stand = 0;'
  - '  return () => ++stand;'
  - '}'
  - const zaehlen = zaehlerBauen();
  - console.log(zaehlen(), zaehlen());
erklaerung: Richtig. stand lebt in zaehlerBauen, die zurückgegebene Funktion nimmt es mit.
hinweis: Erst die Fabrik, dann den Zähler bauen, dann zählen.
```

```augenzwinkern
text: Pit hat einmal mit var einen Fisch im if-Block versteckt. Der Fisch ist trotzdem überall im Programm aufgetaucht. Seitdem nennt Pit var nur noch die undichte Kiste.
```
