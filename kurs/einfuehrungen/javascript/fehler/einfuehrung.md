---
id: js-fehler
sprache: javascript
titel: Fehler abfangen
kurz: Fehler mit try und catch auffangen, mit throw selbst Fehler werfen, mit finally aufräumen und die wichtigsten Fehlerarten kennen.
fuehrt_ein: [try, throw, fehlerarten]
lernziele:
  - mit try und catch einen Fehler auffangen, statt abzubrechen
  - name und message eines Fehlers auslesen
  - mit throw new Error(...) selbst einen Fehler werfen, wenn ein Wert nicht passt
  - mit finally Code ausführen, der immer laufen soll
  - TypeError, ReferenceError und RangeError unterscheiden und nur fangen, was man behandeln kann
karte: Ich falle nicht, ich werde aufgefangen
bilder:
  - schluessel: karte_js_fehler
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin springt vom Steg und landet sicher in einem rot-weißen Rettungsring, den ein zweiter Pinguin hält
---

## Auffangen statt abstürzen

```alltag
text: Pit springt gern vom Steg, auch wenn er nicht weiß, wie tief das Wasser ist. Darum hält Pia einen Rettungsring bereit. Geht alles gut, braucht ihn keiner. Geht etwas schief, landet Pit im Ring statt auf dem Grund. try ist der Sprung, catch der Rettungsring.
zeichnung: rettungsring
```

Bisher hat jeder Fehler das Programm abgebrochen. Mit `try { ... } catch (fehler) { ... }` geht es weiter: JavaScript führt den try-Block aus. Tritt darin ein Fehler auf, springt es sofort in den catch-Block und gibt ihm den Fehler mit. Danach läuft das Programm normal weiter. Ein Fehler ist ein Objekt mit `name` (der Art) und `message` (der Beschreibung).

```beispiel
id: auffangen
code: |
  const kunde = null;
  try {
    console.log("Moin,", kunde.toUpperCase());
    console.log("Diese Zeile kommt nie");
  } catch (fehler) {
    console.log("Aufgefangen:", fehler.name);
  }
  console.log("Weiter geht's");
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Aufgefangen: TypeError
        Weiter geht's
      richtig: true
      erklaerung: Richtig. kunde ist null, das toUpperCase scheitert, der Rest des try-Blocks wird übersprungen, und catch übernimmt.
    - text: |-
        Moin, null
        Diese Zeile kommt nie
        Weiter geht's
      erklaerung: null hat kein toUpperCase, darum gibt es einen Fehler, bevor etwas ausgegeben wird.
    - text: TypeError
      erklaerung: Der Fehler wird aufgefangen, darum bricht das Programm nicht ab und macht danach weiter.
```

```frage
frageart: auswahl
id: was-passiert
text: Was passiert mit den Zeilen im try-Block hinter der Zeile, die den Fehler auslöst?
optionen:
  - text: Sie werden übersprungen, es geht direkt im catch-Block weiter.
    richtig: true
    erklaerung: Richtig, der try-Block wird an der Fehlerstelle verlassen.
  - text: Sie laufen nach dem catch-Block weiter.
    erklaerung: Nach dem catch geht es hinter dem ganzen try ... catch weiter, nicht im try.
  - text: Sie laufen trotzdem, nur ohne Ausgabe.
    erklaerung: Ab der Fehlerstelle läuft im try-Block nichts mehr.
```

## Selbst Fehler werfen

Manchmal ist für JavaScript alles in Ordnung, für dein Programm aber nicht, etwa eine negative Anzahl Brötchen. Dann wirfst du selbst einen Fehler: `throw new Error("Beschreibung");`. Die Funktion endet sofort, und der Fehler fliegt zum nächsten catch, der ihn auffängt, auch über mehrere Aufrufe hinweg.

```beispiel
id: werfen
code: |
  function liesAnzahl(text) {
    const zahl = Number(text);
    if (Number.isNaN(zahl)) {
      throw new Error(`"${text}" ist keine Zahl`);
    }
    if (zahl < 0) {
      throw new RangeError(`${zahl} ist weniger als nichts`);
    }
    return zahl;
  }
  for (const eingabe of ["3", "drei", "-2"]) {
    try {
      console.log("Anzahl:", liesAnzahl(eingabe));
    } catch (fehler) {
      console.log(`${fehler.name}: ${fehler.message}`);
    }
  }
vorhersage:
  art: eintippen
  erklaerung: "3 geht gut. drei ist NaN, also fliegt ein Error. -2 ist eine Zahl, aber kleiner als 0, also ein RangeError. Jeder Fehler wird in der Schleife aufgefangen, darum kommen alle drei Eingaben dran."
```

