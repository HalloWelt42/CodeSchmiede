---
id: js-arrays-bearbeiten
sprache: javascript
titel: Arrays bearbeiten
kurz: Vorne und hinten anfügen und wegnehmen, suchen, mitten drin streichen und einfügen, ordnen, umdrehen und zusammenfügen.
fuehrt_ein: [arraymethoden]
lernziele:
  - mit push, pop, unshift und shift an beiden Enden arbeiten
  - mit includes und indexOf nach Werten suchen
  - mit splice mitten im Array streichen und einfügen, mit slice einen Ausschnitt kopieren
  - mit sort und reverse ordnen und wissen, warum Zahlen dabei Ärger machen
  - mit concat Arrays zusammenfügen
karte: Ich ordne, suche und schiebe um
bilder:
  - schluessel: karte_js_arrays_bearbeiten
    art: sammelkarte
    sprache: javascript
    motiv: Eine Schlange von Pinguinen steht am Fischwagen an, einer drängelt sich vorne hinein, hinten kommt gerade einer dazu
---

## Vorne und hinten

```alltag
text: Am Fischwagen bildet sich eine Schlange. Neue Kunden stellen sich hinten an, bedient wird vorne. Manchmal drängelt sich jemand vor, und manchmal gibt der Letzte auf und geht. Für jede dieser Bewegungen hat ein Array eine Methode.
zeichnung: warteschlange
```

`push(x)` hängt hinten an, `pop()` nimmt den letzten Wert weg und liefert ihn. `unshift(x)` stellt vorne an, `shift()` nimmt den ersten weg und liefert ihn. Alle vier ändern das Array selbst. Spiel das Beispiel ab und beobachte die Schlange im Speicherbild.

```beispiel
id: schlange
code: |
  const schlange = ["Pia", "Ole"];
  schlange.push("Ida");
  schlange.unshift("Bo");
  const bedient = schlange.shift();
  const aufgegeben = schlange.pop();
  console.log("Bedient:", bedient);
  console.log("Aufgegeben:", aufgegeben);
  console.log(schlange);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Bedient: Bo
        Aufgegeben: Ida
        [ 'Pia', 'Ole' ]
      richtig: true
      erklaerung: Richtig. Bo hat sich vorgedrängelt und wird zuerst bedient, Ida stand hinten und gibt auf.
    - text: |-
        Bedient: Pia
        Aufgegeben: Ole
        [ 'Bo', 'Ida' ]
      erklaerung: unshift stellt Bo ganz nach vorn, also nimmt shift ihn als Ersten.
    - text: |-
        Bedient: Bo
        Aufgegeben: Ida
        [ 'Bo', 'Pia', 'Ole', 'Ida' ]
      erklaerung: shift und pop nehmen die Werte wirklich heraus, die Schlange wird kürzer.
```

```frage
frageart: auswahl
id: was-liefert-pop
text: Was liefert `schlange.pop()`?
optionen:
  - text: Den letzten Wert, der dabei aus dem Array verschwindet
    richtig: true
    erklaerung: Richtig. pop nimmt ihn heraus und gibt ihn zurück, damit du ihn noch benutzen kannst.
  - text: Das Array ohne den letzten Wert
    erklaerung: Das Array ändert sich, aber geliefert wird der herausgenommene Wert.
  - text: Die neue Länge
    erklaerung: Die Länge liefert push, pop liefert den Wert.
```

## Suchen

`array.includes(x)` antwortet mit true oder false, ob x vorkommt. `array.indexOf(x)` sagt, an welcher Stelle x zum ersten Mal steht, und liefert -1, wenn es gar nicht drin ist. Beides kennst du schon von Texten.

```beispiel
id: suchen
code: |
  const karte = ["Hering", "Aal", "Makrele", "Dorsch"];
  console.log(karte.includes("Dorsch"));
  console.log(karte.indexOf("Aal"));
  console.log(karte.indexOf("Lachs"));
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        true
        1
        -1
      richtig: true
      erklaerung: Richtig. Dorsch ist dabei, Aal steht an Stelle 1, und Lachs gibt es nicht, also -1.
    - text: |-
        true
        2
        -1
      erklaerung: Gezählt wird ab 0, Aal ist der zweite Wert, also Index 1.
    - text: |-
        true
        1
        undefined
      erklaerung: Fehlt der Wert, liefert indexOf die Zahl -1, nicht undefined.
```

## Mitten drin: splice und slice

