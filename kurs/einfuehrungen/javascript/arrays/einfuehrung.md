---
id: js-arrays
sprache: javascript
titel: Arrays
kurz: Viele Werte in einer Liste, Zugriff über den Index, durchgehen mit for ... of, wachsen mit push, Text zerlegen und verbinden.
fuehrt_ein: [array, anhaengen, zerlegen_verbinden]
lernziele:
  - ein Array mit eckigen Klammern anlegen und über den Index lesen und ändern
  - mit for ... of und mit einem Zähler durch alle Werte gehen
  - mit push Werte anhängen und Eingaben einsammeln
  - mit split Text in ein Array zerlegen und mit join wieder verbinden
  - wissen, dass zwei Namen auf dasselbe Array zeigen können
karte: Ich sammle Werte in Reihen
bilder:
  - schluessel: karte_js_arrays
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin legt Fische in die nummerierten Fächer einer langen Eiswürfelschale
---

## Viele Werte unter einem Namen

```alltag
text: In Pits Kühlschrank liegt eine Eiswürfelschale mit nummerierten Fächern. In jedes Fach passt ein Fisch, und wer Fach 2 sagt, meint immer dasselbe Fach. Ein Array ist so eine Schale, nur dass sie wachsen kann.
zeichnung: eiswuerfel
```

Ein Array ist eine geordnete Liste von Werten in eckigen Klammern, getrennt durch Kommas: `["Hering", "Makrele", "Sprotte"]`. Wie bei Text zählt der Index ab 0, und `length` sagt, wie viele Werte drin sind. Anders als bei Text kannst du einzelne Fächer austauschen: `fische[1] = "Lachs";`. Die Konsole zeigt Arrays mit Klammern und Text in einfachen Anführungszeichen.

```beispiel
id: schale
code: |
  const fische = ["Hering", "Makrele", "Sprotte"];
  console.log(fische.length);
  console.log(fische[0], fische[2]);
  fische[1] = "Lachs";
  console.log(fische);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        3
        Hering Sprotte
        [ 'Hering', 'Lachs', 'Sprotte' ]
      richtig: true
      erklaerung: Richtig. Drei Werte, Index 0 und 2 sind der erste und der letzte, und Fach 1 bekommt Lachs.
    - text: |-
        3
        Makrele Sprotte
        [ 'Hering', 'Lachs', 'Sprotte' ]
      erklaerung: Index 0 ist das erste Fach, also Hering.
    - text: |-
        3
        Hering Sprotte
        Fehler
      erklaerung: Ein Array darf sich ändern, auch wenn der Name ein const ist. Mehr dazu gleich in der Falle.
```

