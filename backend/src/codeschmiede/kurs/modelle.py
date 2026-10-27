"""Datenmodelle des Aufbaukurses: Einführung, Abschnitte und ihre Teile, Fragen, Kurztest, Kurs, Begriffskatalog.

Die Wahrheit liegt im Repo unter kurs/ (Format in docs/KURS-FORMAT.md). Antworten auf Fragen und Vorhersagen
(`richtig`, `antworten`, `zeile`, `erklaerung`) verlassen den Server nie: die Oberfläche bekommt nur die öffentliche
Form (`oeffentlich()`), geprüft wird auf dem Server.
"""

from __future__ import annotations

import hashlib
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from ..steuerung import kv

KENNUNG = r"^[a-z0-9][a-z0-9-]{0,79}$"
Kurssprache = Literal["python", "sql", "javascript", "css", "digital"]
# Übungen eines Kurses sind Aufgaben seiner Sprache; Digitaltechnik übt mit Schaltungen und KV-Diagrammen, die als
# Aufgaben unter "maschine" liegen (sie sind auch Levels der Spiele).
AUFGABEN_SPRACHE: dict[str, str] = {"digital": "maschine"}


def aufgaben_sprache(kurssprache: str) -> str:
    return AUFGABEN_SPRACHE.get(kurssprache, kurssprache)


class Streng(BaseModel):
    """Unbekannte Felder in den Kursdateien sind Tippfehler und fallen beim Einlesen auf."""

    model_config = ConfigDict(extra="forbid")


# ---------- Bilder ----------


class Bildauftrag(Streng):
    """Was ein erzeugtes Bild zeigen soll; Prompt, Stil und Auswahl gehören dem Medienpool (tools/bildschluessel.py).
    Vorerst nur für Karten (Sammelkarte, Bereich); Zeichnungen in den Einführungen sind eigene SVG-Dateien."""

    schluessel: str = Field(pattern=r"^[a-z0-9_]{1,60}$")
    art: Literal["sinnbild", "alltag", "sammelkarte", "bereich"]
    sprache: Kurssprache
    motiv: str = Field(min_length=10)
    groesse: str = Field(default="4 x 3", pattern=r"^\d+ x \d+$")


# ---------- Fragen ----------


class Option(Streng):
    text: str
    richtig: bool = False
    erklaerung: str
    """Warum diese Antwort richtig oder falsch ist; erscheint nach der Wahl."""


class Auswahlfrage(Streng):
    frageart: Literal["auswahl"]
    id: str = Field(pattern=KENNUNG)
    text: str
    code: str | None = None
    optionen: list[Option] = Field(min_length=2, max_length=6)
    als_code: bool = False
    """Optionen als Code mit fester Breite darstellen (etwa Ausgaben)."""

    @model_validator(mode="after")
    def _eine_richtig(self) -> Auswahlfrage:
        if sum(o.richtig for o in self.optionen) < 1:
            raise ValueError(f"Frage {self.id}: mindestens eine Option muss richtig sein")
        return self


class Lueckenfrage(Streng):
    frageart: Literal["luecke"]
    id: str = Field(pattern=KENNUNG)
    text: str
    code: str
    """Code mit ___ für jede Lücke."""
    antworten: list[list[str]]
    """Je Lücke die angenommenen Antworten (ohne Leerzeichen am Rand verglichen)."""
    erklaerung: str
    hinweis: str
    """Was nach einer falschen Antwort hilft, ohne die Lösung zu verraten."""

    @model_validator(mode="after")
    def _luecken_passen(self) -> Lueckenfrage:
        if self.code.count("___") != len(self.antworten) or not self.antworten:
            raise ValueError(f"Frage {self.id}: {self.code.count('___')} Lücken, aber {len(self.antworten)} Antwortlisten")
        return self


class Ordnungsfrage(Streng):
    frageart: Literal["ordnen"]
    id: str = Field(pattern=KENNUNG)
    text: str
    zeilen: list[str] = Field(min_length=3)
    """Die Zeilen in der richtigen Reihenfolge; gezeigt werden sie gemischt."""
    erklaerung: str
    hinweis: str

    def gemischt(self) -> list[str]:
        """Feste, nie richtige Mischung: aus der Kennung abgeleitet, damit jede Anzeige gleich ist."""
        zahl = int(hashlib.sha256(self.id.encode()).hexdigest(), 16)
        reihe = list(self.zeilen)
        for i in range(len(reihe) - 1, 0, -1):
            zahl, j = divmod(zahl, i + 1)
            reihe[i], reihe[j] = reihe[j], reihe[i]
        if reihe == self.zeilen:
            reihe = reihe[1:] + reihe[:1]
        return reihe


