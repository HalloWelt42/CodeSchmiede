---
id: js-json
sprache: javascript
titel: JSON
kurz: Objekte und Arrays mit JSON.stringify als Text verschicken und mit JSON.parse wieder auspacken; was JSON kann, was nicht, und wie man kaputtes JSON abfängt.
fuehrt_ein: [json]
lernziele:
  - mit JSON.stringify ein Objekt in Text verwandeln, kompakt oder eingerückt
  - mit JSON.parse aus Text wieder Objekte und Arrays machen
  - wissen, was JSON speichern kann und was dabei verloren geht
  - kaputtes JSON mit try und catch abfangen
karte: Ich verschicke Objekte als Text
bilder:
  - schluessel: karte_js_json
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin rollt einen Zettel zusammen und steckt ihn in eine Flaschenpost, am Ufer gegenüber zieht ein zweiter Pinguin eine Flasche aus dem Wasser
---

## Objekte als Text

```alltag
text: Pit will Pia auf der Nachbarinsel seine Speisekarte schicken. Eine Kiste voller Objekte passt aber nicht durch den Flaschenhals, nur ein Zettel. Also schreibt er alles fein säuberlich auf, und Pia baut es drüben wieder auf. JSON ist diese Art, Daten auf einen Zettel zu schreiben.
zeichnung: flaschenpost
```

JSON (gesprochen wie der Name Jason) ist ein Textformat für Daten, das aussieht wie JavaScript-Objekte und -Arrays. Fast jedes Programm der Welt kann es lesen, darum verschickt und speichert man damit Daten. `JSON.stringify(wert)` macht aus einem Wert den Text. Die Namen der Eigenschaften stehen dabei immer in doppelten Anführungszeichen. Mit `JSON.stringify(wert, null, 2)` wird der Text eingerückt und lesbar.

```beispiel
id: stringify
code: |
  const kunde = { name: "Pia", stempel: 3, lieblinge: ["Hering", "Aal"] };
  const text = JSON.stringify(kunde);
  console.log(text);
  console.log(typeof text, text.length);
  console.log(JSON.stringify({ ort: "Eishafen", offen: true }, null, 2));
vorhersage:
  art: eintippen
  erklaerung: "stringify schreibt alles in eine Zeile, Namen und Texte in doppelten Anführungszeichen. Heraus kommt ein ganz normaler Text mit 55 Zeichen. Mit null, 2 kommt jede Eigenschaft in eine eigene Zeile, um zwei Leerzeichen eingerückt."
```

```frage
frageart: auswahl
id: was-liefert-stringify
text: Was für ein Wert ist `JSON.stringify([1, 2])`?
optionen:
  - text: Der Text "[1,2]"
    richtig: true
    erklaerung: Richtig. stringify liefert immer Text, ohne Leerzeichen dazwischen.
  - text: Ein Array mit zwei Zahlen
    erklaerung: Das Array ist das, was hineingeht. Heraus kommt Text.
  - text: Die Zahl 12
    erklaerung: Die Klammern und das Komma bleiben im Text erhalten.
```

## Aus Text wird wieder ein Objekt

`JSON.parse(text)` liest JSON-Text und baut die Objekte, Arrays, Zahlen und Texte wieder auf. Danach arbeitest du damit wie mit allem anderen. So lassen sich auch Daten aus einer Eingabe übernehmen.

```beispiel
id: parse
code: |
  const zettel = '{"wagen":"Zum frostigen Hering","karte":[{"name":"Hering","preis":2.5},{"name":"Suppe","preis":4.5}]}';
  const daten = JSON.parse(zettel);
  console.log(daten.wagen);
  for (const g of daten.karte) {
    console.log(`${g.name}: ${g.preis.toFixed(2)}`);
  }
  console.log(daten.karte.length, typeof daten.karte[0].preis);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Zum frostigen Hering
        Hering: 2.50
        Suppe: 4.50
        2 number
      richtig: true
      erklaerung: Richtig. parse baut das Objekt mit dem Array darin wieder auf, und die Preise sind echte Zahlen.
    - text: |-
        Zum frostigen Hering
        Hering: 2.50
        Suppe: 4.50
        2 string
      erklaerung: Zahlen ohne Anführungszeichen im JSON werden beim Lesen wieder Zahlen.
    - text: undefined
      erklaerung: JSON.parse macht aus dem Text ein richtiges Objekt, auf dessen Eigenschaften man zugreifen kann.
```

```merke
text: "`JSON.stringify(wert)` macht Text daraus, `JSON.stringify(wert, null, 2)` eingerückt. `JSON.parse(text)` baut den Wert wieder auf. In JSON stehen Namen und Texte immer in doppelten Anführungszeichen."
```

