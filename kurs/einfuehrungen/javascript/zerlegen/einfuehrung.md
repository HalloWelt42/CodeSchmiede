---
id: js-zerlegen
sprache: javascript
titel: Auspacken und verteilen
kurz: Arrays und Objekte in einzelne Namen auspacken, mit ... kopieren, verteilen und einsammeln, mit ?. und ?? vorsichtig zugreifen.
fuehrt_ein: [destrukturierung, spread, optional]
lernziele:
  - Werte aus Arrays und Objekten in einem Schritt in Namen auspacken
  - beim Auspacken umbenennen, Standardwerte setzen und Objekte als Parameter auspacken
  - mit ... Arrays und Objekte kopieren und zusammenführen und Werte als einzelne Argumente verteilen
  - mit ...rest beliebig viele Werte einsammeln
  - mit ?. ohne Absturz in fehlende Objekte greifen und mit ?? nur bei null und undefined einen Ersatz nehmen
karte: Ich packe aus und verteile
bilder:
  - schluessel: karte_js_zerlegen
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin packt eine Kiste aus und legt jedes Teil auf ein eigenes beschriftetes Feld am Boden
---

## Arrays auspacken

```alltag
text: Die Lieferung kommt in einer Kiste. Statt jedes Mal hineinzugreifen und zu suchen, packt Pit sie einmal aus und legt jedes Teil an seinen Platz, den Hering ins Kühlfach, die Brötchen in den Korb. Auspacken in JavaScript ist genau das, nur in einer Zeile.
zeichnung: auspacken
```

`const [erster, zweiter] = array;` legt zwei Namen an und gibt ihnen die ersten beiden Werte, der Reihe nach. Mit `...rest` am Ende sammelst du den ganzen Rest in ein neues Array. Und weil rechts ein Array stehen darf, das gerade erst entsteht, tauschen zwei Namen ohne Hilfsvariable: `[a, b] = [b, a];`.

```beispiel
id: array
code: |
  const zeile = "Pia;3;Hering;Zwiebeln";
  const [kunde, anzahl, ...extras] = zeile.split(";");
  console.log(kunde, Number(anzahl) + 1, extras);
  let vorne = "Ole";
  let hinten = "Ida";
  [vorne, hinten] = [hinten, vorne];
  console.log(vorne, hinten);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Pia 4 [ 'Hering', 'Zwiebeln' ]
        Ida Ole
      richtig: true
      erklaerung: Richtig. kunde und anzahl bekommen die ersten beiden Teile, extras den Rest als Array. Danach tauschen vorne und hinten.
    - text: |-
        Pia 4 Hering
        Ida Ole
      erklaerung: "...extras sammelt alle übrigen Werte in ein Array, nicht nur den nächsten."
    - text: |-
        Pia 31 [ 'Hering', 'Zwiebeln' ]
        Ida Ole
      erklaerung: Number(anzahl) macht aus dem Text eine Zahl, dann wird gerechnet.
```

```frage
frageart: luecke
id: luecke-array
text: Ergänze, damit x und y die beiden Zahlen bekommen.
code: |
  const punkt = [3, 7];
  const ___ = punkt;
  console.log(x + y);
antworten: [["[x, y]", "[x,y]"]]
erklaerung: Richtig, eckige Klammern links packen ein Array aus.
hinweis: Links stehen die neuen Namen in der Form eines Arrays.
```

## Objekte auspacken

Bei Objekten gehen die Namen nach den Eigenschaften, nicht nach der Reihenfolge: `const { name, preis } = gericht;`. Mit `{ name: titel }` heißt der neue Name anders, und `{ scharf = false }` setzt einen Standardwert, falls die Eigenschaft fehlt. Besonders praktisch ist das bei Parametern: Eine Funktion, die ein Objekt bekommt, packt sich gleich aus, was sie braucht.

```beispiel
id: objekt
code: |
  const gericht = { name: "Fischsuppe", preis: 4.5 };
  const { name, preis, scharf = false } = gericht;
  console.log(name, preis, scharf);
  function zeile({ name: titel, preis }, anzahl = 1) {
    return `${anzahl} x ${titel}: ${(anzahl * preis).toFixed(2)}`;
  }
  console.log(zeile(gericht, 2));
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Fischsuppe 4.5 false
        2 x Fischsuppe: 9.00
      richtig: true
      erklaerung: Richtig. scharf fehlt im Objekt, also gilt der Standardwert. Die Funktion packt name als titel und preis aus.
    - text: |-
        Fischsuppe 4.5 undefined
        2 x Fischsuppe: 9.00
      erklaerung: "= false setzt einen Standardwert für die fehlende Eigenschaft."
    - text: |-
        Fischsuppe 4.5 false
        2 x undefined: 9.00
      erklaerung: "name: titel heißt, die Eigenschaft name kommt in den Namen titel."
```

