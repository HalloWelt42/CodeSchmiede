---
id: js-umwandeln
sprache: javascript
titel: Eingaben und Umwandeln
kurz: Mit prompt nach Eingaben fragen, Text in Zahlen verwandeln und zurück, NaN erkennen, Beträge schön runden, null und undefined.
fuehrt_ein: [eingabe, umwandeln, typeof, nan, nachkommastellen, nichts]
lernziele:
  - mit prompt eine Eingabe lesen und wissen, dass sie immer Text ist
  - mit Number aus Text eine Zahl machen und mit String zurück
  - mit typeof nachsehen, was für ein Wert vor dir liegt
  - NaN erkennen und mit parseInt und parseFloat Zahlen aus Text fischen
  - Beträge mit toFixed auf feste Nachkommastellen bringen
  - null und undefined auseinanderhalten
karte: Ich frage nach und verwandle, was ich bekomme
bilder:
  - schluessel: karte_js_umwandeln
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin wirft Zettel in eine bunte Verwandlungsmaschine, unten purzeln Münzen heraus
---

## Fragen mit prompt

```alltag
text: Am Fischwagen fragt Pit jeden Kunden, wie viele Brötchen es sein dürfen. Die Antwort kommt als Zuruf, also als Wort. Bevor die Kasse damit rechnen kann, muss aus dem Wort "drei" die Zahl 3 werden. Genau diese Verwandlung braucht auch JavaScript.
zeichnung: verwandlung
```

`prompt("Frage")` fragt nach einer Eingabe und liefert sie als Text. Im Browser öffnet sich dafür ein kleines Fenster. Hier in der Konsole erscheint die Frage in der Ausgabe, und die Antwort kommt aus den vorbereiteten Eingaben über der Ausgabe. Die Antwort selbst siehst du in der Ausgabe nicht, die tippt man ja. Die Frage endet darum meist mit einem Leerzeichen.

```beispiel
id: frage
code: |
  const name = prompt("Wie heißt du? ");
  console.log(`Moin, ${name}!`);
eingabe: [Pia]
vorhersage:
  art: auswahl
  optionen:
    - text: Wie heißt du? Moin, Pia!
      richtig: true
      erklaerung: Richtig. Erst steht die Frage da, dann geht es in derselben Zeile weiter, denn prompt beginnt keine neue Zeile.
    - text: |-
        Wie heißt du? Pia
        Moin, Pia!
      erklaerung: Die Antwort tippt man ein, sie erscheint nicht in der Ausgabe.
    - text: Moin, Pia!
      erklaerung: Die Frage aus prompt steht auch in der Ausgabe, direkt vor allem, was danach kommt.
```

```frage
frageart: auswahl
id: prompt-typ
text: Jemand tippt bei `prompt("Wie viele? ")` die Antwort 3 ein. Was liefert prompt?
optionen:
  - text: Den Text "3"
    richtig: true
    erklaerung: Richtig. prompt liefert immer Text, egal was eingetippt wird.
  - text: Die Zahl 3
    erklaerung: Auch Ziffern kommen als Text an. Zur Zahl wird erst, was du umwandelst.
  - text: Nichts, Zahlen kann prompt nicht lesen
    erklaerung: Lesen kann prompt alles, aber eben immer als Text.
```

## Aus Text wird eine Zahl

Weil `prompt` Text liefert, klebt `+` die Antworten zusammen, statt zu rechnen. `Number(text)` verwandelt Text in eine Zahl. Was gerade vor dir liegt, verrät `typeof wert`: `"string"` für Text, `"number"` für Zahlen.

```beispiel
id: umwandeln
code: |
  const broetchen = prompt("Brötchen? ");
  const limonaden = prompt("Limonaden? ");
  console.log(broetchen + limonaden);
  console.log(typeof broetchen);
  const zahl = Number(broetchen);
  console.log(zahl + Number(limonaden));
  console.log(typeof zahl);
eingabe: ["3", "2"]
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Brötchen? Limonaden? 32
        string
        5
        number
      richtig: true
      erklaerung: Richtig. Als Text werden 3 und 2 zu 32 geklebt; erst nach Number wird gerechnet.
    - text: |-
        Brötchen? Limonaden? 5
        number
        5
        number
      erklaerung: prompt liefert Text, und Text plus Text wird geklebt, nicht gerechnet.
    - text: |-
        Brötchen? Limonaden? 32
        string
        32
        string
      erklaerung: Number macht aus dem Text "3" die Zahl 3, danach rechnet das Plus.
```

```merke
text: "`prompt(frage)` liefert immer Text. `Number(text)` macht daraus eine Zahl, `String(zahl)` macht aus einer Zahl Text. `typeof wert` sagt \"string\" oder \"number\"."
```

```frage
frageart: luecke
id: luecke-number
text: Ergänze, damit das Alter um eins erhöht wird, statt eine 1 anzukleben.
code: |
  const alter = ___(prompt("Alter? "));
  console.log(alter + 1);
antworten: [["Number"]]
erklaerung: Richtig. Erst Number, dann wird gerechnet.
hinweis: Gesucht ist die Verwandlung in eine Zahl, großgeschrieben.
```

## Wenn es keine Zahl ist

Nicht jeder Text ist eine Zahl. `Number("drei")` liefert `NaN`, die Abkürzung für "Not a Number", keine Zahl. Wer mit NaN weiterrechnet, bekommt wieder NaN. Ob etwas NaN ist, sagt `Number.isNaN(wert)`. Steht hinter der Zahl noch etwas, fischen `parseInt` (ganze Zahl) und `parseFloat` (Kommazahl) die Zahl vorne heraus.

