---
id: js-rechnen
sprache: javascript
titel: Rechnen
kurz: Plus, minus, mal, geteilt, Rest und Hochzahl, dazu Abkürzungen wie += und ++ und Runden mit Math.
fuehrt_ein: [grundrechnen, rest, potenz, kurzschreibweise, math]
lernziele:
  - mit + - * / rechnen und Klammern setzen
  - mit % den Rest beim Teilen bestimmen und mit ** hochrechnen
  - Werte mit += und ++ verändern
  - mit Math.round, Math.floor und Math.ceil runden
  - wissen, warum 0.1 + 0.2 nicht ganz 0.3 ergibt
karte: Ich rechne, runde und zähle hoch
bilder:
  - schluessel: karte_js_rechnen
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin steht hinter einer altmodischen Registrierkasse, aus der ein langer Kassenzettel quillt
---

## Die Kasse rechnet

```alltag
text: Ein Heringsbrötchen kostet 2,50, Pia nimmt drei. Pit tippt 3 mal 2,50 in die Kasse, und die Kasse sagt 7,50. Rechnen ist das, was Computer am liebsten tun, und JavaScript rechnet mit denselben Zeichen wie eine Kasse.
zeichnung: kasse
```

Plus ist `+`, minus `-`, mal `*` und geteilt `/`. Wie in der Schule gilt Punkt vor Strich, und mit runden Klammern bestimmst du selbst, was zuerst gerechnet wird. Ergebnisse kannst du direkt ausgeben oder einem Namen geben.

```beispiel
id: kasse
code: |
  const preis = 2.5;
  const anzahl = 3;
  const summe = preis * anzahl;
  console.log(summe);
  console.log(1 + 2 * 3);
  console.log((1 + 2) * 3);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        7.5
        7
        9
      richtig: true
      erklaerung: Richtig. 2.5 mal 3 ist 7.5; Punkt vor Strich ergibt 7, die Klammern machen daraus 9.
    - text: |-
        7.5
        9
        9
      erklaerung: Ohne Klammern rechnet JavaScript erst 2 * 3, dann plus 1. Punkt vor Strich wie in der Schule.
    - text: |-
        7.50
        7
        9
      erklaerung: Überflüssige Nullen hinter dem Komma lässt JavaScript weg, auch bei Geld.
```

```frage
frageart: auswahl
id: geteilt
text: Was gibt `console.log(7 / 2);` aus?
als_code: true
optionen:
  - text: '3.5'
    richtig: true
    erklaerung: Richtig. Beim Teilen gibt es in JavaScript immer das genaue Ergebnis, auch mit Komma.
  - text: '3'
    erklaerung: JavaScript schneidet beim Teilen nichts ab. Wie man ganze Zahlen bekommt, zeigt der nächste Abschnitt.
  - text: '3 Rest 1'
    erklaerung: Den Rest gibt es auch, aber mit einem eigenen Zeichen, gleich im nächsten Abschnitt.
```

## Rest und Hochzahl

Sieben Fische für zwei Pinguine: Jeder bekommt drei, einer bleibt übrig. Den Rest beim Teilen liefert `%`, gesprochen modulo. Mit `Math.floor` rundest du ab und bekommst so, wie oft etwas ganz hineinpasst. Und `**` rechnet hoch: `2 ** 3` ist 2 mal 2 mal 2.

```beispiel
id: fische-teilen
code: |
  const fische = 7;
  const pinguine = 2;
  console.log("Jeder bekommt", Math.floor(fische / pinguine));
  console.log("Übrig bleiben", fische % pinguine);
  console.log("Zwei hoch zehn ist", 2 ** 10);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Jeder bekommt 3
        Übrig bleiben 1
        Zwei hoch zehn ist 1024
      richtig: true
      erklaerung: Richtig. 7 / 2 ist 3.5, abgerundet 3; der Rest ist 1; und zehnmal die 2 malgenommen ergibt 1024.
    - text: |-
        Jeder bekommt 3.5
        Übrig bleiben 1
        Zwei hoch zehn ist 1024
      erklaerung: Math.floor rundet ab, aus 3.5 wird 3. Halbe Fische gibt es nicht.
    - text: |-
        Jeder bekommt 3
        Übrig bleiben 0.5
        Zwei hoch zehn ist 20
      erklaerung: "% liefert den Rest als ganze Zahl: 7 = 2 * 3 + 1. Und ** rechnet hoch, nicht mal."
```

```merke
text: "`a % b` ist der Rest beim Teilen, `Math.floor(a / b)` sagt, wie oft b ganz in a passt. `a ** b` ist a hoch b."
```

```frage
frageart: luecke
id: luecke-gerade
text: Bei einer geraden Zahl bleibt beim Teilen durch 2 nichts übrig. Ergänze das Zeichen, damit 0 herauskommt.
code: console.log(10 ___ 2);
antworten: [["%"]]
erklaerung: Richtig, 10 % 2 ist 0, also ist 10 gerade.
hinweis: Gesucht ist das Zeichen für den Rest.
```

## Runden mit Math

`Math` ist ein eingebauter Werkzeugkasten für Zahlen. Darin stecken unter anderem `Math.round` (kaufmännisch runden), `Math.floor` (abrunden), `Math.ceil` (aufrunden), `Math.max` und `Math.min` (größter und kleinster von mehreren Werten) und `Math.abs` (Betrag, ohne Minus).

