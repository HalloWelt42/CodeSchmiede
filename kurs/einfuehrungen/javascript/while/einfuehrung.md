---
id: js-while
sprache: javascript
titel: Wiederholen mit while
kurz: Code so lange wiederholen, wie eine Bedingung stimmt; zählen, sammeln, Eingaben lesen bis zum Ende, mit break aussteigen.
fuehrt_ein: [while]
lernziele:
  - mit while Code wiederholen, solange eine Bedingung stimmt
  - in einer Schleife zählen und Werte aufsammeln
  - Eingaben lesen, bis keine mehr kommen oder ein Endwort fällt
  - mit break mitten aus der Schleife aussteigen und do ... while kennen
  - Endlosschleifen erkennen und vermeiden
karte: Ich wiederhole, bis es reicht
bilder:
  - schluessel: karte_js_while
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin fährt auf einem kleinen Eiskarussell im Kreis, daneben zählt ein Zählwerk die Runden
---

## Solange es stimmt

```alltag
text: Pit fährt Karussell, und zwar so lange, wie er noch Chips hat. Vor jeder Runde schaut er nach, ob noch einer da ist. Ist keiner mehr da, steigt er aus. Genau so arbeitet while, nur ohne Schwindelgefühl.
zeichnung: karussell
```

`while (bedingung) { ... }` prüft die Bedingung und führt den Block aus, wenn sie stimmt. Danach geht es wieder nach oben zur Bedingung. Erst wenn sie nicht mehr stimmt, macht das Programm hinter der Schleife weiter. Damit das irgendwann passiert, muss sich im Block etwas ändern, das die Bedingung betrifft. Spiel das Beispiel ab und sieh zu, wie `chips` kleiner wird.

```beispiel
id: karussell
code: |
  let chips = 3;
  while (chips > 0) {
    console.log("Runde! Chips übrig:", chips - 1);
    chips--;
  }
  console.log("Aussteigen");
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Runde! Chips übrig: 2
        Runde! Chips übrig: 1
        Runde! Chips übrig: 0
        Aussteigen
      richtig: true
      erklaerung: Richtig. Drei Runden, dann ist chips 0, die Bedingung stimmt nicht mehr, und es geht weiter.
    - text: |-
        Runde! Chips übrig: 2
        Aussteigen
      erklaerung: while wiederholt, solange die Bedingung stimmt, nicht nur einmal wie if.
    - text: |-
        Runde! Chips übrig: 2
        Runde! Chips übrig: 1
        Runde! Chips übrig: 0
        Runde! Chips übrig: -1
        Aussteigen
      erklaerung: Bei chips gleich 0 ist chips > 0 falsch, eine vierte Runde gibt es nicht.
```

```frage
frageart: auswahl
id: unterschied-if
text: Was unterscheidet while von if?
optionen:
  - text: while wiederholt den Block, solange die Bedingung stimmt; if führt ihn höchstens einmal aus.
    richtig: true
    erklaerung: Richtig. Nach jedem Durchgang prüft while die Bedingung erneut.
  - text: while braucht keine Bedingung.
    erklaerung: Doch, genau wie if eine in runden Klammern.
  - text: while kennt kein else, darum ist es kürzer.
    erklaerung: Ein else gibt es tatsächlich nicht, aber das ist nicht der Kern. while wiederholt.
```

## Zählen und sammeln

Ein typisches Muster: ein Zähler, der hochzählt, und ein Sammler, der etwas aufnimmt. Beide legt man vor der Schleife an, damit sie über alle Durchgänge hinweg erhalten bleiben.

```beispiel
id: summe
code: |
  let tag = 1;
  let gesamt = 0;
  while (tag <= 4) {
    gesamt += tag * 2;
    tag++;
  }
  console.log("Fische in 4 Tagen:", gesamt);
vorhersage:
  art: eintippen
  erklaerung: "Am Tag t fängt Pit t mal 2 Fische: 2 + 4 + 6 + 8 ergibt 20. Nach Tag 4 wird tag zu 5, und 5 <= 4 stimmt nicht mehr."
```

```falle
titel: Die Endlosschleife
text: "Ändert sich im Block nichts an der Bedingung, stimmt sie für immer. Dann läuft die Schleife endlos, bis die Sandbox nach ein paar Sekunden die Notbremse zieht. Vergisst du im Beispiel oben `tag++`, bleibt tag bei 1, und 1 <= 4 ist immer wahr."
```

