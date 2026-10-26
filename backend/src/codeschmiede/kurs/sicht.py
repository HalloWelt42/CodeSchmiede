"""Was die Oberfläche vom Kurs sieht: Übersicht, Einführung, Kurztest und Merkblatt ohne Lösungen.

Fragen und Vorhersagen erscheinen ohne `richtig`, `antworten`, `zeile` und Erklärungen; die kommen erst mit dem
Urteil nach einer Antwort (`Urteil`).
"""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, Field

Kapitelstand = Literal["fertig", "uebersprungen", "aktuell", "offen", "zu"]


class FrageSicht(BaseModel):
    id: str
    frageart: Literal["auswahl", "luecke", "ordnen", "fehlerstelle"]
    text: str
    code: str | None = None
    optionen: list[str] | None = None
    mehrere: bool = False
    """Auswahl mit mehr als einer richtigen Option."""
    als_code: bool = False
    luecken: int | None = None
    zeilen: list[str] | None = None
    """Ordnen: die Zeilen in fester Mischung; geantwortet wird mit ihren Stellen."""
    beantwortet: bool = False
    richtig: bool = False


class VorhersageSicht(BaseModel):
    art: Literal["auswahl", "eintippen"]
    frage: str | None = None
    optionen: list[str] | None = None
    beantwortet: bool = False
    richtig: bool = False


class BildVerweis(BaseModel):
    schluessel: str
    url: str | None = None
    """None, solange das Bild nicht abgenommen und exportiert ist; dann zeigt die Oberfläche einen Platzhalter."""
    motiv: str


class TextSicht(BaseModel):
    art: Literal["text"] = "text"
    markdown: str


class AlltagSicht(BaseModel):
    art: Literal["alltag"] = "alltag"
    text: str
    zeichnung: str | None = None
    """Adresse der eigenen Zeichnung (SVG)."""


class MerkeSicht(BaseModel):
    art: Literal["merke"] = "merke"
    text: str


class FalleSicht(BaseModel):
    art: Literal["falle"] = "falle"
    titel: str
    text: str


class AugenzwinkernSicht(BaseModel):
    art: Literal["augenzwinkern"] = "augenzwinkern"
    text: str


class ZeichnungSicht(BaseModel):
    art: Literal["zeichnung"] = "zeichnung"
    url: str
    unterschrift: str = ""


class DiagrammSicht(BaseModel):
    art: Literal["diagramm"] = "diagramm"
    url: str | None = None
    titel: str = ""


class BeispielSicht(BaseModel):
    art: Literal["beispiel"] = "beispiel"
    id: str
    code: str
    html: str | None = None
    """CSS: das Markup, auf das das CSS in `code` wirkt."""
    vorhersage: VorhersageSicht | None = None
    eingabe: list[str] = []
    """Was input() liest; die Oberfläche zeigt es neben der Ausgabe."""
    ablauf: bool = True


class FrageTeilSicht(BaseModel):
    art: Literal["frage"] = "frage"
    frage: FrageSicht


TeilSicht = Annotated[TextSicht | AlltagSicht | MerkeSicht | FalleSicht | AugenzwinkernSicht | ZeichnungSicht | DiagrammSicht
                      | BeispielSicht | FrageTeilSicht, Field(discriminator="art")]


class AbschnittSicht(BaseModel):
    nummer: int
    titel: str
    teile: list[TeilSicht]
    fertig: bool


class UebungSicht(BaseModel):
    id: str
    titel: str
    geloest: bool


class KapitelSicht(BaseModel):
    nr: int
    einfuehrung: str
    titel: str
    kurz: str
    lernziele: list[str]
    karte: str
    bild: BildVerweis | None = None
    """Zeichnung der Sammelkarte."""
    stand: Kapitelstand
    abschnitte: int
    abschnitte_fertig: int
    uebungen: list[UebungSicht]
    projekt: list[UebungSicht]
    uebungen_offen: bool
    """Übungen sind freigeschaltet (Einführung fertig oder Kapitel übersprungen)."""
    kurztest: bool
    vertiefung: list[UebungSicht]


class BlockSicht(BaseModel):
    titel: str
    kapitel: list[KapitelSicht]


class KursSicht(BaseModel):
    sprache: str
    titel: str
    bloecke: list[BlockSicht]


class EinfuehrungSicht(BaseModel):
    id: str
    sprache: str
    titel: str
    kurz: str
    lernziele: list[str]
    karte: str
    kapitel: int | None
    datensatz: str | None = None
    """SQL: Name des Datensatzes der Beispiele (Vorschau über /api/sql/datasets/<name>/vorschau)."""
    abschnitte: list[AbschnittSicht]


class KurztestSicht(BaseModel):
    einfuehrung: str
    titel: str
    fragen: list[FrageSicht]
    uebung: UebungSicht
    bestanden: bool


class MerkBeispiel(BaseModel):
    code: str
    html: str | None = None
    """CSS: das Markup; das Merkblatt zeigt dazu die Bühne."""
    ausgabe: str | None


class MerkblattSicht(BaseModel):
    einfuehrung: str
    sprache: str
    titel: str
    kapitel: int | None
    lernziele: list[str]
    merke: list[str]
    beispiele: list[MerkBeispiel]
    fallen: list[FalleSicht]
    begriffe: list[str]
    bild: BildVerweis | None = None


class Antwort(BaseModel):
    """Antwort auf eine Frage oder Vorhersage; je Frageart ist genau ein Feld gefüllt."""

    element: str = Field(min_length=1, max_length=80)
    wahl: list[int] | None = None
    luecken: list[str] | None = Field(default=None, max_length=20)
    reihenfolge: list[int] | None = Field(default=None, max_length=50)
    zeile: int | None = None
    eingetippt: str | None = Field(default=None, max_length=10_000)


class Urteil(BaseModel):
    richtig: bool
    erklaerung: str
    """Bei richtiger Antwort die Erklärung, bei falscher der Hinweis (oder die Erklärung der gewählten Option)."""
    abschnitt_bereit: bool = False
    """Alle Fragen des Abschnitts sind richtig beantwortet; weiter geht es mit `fertig`."""


class AusfuehrenAnfrage(BaseModel):
    code: str | None = Field(default=None, max_length=20_000)
    """Veränderter Code (nur am Rechner); ohne läuft das Original."""