`splice(start, anzahl)` streicht ab der Stelle start so viele Werte und liefert sie als Array. Weitere Werte hinter der Anzahl werden an dieser Stelle eingefügt; mit Anzahl 0 wird nur eingefügt. `slice(von, bis)` dagegen lässt das Array in Ruhe und liefert eine Kopie des Ausschnitts, wie bei Text.

```beispiel
id: splice
code: |
  const karte = ["Hering", "Aal", "Makrele", "Dorsch"];
  const raus = karte.splice(1, 2);
  console.log(raus);
  console.log(karte);
  karte.splice(1, 0, "Lachs", "Butt");
  console.log(karte);
  console.log(karte.slice(1, 3));
vorhersage:
  art: eintippen
  erklaerung: "splice(1, 2) streicht ab Index 1 zwei Werte, Aal und Makrele. Übrig sind Hering und Dorsch. splice(1, 0, ...) fügt bei Index 1 ein, ohne etwas zu streichen. slice(1, 3) kopiert die Indizes 1 und 2, das Array selbst bleibt."
```

```frage
frageart: luecke
id: luecke-splice
text: Ergänze die Zahl, damit genau ein Wert, die Makrele, gestrichen wird.
code: |
  const karte = ["Hering", "Makrele", "Dorsch"];
  karte.splice(1, ___);
antworten: [["1"]]
erklaerung: Richtig, ab Index 1 einen Wert streichen.
hinweis: Die zweite Zahl ist die Anzahl.
```

## Ordnen

`sort()` ordnet ein Array alphabetisch und `reverse()` dreht es um. Beide ändern das Array selbst. Wer das Original behalten will, sortiert eine Kopie: `array.slice().sort()`. Großbuchstaben kommen dabei vor Kleinbuchstaben, ganz wie im Zeichensatz.

```beispiel
id: ordnen
code: |
  const gaeste = ["Pia", "Ole", "Ida", "Bo"];
  const sortiert = gaeste.slice().sort();
  console.log(sortiert.join(", "));
  console.log(gaeste.join(", "));
  sortiert.reverse();
  console.log(sortiert.join(", "));
  console.log([10, 9, 1, 25].sort());
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        Bo, Ida, Ole, Pia
        Pia, Ole, Ida, Bo
        Pia, Ole, Ida, Bo
        [ 1, 10, 25, 9 ]
      richtig: true
      erklaerung: Richtig. Die Kopie wird sortiert, das Original bleibt. reverse dreht die sortierte Liste um. Und Zahlen sortiert sort wie Text, Zeichen für Zeichen.
    - text: |-
        Bo, Ida, Ole, Pia
        Bo, Ida, Ole, Pia
        Pia, Ole, Ida, Bo
        [ 1, 9, 10, 25 ]
      erklaerung: slice() hat eine Kopie gemacht, das Original bleibt ungeordnet. Und sort vergleicht Zahlen als Text, darum steht 10 vor 9.
    - text: |-
        Bo, Ida, Ole, Pia
        Pia, Ole, Ida, Bo
        Pia, Ole, Ida, Bo
        [ 1, 9, 10, 25 ]
      erklaerung: Fast. Aber sort ohne weitere Angabe vergleicht Zahlen wie Text, und als Text kommt "10" vor "9".
```

```falle
titel: sort und Zahlen
text: "`[10, 9, 1, 25].sort()` ergibt `[ 1, 10, 25, 9 ]`, weil sort Zahlen als Text vergleicht. Zahlen richtig zu sortieren braucht eine kleine Vergleichsfunktion, die kommt in Kapitel 15. Bis dahin: sort nur für Texte."
```

```merke
text: "`push`/`pop` hinten, `unshift`/`shift` vorne. `includes(x)` und `indexOf(x)` suchen. `splice(start, anzahl, ...neu)` streicht und fügt ein, `slice(von, bis)` kopiert. `sort()` und `reverse()` ändern das Array selbst, `concat` fügt Arrays zu einem neuen zusammen."
```

```frage
frageart: ordnen
id: ordnen-tagesplan
text: Zwei Listen sollen zu einer werden, alphabetisch sortiert, mit Komma getrennt. Bring die Zeilen in Reihenfolge.
zeilen:
  - const morgens = ["Pia", "Ole"];
  - const abends = ["Ida", "Bo"];
  - const alle = morgens.concat(abends);
  - alle.sort();
  - console.log(alle.join(", "));
erklaerung: Richtig. concat liefert ein neues Array, das dann sortiert und ausgegeben wird.
hinweis: Sortiert wird, nachdem zusammengefügt ist.
```

```augenzwinkern
text: Pit hat seine Warteschlange einmal mit reverse() umgedreht. Die Kunden ganz hinten fanden das großartig, die vorne weniger.
```
