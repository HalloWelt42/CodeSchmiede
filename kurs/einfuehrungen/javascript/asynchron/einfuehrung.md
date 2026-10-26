---
id: js-asynchron
sprache: javascript
titel: Später und gleichzeitig
kurz: Mit setTimeout etwas später erledigen, mit Promise ein Ergebnis versprechen, mit async und await darauf warten und mit Promise.all mehreres gleichzeitig laufen lassen.
fuehrt_ein: [zeitgeber, promise, async]
lernziele:
  - mit setTimeout und setInterval etwas später oder wiederholt ausführen
  - verstehen, dass Rückrufe erst laufen, wenn der übrige Code fertig ist
  - mit new Promise ein Ergebnis versprechen und mit then darauf reagieren
  - mit async und await lesbar auf Ergebnisse warten und Fehler mit try und catch abfangen
  - mit Promise.all auf mehrere Versprechen zugleich warten
karte: Ich warte, ohne stehen zu bleiben
bilder:
  - schluessel: karte_js_asynchron
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin sitzt entspannt auf einer Bank und hält einen blinkenden Abholpieper, im Hintergrund dampft die Küche des Fischwagens
---

## Etwas später

```alltag
text: Wer am Fischwagen eine Suppe bestellt, bekommt einen Pieper und setzt sich. Pit bedient in der Zwischenzeit die nächsten Kunden. Wenn die Suppe fertig ist, piept es, und der Kunde holt sie ab. Niemand steht herum und wartet. Genau so wartet JavaScript.
zeichnung: pieper
```

`setTimeout(funktion, ms)` gibt eine Funktion zum späteren Ausführen ab: frühestens nach ms Millisekunden. Das Programm wartet dabei nicht, es macht sofort weiter. Erst wenn der ganze übrige Code durchgelaufen ist und die Zeit um ist, kommt der Rückruf dran, sogar bei 0 Millisekunden. `setInterval(funktion, ms)` ruft immer wieder auf, bis `clearInterval` es stoppt.

```beispiel
id: spaeter
code: |
  console.log("Bestellung aufgenommen");
  setTimeout(() => console.log("Piep! Suppe ist fertig"), 30);
  setTimeout(() => console.log("Piep! Limonade ist fertig"), 0);
  console.log("Nächster Kunde, bitte");
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Bestellung aufgenommen
        Nächster Kunde, bitte
        Piep! Limonade ist fertig
        Piep! Suppe ist fertig
      richtig: true
      erklaerung: Richtig. Erst läuft alles von oben nach unten, die Rückrufe warten. Dann kommt zuerst die Limonade, ihre Zeit ist zuerst um.
    - text: |-
        Bestellung aufgenommen
        Piep! Limonade ist fertig
        Nächster Kunde, bitte
        Piep! Suppe ist fertig
      erklaerung: Auch bei 0 Millisekunden wartet der Rückruf, bis der übrige Code fertig ist.
    - text: |-
        Bestellung aufgenommen
        Piep! Suppe ist fertig
        Piep! Limonade ist fertig
        Nächster Kunde, bitte
      erklaerung: setTimeout hält das Programm nicht an. Es gibt nur einen Auftrag für später ab.
```

```frage
frageart: auswahl
id: wartet-es
text: Hält `setTimeout(f, 1000)` das Programm eine Sekunde lang an?
optionen:
  - text: Nein, es macht sofort weiter, und f kommt frühestens nach einer Sekunde dran.
    richtig: true
    erklaerung: Richtig, wie beim Pieper. Gewartet wird im Hintergrund.
  - text: Ja, eine Sekunde lang passiert gar nichts.
    erklaerung: Genau das tut setTimeout nicht, darum ist es so nützlich.
  - text: Ja, aber nur, wenn f etwas ausgibt.
    erklaerung: Ob f etwas ausgibt, spielt keine Rolle. Das Programm läuft immer weiter.
```

## Versprechen mit Promise

Ein Promise ist ein Versprechen auf ein Ergebnis, das noch nicht da ist, wie der Pieper. Man baut es mit `new Promise((erfuellen, ablehnen) => { ... })`: Irgendwann ruft der Code darin `erfuellen(wert)` auf, oder `ablehnen(fehler)`, wenn etwas schiefging. Mit `.then(wert => ...)` sagt man, was danach passieren soll, mit `.catch(fehler => ...)`, was bei einem Fehler passiert.

```beispiel
id: versprechen
code: |
  function kochen(gericht, ms) {
    return new Promise((erfuellen, ablehnen) => {
      setTimeout(() => {
        if (gericht === "Eis") {
          ablehnen(new Error("Eis kocht man nicht"));
        } else {
          erfuellen(`${gericht} ist fertig`);
        }
      }, ms);
    });
  }
  kochen("Suppe", 20).then((text) => console.log(text));
  kochen("Eis", 10).catch((fehler) => console.log("Oh nein:", fehler.message));
  console.log("Töpfe stehen auf dem Herd");
vorhersage:
  art: eintippen
  erklaerung: "Zuerst läuft der ganze übrige Code, darum stehen die Töpfe zuerst auf dem Herd. Nach 10 Millisekunden lehnt das Eis ab, nach 20 ist die Suppe fertig."
```