```frage
frageart: fehlerstelle
id: fehler-endlos
text: Diese Schleife hört nie auf. In welcher Zeile müsste sich etwas ändern?
code: |
  let fische = 10;
  while (fische > 0) {
    console.log("Ein Fisch für dich");
    fische + 1;
  }
zeile: 4
erklaerung: Genau. fische + 1 rechnet nur und verwirft das Ergebnis, und zum Ende hin müsste fische ohnehin kleiner werden. Richtig wäre fische--.
hinweis: Welche Zeile soll fische verändern, tut es aber nicht?
```

## Lesen bis zum Ende

Wie viele Eingaben kommen, weiß ein Programm oft nicht vorher. Dann liest es in einer Schleife, bis ein Endwort kommt oder `prompt` gar nichts mehr liefert, also `null`. Ein bewährter Aufbau: `while (true)` läuft eigentlich ewig, und ein `break` mitten im Block steigt aus, sobald das Ende erreicht ist. break kennst du schon aus switch; in einer Schleife beendet es die ganze Schleife.

```beispiel
id: einkauf
code: |
  let anzahl = 0;
  while (true) {
    const ware = prompt("Ware? ");
    if (ware === null || ware === "fertig") {
      break;
    }
    anzahl++;
    console.log(`${anzahl}. ${ware}`);
  }
  console.log("Waren:", anzahl);
eingabe: [Hering, Zwiebeln, Brötchen, fertig]
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Ware? 1. Hering
        Ware? 2. Zwiebeln
        Ware? 3. Brötchen
        Ware? Waren: 3
      richtig: true
      erklaerung: Richtig. Bei fertig steigt break aus, bevor gezählt wird. Die letzte Frage hängt vor der Schlusszeile.
    - text: |-
        Ware? 1. Hering
        Ware? 2. Zwiebeln
        Ware? 3. Brötchen
        Ware? 4. fertig
        Waren: 4
      erklaerung: Das break steht vor dem Zählen und Ausgeben, fertig wird nicht mitgezählt.
    - text: |-
        1. Hering
        2. Zwiebeln
        3. Brötchen
        Waren: 3
      erklaerung: Jedes prompt schreibt seine Frage in die Ausgabe, auch das letzte.
```

```merke
text: "`while (bedingung) { ... }` wiederholt, solange die Bedingung stimmt. Im Block muss sich etwas ändern, sonst läuft es endlos. `break` beendet die Schleife sofort, `while (true)` mit break liest so lange, bis das Ende kommt."
```

```frage
frageart: luecke
id: luecke-break
text: Ergänze, damit die Schleife bei der Eingabe stopp endet.
code: |
  while (true) {
    const wort = prompt();
    if (wort === "stopp") {
      ___;
    }
    console.log(wort);
  }
antworten: [["break"]]
erklaerung: Richtig, break steigt aus der Schleife aus.
hinweis: Dasselbe Wort wie bei switch.
```

## Mindestens einmal mit do ... while

Manchmal soll der Block auf jeden Fall einmal laufen und erst danach geprüft werden, etwa beim Raten: Erst rät man, dann sieht man, ob es stimmt. Dafür gibt es `do { ... } while (bedingung);`, die Bedingung steht am Ende.

```beispiel
id: raten
code: |
  const geheim = 7;
  let versuche = 0;
  let tipp;
  do {
    tipp = Number(prompt("Tipp? "));
    versuche++;
    if (tipp < geheim) {
      console.log("zu klein");
    } else if (tipp > geheim) {
      console.log("zu groß");
    }
  } while (tipp !== geheim);
  console.log(`Richtig nach ${versuche} Versuchen!`);
eingabe: ["4", "9", "7"]
vorhersage:
  art: eintippen
  erklaerung: "Erst 4, zu klein; dann 9, zu groß; dann 7, die Bedingung tipp !== geheim stimmt nicht mehr, die Schleife endet nach drei Versuchen. Vor jeder Antwort steht die Frage Tipp?."
```

```frage
frageart: ordnen
id: ordnen-countdown
text: Bring die Zeilen in Reihenfolge, damit von 3 heruntergezählt und dann gestartet wird.
zeilen:
  - let zahl = 3;
  - while (zahl > 0) {
  - '  console.log(zahl);'
  - '  zahl--;'
  - '}'
  - console.log("Start!");
erklaerung: Richtig. Erst ausgeben, dann herunterzählen, und Start kommt nach der Schleife.
hinweis: Was nur einmal am Ende kommen soll, steht hinter der schließenden Klammer.
```

```augenzwinkern
text: Pits erste Schleife hieß while (fische > 0) { fische++; }. Der Fischwagen hat seitdem einen Überlauf.
```