class Fehlerstellenfrage(Streng):
    frageart: Literal["fehlerstelle"]
    id: str = Field(pattern=KENNUNG)
    text: str
    code: str
    zeile: int = Field(ge=1)
    erklaerung: str
    hinweise: dict[int, str] = Field(default_factory=dict)
    """Je falsch gewählter Zeile ein Hinweis; fehlt einer, gilt `hinweis`."""
    hinweis: str

    @model_validator(mode="after")
    def _zeile_im_code(self) -> Fehlerstellenfrage:
        if self.zeile > len(self.code.rstrip("\n").split("\n")):
            raise ValueError(f"Frage {self.id}: Zeile {self.zeile} gibt es im Code nicht")
        return self


Frage = Annotated[Auswahlfrage | Lueckenfrage | Ordnungsfrage | Fehlerstellenfrage, Field(discriminator="frageart")]


class Vorhersage(Streng):
    """Erst vorhersagen, dann ausführen: Auswahl aus Ausgaben oder die Ausgabe selbst eintippen."""

    art: Literal["auswahl", "eintippen"]
    optionen: list[Option] = Field(default_factory=list)
    erklaerung: str = ""
    """Bei `eintippen`: Erklärung nach dem Vergleich mit dem echten Ergebnis."""
    frage: str | None = None
    """Eigene Frage statt "Was kommt heraus?", etwa "Wie viele Zeilen hat das Ergebnis?"."""
    vergleich: Literal["ausgabe", "zeilen", "anfang"] = "ausgabe"
    """Womit der echte Lauf verglichen wird: die ganze Ausgabe, nur die Zahl ihrer Zeilen (bei SQL: der
    Ergebniszeilen) oder nur ihr Anfang. Bei `zeilen` steht in der richtigen Option die Zahl als erste Zahl im Text,
    bei `anfang` die ersten Zeilen der Ausgabe (etwa "Wer steht ganz oben?")."""

    @model_validator(mode="after")
    def _passend(self) -> Vorhersage:
        if self.art == "auswahl" and (len(self.optionen) < 2 or sum(o.richtig for o in self.optionen) != 1):
            raise ValueError("Vorhersage als Auswahl braucht mindestens zwei Optionen, genau eine richtig")
        if self.art == "eintippen" and (self.optionen or not self.erklaerung):
            raise ValueError("Vorhersage zum Eintippen hat keine Optionen, aber eine Erklärung")
        return self


# ---------- Teile eines Abschnitts ----------


class Text(Streng):
    art: Literal["text"] = "text"
    markdown: str


class Alltag(Streng):
    art: Literal["alltag"] = "alltag"
    text: str
    zeichnung: str | None = Field(default=None, pattern=r"^[a-z0-9-]{1,60}$")
    """Eigene Zeichnung zeichnungen/<name>.svg neben der Einführung."""


class Merke(Streng):
    art: Literal["merke"] = "merke"
    text: str


class Falle(Streng):
    """Typischer Fehler; steht im Text und gesammelt auf dem Merkblatt."""

    art: Literal["falle"] = "falle"
    titel: str
    text: str


class Augenzwinkern(Streng):
    art: Literal["augenzwinkern"] = "augenzwinkern"
    text: str


class Zeichnung(Streng):
    """Eigene Zeichnung (SVG im Ordner zeichnungen/ der Einführung); erzeugte Bilder gibt es vorerst nur auf Karten."""

    art: Literal["zeichnung"] = "zeichnung"
    datei: str = Field(pattern=r"^[a-z0-9-]{1,60}$")
    unterschrift: str = ""


class Diagramm(Streng):
    art: Literal["diagramm"] = "diagramm"
    quelle: str
    """Mermaid; daraus wird beim Bauen ein SVG (kurs/diagramme/<pruefsumme>.svg)."""
    titel: str = ""

    @property
    def pruefsumme(self) -> str:
        return hashlib.sha256(self.quelle.strip().encode()).hexdigest()[:16]


class Beispiel(Streng):
    art: Literal["beispiel"] = "beispiel"
    id: str = Field(pattern=KENNUNG)
    code: str
    vorhersage: Vorhersage | None = None
    html: str | None = None
    """CSS: das Markup, auf das die Regeln in `code` wirken (Pflicht bei CSS, sonst nicht erlaubt)."""
    eingabe: list[str] = Field(default_factory=list)
    """Zeilen, die input() der Reihe nach liest."""
    ablauf: bool = True
    """Ablauf anbieten: bei Python Zeile für Zeile mit Speicherbild, bei SQL die Zwischentabelle je Klausel."""