```merke
text: "`setTimeout(f, ms)` ruft f später auf, das Programm läuft weiter. `new Promise((erfuellen, ablehnen) => ...)` verspricht ein Ergebnis; `.then(...)` reagiert darauf, `.catch(...)` auf Fehler."
```

## Warten mit async und await

Viele then hintereinander werden schnell unübersichtlich. Lesbarer geht es mit `async` und `await`: In einer Funktion, vor der `async` steht, wartet `await versprechen` auf das Ergebnis und liefert es wie einen normalen Wert. Nur diese eine Funktion pausiert, das übrige Programm läuft weiter. Fehler fängt man wie gewohnt mit try und catch. Eine async-Funktion liefert selbst immer ein Promise.

```beispiel
id: warten
code: |
  const warte = (ms) => new Promise((erfuellen) => setTimeout(erfuellen, ms));
  async function bestellung(kunde) {
    console.log(`${kunde} bestellt`);
    await warte(20);
    console.log(`${kunde} bekommt die Suppe`);
    return kunde.length;
  }
  async function hauptprogramm() {
    const zahl = await bestellung("Pia");
    console.log("Zurück kam", zahl);
  }
  hauptprogramm();
  console.log("Pit wischt die Theke");
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Pia bestellt
        Pit wischt die Theke
        Pia bekommt die Suppe
        Zurück kam 3
      richtig: true
      erklaerung: Richtig. Bis zum ersten await läuft bestellung sofort. Dann pausiert sie, und Pit wischt. Nach 20 Millisekunden geht es weiter.
    - text: |-
        Pit wischt die Theke
        Pia bestellt
        Pia bekommt die Suppe
        Zurück kam 3
      erklaerung: Der Aufruf von hauptprogramm läuft zuerst bis zum ersten await, und das kommt erst nach Pia bestellt.
    - text: |-
        Pia bestellt
        Pia bekommt die Suppe
        Zurück kam 3
        Pit wischt die Theke
      erklaerung: await pausiert nur die Funktion, nicht das ganze Programm. Pit wischt in der Zwischenzeit.
```

```frage
frageart: luecke
id: luecke-await
text: Ergänze das Wort, das auf das Ergebnis wartet.
code: |
  async function laden() {
    const text = ___ warte(10);
    return text;
  }
antworten: [["await"]]
erklaerung: Richtig, await wartet in einer async-Funktion.
hinweis: Warten heißt auf Englisch...
```

## Mehreres gleichzeitig

Muss man auf mehrere Versprechen warten, geht es nacheinander (jedes await wartet, bevor das nächste startet) oder gleichzeitig: `await Promise.all([a, b, c])` startet alle zugleich und liefert ein Array der Ergebnisse, in derselben Reihenfolge wie die Versprechen, egal welches zuerst fertig war. Schlägt eines fehl, landet sein Fehler im catch.

```beispiel
id: alle
code: |
  const kochen = (gericht, ms) =>
    new Promise((erfuellen) =>
      setTimeout(() => {
        console.log(`fertig: ${gericht}`);
        erfuellen(gericht);
      }, ms)
    );
  async function kueche() {
    const teller = await Promise.all([kochen("Suppe", 30), kochen("Brötchen", 10), kochen("Limonade", 5)]);
    console.log("Alles da:", teller.join(", "));
  }
  kueche();
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        fertig: Limonade
        fertig: Brötchen
        fertig: Suppe
        Alles da: Suppe, Brötchen, Limonade
      richtig: true
      erklaerung: Richtig. Alle kochen gleichzeitig, das schnellste ist zuerst fertig. Das Ergebnis behält aber die Reihenfolge der Bestellung.
    - text: |-
        fertig: Suppe
        fertig: Brötchen
        fertig: Limonade
        Alles da: Suppe, Brötchen, Limonade
      erklaerung: Promise.all startet alle zugleich, darum kommt das schnellste Gericht zuerst.
    - text: |-
        fertig: Limonade
        fertig: Brötchen
        fertig: Suppe
        Alles da: Limonade, Brötchen, Suppe
      erklaerung: Das Array der Ergebnisse folgt der Reihenfolge im Aufruf, nicht der Reihenfolge des Fertigwerdens.
```

```falle
titel: await vergessen
text: "Ohne await liefert eine async-Funktion kein Ergebnis, sondern ein Promise: `const zahl = bestellung(\"Pia\");` und dann `console.log(zahl)` zeigt `Promise { <pending> }`, ein Versprechen in Arbeit. Und await geht nur in einer async-Funktion."
```

```frage
frageart: ordnen
id: ordnen-async
text: Bring die Zeilen in Reihenfolge, damit erst gewartet und dann Fertig ausgegeben wird.
zeilen:
  - const warte = (ms) => new Promise((erfuellen) => setTimeout(erfuellen, ms));
  - async function los() {
  - '  await warte(10);'
  - '  console.log("Fertig");'
  - '}'
  - los();
erklaerung: Richtig. Erst die Wartefunktion, dann die async-Funktion mit await, dann der Aufruf.
hinweis: Aufgerufen wird ganz am Ende.
```

```augenzwinkern
text: Pit hat seinen Kunden einmal statt eines Piepers ein Promise in die Hand gedrückt. Sie haben bis heute nicht erfahren, ob es erfüllt oder abgelehnt wurde.
```
