---
id: css-schrift
sprache: css
titel: Text und Schrift
kurz: Schriftgröße in Pixeln, fett und schräg, Schriftart, Ausrichtung, Großbuchstaben, Linien und Abstände im Text.
fuehrt_ein: [px, schriftgroesse, schriftschnitt, schriftart, textausrichtung, textschmuck, textabstand]
lernziele:
  - die Schriftgröße mit font-size in Pixeln setzen
  - mit font-weight und font-style fett und schräg schreiben
  - eine Schriftart mit Ersatz in font-family angeben
  - Text mit text-align ausrichten
  - Text mit text-transform und text-decoration schmücken
  - Zeilenhöhe und Buchstabenabstand einstellen
karte: Ich bringe Text in Form
bilder:
  - schluessel: karte_css_schrift
    art: sammelkarte
    sprache: css
    motiv: Ein Pinguin setzt mit großen Holzstempeln Buchstabenformen auf ein Plakat, manche dick, manche schräg
---

## Wie groß?

```alltag
text: 'Pit malt die Tafel vor dem Wagen: den Namen riesig, die Gerichte mittel, die Preise etwas kleiner, und ganz unten winzig "Fisch kann Gräten enthalten". Größe sagt, was wichtig ist.'
zeichnung: stempel
```

`font-size` setzt die **Schriftgröße**. Die erste Einheit dafür ist das **Pixel**, geschrieben `px`, ein Bildpunkt auf dem Bildschirm. Zwischen Zahl und Einheit steht kein Leerzeichen: `font-size: 24px;`. Absätze sind auf unserer Bühne von Haus aus 16 Pixel groß, Überschriften `h1` doppelt so groß.

```beispiel
id: groesse
html: |
  <h1>Zum frostigen Hering</h1>
  <p>Heute: Hering im Eismantel</p>
  <p class="klein">Fisch kann Gräten enthalten.</p>
code: |
  h1 {
    font-size: 20px;
  }
  p {
    font-size: 24px;
  }
  .klein {
    font-size: 11px;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Der mittlere Absatz ist der größte Text, die Überschrift etwas kleiner, der Hinweis winzig
      richtig: true
      erklaerung: Richtig. Die eigene Regel schlägt die Größe, die der Browser der Überschrift von sich aus gibt.
    - text: Die Überschrift bleibt am größten, sie ist schließlich ein h1
      erklaerung: Die Größe von h1 ist nur eine Voreinstellung. Mit 20 Pixeln ist sie kleiner als die 24 der Absätze.
    - text: Beide Absätze sind 24 Pixel groß
      erklaerung: .klein ist genauer als p und setzt 11 Pixel.
```

```frage
frageart: auswahl
id: px-richtig
text: Welche Angabe ist richtig geschrieben?
als_code: true
optionen:
  - text: "font-size: 18px;"
    richtig: true
    erklaerung: Richtig, Zahl und Einheit ohne Leerzeichen.
  - text: "font-size: 18 px;"
    erklaerung: Mit Leerzeichen erkennt der Browser die Einheit nicht, die Angabe fällt weg.
  - text: "font-size: 18;"
    erklaerung: Ohne Einheit weiß der Browser nicht, was 18 heißen soll. Die Angabe fällt weg.
```

## Fett und schräg

`font-weight` macht Schrift **fett** (`bold` oder die Zahl `700`) oder wieder normal (`normal` oder `400`). `font-style: italic` macht sie **schräg**, `normal` wieder gerade. So kann man auch die Voreinstellungen ändern: Überschriften sind von Haus aus fett, `strong` auch, `em` schräg.