class KvFormel(Streng):
    titel: str
    formel: str
    """Blöcke als Terme wie in der KV-Werkstatt: `C + A B`, `!` heißt 0."""


class KvTeil(Streng):
    """Digitaltechnik: eine Funktion zum Anschauen in der Werkbank, als Würfel der Belegungen (bei drei Eingängen,
    mit Regler zum Aufklappen) oder als KV-Raster, mit Formeln, deren Blöcke man einzeln zeigen kann."""

    art: Literal["kv"] = "kv"
    id: str = Field(pattern=KENNUNG)
    eingaenge: list[str] = Field(min_length=2, max_length=4)
    werte: str
    """je Belegung 0, 1 oder x, binär gezählt mit dem ersten Eingang vorn"""
    start: Literal["wuerfel", "raster"] = "raster"
    regler: bool = False
    """Würfel per Regler zum Raster aufklappen"""
    plan: bool = False
    """zu jeder Formel den Schaltplan zeigen"""
    formeln: list[KvFormel] = Field(min_length=1)

    @model_validator(mode="after")
    def _stimmig(self) -> KvTeil:
        n = len(self.eingaenge)
        if len(self.werte) != 2 ** n or set(self.werte) - set("01x"):
            raise ValueError(f"KV {self.id}: werte braucht {2 ** n} Zeichen aus 0, 1 und x")
        if (self.start == "wuerfel" or self.regler) and n != 3:
            raise ValueError(f"KV {self.id}: den Würfel gibt es nur bei drei Eingängen")
        for f in self.formeln:
            gelesen = kv.lies(f"f = {f.formel}", self.eingaenge, ["f"])
            if gelesen.fehler:
                raise ValueError(f"KV {self.id}, Formel {f.titel}: {gelesen.fehler[0]}")
            falsch = [x for x in range(2 ** n) if self.werte[x] != "x" and kv.wert(gelesen.bloecke["f"], x, n) != int(self.werte[x])]
            if falsch:
                raise ValueError(f"KV {self.id}, Formel {f.titel}: stimmt nicht bei Belegung {falsch[0]}")
        return self


class FrageTeil(Streng):
    art: Literal["frage"] = "frage"
    frage: Frage


Teil = Annotated[Text | Alltag | Merke | Falle | Augenzwinkern | Zeichnung | Diagramm | Beispiel | KvTeil | FrageTeil,
                 Field(discriminator="art")]


class Abschnitt(Streng):
    nummer: int
    titel: str
    teile: list[Teil]

    def fragen(self) -> list[Auswahlfrage | Lueckenfrage | Ordnungsfrage | Fehlerstellenfrage]:
        return [t.frage for t in self.teile if isinstance(t, FrageTeil)]

    def beispiele(self) -> list[Beispiel]:
        return [t for t in self.teile if isinstance(t, Beispiel)]


class Kopf(Streng):
    id: str = Field(pattern=KENNUNG)
    sprache: Kurssprache
    titel: str
    kurz: str
    """Ein Satz für die Kursübersicht."""
    fuehrt_ein: list[str] = Field(default_factory=list)
    """Kennungen aus dem Begriffskatalog der Sprache."""
    lernziele: list[str] = Field(min_length=1)
    """Sätze für "Danach kannst du" und die Karte "Kann ich jetzt"."""
    karte: str
    """Kurzer Satz auf der Sammelkarte."""
    bilder: list[Bildauftrag] = Field(default_factory=list)
    datensatz: str | None = Field(default=None, pattern=r"^[a-z0-9_]+$")
    """SQL: Datensatz aus aufgaben/sql/datasets/, auf dem die Beispiele laufen."""

    @model_validator(mode="after")
    def _datensatz_bei_sql(self) -> Kopf:
        if (self.sprache == "sql") != (self.datensatz is not None):
            raise ValueError("Einführungen zu SQL brauchen einen Datensatz, andere haben keinen")
        return self


