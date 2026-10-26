---
id: css-pseudoklassen
sprache: css
titel: Pseudoklassen
kurz: Elemente nach ihrer Stelle wählen, das erste, das letzte, jedes zweite, alle außer einem, und nach ihrem Zustand wie unter dem Zeiger.
fuehrt_ein: [erstes_letztes, nth_child, not, zustand]
lernziele:
  - mit :first-child und :last-child das erste und letzte Kind wählen
  - mit :nth-child Kinder abzählen, auch gerade, ungerade und in Mustern
  - mit :not alle außer bestimmten Elementen wählen
  - erklären, wann :hover und :focus greifen
karte: Ich zähle Elemente ab, ohne das HTML anzufassen
bilder:
  - schluessel: karte_css_pseudoklassen
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin zählt eine lange Reihe von Fischen ab und tippt jeden zweiten mit einem Pinsel an
---

## Das erste und das letzte

```alltag
text: "Pit braucht keine Namensschilder, um in der Schlange \"den Ersten\" oder \"jeden Zweiten\" aufzurufen. Die Stelle in der Reihe genügt. Pseudoklassen wählen Elemente genauso: nach ihrer Stelle oder ihrem Zustand, ohne Klasse im HTML."
zeichnung: abzaehlen
```

Eine **Pseudoklasse** hängt mit einem Doppelpunkt an einem Selektor und schränkt ihn ein. `li:first-child` heißt: ein li, das das **erste Kind** seiner Eltern ist. `li:last-child` das letzte. Ohne Leerzeichen, denn gemeint ist das li selbst. Steht vor dem gesuchten Element ein anderes, etwa ein Bild vor der ersten Überschrift, hilft `:first-of-type`: das erste Element **seiner Art** unter den Geschwistern (entsprechend `:last-of-type`).

```beispiel
id: erstes-letztes
html: |
  <ul>
    <li>Hering</li>
    <li>Makrele</li>
    <li>Sardine</li>
  </ul>
code: |
  li:first-child {
    color: gold;
  }
  li:last-child {
    text-decoration: line-through;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Hering ist gold, Sardine ist durchgestrichen, Makrele bleibt unverändert
      richtig: true
      erklaerung: Richtig. Die Stelle in der Liste entscheidet, ganz ohne Klassen.
    - text: Alle drei sind gold und durchgestrichen
      erklaerung: first-child trifft nur das erste, last-child nur das letzte.
    - text: Nichts ändert sich, die li haben keine Klassen
      erklaerung: Pseudoklassen brauchen keine Klassen im HTML, sie wählen nach der Stelle.
```

```frage
frageart: luecke
id: luecke-letztes
text: Der letzte Absatz soll grau werden. Ergänze die Pseudoklasse.
code: |
  p:___ {
    color: gray;
  }
antworten: [["last-child"]]
erklaerung: Richtig.
hinweis: Das letzte Kind heißt last-child.
```

## Abzählen mit nth-child

`:nth-child(n)` wählt das Kind an Stelle n, gezählt ab 1: `li:nth-child(2)` ist das zweite. Statt einer Zahl gehen `odd` (ungerade: 1, 3, 5 ...) und `even` (gerade: 2, 4, 6 ...). So entstehen Streifen wie bei einer Tabelle, ohne jeder Zeile eine Klasse zu geben.

```beispiel
id: streifen
html: |
  <ul class="liste">
    <li>Hering</li>
    <li>Makrele</li>
    <li>Sardine</li>
    <li>Lachs</li>
    <li>Dorsch</li>
  </ul>
code: |
  .liste li {
    padding: 4px;
  }
  .liste li:nth-child(even) {
    background-color: #2b3442;
  }
  .liste li:nth-child(1) {
    color: gold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Makrele und Lachs haben einen dunklen Streifen, Hering ist gold
      richtig: true
      erklaerung: Richtig. even sind die Stellen 2 und 4, und nth-child(1) ist der Hering.
    - text: Hering, Sardine und Dorsch haben einen Streifen
      erklaerung: Das wäre odd. even trifft die geraden Stellen.
    - text: Nur die Makrele hat einen Streifen
      erklaerung: even trifft jede gerade Stelle, also auch den Lachs.
```

```frage
frageart: auswahl
id: odd
text: "Welche Stellen wählt `:nth-child(odd)`?"
optionen:
  - text: 1, 3, 5 und so weiter
    richtig: true
    erklaerung: Richtig, die ungeraden.
  - text: 2, 4, 6 und so weiter
    erklaerung: Das sind die geraden, even.
  - text: Nur die erste
    erklaerung: odd trifft jede ungerade Stelle.
```

## Muster

In die Klammern darf auch ein Muster mit `n`: Der Browser setzt für n nacheinander 0, 1, 2 ... ein. `3n` trifft also die Stellen 3, 6, 9; `3n+1` die Stellen 1, 4, 7; `n+3` alle ab der dritten.