```beispiel
id: keine-zahl
code: |
  console.log(Number("drei"));
  console.log(Number("drei") + 1);
  console.log(Number.isNaN(Number("drei")));
  console.log(parseInt("12 Fische"));
  console.log(parseFloat("2.5 kg Hering"));
  console.log(Number("2,5"));
vorhersage:
  art: eintippen
  erklaerung: "drei ist keine Zahl, also NaN, und NaN + 1 bleibt NaN. Number.isNaN bestätigt es mit true. parseInt nimmt die 12 vorne, parseFloat die 2.5. Und 2,5 mit Komma ist für JavaScript keine Zahl: NaN."
```

```falle
titel: Der leere Text ist null
text: "`Number(\"\")` ergibt 0, nicht NaN. Drückt jemand bei prompt nur Enter, rechnet das Programm also mit 0 weiter, ohne zu meckern. Und `NaN === NaN` ist falsch, NaN ist nicht einmal sich selbst gleich. Prüfe darum immer mit `Number.isNaN(...)`."
```

```frage
frageart: auswahl
id: parse-oder-number
text: Was ergibt `parseInt("4 Brötchen") + Number("4 Brötchen")`?
als_code: true
optionen:
  - text: NaN
    richtig: true
    erklaerung: Richtig. parseInt holt die 4, aber Number lehnt den ganzen Text ab und liefert NaN. Und 4 + NaN ist NaN.
  - text: '8'
    erklaerung: Number ist strenger als parseInt; mit Text hinter der Zahl gibt es NaN.
  - text: '4'
    erklaerung: Mit NaN gerechnet bleibt alles NaN, auch 4 + NaN.
```

## Beträge schön runden

Geld hat zwei Stellen hinter dem Komma. JavaScript lässt Nullen am Ende aber weg und zeigt 7.5 statt 7.50. `zahl.toFixed(2)` liefert einen Text mit genau zwei Nachkommastellen, gerundet. Weil das Ergebnis Text ist, rechnest du vorher fertig und rundest erst zum Anzeigen.

```beispiel
id: zwei-stellen
code: |
  const summe = 3 * 2.5;
  console.log(summe);
  console.log(summe.toFixed(2));
  console.log((10 / 3).toFixed(2));
  console.log(typeof summe.toFixed(2));
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        7.5
        7.50
        3.33
        string
      richtig: true
      erklaerung: Richtig. toFixed(2) füllt mit Nullen auf oder rundet, und das Ergebnis ist Text.
    - text: |-
        7.50
        7.50
        3.33
        number
      erklaerung: Ohne toFixed zeigt JavaScript 7.5. Und toFixed liefert Text, keine Zahl.
    - text: |-
        7.5
        7.50
        3.3333333333333335
        string
      erklaerung: toFixed(2) schneidet nach zwei Stellen ab und rundet.
```

```frage
frageart: ordnen
id: ordnen-preis
text: Bring die Zeilen in Reihenfolge, damit für die eingegebene Zahl Brötchen zu 2.5 der Preis mit zwei Stellen erscheint.
zeilen:
  - const eingabe = prompt("Wie viele? ");
  - const anzahl = Number(eingabe);
  - const preis = anzahl * 2.5;
  - "console.log(`Preis: ${preis.toFixed(2)} Euro`);"
erklaerung: Richtig. Fragen, umwandeln, rechnen, schön ausgeben.
hinweis: Erst die Eingabe, ganz am Ende die Ausgabe.
```

## null und undefined

JavaScript hat zwei Werte für "nichts". `undefined` heißt nicht festgelegt: So ist ein Name, der noch keinen Wert bekommen hat, oder ein Index hinter dem Ende eines Textes. `null` heißt absichtlich leer: Diesen Wert setzt man selbst, und `prompt` liefert ihn, wenn keine Antwort kommt, im Browser etwa beim Abbrechen.

```beispiel
id: nichts
code: |
  let notiz;
  console.log(notiz);
  notiz = null;
  console.log(notiz);
  const antwort = prompt("Noch ein Brötchen? ");
  console.log(antwort);
  console.log(typeof undefined, typeof null);
vorhersage:
  art: auswahl
  frage: Für dieses Beispiel gibt es keine vorbereitete Eingabe. Was erscheint?
  optionen:
    - text: |-
        undefined
        null
        Noch ein Brötchen? null
        undefined object
      richtig: true
      erklaerung: Richtig. Ohne Antwort liefert prompt null. Dass typeof null "object" sagt, ist ein alter Fehler aus den ersten Tagen von JavaScript, der nie repariert wurde, weil sonst zu viele Webseiten kaputtgingen.
    - text: |-
        undefined
        undefined
        Noch ein Brötchen? undefined
        undefined undefined
      erklaerung: Ab Zeile 3 steht null in notiz, gesetzt mit Absicht. Und prompt liefert ohne Antwort null.
    - text: |-
        null
        null
        Noch ein Brötchen? null
        null null
      erklaerung: Ein Name ohne Wert ist undefined, nicht null; null setzt man selbst.
```

```merke
text: "`undefined`: noch nicht festgelegt. `null`: absichtlich leer. prompt liefert `null`, wenn keine Antwort kommt."
```

```augenzwinkern
text: Pit hat einmal "zwölf" in die Kasse getippt. Die Kasse sagte NaN, und Pit dachte, das sei eine neue Fischsorte.
```