```merke
text: "`const [a, b, ...rest] = array;` packt nach Reihenfolge aus, `const { name, preis = 0 } = objekt;` nach Eigenschaften. Auch Parameter lassen sich so auspacken."
```

## Kopieren und verteilen mit ...

Die drei Punkte haben noch eine zweite Aufgabe: In einem neuen Array oder Objekt verteilen sie den Inhalt eines anderen. `[...alt, neu]` ist eine Kopie mit einem Wert mehr, `{ ...alt, preis: 5 }` eine Kopie mit geändertem Preis; das Original bleibt jeweils unberührt. Beim Aufruf verteilt `Math.max(...zahlen)` ein Array auf einzelne Argumente. Und als letzter Parameter sammelt `...werte` beliebig viele Argumente ein.

```beispiel
id: verteilen
code: |
  const karte = ["Hering", "Aal"];
  const neueKarte = [...karte, "Suppe"];
  console.log(karte.length, neueKarte.length);
  const suppe = { name: "Suppe", preis: 4.5 };
  const teurer = { ...suppe, preis: 5 };
  console.log(suppe.preis, teurer.preis);
  console.log(Math.max(...[3, 9, 2]));
  function summe(...werte) {
    return werte.reduce((s, w) => s + w, 0);
  }
  console.log(summe(1, 2, 3), summe());
vorhersage:
  art: eintippen
  erklaerung: "Die Kopien wachsen oder ändern sich, die Originale nicht: 2 und 3, 4.5 und 5. Math.max bekommt drei einzelne Zahlen und liefert 9. summe sammelt alle Argumente ein, ohne Argumente ist es ein leeres Array mit Summe 0."
```

```falle
titel: Kopie nur eine Ebene tief
text: "`{ ...kunde }` kopiert nur die erste Ebene. Steckt in kunde ein Array, etwa `bestellungen`, zeigen Original und Kopie auf dasselbe Array. Ein push über die Kopie landet dann auch im Original."
```

## Vorsichtig zugreifen mit ?. und ??

`kunde.adresse.ort` bricht ab, wenn adresse null oder undefined ist. `kunde.adresse?.ort` liefert in diesem Fall einfach undefined. `a ?? b` liefert a, außer a ist null oder undefined, dann b. Anders als `||` lässt `??` die 0 und den leeren Text in Ruhe, und genau das will man oft bei Zahlen.

```beispiel
id: vorsichtig
code: |
  const pia = { name: "Pia", adresse: { ort: "Eishafen" }, stempel: 0 };
  const ole = { name: "Ole", adresse: null };
  console.log(pia.adresse?.ort, ole.adresse?.ort);
  console.log(pia.stempel || 5, pia.stempel ?? 5);
  console.log(ole.stempel ?? "keine Karte");
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Eishafen undefined
        5 0
        keine Karte
      richtig: true
      erklaerung: Richtig. Bei Ole hält ?. an der leeren Adresse an. || ersetzt auch die 0, ?? nur null und undefined.
    - text: |-
        Eishafen undefined
        0 0
        keine Karte
      erklaerung: "|| nimmt den rechten Wert, sobald links etwas Falsches steht, und 0 gilt als falsch."
    - text: Fehler, ole.adresse ist null
      erklaerung: Genau davor schützt ?.; ohne das Fragezeichen gäbe es einen TypeError.
```

```frage
frageart: ordnen
id: ordnen-kopie
text: Bring die Zeilen in Reihenfolge, damit eine geänderte Kopie entsteht und beide Preise ausgegeben werden.
zeilen:
  - 'const original = { name: "Hering", preis: 2.5 };'
  - 'const angebot = { ...original, preis: 2 };'
  - 'const { preis: alt } = original;'
  - console.log(alt, angebot.preis);
erklaerung: Richtig. Erst das Original, dann die Kopie mit neuem Preis, dann der alte Preis ausgepackt.
hinweis: Aus dem Original wird kopiert und ausgepackt, also kommt es zuerst.
```

```augenzwinkern
text: Pit hat einmal versucht, mit ... einen Fisch zu verteilen. Jetzt hat jeder Gast ein Stück, und der Fisch ist ein leeres Array.
```