class Einfuehrung(Streng):
    kopf: Kopf
    abschnitte: list[Abschnitt] = Field(min_length=1)
    pfad: str
    """Ordner relativ zu kurs/, für Bilder und Befunde."""

    @property
    def id(self) -> str:
        return self.kopf.id

    @model_validator(mode="after")
    def _beispiele_passend(self) -> Einfuehrung:
        """CSS-Beispiele brauchen Markup und lassen sich nur als Auswahl vorhersagen (es gibt keine Textausgabe, nur
        ein Bild); Beispiele anderer Sprachen haben kein Markup."""
        css = self.kopf.sprache == "css"
        for a in self.abschnitte:
            for b in a.beispiele():
                if css and not b.html:
                    raise ValueError(f"Beispiel {b.id}: CSS-Beispiele brauchen html")
                if not css and b.html is not None:
                    raise ValueError(f"Beispiel {b.id}: html gibt es nur bei CSS")
                if css and b.vorhersage is not None and b.vorhersage.art != "auswahl":
                    raise ValueError(f"Beispiel {b.id}: Vorhersagen zu CSS gehen nur als Auswahl")
        return self


class Kurztest(Streng):
    fragen: list[Frage] = Field(min_length=2)
    uebung: str
    """Kennung einer Aufgabe, die alle Teile des Kapitels braucht."""


# ---------- Kurs und Begriffe ----------


class Kapitel(Streng):
    einfuehrung: str
    uebungen: list[str] = Field(default_factory=list)
    """Aufgaben in Reihenfolge: verblassende Beispiele, dann je Übung eine neue Sache."""
    projekt: list[str] = Field(default_factory=list)
    """Stück des Kapitelprojekts (Aufgaben), das in diesem Kapitel dazukommt."""


class Block(Streng):
    titel: str
    kapitel: list[Kapitel]


class Kurs(Streng):
    sprache: Kurssprache
    titel: str
    bloecke: list[Block]

    def kapitel(self) -> list[Kapitel]:
        return [k for b in self.bloecke for k in b.kapitel]


class Erkennung(Streng):
    knoten: list[str] = Field(default_factory=list)
    """Python: Namen von Knoten des Syntaxbaums (For, While, ListComp ...); SQL: Ausdrucksarten des SQL-Parsers
    (Select, Where, Order, Join, Like ...); JavaScript: Knotenarten von tree-sitter (if_statement, template_string,
    arrow_function ...); CSS: Selektorarten (typ, klasse, id, nachfahre, kind, gruppe ...), Pseudoklassen und
    -elemente mit Namen (:first-child, ::before), at-Regeln (@media), regel, kommentar, eigene_eigenschaft."""
    aufrufe: list[str] = Field(default_factory=list)
    """Python: aufgerufene Namen (print, range, len ...); SQL: Funktionen in Großbuchstaben (COUNT, UPPER ...);
    JavaScript: aufgerufene Namen (prompt, Number ...) und Aufrufe an einem Namen mit Punkt (console.log, Math.round);
    CSS: Funktionen (rgb, calc, var, linear-gradient ...)."""
    methoden: list[str] = Field(default_factory=list)
    """Python und JavaScript: aufgerufene Methoden (append, split; push, toUpperCase ...)."""
    operatoren: list[str] = Field(default_factory=list)
    """Python: Operatoren als Knotennamen (Add, Mod, Eq, In ...); JavaScript: Operatoren und Schlüsselwörter, wie sie
    im Code stehen (===, %, let, const ...)."""
    literale: list[str] = Field(default_factory=list)
    """Python: Typen fester Werte im Code (str, int, float, bool, NoneType); JavaScript: Knotenarten fester Werte
    (number, string, template_string, true, false, null, undefined); CSS: Einheiten (px, em, %), hex, zahl, text."""
    eigenschaften: list[str] = Field(default_factory=list)
    """JavaScript: gelesene Eigenschaften hinter einem Punkt, die keine Methoden sind (length, size ...); CSS:
    Eigenschaften der Angaben (color, margin ...)."""
    werte: list[str] = Field(default_factory=list)
    """CSS: Schlüsselwörter als eigenschaft:wert (display:flex, position:absolute) oder *:wert für jede Eigenschaft
    (*:inherit)."""
    elemente: list[str] = Field(default_factory=list)
    """CSS: Elemente im Markup und als Selektor (p, li, div ...)."""
    attribute: list[str] = Field(default_factory=list)
    """CSS: Attribute im Markup (class, id ...)."""


class Begriff(Streng):
    id: str = Field(pattern=r"^[a-z0-9_]{1,60}$")
    titel: str
    erkennung: Erkennung = Field(default_factory=Erkennung)


class Begriffskatalog(Streng):
    sprache: Kurssprache
    begriffe: list[Begriff]