```beispiel
id: muster
html: |
  <div class="fach">
    <div>1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div><div>7</div>
  </div>
code: |
  .fach {
    display: flex;
    gap: 4px;
  }
  .fach div {
    padding: 8px 12px;
    background-color: teal;
  }
  .fach div:nth-child(3n) {
    background-color: crimson;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die Kästen 3 und 6 sind rot
      richtig: true
      erklaerung: Richtig, 3 mal 1 und 3 mal 2. 3 mal 3 wäre 9, so viele gibt es nicht.
    - text: Nur Kasten 3 ist rot
      erklaerung: 3n trifft jede dritte Stelle, also auch die 6.
    - text: Die Kästen 1, 4 und 7 sind rot
      erklaerung: Das wäre 3n+1.
```

```frage
frageart: auswahl
id: ab-dritter
text: Welches Muster trifft alle Kinder ab dem dritten?
als_code: true
optionen:
  - text: ":nth-child(n+3)"
    richtig: true
    erklaerung: Richtig. Für n gleich 0, 1, 2 ergibt das 3, 4, 5 und so weiter.
  - text: ":nth-child(3n)"
    erklaerung: Das trifft nur jede dritte Stelle.
  - text: ":nth-child(3)"
    erklaerung: Das ist nur das dritte Kind.
```

## Alle außer

`:not(selektor)` dreht um: `li:not(.ausverkauft)` sind alle li, die **nicht** die Klasse ausverkauft tragen. Praktisch, um eine Ausnahme zu machen, ohne sie hinterher wieder zu überschreiben, etwa eine Linie zwischen allen Einträgen außer nach dem letzten.

```beispiel
id: not
html: |
  <ul class="liste">
    <li>Hering</li>
    <li class="weg">Eisscholle</li>
    <li>Makrele</li>
  </ul>
code: |
  .liste li:not(.weg) {
    color: lightgreen;
  }
  .liste li:not(:last-child) {
    border-bottom: 1px solid gray;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Hering und Makrele sind grün, die Eisscholle hell; unter Hering und Eisscholle liegt eine Linie, unter Makrele keine
      richtig: true
      erklaerung: Richtig. not schließt aus, und die Linie fehlt beim letzten Eintrag.
    - text: Nur die Eisscholle ist grün
      erklaerung: not dreht um, gemeint sind alle außer der Eisscholle.
    - text: Unter allen drei liegt eine Linie
      erklaerung: :not(:last-child) lässt den letzten aus.
```

```frage
frageart: luecke
id: luecke-not
text: Alle Absätze außer denen mit der Klasse leise sollen fett werden. Ergänze.
code: |
  p:___(.leise) {
    font-weight: bold;
  }
antworten: [["not"]]
erklaerung: Richtig.
hinweis: Nicht heißt not.
```

## Zustände: hover und focus

Manche Pseudoklassen hängen am **Zustand**: `:hover` greift, solange der Mauszeiger über dem Element ist, `:focus`, solange es bedient wird, etwa ein Eingabefeld beim Tippen. Ein Standbild zeigt diesen Zustand nicht. In der Werkbank kannst du es aber ausprobieren: Zeige auf die Bühne.

```beispiel
id: hover
html: |
  <p class="knopf">Bestellen</p>
code: |
  .knopf {
    width: 120px;
    padding: 8px;
    text-align: center;
    background-color: teal;
  }
  .knopf:hover {
    background-color: crimson;
  }
vorhersage:
  art: auswahl
  frage: Wie sieht der Knopf aus, solange niemand auf ihn zeigt?
  optionen:
    - text: Türkis
      richtig: true
      erklaerung: Richtig. Rot wird er erst unter dem Zeiger. Probier es in der Werkbank aus.
    - text: Rot
      erklaerung: :hover greift nur, solange der Zeiger darüber ist.
    - text: Halb türkis, halb rot
      erklaerung: Es gilt entweder die eine oder die andere Farbe, je nach Zustand.
```

```frage
frageart: auswahl
id: wann-hover
text: Wann gilt eine Regel mit :hover?
optionen:
  - text: Solange der Mauszeiger über dem Element ist
    richtig: true
    erklaerung: Richtig.
  - text: Nachdem man einmal darauf geklickt hat, für immer
    erklaerung: Sobald der Zeiger weg ist, gilt die Regel nicht mehr.
  - text: Immer, wenn die Seite lädt
    erklaerung: Beim Laden zeigt meist niemand darauf.
```

```merke
text: "`:first-child`, `:last-child`, `:nth-child(2)`, `:nth-child(odd)` und `even`, Muster wie `3n` oder `n+3`, `:not(...)` zum Ausschließen, `:hover` und `:focus` für Zustände. Immer ohne Leerzeichen am Selektor."
```

```falle
titel: Leerzeichen vor dem Doppelpunkt
text: "`li :first-child` mit Leerzeichen sucht das erste Kind **in** jedem li, nicht das erste li. Gemeint ist fast immer `li:first-child`."
```

```augenzwinkern
text: "Pit hat jeden dritten Gast mit :nth-child(3n) zum Gratisfisch eingeladen. Am nächsten Tag standen alle an Stelle 3, 6 und 9 und haben sich gegenseitig vorgelassen."
```
