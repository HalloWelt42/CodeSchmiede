---
id: js-funktionen
sprache: javascript
titel: Eigene Funktionen
kurz: Code mit function unter einem Namen ablegen, mit Parametern füttern, mit return ein Ergebnis zurückgeben, Standardwerte setzen.
fuehrt_ein: [funktion, return, standardwert]
lernziele:
  - mit function eine eigene Funktion anlegen und aufrufen
  - Parameter übergeben und mit return ein Ergebnis zurückgeben
  - wissen, dass eine Funktion ohne return undefined liefert und return sofort beendet
  - Standardwerte für fehlende Parameter setzen
  - Funktionen aus Funktionen aufrufen und eine Funktion als Wert in einen Namen legen
karte: Ich baue mir eigene Befehle
bilder:
  - schluessel: karte_js_funktionen
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin wirft Zutaten oben in einen kleinen Automaten, unten kommt ein fertiges Fischbrötchen heraus
---

## Ein Automat für Fischbrötchen

```alltag
text: Pit hat sich einen Automaten gebaut. Oben wirft er Fisch und Brötchen hinein, drückt auf den Knopf, und unten fällt ein fertiges Fischbrötchen heraus. Wie der Automat innen arbeitet, muss er nicht jedes Mal neu erklären. Eine Funktion ist so ein Automat für Code.
zeichnung: automat
```

`function name(parameter) { ... }` legt eine Funktion an. Dabei passiert noch nichts, sie wird nur gebaut. Erst ein Aufruf `name(wert)` lässt den Block laufen; der Wert landet dabei im Parameter. Eine Funktion lässt sich beliebig oft aufrufen, mit immer neuen Werten. Spiel das Beispiel ab: Bei jedem Aufruf erscheint ein eigener Rahmen im Speicher.

```beispiel
id: begruessen
code: |
  function begruessen(name) {
    console.log(`Moin, ${name}!`);
  }
  begruessen("Pia");
  begruessen("Ole");
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Moin, Pia!
        Moin, Ole!
      richtig: true
      erklaerung: Richtig. Die Funktion wird gebaut und dann zweimal aufgerufen, jedes Mal mit einem anderen Namen.
    - text: |-
        Moin, name!
        Moin, name!
      erklaerung: name ist ein Parameter, er steht für den Wert, der beim Aufruf übergeben wird.
    - text: |-
        Moin, undefined!
        Moin, Pia!
        Moin, Ole!
      erklaerung: Beim Anlegen läuft der Block noch nicht. Ausgegeben wird nur bei den Aufrufen.
```

```frage
frageart: auswahl
id: wann-laeuft
text: Wann läuft der Code im Block einer Funktion?
optionen:
  - text: Jedes Mal, wenn die Funktion aufgerufen wird
    richtig: true
    erklaerung: Richtig. Das Anlegen baut nur den Automaten, der Aufruf drückt auf den Knopf.
  - text: Einmal, sobald JavaScript die Zeile mit function erreicht
    erklaerung: function legt die Funktion nur an. Laufen tut sie erst beim Aufruf.
  - text: Nur, wenn sie ein return hat
    erklaerung: Auch ohne return läuft der Block, sobald man die Funktion aufruft.
```

## Etwas zurückgeben mit return

Viele Funktionen sollen etwas ausrechnen und das Ergebnis liefern, statt es selbst auszugeben. Dafür gibt es `return wert;`: Die Funktion endet sofort, und der Aufruf steht dann für diesen Wert. Ohne return liefert eine Funktion `undefined`. Mehrere Parameter trennst du mit Kommas.

```beispiel
id: preis
code: |
  function preis(anzahl, einzelpreis) {
    const summe = anzahl * einzelpreis;
    return summe;
  }
  const broetchen = preis(3, 2.5);
  const limo = preis(2, 1.75);
  console.log(broetchen + limo);
  console.log(preis(1, 4.5).toFixed(2));
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        11
        4.50
      richtig: true
      erklaerung: Richtig. Die Aufrufe liefern 7.5 und 3.5, zusammen 11. Und auf das Ergebnis eines Aufrufs lässt sich direkt toFixed anwenden.
    - text: |-
        7.53.5
        4.50
      erklaerung: preis liefert Zahlen, keine Texte; das Plus rechnet.
    - text: |-
        undefined
        4.50
      erklaerung: Mit return liefert die Funktion ihr Ergebnis, das in broetchen und limo landet.
```