```frage
frageart: luecke
id: luecke-parse
text: Ergänze die Methode, die aus dem Text wieder ein Array macht.
code: |
  const zahlen = JSON.___("[3, 1, 4]");
  console.log(zahlen.length);
antworten: [["parse"]]
erklaerung: Richtig, parse liest den Text.
hinweis: Lesen im Sinn von zerlegen heißt auf Englisch...
```

## Was JSON kann und was nicht

JSON kennt nur Objekte, Arrays, Texte, Zahlen, true, false und null. Alles andere geht beim Schreiben verloren oder verändert sich: Funktionen und Eigenschaften mit undefined fallen weg, eine Map wird zu einem leeren Objekt, eine Klasse verliert ihren Namen. Praktisch ist dafür ein Trick: `JSON.parse(JSON.stringify(wert))` macht eine tiefe Kopie, auch aller verschachtelten Arrays und Objekte.

```beispiel
id: grenzen
code: |
  const kunde = { name: "Ole", gruss() { return "Moin"; }, notiz: undefined, karte: new Map([["Hering", 2]]) };
  console.log(JSON.stringify(kunde));
  const original = { name: "Ida", fische: ["Butt"] };
  const kopie = JSON.parse(JSON.stringify(original));
  kopie.fische.push("Aal");
  console.log(original.fische, kopie.fische);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        {"name":"Ole","karte":{}}
        [ 'Butt' ] [ 'Butt', 'Aal' ]
      richtig: true
      erklaerung: Richtig. Die Funktion und undefined fallen weg, die Map wird leer. Die Kopie ist ganz eigenständig, auch ihr Array.
    - text: |-
        {"name":"Ole","notiz":null,"karte":{"Hering":2}}
        [ 'Butt' ] [ 'Butt', 'Aal' ]
      erklaerung: undefined lässt stringify weg, und eine Map kennt JSON nicht, sie wird zu {}.
    - text: |-
        {"name":"Ole","karte":{}}
        [ 'Butt', 'Aal' ] [ 'Butt', 'Aal' ]
      erklaerung: Anders als ... kopiert der Umweg über JSON alle Ebenen, das Array der Kopie ist ein neues.
```

## Kaputtes JSON

JSON ist streng: Namen ohne Anführungszeichen, einfache Anführungszeichen oder ein Komma zu viel, und `JSON.parse` wirft einen `SyntaxError`. Wer Text von außen liest, packt parse darum in ein try.

```beispiel
id: kaputt
code: |
  const eingaben = ['{"name":"Pia"}', "{name: 'Pia'}", ""];
  for (const text of eingaben) {
    try {
      const daten = JSON.parse(text);
      console.log("Gelesen:", daten.name);
    } catch (fehler) {
      console.log("Unlesbar:", fehler.name);
    }
  }
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Gelesen: Pia
        Unlesbar: SyntaxError
        Unlesbar: SyntaxError
      richtig: true
      erklaerung: Richtig. Nur der erste Text ist gültiges JSON. Namen ohne doppelte Anführungszeichen und leerer Text scheitern.
    - text: |-
        Gelesen: Pia
        Gelesen: Pia
        Unlesbar: SyntaxError
      erklaerung: In JSON müssen Namen und Texte in doppelten Anführungszeichen stehen, sonst ist es kein JSON.
    - text: |-
        Gelesen: Pia
        Unlesbar: SyntaxError
        Gelesen: undefined
      erklaerung: Ein leerer Text ist kein JSON, auch er führt zu einem SyntaxError.
```

```falle
titel: JSON ist kein JavaScript
text: "JSON sieht aus wie ein JavaScript-Objekt, ist aber strenger: `{name: 'Pia'}` ist gültiges JavaScript und ungültiges JSON. Und ein JSON-Text ist ein Text, kein Objekt; vor dem Zugriff auf Eigenschaften muss parse kommen."
```

```frage
frageart: ordnen
id: ordnen-speichern
text: Bring die Zeilen in Reihenfolge, damit ein Spielstand gespeichert, wieder geladen und verändert wird.
zeilen:
  - 'const stand = { punkte: 10 };'
  - const gespeichert = JSON.stringify(stand);
  - const geladen = JSON.parse(gespeichert);
  - geladen.punkte += 5;
  - console.log(geladen.punkte, stand.punkte);
erklaerung: Richtig. Schreiben, lesen, ändern. Das geladene Objekt ist ein neues, das Original bleibt bei 10.
hinweis: Lesen kann man nur, was vorher geschrieben wurde.
```

```augenzwinkern
text: Pit hat seinen Lieblingsfisch mit JSON.stringify verschickt. Angekommen ist ein Text, der genau so aussieht wie der Fisch. Pia sagt, er schmeckt nach Anführungszeichen.
```
