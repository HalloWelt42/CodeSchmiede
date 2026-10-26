---
id: js-objekte
sprache: javascript
titel: Objekte
kurz: Zusammengehörige Werte mit Namen in einem Objekt, Zugriff mit Punkt und eckigen Klammern, alle Eigenschaften durchgehen, Objekte in Arrays.
fuehrt_ein: [objekt, for_in, objektmethoden, delete]
lernziele:
  - ein Objekt mit geschweiften Klammern anlegen und mit Punkt lesen, ändern und erweitern
  - mit eckigen Klammern über einen Namen in einer Variable zugreifen und mit in nachsehen
  - mit for ... in und Object.keys, values und entries alle Eigenschaften durchgehen
  - Objekte als Zähler nutzen und Eigenschaften mit delete entfernen
  - Arrays aus Objekten bauen und durchgehen
karte: Ich halte zusammen, was zusammengehört
bilder:
  - schluessel: karte_js_objekte
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin füllt eine große Karteikarte mit beschrifteten Feldern aus, daneben liegt ein Stapel weiterer Karten
---

## Werte mit Namen

```alltag
text: Für jeden Stammkunden hat Pit eine Karteikarte. Darauf stehen Felder mit Namen, Name, Lieblingsfisch, Stempel. Will er wissen, was Pia am liebsten isst, schaut er nicht in Fach 2, sondern ins Feld Lieblingsfisch. Ein Objekt ist so eine Karteikarte.
zeichnung: karteikarte
```

Ein Objekt fasst Werte zusammen, die zusammengehören, und gibt jedem einen Namen. Es steht in geschweiften Klammern, jede Eigenschaft als `name: wert`, getrennt durch Kommas. Mit dem Punkt liest du eine Eigenschaft (`kunde.name`), änderst sie oder legst eine neue an.

```beispiel
id: karte
code: |
  const kunde = { name: "Pia", fisch: "Hering", stempel: 3 };
  console.log(kunde.name, "mag", kunde.fisch);
  kunde.stempel++;
  kunde.stadt = "Eishafen";
  console.log(kunde);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Pia mag Hering
        { name: 'Pia', fisch: 'Hering', stempel: 4, stadt: 'Eishafen' }
      richtig: true
      erklaerung: Richtig. stempel wird hochgezählt, und stadt kommt als neue Eigenschaft hinten dazu.
    - text: |-
        Pia mag Hering
        { name: 'Pia', fisch: 'Hering', stempel: 3 }
      erklaerung: Ein Objekt darf sich ändern, auch unter einem const-Namen, genau wie ein Array.
    - text: |-
        kunde.name mag kunde.fisch
        { name: 'Pia', fisch: 'Hering', stempel: 4, stadt: 'Eishafen' }
      erklaerung: Ohne Anführungszeichen sind es Zugriffe, ausgegeben werden die Werte.
```

```frage
frageart: luecke
id: luecke-punkt
text: Ergänze, damit das Alter des Pinguins ausgegeben wird.
code: |
  const pinguin = { name: "Pit", alter: 4 };
  console.log(pinguin___);
antworten: [[".alter"]]
erklaerung: Richtig, Punkt und der Name der Eigenschaft.
hinweis: Punkt und Name.
```

## Eckige Klammern und in

Steht der Name einer Eigenschaft in einer Variable, geht der Punkt nicht, denn `kunde.feld` sucht eine Eigenschaft, die wirklich feld heißt. Dann nimmst du eckige Klammern: `kunde[feld]`. Eine Eigenschaft, die es nicht gibt, liefert `undefined`. Ob es sie gibt, fragt `"name" in kunde`.

```beispiel
id: klammern
code: |
  const kunde = { name: "Ole", stempel: 2 };
  const feld = "stempel";
  console.log(kunde[feld]);
  console.log(kunde.feld);
  console.log("stempel" in kunde, "telefon" in kunde);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        2
        undefined
        true false
      richtig: true
      erklaerung: Richtig. kunde[feld] schaut nach, was in feld steht, also stempel. kunde.feld sucht eine Eigenschaft feld, die es nicht gibt.
    - text: |-
        2
        2
        true false
      erklaerung: Der Punkt nimmt den Namen wörtlich, kunde.feld sucht die Eigenschaft feld.
    - text: |-
        undefined
        2
        true false
      erklaerung: Mit eckigen Klammern wird der Wert von feld eingesetzt, also stempel.
```