```beispiel
id: runden
code: |
  const preis = 2.65;
  console.log(Math.round(preis));
  console.log(Math.floor(preis));
  console.log(Math.ceil(preis));
  console.log(Math.max(3, 8, 5));
  console.log(Math.round(preis * 10) / 10);
vorhersage:
  art: eintippen
  erklaerung: "round rundet 2.65 auf 3, floor ab auf 2, ceil auf zu 3. max nimmt die größte Zahl, 8. Die letzte Zeile ist ein Trick für eine Stelle hinter dem Komma: erst mal 10 (26.5), runden (27), dann durch 10 (2.7)."
```

```frage
frageart: auswahl
id: aufrunden
text: Für 23 Gäste braucht der Wagen Tische, an jeden passen 4. Was rechnet die Zahl der Tische richtig aus?
als_code: true
optionen:
  - text: Math.ceil(23 / 4)
    richtig: true
    erklaerung: Richtig. 23 / 4 ist 5.75, aufgerundet 6. Der letzte Tisch ist nicht ganz voll, aber niemand steht.
  - text: Math.floor(23 / 4)
    erklaerung: Abgerundet wären es 5 Tische, und drei Gäste müssten stehen.
  - text: 23 % 4
    erklaerung: Das ist der Rest, 3 Gäste, aber nicht die Zahl der Tische.
```

## Abkürzungen beim Ändern

Oft ändert sich ein Wert ausgehend vom alten: Die Kasse bekommt 5 dazu. Lang geschrieben heißt das `kasse = kasse + 5;`: Rechts wird mit dem alten Wert gerechnet, das Ergebnis wird der neue. Kürzer geht es mit `kasse += 5;`. Genauso gibt es `-=`, `*=` und `/=`. Und um genau eins hochzuzählen, gibt es `kunden++`, für eins weniger `kunden--`. Spiel das Beispiel ab und sieh im Speicher, wie die Werte wachsen.

```beispiel
id: abkuerzungen
code: |
  let kasse = 0;
  let kunden = 0;
  kasse = kasse + 5;
  kunden++;
  kasse += 7.5;
  kunden++;
  kasse -= 2;
  console.log(kunden, "Kunden, Kasse:", kasse);
vorhersage:
  art: auswahl
  optionen:
    - text: "2 Kunden, Kasse: 10.5"
      richtig: true
      erklaerung: Richtig. 0 + 5 + 7.5 - 2 ergibt 10.5, und kunden wurde zweimal um eins erhöht.
    - text: "2 Kunden, Kasse: 12.5"
      erklaerung: kasse -= 2 nimmt am Ende noch 2 weg, etwa für Wechselgeld.
    - text: "0 Kunden, Kasse: 10.5"
      erklaerung: kunden++ zählt kunden jedes Mal um eins hoch, zweimal ergibt 2.
```

```merke
text: "`x += 5` heißt `x = x + 5`, entsprechend `-=`, `*=` und `/=`. `x++` zählt um eins hoch, `x--` um eins herunter. Das geht nur mit let, denn der Wert ändert sich."
```

```frage
frageart: ordnen
id: ordnen-konto
text: Erst 10 in die Kasse, dann verdoppeln, dann 4 heraus. Bring die Zeilen so in Reihenfolge, dass 16 ausgegeben wird.
zeilen:
  - let kasse = 0;
  - kasse += 10;
  - kasse *= 2;
  - kasse -= 4;
  - console.log(kasse);
erklaerung: Richtig. 0, dann 10, dann 20, dann 16.
hinweis: Rechne im Kopf mit, was nach jeder Zeile in der Kasse ist.
```

## Kommazahlen sind nicht ganz genau

Der Computer speichert Zahlen im Zweiersystem. Viele Kommazahlen, die im Zehnersystem harmlos aussehen, gehen dort nicht ganz auf, so wie 1/3 im Zehnersystem nie aufhört. Meistens merkt man davon nichts, aber manchmal blitzt es auf.

```beispiel
id: ungenau
code: |
  console.log(0.1 + 0.2);
  console.log(Math.round((0.1 + 0.2) * 100) / 100);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        0.30000000000000004
        0.3
      richtig: true
      erklaerung: Richtig, und das ist kein Fehler von JavaScript, sondern von Kommazahlen im Zweiersystem. Gerundet auf zwei Stellen ist es wieder ordentlich.
    - text: |-
        0.3
        0.3
      erklaerung: Das wäre schön. 0.1 und 0.2 sind im Speicher aber beide ein winziges bisschen ungenau, und die Summe zeigt es.
    - text: |-
        0.30000000000000004
        0.30000000000000004
      erklaerung: Mal 100, runden, durch 100 schneidet den Krümel ab.
```

```falle
titel: Geteilt durch null
text: "Andere Sprachen brechen beim Teilen durch null ab. JavaScript nicht: `console.log(5 / 0);` gibt `Infinity` aus, unendlich. Das Programm läuft weiter, rechnet dann aber mit einem unsinnigen Wert. Prüfe vor dem Teilen, ob der Teiler null sein kann."
```

```augenzwinkern
text: Pit hat einmal 0.1 + 0.2 Euro Trinkgeld bekommen. Er wartet bis heute auf die fehlenden 0.00000000000000004 Euro.
```