```falle
titel: const und trotzdem änderbar
text: "`const fische = [...]` heißt: Der Name fische zeigt immer auf dieses eine Array. Was im Array liegt, darf sich trotzdem ändern, mit `fische[1] = ...` oder push. Nur `fische = [\"anderes Array\"]` geht nicht. Darum schreibt man Arrays meist mit const."
```

```frage
frageart: auswahl
id: letzter-index
text: Ein Array hat 5 Werte. Welchen Index hat der letzte?
optionen:
  - text: '4'
    richtig: true
    erklaerung: Richtig. Gezählt wird ab 0, also 0 bis 4.
  - text: '5'
    erklaerung: Index 5 wäre schon das sechste Fach, da steht undefined.
  - text: '-1'
    erklaerung: Mit eckigen Klammern gibt es keine negativen Indizes; fische.at(-1) ginge aber.
```

## Alle durchgehen

Mit `for (const fisch of fische)` bekommst du jeden Wert der Reihe nach, genau wie die Zeichen eines Textes. Brauchst du dazu die Nummer, nimm die Zählschleife von 0 bis `length - 1`. Ein häufiges Muster: einen Sammler vor der Schleife anlegen und in der Schleife füllen.

```beispiel
id: durchgehen
code: |
  const faenge = [4, 9, 2, 7];
  let summe = 0;
  let groesster = faenge[0];
  for (const f of faenge) {
    summe += f;
    if (f > groesster) {
      groesster = f;
    }
  }
  console.log("Summe:", summe, "Größter:", groesster);
  for (let i = 0; i < faenge.length; i++) {
    console.log(`Tag ${i + 1}: ${faenge[i]}`);
  }
vorhersage:
  art: eintippen
  erklaerung: "4 + 9 + 2 + 7 ist 22, der größte Fang ist 9. Die zweite Schleife zählt i von 0 bis 3 und zeigt die Tage ab 1 an, darum i + 1."
```

```frage
frageart: luecke
id: luecke-of
text: Ergänze, damit jeder Name begrüßt wird.
code: |
  const gaeste = ["Pia", "Ole"];
  for (const name ___ gaeste) {
    console.log(`Moin, ${name}!`);
  }
antworten: [["of"]]
erklaerung: Richtig, for ... of geht durch alle Werte.
hinweis: Dasselbe Wort wie bei Text.
```

## Wachsen mit push

`array.push(wert)` hängt einen Wert hinten an. So füllt man ein leeres Array `[]` nach und nach, etwa mit Eingaben, deren Zahl man vorher nicht kennt.

```beispiel
id: einsammeln
code: |
  const bestellung = [];
  while (true) {
    const ware = prompt("Ware? ");
    if (!ware) {
      break;
    }
    bestellung.push(ware);
  }
  console.log(bestellung);
  console.log(`${bestellung.length} Waren`);
eingabe: [Hering, Gurke, Zwiebel, ""]
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Ware? Ware? Ware? Ware? [ 'Hering', 'Gurke', 'Zwiebel' ]
        3 Waren
      richtig: true
      erklaerung: Richtig. Viermal wird gefragt, die leere Antwort beendet die Schleife. push hat drei Waren angehängt.
    - text: |-
        Ware? Ware? Ware? Ware? [ 'Hering', 'Gurke', 'Zwiebel', '' ]
        4 Waren
      erklaerung: Bei der leeren Antwort steigt break aus, bevor push sie anhängt.
    - text: |-
        Ware? Ware? Ware? Ware? []
        0 Waren
      erklaerung: Auch ein const-Array lässt sich mit push füllen.
```

```merke
text: "`[a, b, c]` ist ein Array, `arr[i]` liest oder ändert Fach i (ab 0), `arr.length` zählt. `arr.push(x)` hängt hinten an. `for (const x of arr)` geht durch alle Werte."
```

## Zerlegen und verbinden

Viele Daten kommen als Text an, etwa `"Hering,Makrele,Sprotte"`. `text.split(",")` zerlegt ihn an jedem Komma in ein Array. Der Weg zurück ist `array.join(", ")`: Er verbindet alle Werte zu einem Text, mit dem angegebenen Trenner dazwischen.

```beispiel
id: zerlegen
code: |
  const zeile = "Hering,Makrele,Sprotte";
  const fische = zeile.split(",");
  console.log(fische.length);
  console.log(fische.join(" und "));
  const woerter = "Frischer Fisch vom Wagen".split(" ");
  console.log(woerter[1]);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        3
        Hering und Makrele und Sprotte
        Fisch
      richtig: true
      erklaerung: Richtig. split macht aus dem Text drei Werte, join klebt sie mit dem Trenner zusammen, und der zweite Wert des Satzes ist Fisch.
    - text: |-
        22
        Hering und Makrele und Sprotte
        Fisch
      erklaerung: Nach dem split ist fische ein Array mit drei Werten; length zählt jetzt Werte, keine Zeichen.
    - text: |-
        3
        Hering,Makrele,Sprotte
        Frischer
      erklaerung: join setzt den neuen Trenner ein, und Index 1 ist das zweite Wort.
```

```falle
titel: Zwei Namen, ein Array
text: "`const kopie = fische;` macht keine Kopie. Beide Namen zeigen auf dasselbe Array, und ein push über kopie ändert auch fische. Spiel so etwas in der Werkbank ab: Im Speicherbild steht dann dasselbe wie. Wie man echte Kopien macht, zeigt Kapitel 18."
```

```frage
frageart: ordnen
id: ordnen-zerlegen
text: Bring die Zeilen in Reihenfolge, damit aus "Pia;Ole;Ida" die Ausgabe "Pia, Ole, Ida, Bo" wird.
zeilen:
  - const text = "Pia;Ole;Ida";
  - const namen = text.split(";");
  - namen.push("Bo");
  - console.log(namen.join(", "));
erklaerung: Richtig. Zerlegen, anhängen, verbinden.
hinweis: push braucht schon das Array.
```

```augenzwinkern
text: Pit hat sein Sortiment einmal mit split("") zerlegt. Seitdem verkauft er einzelne Buchstaben, das H ist besonders beliebt.
```