```merke
text: "`{ name: wert, ... }` ist ein Objekt. `obj.name` liest mit festem Namen, `obj[variable]` mit einem Namen aus einer Variable. Fehlende Eigenschaften sind undefined, `\"name\" in obj` fragt, ob es sie gibt."
```

## Alle Eigenschaften durchgehen

`for (const name in objekt)` liefert nacheinander die Namen aller Eigenschaften, in der Reihenfolge, in der sie angelegt wurden. Die Werte holst du mit `objekt[name]`. Als Arrays bekommst du dasselbe mit `Object.keys(objekt)` (die Namen), `Object.values(objekt)` (die Werte) und `Object.entries(objekt)` (Paare aus Name und Wert).

```beispiel
id: zaehler
code: |
  const verkauft = {};
  const bestellungen = ["Hering", "Aal", "Hering", "Hering", "Aal"];
  for (const fisch of bestellungen) {
    if (fisch in verkauft) {
      verkauft[fisch]++;
    } else {
      verkauft[fisch] = 1;
    }
  }
  for (const fisch in verkauft) {
    console.log(`${fisch}: ${verkauft[fisch]}`);
  }
  console.log(Object.keys(verkauft).length, "Sorten");
vorhersage:
  art: eintippen
  erklaerung: "Das leere Objekt zählt mit: Kommt ein Fisch zum ersten Mal, bekommt er 1, sonst wird hochgezählt. Hering kommt dreimal, Aal zweimal. Object.keys liefert die beiden Namen, also 2 Sorten."
```

```falle
titel: in und of verwechselt
text: "`for ... in` liefert Namen von Eigenschaften und ist für Objekte gedacht. `for ... of` liefert Werte und ist für Arrays und Text gedacht. Auf ein Objekt angewendet bricht for ... of ab mit `TypeError: verkauft is not iterable`, auf Deutsch: lässt sich nicht durchgehen."
```

```frage
frageart: auswahl
id: keys
text: 'Was liefert `Object.keys({ a: 1, b: 2 })`?'
als_code: true
optionen:
  - text: "[ 'a', 'b' ]"
    richtig: true
    erklaerung: Richtig, die Namen der Eigenschaften als Array.
  - text: '[ 1, 2 ]'
    erklaerung: Das wären die Werte, die liefert Object.values.
  - text: '2'
    erklaerung: Die Anzahl wäre Object.keys(...).length.
```

## Objekte in Arrays

Richtig stark werden Objekte im Team mit Arrays: ein Array, in dem jedes Fach ein Objekt ist, etwa eine Speisekarte, bei der jedes Gericht Name und Preis hat. Mit `delete objekt.name` entfernst du eine Eigenschaft ganz.

```beispiel
id: speisekarte
code: |
  const karte = [
    { name: "Heringsbrötchen", preis: 2.5 },
    { name: "Fischsuppe", preis: 4.5, scharf: true },
  ];
  for (const gericht of karte) {
    console.log(`${gericht.name}: ${gericht.preis.toFixed(2)} Euro`);
  }
  delete karte[1].scharf;
  console.log(karte[1]);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Heringsbrötchen: 2.50 Euro
        Fischsuppe: 4.50 Euro
        { name: 'Fischsuppe', preis: 4.5 }
      richtig: true
      erklaerung: Richtig. for ... of liefert jedes Objekt, dessen Eigenschaften der Punkt holt. delete entfernt scharf ganz.
    - text: |-
        Heringsbrötchen: 2.5 Euro
        Fischsuppe: 4.5 Euro
        { name: 'Fischsuppe', preis: 4.5 }
      erklaerung: toFixed(2) sorgt für die zwei Nachkommastellen.
    - text: |-
        Heringsbrötchen: 2.50 Euro
        Fischsuppe: 4.50 Euro
        { name: 'Fischsuppe', preis: 4.5, scharf: undefined }
      erklaerung: delete entfernt die Eigenschaft, sie bekommt nicht nur den Wert undefined.
```

```frage
frageart: ordnen
id: ordnen-karte
text: Bring die Zeilen in Reihenfolge, damit der Preis des Aals ausgegeben wird.
zeilen:
  - 'const karte = [{ name: "Hering", preis: 2 }, { name: "Aal", preis: 5 }];'
  - for (const gericht of karte) {
  - '  if (gericht.name === "Aal") {'
  - '    console.log(gericht.preis);'
  - '  }'
  - '}'
erklaerung: Richtig. Durch alle Gerichte gehen und beim Aal den Preis ausgeben.
hinweis: Die Klammern schließen in umgekehrter Reihenfolge, wie sie aufgehen.
```

```augenzwinkern
text: Pits eigene Karteikarte hat die Eigenschaft lieblingsfisch mit dem Wert "alle". Er findet, das zählt.
```
