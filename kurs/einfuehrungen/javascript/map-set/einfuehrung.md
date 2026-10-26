---
id: js-map-set
sprache: javascript
titel: Map und Set
kurz: Neue Objekte mit new, Wörterbücher mit Map (beliebige Schlüssel, feste Reihenfolge, size) und Mengen mit Set (jeder Wert nur einmal).
fuehrt_ein: [new, map, set]
lernziele:
  - mit new Map() ein Wörterbuch anlegen und mit set, get, has und delete benutzen
  - eine Map durchgehen und wissen, wann sie besser passt als ein Objekt
  - mit new Set() Doppelte loswerden und mit add, has und delete arbeiten
  - zwei Mengen vergleichen, etwa auf gemeinsame Werte
karte: Ich schlage nach und kenne jeden nur einmal
bilder:
  - schluessel: karte_js_map_set
    art: sammelkarte
    sprache: javascript
    motiv: Ein Pinguin hängt Schlüssel mit Anhängern an ein Schlüsselbrett, daneben steht eine Schale mit lauter verschiedenen Muscheln
---

## Nachschlagen mit Map

```alltag
text: Im Fischwagen hängt ein Schlüsselbrett. An jedem Haken hängt ein Anhänger mit einem Namen, und dahinter der passende Schlüssel. Wer den Kühlraum sucht, schaut nach dem Anhänger Kühlraum. Eine Map ist so ein Schlüsselbrett, und die Anhänger dürfen alles sein, nicht nur Wörter.
zeichnung: schluesselbrett
```

`new` baut ein neues Objekt einer bestimmten Art; `new Map()` eine leere Map. Mit `map.set(schluessel, wert)` hängst du etwas auf, mit `map.get(schluessel)` holst du es, `map.has(schluessel)` fragt, ob es da ist, `map.delete(schluessel)` nimmt es ab, und `map.size` zählt. In der Konsole erscheint eine Map mit Pfeilen.

```beispiel
id: preise
code: |
  const preise = new Map();
  preise.set("Hering", 2.5);
  preise.set("Aal", 5);
  console.log(preise.get("Aal"));
  console.log(preise.has("Lachs"), preise.size);
  preise.delete("Aal");
  console.log(preise);
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        5
        false 2
        Map(1) { 'Hering' => 2.5 }
      richtig: true
      erklaerung: Richtig. get holt den Preis des Aals, Lachs gibt es nicht, und nach delete bleibt nur der Hering.
    - text: |-
        5
        false 2
        Map(2) { 'Hering' => 2.5, 'Aal' => 5 }
      erklaerung: delete nimmt den Aal wirklich heraus.
    - text: |-
        undefined
        false 2
        Map(1) { 'Hering' => 2.5 }
      erklaerung: get findet den Aal, er wurde vorher mit set aufgehängt.
```

```frage
frageart: luecke
id: luecke-get
text: Ergänze die Methode, die den Wert zum Schlüssel holt.
code: |
  const lager = new Map();
  lager.set("Hering", 12);
  console.log(lager.___("Hering"));
antworten: [["get"]]
erklaerung: Richtig, get holt, set hängt auf.
hinweis: Das Gegenstück zu set.
```

## Map oder Objekt?

Beides ordnet Werten Namen zu. Ein Objekt passt, wenn die Namen feststehen, wie beim Steckbrief. Eine Map passt, wenn ständig Einträge dazukommen und wegfallen, wie bei einem Zähler oder einem Lager: Sie hat `size`, behält die Reihenfolge, und ihre Schlüssel dürfen jeder Wert sein. Eine Zahl als Schlüssel bleibt eine Zahl. Durchgehen geht mit `for ... of` über `map.keys()`, `map.values()` oder die Map selbst, die Paare aus Schlüssel und Wert liefert.

```beispiel
id: durchgehen
code: |
  const tische = new Map();
  tische.set(1, "Pia");
  tische.set(2, "Ole");
  console.log(tische.get(1), tische.get("1"));
  for (const nummer of tische.keys()) {
    console.log(`Tisch ${nummer}: ${tische.get(nummer)}`);
  }
  for (const paar of tische) {
    console.log(paar);
  }
vorhersage:
  art: eintippen
  erklaerung: "Schlüssel 1 ist die Zahl 1, der Text \"1\" ist ein anderer Schlüssel, darum undefined. keys liefert 1 und 2 in der Reihenfolge, in der sie dazukamen. Die Map selbst liefert Paare als kleine Arrays aus Schlüssel und Wert."
```