```beispiel
id: schnitt
html: |
  <h2>Heute frisch</h2>
  <p>Hering mit <strong>doppelt</strong> Eis</p>
  <p class="motto">Fangfrisch seit 1999</p>
code: |
  h2 {
    font-weight: normal;
  }
  .motto {
    font-style: italic;
    font-weight: bold;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die Überschrift ist nicht mehr fett, doppelt bleibt fett, das Motto ist fett und schräg
      richtig: true
      erklaerung: Richtig. Die Regel für h2 nimmt der Überschrift das Fett. strong ist davon nicht betroffen.
    - text: Alles ist fett, eine Überschrift kann man nicht dünner machen
      erklaerung: Auch Voreinstellungen lassen sich überschreiben, mit font-weight normal.
    - text: Die Überschrift ist schräg, das Motto nur fett
      erklaerung: italic steht in der Regel für das Motto, nicht für h2.
```

```frage
frageart: luecke
id: luecke-schraeg
text: Der Hinweis soll schräg stehen. Ergänze Eigenschaft und Wert.
code: |
  .hinweis {
    ___: ___;
  }
antworten: [["font-style"], ["italic"]]
erklaerung: Richtig, font-style italic.
hinweis: Die Eigenschaft für den Stil der Schrift, der Wert für schräg ist italic.
```

## Welche Schrift?

`font-family` wählt die **Schriftart**. Weil nicht jede Schrift auf jedem Gerät vorhanden ist, schreibt man eine Liste: Der Browser nimmt die erste, die er hat. Am Ende steht immer eine **Schriftfamilie**, die es überall gibt: `serif` (mit kleinen Füßchen), `sans-serif` (ohne), `monospace` (jedes Zeichen gleich breit) oder `cursive` (geschwungen).

```beispiel
id: familie
html: |
  <h2>Tageskarte</h2>
  <p class="code">Bon 0042: 4,50</p>
  <p class="schreibschrift">Mit Liebe gebraten</p>
code: |
  h2 {
    font-family: serif;
  }
  .code {
    font-family: monospace;
  }
  .schreibschrift {
    font-family: cursive;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Die Überschrift mit Füßchen, der Bon in gleich breiten Zeichen, der letzte Satz geschwungen
      richtig: true
      erklaerung: Richtig, drei Schriftfamilien, drei ganz verschiedene Bilder.
    - text: Alles bleibt in derselben Schrift, die Bühne gibt sie vor
      erklaerung: Die Bühne gibt nur die Voreinstellung vor. Jede Regel mit font-family ersetzt sie.
    - text: Nur der Bon ändert sich, die anderen Namen gibt es nicht
      erklaerung: serif, monospace und cursive sind Familien, die jeder Browser kennt.
```

```frage
frageart: auswahl
id: liste-schrift
text: "Was macht der Browser bei `font-family: Wunschschrift, sans-serif;`, wenn er Wunschschrift nicht kennt?"
optionen:
  - text: Er nimmt eine Schrift ohne Füßchen
    richtig: true
    erklaerung: Richtig. Er geht die Liste durch und nimmt den ersten Eintrag, den er hat.
  - text: Er zeigt gar keinen Text
    erklaerung: Text zeigt er immer. Genau dafür steht am Ende eine Familie, die es überall gibt.
  - text: Er meldet einen Fehler
    erklaerung: CSS meldet nichts. Fehlende Schriften werden still übersprungen.
```

## Ausrichten

`text-align` richtet den Text in seinem Kasten aus: `left` (links, die Voreinstellung), `center` (mittig) oder `right` (rechts). Ausgerichtet wird innerhalb des Kastens. Bei einem Absatz, der die ganze Breite einnimmt, also über die ganze Bühne.

```beispiel
id: ausrichten
html: |
  <h1>Zum frostigen Hering</h1>
  <p>Seit 1999</p>
  <p class="preis">4,50</p>
code: |
  h1, p {
    text-align: center;
  }
  .preis {
    text-align: right;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: Überschrift und Seit 1999 stehen in der Mitte, der Preis ganz rechts
      richtig: true
      erklaerung: Richtig. .preis ist genauer als p und schiebt den Preis nach rechts.
    - text: Alles steht in der Mitte
      erklaerung: Für den Preis gibt es eine genauere Regel, die rechts sagt.
    - text: Nur die Überschrift steht in der Mitte
      erklaerung: Die Gruppe h1, p trifft auch die Absätze.
```

