---
id: css-variablen
sprache: css
titel: Variablen und calc
kurz: Werte einmal festlegen und überall benutzen, für einen Bereich anders setzen und mit calc Breiten und Abstände ausrechnen.
fuehrt_ein: [variablen, calc]
lernziele:
  - eigene Eigenschaften mit zwei Bindestrichen in :root festlegen
  - sie mit var() benutzen, auch mit Ersatzwert
  - eine Variable für einen Bereich anders setzen
  - mit calc Werte und Einheiten mischen
  - Variablen in calc verrechnen
karte: Ich ändere eine Zeile, und alles passt sich an
bilder:
  - schluessel: karte_css_variablen
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin dreht an einem einzigen großen Farbrad, und alle Schilder des Fischwagens wechseln gleichzeitig die Farbe
---

## Werte mit Namen

```alltag
text: "Pit hat seine Hausfarbe an zwanzig Stellen ins CSS geschrieben. Als Pia eine neue will, muss er zwanzigmal ändern und vergisst natürlich eine. Mit einer Variable ändert er die Farbe an einer einzigen Stelle."
zeichnung: farbrad
```

Eine **eigene Eigenschaft**, oft Variable genannt, beginnt mit **zwei Bindestrichen**, etwa `--hausfarbe: #ffd166;`. Man legt sie meist in `:root` fest, einer Pseudoklasse für das oberste Element der Seite; von dort erben alle sie. Benutzt wird sie mit `var(--hausfarbe)`, überall, wo der Wert stehen dürfte.

```beispiel
id: variable
html: |
  <h2>Speisekarte</h2>
  <p class="preis">4,50</p>
  <div class="streifen"></div>
code: |
  :root {
    --hausfarbe: #ffd166;
  }
  h2, .preis {
    color: var(--hausfarbe);
  }
  .streifen {
    height: 10px;
    background-color: var(--hausfarbe);
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Überschrift und Preis sind gelb, darunter ein gelber Streifen
      richtig: true
      erklaerung: Richtig. Drei Stellen, eine Variable.
    - text: Nichts ist gelb, --hausfarbe ist keine echte Eigenschaft
      erklaerung: Eigene Eigenschaften sind erlaubt und werden mit var() eingesetzt.
    - text: Nur der Streifen ist gelb
      erklaerung: Auch Überschrift und Preis benutzen die Variable.
```

```frage
frageart: luecke
id: luecke-var
text: Ergänze, damit die Variable --akzent benutzt wird.
code: |
  h1 {
    color: ___(--akzent);
  }
antworten: [["var"]]
erklaerung: Richtig.
hinweis: Die Funktion heißt wie Variable, nur kurz.
```

## Mit Ersatzwert

Gibt es eine Variable nicht, etwa weil der Name falsch geschrieben ist, ist die ganze Angabe ungültig. Ein **Ersatzwert** nach einem Komma hilft: `var(--akzent, gold)` nimmt gold, wenn `--akzent` nicht festgelegt ist.

```beispiel
id: ersatz
html: |
  <p class="a">Hering</p>
  <p class="b">Makrele</p>
code: |
  :root {
    --fisch: skyblue;
  }
  .a {
    color: var(--fisch, tomato);
  }
  .b {
    color: var(--fish, tomato);
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Hering ist himmelblau, Makrele tomatenrot
      richtig: true
      erklaerung: Richtig. --fish gibt es nicht, also greift der Ersatzwert.
    - text: Beide sind himmelblau
      erklaerung: Bei der Makrele steht --fish, nicht --fisch. Diese Variable gibt es nicht.
    - text: Beide sind tomatenrot
      erklaerung: --fisch ist festgelegt, also nimmt der Hering skyblue.
```

```frage
frageart: auswahl
id: ersatz-wann
text: "Wann gilt der Ersatzwert in `var(--x, 10px)`?"
optionen:
  - text: Wenn --x nirgends festgelegt ist
    richtig: true
    erklaerung: Richtig.
  - text: Immer zusätzlich zu --x
    erklaerung: Es gilt entweder der Wert von --x oder der Ersatz.
  - text: Nur am Telefon
    erklaerung: Mit dem Gerät hat das nichts zu tun.
```

## Für einen Bereich anders

Variablen werden **vererbt** wie color. Setzt man sie bei einem Element neu, gilt der neue Wert für dieses Element und alles darin. So bekommt ein Bereich ein eigenes Farbschema, ohne dass eine einzige andere Regel sich ändert.