```merke
text: "`new Map()` legt eine Map an. `set(k, w)`, `get(k)`, `has(k)`, `delete(k)`, `size`. Schlüssel dürfen alles sein und behalten ihre Reihenfolge. Durchgehen mit `for (const k of map.keys())`."
```

## Jeder nur einmal mit Set

Ein Set ist eine Menge: Jeder Wert ist höchstens einmal darin. `new Set(array)` nimmt die Werte eines Arrays und wirft Doppelte dabei weg. Mit `add(x)` kommt ein Wert dazu, wenn er noch fehlt, `has(x)` fragt nach, `delete(x)` nimmt ihn heraus, `size` zählt. Durchgehen geht mit `for ... of`.

```beispiel
id: menge
code: |
  const bestellungen = ["Pia", "Ole", "Pia", "Ida", "Ole", "Pia"];
  const kunden = new Set(bestellungen);
  console.log(kunden.size, "verschiedene Kunden");
  kunden.add("Bo");
  kunden.add("Pia");
  console.log(kunden.has("Bo"), kunden.size);
  for (const name of kunden) {
    console.log(name);
  }
vorhersage:
  art: auswahl
  optionen:
    - text: |-
        3 verschiedene Kunden
        true 4
        Pia
        Ole
        Ida
        Bo
      richtig: true
      erklaerung: Richtig. Aus sechs Bestellungen werden drei verschiedene Kunden. Bo kommt dazu, Pia ist schon drin und zählt nicht doppelt.
    - text: |-
        6 verschiedene Kunden
        true 8
        Pia
        Ole
        Pia
        Ida
        Ole
        Pia
        Bo
        Pia
      erklaerung: Ein Set behält jeden Wert nur einmal, Doppelte fallen weg.
    - text: |-
        3 verschiedene Kunden
        true 5
        Pia
        Ole
        Ida
        Bo
        Pia
      erklaerung: add mit einem Wert, der schon drin ist, ändert nichts.
```

```falle
titel: Kein Index im Set
text: "Ein Set hat keine Fächer mit Nummern, `kunden[0]` liefert undefined. Brauchst du einen Index oder sort, mach erst ein Array daraus, etwa mit einer Schleife und push."
```

```frage
frageart: auswahl
id: set-oder-map
text: Du willst wissen, welche verschiedenen Fischsorten heute bestellt wurden. Was passt am besten?
optionen:
  - text: Ein Set
    richtig: true
    erklaerung: Richtig. Es geht nur um verschiedene Werte, ohne etwas dazu.
  - text: Eine Map
    erklaerung: Eine Map lohnt sich, wenn zu jeder Sorte noch etwas gehört, etwa die Anzahl.
  - text: Ein Array
    erklaerung: Ein Array behält Doppelte; du müsstest selbst aufpassen.
```

## Mengen vergleichen

Mit `has` lassen sich zwei Mengen vergleichen: Geh durch die eine und frag bei der anderen nach. So findest du, was beide gemeinsam haben oder was nur in einer steckt.

```beispiel
id: gemeinsam
code: |
  const montag = new Set(["Pia", "Ole", "Ida"]);
  const dienstag = new Set(["Ole", "Bo", "Ida"]);
  const beide = [];
  for (const name of montag) {
    if (dienstag.has(name)) {
      beide.push(name);
    }
  }
  console.log("An beiden Tagen:", beide.join(", "));
vorhersage:
  art: auswahl
  optionen:
    - text: 'An beiden Tagen: Ole, Ida'
      richtig: true
      erklaerung: Richtig. Nur Ole und Ida stehen in beiden Mengen, in der Reihenfolge von montag.
    - text: 'An beiden Tagen: Pia, Ole, Ida, Bo'
      erklaerung: Das wären alle zusammen. has lässt nur durch, wer auch am Dienstag da war.
    - text: 'An beiden Tagen: Pia, Bo'
      erklaerung: Das sind die, die nur an einem Tag kamen.
```

```frage
frageart: ordnen
id: ordnen-set
text: Bring die Zeilen in Reihenfolge, damit die Zahl der verschiedenen Buchstaben in "Hering" ausgegeben wird.
zeilen:
  - const buchstaben = new Set();
  - for (const z of "Hering") {
  - '  buchstaben.add(z);'
  - '}'
  - console.log(buchstaben.size);
erklaerung: Richtig. Erst die leere Menge, dann jedes Zeichen hinein, zuletzt zählen.
hinweis: Gezählt wird nach der Schleife.
```

```augenzwinkern
text: Pit wollte seine Stammkunden in ein Set stecken. Jetzt hat er nur noch einen Pia, und alle anderen Pias sind beleidigt.
```