```merke
text: "`try { ... } catch (fehler) { ... }` fängt Fehler auf; `fehler.name` und `fehler.message` sagen, was los war. `throw new Error(\"...\")` wirft selbst einen Fehler, die Funktion endet sofort."
```

```frage
frageart: luecke
id: luecke-throw
text: Ergänze das Wort, das einen Fehler auslöst.
code: |
  function teilen(a, b) {
    if (b === 0) {
      ___ new Error("Teilen durch null");
    }
    return a / b;
  }
antworten: [["throw"]]
erklaerung: Richtig, throw wirft den Fehler.
hinweis: Werfen heißt auf Englisch...
```

## Aufräumen mit finally

Hinter catch darf noch `finally { ... }` stehen. Dieser Block läuft immer: wenn alles gut ging, wenn ein Fehler aufgefangen wurde, sogar wenn im try ein return steht. Dort gehört hin, was auf jeden Fall passieren muss, etwa die Kasse schließen.

```beispiel
id: finally
code: |
  function verkaufen(anzahl) {
    try {
      if (anzahl > 10) {
        throw new Error("So viele Brötchen gibt es nicht");
      }
      return `${anzahl} Brötchen verkauft`;
    } catch (fehler) {
      return `Abgelehnt: ${fehler.message}`;
    } finally {
      console.log("Kassenlade zu");
    }
  }
  console.log(verkaufen(3));
  console.log(verkaufen(50));
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Kassenlade zu
        3 Brötchen verkauft
        Kassenlade zu
        Abgelehnt: So viele Brötchen gibt es nicht
      richtig: true
      erklaerung: Richtig. finally läuft vor dem Verlassen der Funktion, also bevor das Ergebnis ausgegeben wird, und zwar in beiden Fällen.
    - text: |-
        3 Brötchen verkauft
        Abgelehnt: So viele Brötchen gibt es nicht
      erklaerung: finally läuft immer, auch wenn try oder catch ein return haben.
    - text: |-
        3 Brötchen verkauft
        Kassenlade zu
        Abgelehnt: So viele Brötchen gibt es nicht
        Kassenlade zu
      erklaerung: Das console.log draußen wartet auf das Ergebnis der Funktion, und finally läuft noch in der Funktion, also vorher.
```

## Welche Fehler, und wann fangen?

Die häufigsten Fehlerarten sind `TypeError` (falscher Typ, etwa eine Methode auf null), `ReferenceError` (unbekannter Name), `SyntaxError` (falsch geschriebener Code, der gar nicht erst startet und sich darum auch nicht fangen lässt) und `RangeError` (Wert außerhalb des Erlaubten). Mit `fehler.name` kannst du im catch unterscheiden. Und alles, was du nicht behandeln kannst, wirfst du mit `throw fehler;` weiter.

```falle
titel: Fehler verschlucken
text: "Ein leeres `catch (fehler) {}` fängt jeden Fehler und tut nichts. Das Programm läuft dann mit falschen Werten weiter, und niemand merkt etwas, bis es viel später an ganz anderer Stelle knallt. Fang nur, was du wirklich behandeln kannst, und sag wenigstens, was passiert ist."
```

```frage
frageart: ordnen
id: ordnen-try
text: Bring die Zeilen in Reihenfolge, damit eine ungültige Eingabe mit einer Meldung abgefangen wird.
zeilen:
  - try {
  - '  const zahl = liesAnzahl("drei");'
  - '  console.log(zahl);'
  - '} catch (fehler) {'
  - '  console.log("Ungültig:", fehler.message);'
  - '}'
erklaerung: Richtig. Im try der riskante Teil, im catch die Antwort auf den Fehler.
hinweis: catch hängt an der schließenden Klammer des try.
```

```augenzwinkern
text: Pit hat sein ganzes Programm in ein try mit leerem catch gepackt. Es stürzt nie mehr ab. Es tut allerdings auch nichts mehr.
```