```frage
frageart: auswahl
id: mitte-wovon
text: "`span { text-align: center; }` ändert bei einem kurzen span mitten im Satz nichts. Warum?"
optionen:
  - text: Der span ist nur so breit wie sein Text, darin ist nichts zu verschieben
    richtig: true
    erklaerung: Richtig. Ausgerichtet wird im eigenen Kasten, und der ist beim span genau so breit wie sein Inhalt.
  - text: text-align gilt nur für Überschriften
    erklaerung: text-align geht bei allen Elementen, die eine eigene Zeile einnehmen, auch bei Absätzen und div.
  - text: center schreibt man centre
    erklaerung: CSS schreibt amerikanisch, center ist richtig.
```

## Schmuck und Abstand

Noch ein paar Werkzeuge für Text:

- `text-transform: uppercase` schreibt alles in Großbuchstaben, ohne das HTML zu ändern
- `text-decoration: underline` unterstreicht, `line-through` streicht durch, `none` nimmt Linien weg
- `letter-spacing` setzt zusätzlichen Abstand zwischen die Buchstaben, etwa `3px`
- `line-height` bestimmt die Zeilenhöhe; eine Zahl ohne Einheit wie `1.8` heißt das 1,8-Fache der Schriftgröße

```beispiel
id: schmuck
html: |
  <h2>Speisekarte</h2>
  <p class="weg">Eisscholle mit Sardinen</p>
  <p class="luftig">Hering im Eismantel, dazu ein Klecks Remoulade und frisches Brot vom Bäcker nebenan</p>
code: |
  h2 {
    text-transform: uppercase;
    letter-spacing: 6px;
  }
  .weg {
    text-decoration: line-through;
  }
  .luftig {
    line-height: 2;
  }
vorhersage:
  art: auswahl
  optionen:
    - text: SPEISEKARTE in weit gesperrten Großbuchstaben, die Eisscholle durchgestrichen, der lange Absatz mit viel Platz zwischen den Zeilen
      richtig: true
      erklaerung: Richtig, vier Werkzeuge, vier Wirkungen.
    - text: Speisekarte bleibt klein geschrieben, weil im HTML Kleinbuchstaben stehen
      erklaerung: text-transform ändert nur die Anzeige. Im HTML bleibt alles, wie es ist.
    - text: Die Eisscholle ist unterstrichen
      erklaerung: Unterstreichen wäre underline. line-through streicht durch.
```

```frage
frageart: ordnen
id: ordnen-schrift
text: Bring die Zeilen in Reihenfolge, damit die Überschrift groß, mittig und in Großbuchstaben erscheint.
zeilen:
  - h1 {
  - '  font-size: 32px;'
  - '  text-align: center;'
  - '  text-transform: uppercase;'
  - '}'
erklaerung: Richtig. Die Reihenfolge der Angaben in der Regel ist egal, die Klammern nicht.
hinweis: Erst Selektor und Klammer, dann die drei Angaben, dann die schließende Klammer.
```

```merke
text: "`font-size` in `px`, `font-weight: bold`, `font-style: italic`, `font-family` mit Ersatzfamilie am Ende, `text-align`, `text-transform`, `text-decoration`, `letter-spacing`, `line-height` als Zahl."
```

```falle
titel: Leerzeichen vor der Einheit
text: "`font-size: 24 px` ist ungültig, die Angabe fällt still weg. Zahl und Einheit gehören zusammen: `24px`. Nur bei 0 darf die Einheit fehlen."
```

```augenzwinkern
text: Pit hat einmal alles in cursive gesetzt, auch die Preise. Seitdem lesen die Kunden 4,50 als 450 und bestellen ganz vorsichtig.
```