```beispiel
id: bereich
html: |
  <div class="karte">Tageskarte</div>
  <div class="karte nacht">Nachtkarte</div>
code: |
  :root {
    --grund: #fbf4e2;
    --schrift: #2b3442;
  }
  .nacht {
    --grund: #0b1d3a;
    --schrift: #ffd166;
  }
  .karte {
    padding: 16px;
    margin-bottom: 8px;
    background-color: var(--grund);
    color: var(--schrift);
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Oben hell mit dunkler Schrift, unten dunkelblau mit gelber Schrift
      richtig: true
      erklaerung: Richtig. Die Nachtkarte setzt die Variablen neu, dieselbe Regel .karte malt sie anders.
    - text: Beide Karten sind hell
      erklaerung: In der Nachtkarte gelten die neu gesetzten Werte.
    - text: Beide Karten sind dunkelblau
      erklaerung: Die neuen Werte gelten nur in .nacht, nicht für alle.
```

```frage
frageart: auswahl
id: wo-gilt
text: "Eine Variable wird bei `.nacht` neu gesetzt. Wo gilt der neue Wert?"
optionen:
  - text: Bei .nacht und allem, was darin steckt
    richtig: true
    erklaerung: Richtig, Variablen werden vererbt.
  - text: Auf der ganzen Seite
    erklaerung: Der Wert aus :root gilt weiter überall sonst.
  - text: Nur bei .nacht selbst, nicht bei den Kindern
    erklaerung: Variablen werden an die Kinder vererbt.
```

## Rechnen mit calc

`calc()` rechnet Werte aus, auch mit verschiedenen Einheiten: `width: calc(100% - 60px)` ist die volle Breite der Eltern minus 60 Pixel, was keine einzelne Einheit kann. Plus und Minus brauchen **Leerzeichen** drumherum, mal und geteilt schreibt man `*` und `/`.

```beispiel
id: calc
html: |
  <div class="leiste">
    <div class="knopf">Los</div>
    <div class="feld">Suchen ...</div>
  </div>
code: |
  .knopf, .feld {
    display: inline-block;
    padding: 8px 0;
    text-align: center;
  }
  .knopf {
    width: 60px;
    background-color: teal;
  }
  .feld {
    width: calc(100% - 70px);
    background-color: #e3f1f8;
    color: #555;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Ein schmaler Knopf und daneben ein Feld, das fast die ganze restliche Breite füllt
      richtig: true
      erklaerung: Richtig. 100 Prozent minus 70 Pixel lassen Platz für den Knopf und die kleine Lücke.
    - text: Das Feld ist 30 Pixel breit
      erklaerung: calc rechnet 100 Prozent der Eltern minus 70 Pixel, das ist viel mehr.
    - text: Das Feld rutscht unter den Knopf
      erklaerung: Gerade so viel abgezogen, dass beide in eine Zeile passen.
```

```frage
frageart: fehlerstelle
id: calc-leerzeichen
text: Eine Breite wird nicht berechnet. In welcher Zeile steckt der Fehler?
code: |
  .a {
    width: calc(50% + 20px);
  }
  .b {
    width: calc(50%-20px);
  }
zeile: 5
erklaerung: Genau. Ohne Leerzeichen um das Minus ist calc ungültig.
hinweis: Schau dir die Rechenzeichen genau an.
```

## Variablen verrechnen

Richtig stark wird es zusammen: `calc(var(--abstand) * 2)` verdoppelt einen Abstand, der an einer einzigen Stelle festgelegt ist. Ändert man `--abstand`, wachsen alle abgeleiteten Werte mit.

```beispiel
id: zusammen
html: |
  <div class="kasten">
    <p class="innen">Hering</p>
  </div>
code: |
  :root {
    --abstand: 10px;
  }
  .kasten {
    padding: calc(var(--abstand) * 3);
    background-color: teal;
  }
  .innen {
    margin: 0;
    padding: var(--abstand);
    background-color: #2b3442;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Ein türkiser Rahmen von 30 Pixeln um einen dunklen Kasten mit 10 Pixeln Polster
      richtig: true
      erklaerung: Richtig. Dreimal 10 Pixel außen, einmal innen.
    - text: Beide Polster sind 10 Pixel
      erklaerung: Beim Kasten wird die Variable mal drei gerechnet.
    - text: Kein Polster, Variablen gehen nicht in calc
      erklaerung: Doch, var() darf in calc stehen.
```

```merke
text: "`--name: wert;` (meist in `:root`) legt fest, `var(--name, ersatz)` benutzt. Neu gesetzt bei einem Element gilt die Variable für alles darin. `calc()` rechnet mit gemischten Einheiten, Plus und Minus mit Leerzeichen."
```

```falle
titel: Variable ohne var
text: "`color: --hausfarbe;` ist ungültig. Benutzt wird eine Variable immer mit `var(--hausfarbe)`."
```

```augenzwinkern
text: Pia hat --pits-laune als Variable eingeführt. Je nach Wert ist die Speisekarte sonnig gelb oder gewittergrau. Heute ist sie gelb, es gab Hering.
```