```falle
titel: Nach return ist Schluss
text: "Code hinter einem `return` im selben Block läuft nie, die Funktion ist da schon zu Ende. Und ein `console.log` in der Funktion ist kein return: Es zeigt den Wert nur an, der Aufruf liefert trotzdem undefined."
```

```frage
frageart: fehlerstelle
id: fehler-return
text: 'Die Funktion soll das Doppelte liefern, aber es erscheint `Doppelt: undefined`. Welche Zeile ist schuld?'
code: |
  function doppelt(x) {
    console.log(x * 2);
  }
  const ergebnis = doppelt(21);
  console.log("Doppelt:", ergebnis);
zeile: 2
erklaerung: Genau. Die Funktion gibt das Ergebnis nur aus, statt es mit return zurückzugeben. Darum liefert sie undefined.
hinweis: Welche Zeile müsste ein return sein?
```

## Standardwerte

Ruft man eine Funktion mit weniger Werten auf, als sie Parameter hat, sind die übrigen `undefined`. Ein Standardwert hilft: `function gruss(name = "Gast")` nimmt Gast, wenn kein Name übergeben wird.

```beispiel
id: standard
code: |
  function bon(kunde = "Gast", trinkgeld = 0) {
    return `Bon für ${kunde}, Trinkgeld ${trinkgeld} Euro`;
  }
  console.log(bon("Pia", 2));
  console.log(bon("Ole"));
  console.log(bon());
vorhersage:
  art: eintippen
  erklaerung: "Pia gibt 2 Euro. Bei Ole fehlt das Trinkgeld, es wird 0. Ohne jeden Wert springen beide Standardwerte ein."
```

```merke
text: "`function name(a, b = 0) { ... return wert; }` legt eine Funktion an. Aufrufen mit `name(1, 2)`. return liefert ein Ergebnis und beendet die Funktion; ohne return ist es undefined. Fehlende Werte nehmen den Standardwert."
```

```frage
frageart: luecke
id: luecke-return
text: Ergänze, damit die Funktion das Quadrat liefert.
code: |
  function quadrat(x) {
    ___ x * x;
  }
  console.log(quadrat(7));
antworten: [["return"]]
erklaerung: Richtig, return liefert das Ergebnis.
hinweis: Zurückgeben heißt auf Englisch...
```

## Funktionen im Team

Funktionen können andere Funktionen aufrufen; so baut man aus kleinen Teilen größere. Mit `function` angelegte Funktionen kennt JavaScript schon vor ihrer Zeile, man darf sie also weiter oben aufrufen. Eine Funktion ist außerdem ein ganz normaler Wert: `const quadrat = function (x) { return x * x; };` legt sie in einen Namen, wie eine Zahl.

```beispiel
id: team
code: |
  console.log(bon(3));
  function euro(betrag) {
    return `${betrag.toFixed(2)} Euro`;
  }
  function bon(broetchen) {
    return `${broetchen} Brötchen: ${euro(broetchen * 2.5)}`;
  }
  const verdoppeln = function (x) {
    return x * 2;
  };
  console.log(bon(verdoppeln(2)));
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        3 Brötchen: 7.50 Euro
        4 Brötchen: 10.00 Euro
      richtig: true
      erklaerung: Richtig. bon darf schon in Zeile 1 aufgerufen werden und benutzt euro. Unten wird erst verdoppelt, dann der Bon gebaut.
    - text: Fehler, bon ist in Zeile 1 noch nicht bekannt
      erklaerung: Mit function angelegte Funktionen kennt JavaScript von Anfang an.
    - text: |-
        3 Brötchen: 7.5 Euro
        4 Brötchen: 10 Euro
      erklaerung: euro rundet mit toFixed(2) auf zwei Stellen.
```

```frage
frageart: ordnen
id: ordnen-funktion
text: Bring die Zeilen in Reihenfolge, damit eine Funktion den größeren von zwei Werten liefert und ausgegeben wird.
zeilen:
  - function groesser(a, b) {
  - '  if (a > b) {'
  - '    return a;'
  - '  }'
  - '  return b;'
  - '}'
  - console.log(groesser(4, 9));
erklaerung: Richtig. Ist a größer, endet die Funktion mit a, sonst geht es weiter zu return b.
hinweis: Der Aufruf kommt nach der schließenden Klammer der Funktion.
```

```augenzwinkern
text: Pit hat eine Funktion pinguinMachen() geschrieben. Sie gibt undefined zurück. Er sagt, das sei ein sehr schüchterner Pinguin.
```
